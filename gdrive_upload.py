"""
Google Drive 作業上傳模組
使用 Service Account 將學員作業自動上傳到指定的 Google Drive 資料夾
"""
import io
import streamlit as st
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload


def get_drive_service():
    """從 Streamlit secrets 取得 Google Drive API 服務"""
    try:
        creds_info = st.secrets["google_service_account"]
        creds = service_account.Credentials.from_service_account_info(
            dict(creds_info),
            scopes=["https://www.googleapis.com/auth/drive.file"],
        )
        return build("drive", "v3", credentials=creds, cache_discovery=False)
    except Exception:
        return None


def get_or_create_folder(service, folder_name, parent_id):
    """在指定的父資料夾下取得或建立子資料夾"""
    query = (
        f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder' "
        f"and '{parent_id}' in parents and trashed=false"
    )
    results = service.files().list(q=query, fields="files(id)").execute()
    files = results.get("files", [])

    if files:
        return files[0]["id"]

    file_metadata = {
        "name": folder_name,
        "mimeType": "application/vnd.google-apps.folder",
        "parents": [parent_id],
    }
    folder = service.files().create(body=file_metadata, fields="id").execute()
    return folder["id"]


def upload_to_gdrive(uploaded_file, hw_name, filename):
    """
    將檔案上傳到 Google Drive。
    資料夾結構：[根資料夾] / [HW名稱] / [檔案]

    Returns:
        str: 成功時回傳 Google Drive 檔案連結，失敗回傳 None
    """
    service = get_drive_service()
    if service is None:
        return None

    try:
        root_folder_id = st.secrets.get("gdrive_folder_id", "")
        if not root_folder_id:
            return None

        # 建立 HW 子資料夾（如 HW1, HW2...）
        hw_folder_id = get_or_create_folder(service, hw_name, root_folder_id)

        # 上傳檔案
        file_metadata = {
            "name": filename,
            "parents": [hw_folder_id],
        }
        media = MediaIoBaseUpload(
            io.BytesIO(uploaded_file.getbuffer()),
            mimetype=uploaded_file.type or "application/octet-stream",
        )
        file = service.files().create(
            body=file_metadata, media_body=media, fields="id,webViewLink"
        ).execute()

        return file.get("webViewLink")
    except Exception as e:
        st.warning(f"Google Drive 上傳失敗：{e}")
        return None
