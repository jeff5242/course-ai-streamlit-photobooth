import streamlit as st
import time
import io
import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from gdrive_upload import upload_to_gdrive


def save_uploaded_file(uploaded_file, hw_name, student_name=""):
    """將上傳的作業檔案存入本機 + 上傳到 Google Drive"""
    # 本機存檔（備份）
    save_dir = os.path.join(os.path.dirname(__file__), "uploads", "homework", hw_name)
    os.makedirs(save_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    prefix = f"{student_name}_" if student_name else ""
    filename = f"{prefix}{timestamp}_{uploaded_file.name}"
    filepath = os.path.join(save_dir, filename)
    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # 上傳到 Google Drive
    gdrive_link = upload_to_gdrive(uploaded_file, hw_name, filename)

    return filepath, gdrive_link

# 設定頁面配置
st.set_page_config(layout="wide", page_title="AI 領航員：Vibe Coding 實戰教學")

# --- 自定義樣式 ---
st.markdown("""
    <style>
    /* Tab 樣式 */
    .stTabs [data-baseweb="tab-list"] { gap: 20px; }
    .stTabs [data-baseweb="tab"] { height: 50px; font-size: 18px; font-weight: bold; }

    /* 統一卡片風格 */
    .course-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px; padding: 25px; color: white; text-align: center;
    }
    .course-card h3, .course-card h4 { color: white; }
    .course-card hr { border-color: rgba(255,255,255,0.3); }

    /* 資訊框統一間距 */
    .stAlert { margin-top: 10px; margin-bottom: 10px; }

    /* 表格美化 */
    table { width: 100%; }
    th { background: rgba(102, 126, 234, 0.2); }

    /* 側邊欄分隔線樣式 */
    .stRadio > label { font-size: 14px; }

    /* 封面標題樣式 */
    .lesson-cover {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px; padding: 30px 20px; text-align: center;
        color: white; margin-bottom: 20px;
    }
    .lesson-cover h2 { color: white; margin: 0; }
    .lesson-cover p { color: rgba(255,255,255,0.8); margin: 8px 0 0 0; font-size: 14px; }

    /* RWD 手機適配 */
    @media (max-width: 768px) {
        .stTabs [data-baseweb="tab"] { height: 40px; font-size: 14px; }
        .lesson-cover { padding: 20px 15px; }
        .lesson-cover h2 { font-size: 20px; }
        div[style*="display: flex"] { flex-direction: column !important; align-items: center !important; }
        div[style*="min-width: 140px"], div[style*="min-width: 160px"] { min-width: 100% !important; }
    }
    </style>
    """, unsafe_allow_html=True)

# --- 側邊欄：課程與章節導覽 ---
st.sidebar.title("🚢 AI 領航員課程")
course = st.sidebar.selectbox("選擇課程", [
    "第一堂：Vibe Coding 入門",
    "第二堂：實戰體驗與案例",
    "第三堂：需求分析與架構規劃",
    "第四堂：截圖復刻與在地化",
    "第五堂：支付串接與部署策略",
    "第六堂：硬體整合與總結",
    "第七堂：部署與 MVP 驗收",
    "第八堂：GitHub 版本控制與協作",
    "第九堂：測試迭代與品質優化",
    "第十堂：會員系統與社群經營",
    "第十一堂：維護自動化與周邊商品",
    "第十二堂：成果發表與未來路線圖",
    "───────────────",
    "📊 教師後台",
])

if course == "第一堂：Vibe Coding 入門":
    current_section = st.sidebar.radio("課程章節", [
        "0. 啟航：計畫願景",
        "1. 認識 Vibe Coding",
        "2. 為什麼需要 Vibe Coding",
        "3. 照相任務全面進化",
        "4. 權限與工具設定",
        "HW1. 課後練習",
    ])
elif course == "第二堂：實戰體驗與案例":
    current_section = st.sidebar.radio("課程章節", [
        "R1. 上堂回顧與 Q&A",
        "5. 拍貼機實戰 Demo",
        "6. Vibe Coding 實戰案例",
        "6.5. 代碼考古學",
        "HW2. 課後練習",
    ])
elif course == "第三堂：需求分析與架構規劃":
    current_section = st.sidebar.radio("課程章節", [
        "R2. 上堂回顧與 Q&A",
        "7. 真實痛點深掘",
        "8. 需求描述與架構訓練",
        "9. 設備選型決策討論",
        "HW3. 課後練習",
    ])
elif course == "第四堂：截圖復刻與在地化":
    current_section = st.sidebar.radio("課程章節", [
        "R3. 上堂回顧與 Q&A",
        "10. 截圖轉程式實戰",
        "11. 在地化調整實作",
        "12. Before/After 成果驗收",
        "HW4. 課後練習",
    ])
elif course == "第五堂：支付串接與部署策略":
    current_section = st.sidebar.radio("課程章節", [
        "R4. 上堂回顧與 Q&A",
        "13. QR Code 行動支付實作",
        "14. 支付與列印串接規劃",
        "14.5. 異常處理 Vibe 化",
        "15. 快閃店部署策略",
        "16. 數據儀表板願景",
        "HW5. 課後練習",
    ])
elif course == "第六堂：硬體整合與總結":
    current_section = st.sidebar.radio("課程章節", [
        "R5. 上堂回顧與 Q&A",
        "17. 硬體 SDK 規格收集",
        "17.5. AI 加值應用實驗",
        "18. 通訊協定解析",
        "19. 整合架構設計",
        "20. 整合實作與測試",
        "21. 課程總結與後續規劃",
        "HW6. 課後練習",
    ])
elif course == "第七堂：部署與 MVP 驗收":
    current_section = st.sidebar.radio("課程章節", [
        "R6. 上堂回顧與 Q&A",
        "22. MVP 版本定義與範圍",
        "23. 部署工作流程",
        "24. 現場部署實作",
        "HW7. 課後練習",
    ])
elif course == "第八堂：GitHub 版本控制與協作":
    current_section = st.sidebar.radio("課程章節", [
        "R7. 上堂回顧與 Q&A",
        "25. Git 版本控制入門",
        "26. GitHub 協作流程",
        "27. 用 AI 管理程式碼變更",
        "HW8. 課後練習",
    ])
elif course == "第九堂：測試迭代與品質優化":
    current_section = st.sidebar.radio("課程章節", [
        "R8. 上堂回顧與 Q&A",
        "28. 系統測試策略",
        "29. 迭代修正工作坊",
        "HW9. 課後練習",
    ])
elif course == "第十堂：會員系統與社群經營":
    current_section = st.sidebar.radio("課程章節", [
        "R9. 上堂回顧與 Q&A",
        "30. 會員關係建立與維護",
        "31. 官方帳號與社群經營",
        "HW10. 課後練習",
    ])
elif course == "第十一堂：維護自動化與周邊商品":
    current_section = st.sidebar.radio("課程章節", [
        "R10. 上堂回顧與 Q&A",
        "32. 維護流程自動化",
        "33. 周邊商品功能規劃",
        "HW11. 課後練習",
    ])
elif course == "第十二堂：成果發表與未來路線圖":
    current_section = st.sidebar.radio("課程章節", [
        "R11. 上堂回顧與 Q&A",
        "34. 成果發表準備",
        "35. 未來路線圖",
        "HW12. 課後練習",
    ])
elif course == "📊 教師後台":
    current_section = st.sidebar.radio("功能", [
        "📋 作業繳交追蹤",
        "📈 課程進度總覽",
    ])
else:
    current_section = "0. 啟航：計畫願景"

def lesson_cover(number, title, subtitle, icon="📖"):
    """顯示課程封面橫幅"""
    colors = {
        1: ("#e74c3c", "#c0392b"), 2: ("#e67e22", "#d35400"), 3: ("#f1c40f", "#f39c12"),
        4: ("#2ecc71", "#27ae60"), 5: ("#3498db", "#2980b9"), 6: ("#9b59b6", "#8e44ad"),
        7: ("#1abc9c", "#16a085"), 8: ("#34495e", "#2c3e50"), 9: ("#e74c3c", "#c0392b"),
        10: ("#e67e22", "#d35400"), 11: ("#2ecc71", "#27ae60"), 12: ("#9b59b6", "#8e44ad"),
    }
    c1, c2 = colors.get(number, ("#667eea", "#764ba2"))
    st.markdown(f"""
    <div class="lesson-cover" style="background: linear-gradient(135deg, {c1} 0%, {c2} 100%);">
        <p style="font-size: 36px; margin: 0;">{icon}</p>
        <h2>第{number}堂：{title}</h2>
        <p>{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# 第一堂課
# =====================================================

if current_section == "0. 啟航：計畫願景":
    lesson_cover(1, "Vibe Coding 入門", "部署 AI 開發環境，掌握意圖驅動編碼的提問心法", "🚀")
    st.title("⚓ 航向自主掌控：21 天硬體轉型實戰")
    col1, col2 = st.columns([6, 4])
    with col1:
        st.markdown("""
        ### 為何我們在這裡？
        * **合規需求：** 現有 PhotoBooth 系統含簡體字，無法參加政府活動（如文博會）。
        * **打破黑盒：** 大陸廠商限制功能，出問題只能等原廠，亟需自主掌控。
        * **行政減負：** 同仁在 ERP、POS、蝦皮、Pinkoi、官網間重複登入、手動整理數據。
        * **降低門檻：** 團隊多為工廠出身，透過 AI 讓非工程背景也能參與開發。

        > **由 JD 親自參與開發流程，作為內部示範，消除團隊對新技術的畏懼感。**
        """)
    with col2:
        st.image("images/transfer.png", caption="系統轉型示意圖", use_container_width=True)

    st.divider()
    st.subheader("🎯 轉型願景")
    st.markdown("""
    不更動大架構，利用 AI 的「小工具」模式：
    * **第一步：** PhotoBooth 軟體重構與繁體化
    * **第二步：** 流程串接與 QR Code 行動支付
    * **第三步：** 數據儀表板化，減少人工作業
    """)

elif current_section == "1. 認識 Vibe Coding":
    st.title("🧩 什麼是 Vibe Coding？")

    tab1, tab_history, tab_trust, tab2, tab3 = st.tabs([
        "💡 核心概念", "📜 程式開發演進史", "🤝 與 AI 建立信任", "⚔️ 能與不能", "🎯 Prompt 實戰練習"
    ])

    with tab1:
        st.markdown("""
        ### Vibe Coding 的定義
        不再糾結於每行代碼的語法，而是專注於描述**「產品的氛圍 (Vibe)」**與**「邏輯意圖」**。
        """)

        # 傳統開發 vs Vibe Coding 對比圖
        col_old, col_vs, col_new = st.columns([5, 1, 5])
        with col_old:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #4a4a4a 0%, #2c2c2c 100%);
                        border-radius: 15px; padding: 30px; color: white;">
                <h3 style="text-align:center; color: #ff6b6b;">傳統開發</h3>
                <p style="text-align:center; color: #aaa; font-size: 14px;">像在學外語</p>
                <hr style="border-color: #555;">
                <p>- 花數週學習語法規則</p>
                <p>- 逐行 Debug 找分號、括號</p>
                <p>- 翻文件查 API 用法</p>
                <p>- 一個功能寫數小時</p>
            </div>
            """, unsafe_allow_html=True)
        with col_vs:
            st.markdown("""
            <div style="display:flex; align-items:center; justify-content:center; height:250px;">
                <p style="font-size:48px; font-weight:bold; color:#888;">→</p>
            </div>
            """, unsafe_allow_html=True)
        with col_new:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        border-radius: 15px; padding: 30px; color: white;">
                <h3 style="text-align:center; color: #7bff7b;">Vibe Coding</h3>
                <p style="text-align:center; color: rgba(255,255,255,0.7); font-size: 14px;">像在帶部屬</p>
                <hr style="border-color: rgba(255,255,255,0.3);">
                <p>- 用自然語言描述意圖</p>
                <p>- AI 自動產出完整程式</p>
                <p>- 看結果、給回饋、迭代</p>
                <p>- 一個功能幾分鐘完成</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("")
        st.markdown("#### 核心公式：")
        st.markdown("### **明確背景 + 具體目標 + 期望風格 = 完美產出**")

    with tab_history:
        st.markdown("### 從打孔卡到自然語言：程式開發的演進歷程")
        st.markdown("在理解 Vibe Coding 之前，先看看人類「跟電腦溝通」的方式是如何演變的：")

        timeline = [
            ("1950s", "機器語言", "0 和 1", "直接寫二進位指令，一個錯就整台當機", "#e74c3c"),
            ("1960s", "組合語言", "MOV AX, 01", "用助記符代替二進位，但仍需理解硬體架構", "#e67e22"),
            ("1970-80s", "高階語言", "C / Pascal", "接近英文的語法，一行程式可以做很多事", "#f1c40f"),
            ("1990-2000s", "物件導向 + 框架", "Java / Python", "用「物件」組織程式碼，框架幫你處理重複的事", "#2ecc71"),
            ("2010s", "低代碼 / 無代碼", "Drag & Drop", "拖拉元件就能做 App，但客製化受限", "#3498db"),
            ("2024-Now", "Vibe Coding", "自然語言", "用日常用語描述需求，AI 幫你寫完整程式", "#9b59b6"),
        ]

        for i, (year, era, example, desc, color) in enumerate(timeline):
            col_year, col_content = st.columns([2, 8])
            with col_year:
                st.markdown(f"""
                <div style="background: {color}; border-radius: 8px; padding: 10px; text-align: center; color: white;">
                    <strong>{year}</strong>
                </div>
                """, unsafe_allow_html=True)
            with col_content:
                st.markdown(f"**{era}**　`{example}`　— {desc}")

            if i < len(timeline) - 1:
                st.markdown("<div style='margin-left: 60px; color: #636e72; font-size: 16px;'>↓</div>", unsafe_allow_html=True)

        st.markdown("")
        st.success("""
        💡 **關鍵趨勢：** 每一次演進，人類離「用自己的語言跟電腦溝通」就更近一步。
        Vibe Coding 不是突然出現的，而是這條路走了 70 年的自然結果。

        **你不需要學程式語言，因為你的母語就是最好的程式語言。**
        """)

    with tab_trust:
        st.markdown("### 與 AI Agent 建立信任：從懷疑到放手")
        st.markdown("第一次使用 AI Agent，大多數人的反應是：「真的可以信任它嗎？」這很正常。")

        st.divider()
        st.markdown("#### 🚗 類比：Tesla 自動駕駛的信任過程")
        st.markdown("你與 AI Agent 建立信任的過程，跟開 Tesla 放手讓自動駕駛接管非常相似：")

        trust_stages = [
            ("😰 階段一：完全不信任", "雙手緊握方向盤", "一問一答，每個結果都仔細檢查",
             "剛開始用 AI，每行程式都要逐字看過", "#e74c3c"),
            ("🤔 階段二：有條件信任", "偶爾放手，但隨時準備接管", "開始交付小任務，看結果再決定下一步",
             "讓 AI 寫一個小功能，確認品質後再交更多", "#f39c12"),
            ("😊 階段三：逐漸放手", "大部分時間放手，只在複雜路段接管", "交付整個模組，只在關鍵決策點介入",
             "讓 AI 規劃整個功能，你負責審核方向", "#27ae60"),
            ("😎 階段四：充分信任", "全程放手，專注在目的地", "描述目標，讓 AI 自主規劃並執行",
             "像今天的案例——一段話就完成 8 個階段的開發", "#2980b9"),
        ]

        for stage, tesla, ai, example, color in trust_stages:
            st.markdown(f"""
            <div style="border-left: 4px solid {color}; padding: 15px 20px; margin-bottom: 12px;
                        background: rgba(45,52,54,0.3); border-radius: 0 8px 8px 0;">
                <strong style="color: {color}; font-size: 16px;">{stage}</strong><br>
                <table style="width: 100%; margin-top: 8px;">
                    <tr>
                        <td style="width: 50%; padding: 5px; color: #b2bec3; font-size: 13px;">
                            🚗 Tesla：{tesla}
                        </td>
                        <td style="width: 50%; padding: 5px; color: #dfe6e9; font-size: 13px;">
                            🤖 AI Agent：{ai}
                        </td>
                    </tr>
                    <tr>
                        <td colspan="2" style="padding: 5px; color: #74b9ff; font-size: 13px;">
                            📌 {example}
                        </td>
                    </tr>
                </table>
            </div>
            """, unsafe_allow_html=True)

        st.divider()
        st.markdown("#### 📈 信任帶來指數型成長")

        st.markdown("""
        <div style="background: linear-gradient(135deg, #0984e3 0%, #6c5ce7 100%);
                    border-radius: 15px; padding: 25px; color: white;">
            <h4 style="color: white; text-align: center;">效益成長曲線</h4>
            <hr style="border-color: rgba(255,255,255,0.3);">
            <table style="width: 100%; color: white; text-align: center;">
                <tr style="font-size: 14px;">
                    <td style="padding: 12px;">😰 一問一答<br><strong style="font-size: 20px;">1x</strong><br>基礎效率</td>
                    <td style="padding: 12px;">🤔 小任務委派<br><strong style="font-size: 20px;">3x</strong><br>節省重複工作</td>
                    <td style="padding: 12px;">😊 模組級委派<br><strong style="font-size: 20px;">10x</strong><br>大幅加速開發</td>
                    <td style="padding: 12px;">😎 自主執行<br><strong style="font-size: 20px;">50x+</strong><br>指數型成長</td>
                </tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("")
        st.info("""
        💡 **信任不是盲目的。** 建立信任的關鍵是：
        1. **持續使用** — 瞭解 AI 的「脾氣」，就像認識一個新同事
        2. **從小事開始** — 先交小任務，累積信心後再放大範圍
        3. **保持監督** — 即使放手，關鍵決策仍由你做主
        4. **給予回饋** — 告訴 AI 什麼做得好、什麼需要改，它會越來越懂你
        """)

    with tab2:
        col_can, col_cannot = st.columns(2)
        with col_can:
            st.success("✅ **AI Agent 能做什麼**")
            st.markdown("""
            * **解釋舊代碼：** 掃描大陸簡體代碼並用繁體解釋邏輯。
            * **快速原型：** 30 秒內寫出支付或拍照的介面。
            * **語言轉譯：** 將技術術語翻譯成優雅的繁體中文。
            * **除錯優化：** 根據錯誤回報自動修正程式碼。
            """)
        with col_cannot:
            st.error("❌ **AI Agent 不能做什麼**")
            st.markdown("""
            * **物理維修：** 無法解決線路鬆脫或硬體故障。
            * **通靈猜測：** 如果不提供硬體手冊（Spec），它會胡說八道。
            * **情感共感：** 最終的「品味」與「在地體驗」仍需長官決定。
            * **安全驗證：** 關鍵硬體操作（如電壓控制）仍需技術同事把關。
            """)

    with tab3:
        st.markdown("""
        ### 🧪 動手試試看！
        還記得核心公式嗎？ **明確背景 + 具體目標 + 期望風格 = 完美產出**

        請在下方三個欄位分別填入內容，組合出一個完整的 Prompt。
        """)

        example = st.selectbox("或選擇一個範例情境快速填入：", [
            "（自行輸入）",
            "拍貼機：支付模組",
            "拍貼機：拍照倒數介面",
            "硬體監控：溫度警報系統",
        ])

        examples_data = {
            "拍貼機：支付模組": {
                "background": "我正在開發一台拍貼機的嵌入式系統，使用 Python + Streamlit 做前端介面，目標客群是台灣的年輕消費者。",
                "goal": "請幫我寫一個支付頁面，支援紙鈔辨識（模擬）和 LINE Pay QR Code 掃碼兩種付款方式，付款成功後自動跳轉到拍照頁面。",
                "style": "介面文字請使用繁體中文，風格活潑可愛，適合 18-30 歲的女性使用者。按鈕要大且明顯，配色以粉紅色系為主。",
            },
            "拍貼機：拍照倒數介面": {
                "background": "我在用 Streamlit 開發拍貼機原型，需要模擬相機拍照流程，目前已完成支付階段。",
                "goal": "請製作一個拍照倒數畫面，顯示 3、2、1 倒數動畫後模擬拍照，共需拍攝 6 張，每張之間有 3 秒準備時間。",
                "style": "使用繁體中文，畫面中央大字顯示倒數數字，底部顯示目前第幾張/共幾張的進度。整體風格簡潔專業。",
            },
            "硬體監控：溫度警報系統": {
                "background": "我們工廠有一批印表機設備，需要即時監控其運作溫度，目前用 Python 讀取感測器資料。",
                "goal": "請用 Streamlit 做一個溫度監控儀表板，即時顯示三台印表機的溫度折線圖，超過 75°C 時自動顯示紅色警告。",
                "style": "介面使用繁體中文，風格仿工業監控系統，配色以深灰底搭配綠色/紅色指示燈。數據每秒更新一次。",
            },
        }

        if example != "（自行輸入）":
            default = examples_data[example]
        else:
            default = {"background": "", "goal": "", "style": ""}

        st.divider()
        col_input, col_output = st.columns([1, 1])

        with col_input:
            st.markdown("#### 📝 填寫你的 Prompt 三要素")
            background = st.text_area(
                "1️⃣ 明確背景（你是誰？在做什麼專案？）",
                value=default["background"], height=100,
                placeholder="例：我正在開發一台拍貼機系統，使用 Python 語言...",
            )
            goal = st.text_area(
                "2️⃣ 具體目標（你希望 AI 產出什麼？）",
                value=default["goal"], height=100,
                placeholder="例：請幫我寫一個支付頁面，支援投幣和掃碼...",
            )
            style = st.text_area(
                "3️⃣ 期望風格（語言、語氣、外觀偏好）",
                value=default["style"], height=100,
                placeholder="例：請使用繁體中文，風格活潑可愛...",
            )

        with col_output:
            st.markdown("#### 🔗 組合後的完整 Prompt")
            if background or goal or style:
                combined = ""
                if background:
                    combined += f"【背景】\n{background}\n\n"
                if goal:
                    combined += f"【目標】\n{goal}\n\n"
                if style:
                    combined += f"【風格】\n{style}"
                st.code(combined, language=None)

                score = 0
                feedback_items = []
                if len(background) > 20:
                    score += 1
                    feedback_items.append("✅ 背景描述足夠具體")
                else:
                    feedback_items.append("⚠️ 背景描述太短，建議補充專案類型、技術棧、目標客群")
                if len(goal) > 20:
                    score += 1
                    feedback_items.append("✅ 目標描述明確")
                else:
                    feedback_items.append("⚠️ 目標描述太短，建議說明具體要產出什麼功能")
                if len(style) > 10:
                    score += 1
                    feedback_items.append("✅ 有指定風格偏好")
                else:
                    feedback_items.append("⚠️ 缺少風格指定，AI 可能用預設語氣回覆")

                st.divider()
                st.markdown("#### 📊 Prompt 品質檢測")
                quality_labels = {0: "🔴 需要加強", 1: "🟡 尚可", 2: "🟢 不錯", 3: "🎯 優秀！"}
                st.progress(score / 3)
                st.markdown(f"**評分：{quality_labels[score]}**（{score}/3）")
                for item in feedback_items:
                    st.markdown(item)
            else:
                st.info("👈 請在左側填入內容，或選擇範例情境快速體驗")

elif current_section == "2. 為什麼需要 Vibe Coding":
    st.title("🔥 為什麼我們現在需要 Vibe Coding？")

    st.markdown("")
    col_now, col_chance, col_goal = st.columns(3)
    with col_now:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
                    border-radius: 15px; padding: 30px; color: white; min-height: 280px;">
            <h3 style="text-align:center; color: white;">😰 現狀挑戰</h3>
            <hr style="border-color: rgba(255,255,255,0.3);">
            <p>🔤 介面充斥簡體字，用語不符台灣習慣</p>
            <p>📦 底層邏輯像黑盒，出問題只能等原廠</p>
            <p>🔒 被動使用大陸系統，無法自行修改調整</p>
        </div>
        """, unsafe_allow_html=True)
    with col_chance:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #f39c12 0%, #e67e22 100%);
                    border-radius: 15px; padding: 30px; color: white; min-height: 280px;">
            <h3 style="text-align:center; color: white;">💡 轉型契機</h3>
            <hr style="border-color: rgba(255,255,255,0.3);">
            <p>🤖 透過 AI Agent 快速掃描現有代碼</p>
            <p>🔍 「轉繁體」只是第一步</p>
            <p>🧠 「搞懂它」才是真功夫</p>
        </div>
        """, unsafe_allow_html=True)
    with col_goal:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #27ae60 0%, #2ecc71 100%);
                    border-radius: 15px; padding: 30px; color: white; min-height: 280px;">
            <h3 style="text-align:center; color: white;">🎯 最終目標</h3>
            <hr style="border-color: rgba(255,255,255,0.3);">
            <p>🚀 從「被動使用」轉為「主動定義」</p>
            <p>🏗️ 建立自研整合流程</p>
            <p>🔧 自主掌控系統的每一個環節</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("")
    st.divider()

    st.subheader("🎤 需求訪談：關鍵提問")
    st.markdown("在啟動專案前，我們需要先釐清以下問題：")

    questions = [
        "除了文字，目前大陸系統的操作邏輯有哪些是不符合台灣使用者習慣的？",
        "在設備串接流程中，哪個環節最常出錯或讓我們感到像「黑盒子」？",
        "我們希望建立的「整合能力」，具體包含哪些部分？（如：更換硬體的能力、自定義 UI 的能力？）",
    ]
    for i, q in enumerate(questions):
        with st.expander(f"提問 {i+1}：{q[:20]}...", expanded=(i == 0)):
            st.info(f"💬 {q}")
            st.text_area(f"你的想法（提問 {i+1}）", key=f"interview_q{i}", height=80,
                         placeholder="請在這裡寫下你的回答或觀察...")

    st.divider()

    st.subheader("👥 技術同事的關鍵任務")
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.markdown("""
        <div style="background: #1a1a2e; border-radius: 15px; padding: 25px; color: white;">
            <h4 style="color: #e94560;">🔎 原始代碼審查</h4>
            <p>協助 Claude 定位簡體資源檔與硬體溝通協議，找出需要在地化的關鍵檔案。</p>
        </div>
        """, unsafe_allow_html=True)
    with col_t2:
        st.markdown("""
        <div style="background: #1a1a2e; border-radius: 15px; padding: 25px; color: white;">
            <h4 style="color: #0f3460;">🗺️ 整合架構梳理</h4>
            <p>與 AI 協同畫出目前的系統架構圖，找出可優化的斷點與改善機會。</p>
        </div>
        """, unsafe_allow_html=True)

elif current_section == "3. 照相任務全面進化":
    st.title("📸 照相任務全面進化")

    st.subheader("🔤 語系升級：不只是翻譯，更是在地化")
    st.markdown("簡體轉繁體不僅是文字轉換，更是**語意在地化**——讓用語符合台灣使用者的直覺。")

    st.markdown("")
    col_before, col_arrow, col_after = st.columns([5, 1, 5])
    with col_before:
        st.markdown("""
        <div style="background: #fee2e2; border-radius: 12px; padding: 25px; border-left: 5px solid #ef4444;">
            <h4 style="color: #dc2626;">🇨🇳 大陸原始用語</h4>
            <table style="width:100%; font-size:16px; color: #333;">
                <tr><td style="padding:8px; color:#333;">摄像</td></tr>
                <tr><td style="padding:8px; color:#333;">刷新</td></tr>
                <tr><td style="padding:8px; color:#333;">导航</td></tr>
                <tr><td style="padding:8px; color:#333;">打印机</td></tr>
                <tr><td style="padding:8px; color:#333;">用户界面</td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
    with col_arrow:
        st.markdown("""
        <div style="display:flex; align-items:center; justify-content:center; height:250px;">
            <p style="font-size:48px;">➜</p>
        </div>
        """, unsafe_allow_html=True)
    with col_after:
        st.markdown("""
        <div style="background: #dcfce7; border-radius: 12px; padding: 25px; border-left: 5px solid #22c55e;">
            <h4 style="color: #16a34a;">🇹🇼 台灣在地化用語</h4>
            <table style="width:100%; font-size:16px; color: #333;">
                <tr><td style="padding:8px; color:#1a5c2a;"><b>照相</b></td></tr>
                <tr><td style="padding:8px; color:#1a5c2a;"><b>重新整理</b></td></tr>
                <tr><td style="padding:8px; color:#1a5c2a;"><b>導引</b></td></tr>
                <tr><td style="padding:8px; color:#1a5c2a;"><b>印表機</b></td></tr>
                <tr><td style="padding:8px; color:#1a5c2a;"><b>使用者介面</b></td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("")
    st.divider()

    st.subheader("🔧 流程拆解與自主掌控")
    col_step1, col_step2, col_step3 = st.columns(3)
    with col_step1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    border-radius: 15px; padding: 25px; color: white; min-height: 200px;">
            <h4 style="text-align:center; color: white;">Step 1</h4>
            <h4 style="text-align:center; color: white;">🔍 流程拆解</h4>
            <hr style="border-color: rgba(255,255,255,0.3);">
            <p style="font-size:14px;">藉由 Claude 分析現有大陸廠商的整合邏輯，理解每一段代碼的職責。</p>
        </div>
        """, unsafe_allow_html=True)
    with col_step2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                    border-radius: 15px; padding: 25px; color: white; min-height: 200px;">
            <h4 style="text-align:center; color: white;">Step 2</h4>
            <h4 style="text-align:center; color: white;">📐 建立標準</h4>
            <hr style="border-color: rgba(255,255,255,0.3);">
            <p style="font-size:14px;">建立自己的整合標準與設備串接手冊，不再依賴原廠文件。</p>
        </div>
        """, unsafe_allow_html=True)
    with col_step3:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
                    border-radius: 15px; padding: 25px; color: white; min-height: 200px;">
            <h4 style="text-align:center; color: white;">Step 3</h4>
            <h4 style="text-align:center; color: white;">🏆 自主掌控</h4>
            <hr style="border-color: rgba(255,255,255,0.3);">
            <p style="font-size:14px;">擁有更換硬體、自定義 UI、獨立除錯的完整能力。</p>
        </div>
        """, unsafe_allow_html=True)

elif current_section == "4. 權限與工具設定":
    st.title("🔐 權限、工具與部署流程")

    with st.expander("🔑 運作所需的權限與工具", expanded=True):
        st.markdown("""
        1. **模型權限：** 需具備 Claude API 存取權。
        2. **開發環境：** VS Code 必須安裝 Claude Code 官方插件（claude.ai/code）。
        3. **檔案權限：** AI 需要具備對專案資料夾的「讀寫權限」以便修改代碼。
        4. **硬體介面：** 技術同事需預先開放 Serial Port 或 Network SDK 接口。
        """)

    with st.expander("🚀 軟體部署流程"):
        st.markdown("""
        ### 從開發到落地的三步驟：
        1. **本地模擬 (Local Dev):** 在 Streamlit 網頁上確認流程（如今天的 Demo）。
        2. **容器封裝 (Docker):** 由技術同事將 AI 寫好的代碼包裝成獨立環境。
        3. **實機推播 (Deployment):** 將軟體部署至大頭貼設備，完成測試。
        """)

elif current_section == "HW1. 課後練習":
    st.title("📝 課後練習：與 AI 對話，產出規格書")

    st.markdown("""
    恭喜完成第一堂課！在下堂課之前，請完成以下練習，幫助你熟悉與 AI 溝通的方式。
    """)

    st.divider()
    st.subheader("🎯 練習目標")
    st.markdown("""
    **用自然語言跟 AI 聊天，把你的需求轉化成一份規格書文件。**

    你不需要寫程式，只需要用日常用語描述你想要的東西，讓 AI 幫你整理成結構化的規格。
    """)

    st.divider()
    st.subheader("📋 練習步驟")

    with st.expander("Step 1：選一個你想改善的工作流程", expanded=True):
        st.markdown("""
        可以是拍貼機的某個功能，也可以是日常工作中重複做的事情。例如：
        - 「我每天要手動把蝦皮的訂單抄到 Excel 裡面」
        - 「拍貼機拍完照之後，客人要等很久才能拿到照片」
        - 「每次換快閃店地點，設備設定都要重來」
        """)

    with st.expander("Step 2：跟 AI 描述這個問題", expanded=True):
        st.markdown("""
        打開 ChatGPT 或 Claude，用你自己的話把問題講一遍。參考格式：

        > 「我在做 _____ 的時候，遇到 _____ 的問題。
        > 目前的做法是 _____，但我希望能 _____。
        > 你可以幫我整理成一份規格書嗎？」
        """)

    with st.expander("Step 3：請 AI 產出規格書", expanded=True):
        st.markdown("""
        跟 AI 說：「請幫我把剛才的需求整理成一份規格書，包含：」
        1. 系統背景
        2. 問題描述
        3. 期望功能
        4. 使用者操作流程
        5. 預期成果
        """)

    st.divider()
    st.subheader("📤 繳交作業")
    student = st.text_input("你的名字", key="hw1_name", placeholder="例：JD")
    hw1_file = st.file_uploader(
        "上傳 AI 產出的規格書（截圖或文字檔）",
        type=["png", "jpg", "jpeg", "pdf", "txt", "docx", "md"],
        key="hw1_upload",
    )
    if hw1_file and student:
        path, gdrive_link = save_uploaded_file(hw1_file, "HW1", student)
        st.success(f"✅ 作業已儲存！檔案：`{os.path.basename(path)}`")
        if gdrive_link:
            st.info(f"☁️ 已同步到 Google Drive")
    elif hw1_file and not student:
        st.warning("請先填寫你的名字再上傳。")

# =====================================================
# 第二堂課：實戰體驗與案例
# =====================================================

elif current_section == "5. 拍貼機實戰 Demo":
    st.title("📸 實戰演練：拍貼機原型系統")
    st.info("💡 這是 AI Agent 根據您的需求（Spec）即時生成的原型介面")

    # --- 背景板定義 ---
    BACKGROUNDS = {
        "櫻花粉": {"bg": "#ffb7c5", "accent": "#ff69b4", "deco": "🌸", "desc": "浪漫櫻花風，適合春季活動"},
        "海洋藍": {"bg": "#87ceeb", "accent": "#1e90ff", "deco": "🌊", "desc": "清涼海洋風，適合夏日快閃"},
        "森林綠": {"bg": "#90ee90", "accent": "#228b22", "deco": "🌿", "desc": "自然森林風，適合文博會展場"},
        "星空紫": {"bg": "#9370db", "accent": "#4b0082", "deco": "✨", "desc": "夢幻星空風，適合夜間活動"},
        "復古橘": {"bg": "#ffa07a", "accent": "#ff4500", "deco": "🎞️", "desc": "懷舊復古風，適合主題派對"},
        "經典白": {"bg": "#f5f5f5", "accent": "#dcdcdc", "deco": "⬜", "desc": "簡約經典風，適合證件或正式場合"},
    }

    def generate_background_preview(name, config, width=300, height=200):
        img = Image.new("RGB", (width, height), config["bg"])
        draw = ImageDraw.Draw(img)
        draw.rectangle([5, 5, width-6, height-6], outline=config["accent"], width=3)
        for x, y in [(20, 20), (width-35, 20), (20, height-35), (width-35, height-35)]:
            draw.ellipse([x, y, x+15, y+15], fill=config["accent"])
        cx, cy = width//2, height//2
        box_w, box_h = 80, 100
        for i in range(0, box_w*2 + box_h*2, 8):
            if i < box_w:
                draw.point((cx - box_w//2 + i, cy - box_h//2), fill=config["accent"])
                draw.point((cx - box_w//2 + i, cy + box_h//2), fill=config["accent"])
            elif i < box_w + box_h:
                j = i - box_w
                draw.point((cx + box_w//2, cy - box_h//2 + j), fill=config["accent"])
            elif i < box_w*2 + box_h:
                j = i - box_w - box_h
                draw.point((cx + box_w//2 - j, cy + box_h//2), fill=config["accent"])
            else:
                j = i - box_w*2 - box_h
                draw.point((cx - box_w//2, cy + box_h//2 - j), fill=config["accent"])
        return img

    def generate_pdf_image(layout, bg_name, bg_config):
        if layout == "經典長條四格":
            w, h, grid = 400, 1200, (1, 4)
        elif layout == "2x3 六格拍貼":
            w, h, grid = 600, 900, (2, 3)
        else:
            w, h, grid = 800, 600, (1, 1)

        img = Image.new("RGB", (w, h), bg_config["bg"])
        draw = ImageDraw.Draw(img)
        draw.rectangle([10, 10, w-11, h-11], outline=bg_config["accent"], width=4)

        cols, rows = grid
        pad = 20
        cell_w = (w - pad * (cols + 1)) // cols
        cell_h = (h - pad * (rows + 1) - 60) // rows

        for r in range(rows):
            for c in range(cols):
                x = pad + c * (cell_w + pad)
                y = pad + r * (cell_h + pad)
                draw.rectangle([x, y, x + cell_w, y + cell_h], fill="white", outline=bg_config["accent"], width=2)
                cx, cy = x + cell_w // 2, y + cell_h // 2
                draw.ellipse([cx-25, cy-35, cx+25, cy+15], fill="#ffdab9")
                draw.ellipse([cx-30, cy+15, cx+30, cy+55], fill=bg_config["accent"])
                draw.ellipse([x+5, y+5, x+15, y+15], fill=bg_config["accent"])
                draw.ellipse([x+cell_w-15, y+5, x+cell_w-5, y+15], fill=bg_config["accent"])

        try:
            font = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 18)
        except (OSError, IOError):
            font = ImageFont.load_default()
        text = f"AI 領航員 PhotoBooth | {bg_name}風格 | {layout}"
        bbox = draw.textbbox((0, 0), text, font=font)
        tw = bbox[2] - bbox[0]
        draw.text(((w - tw) // 2, h - 45), text, fill=bg_config["accent"], font=font)
        return img

    def composite_photo_on_bg(photo_img, bg_config, size=(200, 200)):
        """將拍攝的照片合成到背景板上"""
        bg = Image.new("RGB", size, bg_config["bg"])
        draw = ImageDraw.Draw(bg)
        # 裝飾邊框
        draw.rectangle([3, 3, size[0]-4, size[1]-4], outline=bg_config["accent"], width=2)
        # 縮放照片並置中
        pad = 15
        inner_w, inner_h = size[0] - pad*2, size[1] - pad*2
        photo_resized = photo_img.resize((inner_w, inner_h), Image.LANCZOS)
        bg.paste(photo_resized, (pad, pad))
        # 角落裝飾
        for x, y in [(5, 5), (size[0]-15, 5), (5, size[1]-15), (size[0]-15, size[1]-15)]:
            draw.ellipse([x, y, x+10, y+10], fill=bg_config["accent"])
        return bg

    def generate_pdf_with_photos(layout, bg_name, bg_config, photo_list):
        """用實際拍攝照片產生列印成品"""
        if layout == "經典長條四格":
            w, h, grid = 400, 1200, (1, 4)
        elif layout == "2x3 六格拍貼":
            w, h, grid = 600, 900, (2, 3)
        else:
            w, h, grid = 800, 600, (1, 1)

        img = Image.new("RGB", (w, h), bg_config["bg"])
        draw = ImageDraw.Draw(img)
        draw.rectangle([10, 10, w-11, h-11], outline=bg_config["accent"], width=4)
        # 角落大裝飾
        for ox, oy in [(15, 15), (w-35, 15), (15, h-35), (w-35, h-35)]:
            draw.ellipse([ox, oy, ox+20, oy+20], fill=bg_config["accent"])

        cols_n, rows_n = grid
        pad = 20
        cell_w = (w - pad * (cols_n + 1)) // cols_n
        cell_h = (h - pad * (rows_n + 1) - 60) // rows_n

        idx = 0
        for r in range(rows_n):
            for c in range(cols_n):
                x = pad + c * (cell_w + pad)
                y = pad + r * (cell_h + pad)
                draw.rectangle([x, y, x + cell_w, y + cell_h], fill="white", outline=bg_config["accent"], width=2)
                if idx < len(photo_list) and photo_list[idx] is not None:
                    photo = photo_list[idx].resize((cell_w - 10, cell_h - 10), Image.LANCZOS)
                    img.paste(photo, (x + 5, y + 5))
                else:
                    cx, cy = x + cell_w // 2, y + cell_h // 2
                    draw.ellipse([cx-25, cy-35, cx+25, cy+15], fill="#ffdab9")
                    draw.ellipse([cx-30, cy+15, cx+30, cy+55], fill=bg_config["accent"])
                idx += 1

        try:
            font = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 18)
        except (OSError, IOError):
            font = ImageFont.load_default()
        text = f"AI 領航員 PhotoBooth | {bg_name}風格 | {layout}"
        bbox = draw.textbbox((0, 0), text, font=font)
        tw = bbox[2] - bbox[0]
        draw.text(((w - tw) // 2, h - 45), text, fill=bg_config["accent"], font=font)
        return img

    # --- 濾鏡效果函式 ---
    def apply_filter(img, filter_name):
        """套用濾鏡效果到照片"""
        if filter_name == "原圖":
            return img.copy()
        elif filter_name == "黑白":
            return img.convert("L").convert("RGB")
        elif filter_name == "柔化":
            return img.filter(ImageFilter.GaussianBlur(radius=2))
        elif filter_name == "銳利":
            return img.filter(ImageFilter.SHARPEN)
        elif filter_name == "柔邊":
            return img.filter(ImageFilter.SMOOTH_MORE)
        return img.copy()

    TOTAL_SHOTS = 4

    # --- 拍貼機模擬器邏輯 ---
    if 'stage' not in st.session_state: st.session_state.stage = "payment"
    if 'photos' not in st.session_state: st.session_state.photos = 0
    if 'photo_images' not in st.session_state: st.session_state.photo_images = []
    if 'selected_bg' not in st.session_state: st.session_state.selected_bg = None
    if 'shooting_started' not in st.session_state: st.session_state.shooting_started = False
    if 'selected_filter' not in st.session_state: st.session_state.selected_filter = "原圖"
    if 'retake_index' not in st.session_state: st.session_state.retake_index = None

    with st.sidebar:
        st.divider()
        st.subheader("📟 硬體日誌 (Monitor)")
        if st.session_state.stage == "payment": st.write("`[系統]` 等待支付中...")
        elif st.session_state.stage == "filter_select": st.write("`[系統]` 等待選擇濾鏡...")
        elif st.session_state.stage == "shooting": st.write("`[相機]` 燈光已就緒，定時拍攝模式")
        elif st.session_state.stage == "review": st.write("`[系統]` 照片確認中...")
        elif st.session_state.stage == "format_select": st.write("`[系統]` 等待選擇輸出格式...")
        elif st.session_state.stage == "output": st.write("`[印表機]` 紙張充足，準備出圖")

    if st.session_state.stage == "payment":
        st.subheader("第一階段：啟動與支付")
        st.write("目前設備狀態：待機中")
        col_pay1, col_pay2 = st.columns(2)
        with col_pay1:
            if st.button("🧧 模擬投入紙鈔 $100"):
                st.session_state.stage = "filter_select"
                st.rerun()
        with col_pay2:
            st.button("📱 iPad 支付介面 (開發中)", disabled=True)

    elif st.session_state.stage == "filter_select":
        st.subheader("第二階段：選擇濾鏡")
        st.markdown("請選擇拍攝時要套用的濾鏡效果，所有照片將使用相同濾鏡：")

        # 生成預覽底圖
        preview_base = Image.new("RGB", (200, 200), "#4ECDC4")
        draw_p = ImageDraw.Draw(preview_base)
        draw_p.ellipse([50, 50, 150, 150], fill="#FF6B6B")
        draw_p.text((75, 85), "Preview", fill="white")

        filter_names = ["原圖", "黑白", "柔化", "銳利", "柔邊"]
        filter_cols = st.columns(5)
        for i, fname in enumerate(filter_names):
            with filter_cols[i]:
                filtered_preview = apply_filter(preview_base, fname)
                st.image(filtered_preview, caption=fname, use_container_width=True)
                if st.button(f"選擇「{fname}」", key=f"filter_{fname}"):
                    st.session_state.selected_filter = fname

        st.markdown("")
        st.info(f"目前選擇：**{st.session_state.selected_filter}**")

        if st.button("✅ 確認濾鏡，開始拍攝"):
            st.session_state.stage = "shooting"
            st.rerun()

    elif st.session_state.stage == "shooting":
        st.subheader(f"第三階段：定時拍攝 ({st.session_state.photos}/{TOTAL_SHOTS})")
        st.progress(st.session_state.photos / TOTAL_SHOTS)
        st.caption(f"🎨 濾鏡：{st.session_state.selected_filter}")

        # 顯示已拍照片的縮圖進度
        thumb_cols = st.columns(TOTAL_SHOTS)
        for i in range(TOTAL_SHOTS):
            with thumb_cols[i]:
                if i < len(st.session_state.photo_images):
                    st.image(st.session_state.photo_images[i], caption=f"第 {i+1} 張", use_container_width=True)
                else:
                    st.markdown(f"""
                    <div style="background: #333; border: 2px dashed #666; border-radius: 8px;
                                aspect-ratio: 1; display: flex; align-items: center;
                                justify-content: center; color: #666; font-size: 24px;">
                        {i+1}
                    </div>
                    """, unsafe_allow_html=True)

        st.markdown("")

        is_retake = st.session_state.retake_index is not None
        remaining = 1 if is_retake else (TOTAL_SHOTS - st.session_state.photos)

        if remaining > 0:
            if not st.session_state.shooting_started:
                if is_retake:
                    st.info(f"📸 即將重拍第 {st.session_state.retake_index + 1} 張照片。")
                else:
                    st.info(f"📸 按下開始後，系統將每 5 秒自動拍攝一張，共 {TOTAL_SHOTS} 張。請準備好姿勢！")

                # 相機預覽區
                st.markdown("""
                <div style="background: #1a1a2e; border: 2px solid #16213e; border-radius: 12px;
                            padding: 40px; text-align: center; margin: 10px 0;">
                    <p style="font-size: 60px; margin: 0;">📷</p>
                    <p style="color: #e94560; font-size: 18px; font-weight: bold;">相機預覽畫面</p>
                    <p style="color: #888; font-size: 14px;">（實際部署時此區域會顯示即時相機畫面）</p>
                </div>
                """, unsafe_allow_html=True)

                if st.button("🎬 開始自動拍攝" if not is_retake else "🎬 開始重拍"):
                    st.session_state.shooting_started = True
                    st.rerun()
            else:
                # 相機預覽 + 倒數
                preview_area = st.empty()
                countdown_area = st.empty()

                shot_num = (st.session_state.retake_index + 1) if is_retake else (st.session_state.photos + 1)

                # 顯示相機預覽
                preview_area.markdown("""
                <div style="background: #1a1a2e; border: 2px solid #e94560; border-radius: 12px;
                            padding: 30px; text-align: center;">
                    <p style="font-size: 48px; margin: 0;">📷</p>
                    <p style="color: #e94560; font-size: 16px;">🔴 相機預覽中 — 請看鏡頭</p>
                </div>
                """, unsafe_allow_html=True)

                # 5 秒倒數
                for sec in range(5, 0, -1):
                    countdown_area.markdown(f"""
                    <div style="text-align: center; padding: 20px;">
                        <p style="font-size: 18px; color: #aaa;">第 {shot_num} 張即將拍攝</p>
                        <p style="font-size: 100px; font-weight: bold; color: #FF6B6B; line-height: 1;">{sec}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    time.sleep(1)

                # 模擬快門閃光
                preview_area.empty()
                countdown_area.markdown("""
                <div style="text-align: center; padding: 30px; background: white; border-radius: 12px;">
                    <p style="font-size: 48px; color: #333;">📸 咔嚓！</p>
                </div>
                """, unsafe_allow_html=True)
                time.sleep(0.5)
                countdown_area.empty()

                # 生成模擬照片 + 套用濾鏡
                colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4"]
                idx = (st.session_state.retake_index if is_retake else st.session_state.photos)
                color = colors[idx % len(colors)]
                sim_photo = Image.new("RGB", (400, 400), color)
                draw = ImageDraw.Draw(sim_photo)
                draw.text((150, 170), f"#{shot_num}", fill="white")
                circle_r = 60
                cx, cy = 200, 200
                draw.ellipse([cx - circle_r, cy - circle_r, cx + circle_r, cy + circle_r], outline="white", width=3)

                # 套用濾鏡
                sim_photo = apply_filter(sim_photo, st.session_state.selected_filter)

                if is_retake:
                    st.session_state.photo_images[st.session_state.retake_index] = sim_photo
                    st.toast(f"第 {shot_num} 張重拍完成！")
                    st.session_state.retake_index = None
                    st.session_state.shooting_started = False
                    st.session_state.stage = "review"
                    st.rerun()
                else:
                    st.session_state.photo_images.append(sim_photo)
                    st.session_state.photos += 1
                    st.toast(f"第 {st.session_state.photos} 張拍攝完成！")

                    if st.session_state.photos < TOTAL_SHOTS:
                        time.sleep(0.3)
                        st.rerun()
                    else:
                        st.session_state.shooting_started = False
                        st.session_state.stage = "review"
                        st.rerun()
        else:
            st.session_state.stage = "review"
            st.rerun()

    elif st.session_state.stage == "review":
        st.subheader("第四階段：確認照片")
        st.markdown(f"🎨 濾鏡：**{st.session_state.selected_filter}** — 請確認每張照片，不滿意的可以選擇重拍：")

        review_cols = st.columns(TOTAL_SHOTS)
        for i, photo in enumerate(st.session_state.photo_images):
            with review_cols[i]:
                st.image(photo, caption=f"第 {i+1} 張", use_container_width=True)
                if st.button(f"🔄 重拍第 {i+1} 張", key=f"retake_{i}"):
                    st.session_state.retake_index = i
                    st.session_state.shooting_started = False
                    st.session_state.stage = "shooting"
                    st.rerun()

        st.markdown("")
        if st.button("👍 照片全部 OK，選擇輸出格式"):
            st.session_state.stage = "format_select"
            st.rerun()

    elif st.session_state.stage == "format_select":
        st.subheader("第三階段：選擇格式")

        # 背景板選擇
        st.markdown("**1. 選擇背景板風格**")
        st.markdown("我們提供多款 IP 合作背景板，請選擇您喜歡的風格：")

        preview_photo = st.session_state.photo_images[0] if st.session_state.photo_images else None

        bg_cols = st.columns(3)
        for i, (bg_name, bg_config) in enumerate(BACKGROUNDS.items()):
            with bg_cols[i % 3]:
                if preview_photo:
                    preview = composite_photo_on_bg(preview_photo, bg_config, size=(300, 300))
                else:
                    preview = generate_background_preview(bg_name, bg_config)
                st.image(preview, use_container_width=True)
                st.markdown(f"**{bg_config['deco']} {bg_name}**")
                st.caption(bg_config["desc"])
                if st.button(f"選擇「{bg_name}」", key=f"bg_{bg_name}"):
                    st.session_state.selected_bg = bg_name

        st.divider()

        # 版型選擇
        st.markdown("**2. 選擇列印版型**")
        layout = st.radio("請選擇您的繁體中文列印版型：", ["經典長條四格", "2x3 六格拍貼", "4x6 紀念大張"], key="layout_radio")

        # 預覽合成效果
        if st.session_state.selected_bg:
            bg_name = st.session_state.selected_bg
            bg_config = BACKGROUNDS[bg_name]
            st.markdown(f"**預覽：{bg_config['deco']} {bg_name}**")
            preview_cols = st.columns(TOTAL_SHOTS)
            for i, photo in enumerate(st.session_state.photo_images):
                with preview_cols[i]:
                    comp = composite_photo_on_bg(photo, bg_config, size=(150, 150))
                    st.image(comp, caption=f"第 {i+1} 張", use_container_width=True)

        st.markdown("")
        if st.button("✅ 確認格式，開始出圖", disabled=(st.session_state.selected_bg is None)):
            st.session_state.selected_layout = layout
            st.session_state.stage = "output"
            st.rerun()

    elif st.session_state.stage == "output":
        st.subheader("第四階段：出圖")

        bg_name = st.session_state.selected_bg or "經典白"
        bg_config = BACKGROUNDS[bg_name]
        layout = st.session_state.get("selected_layout", "2x3 六格拍貼")

        with st.spinner("正在進行影像合成與輸出..."):
            time.sleep(2)

        st.success("✅ 出圖完成！")

        result_img = generate_pdf_with_photos(layout, bg_name, bg_config, st.session_state.photo_images)
        st.image(result_img, caption=f"{layout} — {bg_name}風格", use_container_width=True)

        pdf_buffer = io.BytesIO()
        rgb_img = result_img.convert("RGB")
        rgb_img.save(pdf_buffer, format="PDF", resolution=150)
        pdf_buffer.seek(0)

        st.download_button(
            label="📥 下載 PDF 檔案",
            data=pdf_buffer,
            file_name=f"photobooth_{bg_name}_{layout}.pdf",
            mime="application/pdf",
        )

        st.markdown("")
        if st.button("🔄 重新開始"):
            st.session_state.stage = "payment"
            st.session_state.photos = 0
            st.session_state.photo_images = []
            st.session_state.selected_bg = None
            st.session_state.shooting_started = False
            st.session_state.selected_layout = None
            st.session_state.selected_filter = "原圖"
            st.session_state.retake_index = None
            st.rerun()

# =====================================================
# 第二堂課
# =====================================================

elif current_section == "R1. 上堂回顧與 Q&A":
    lesson_cover(2, "實戰體驗與案例", "看一次真正的 Vibe Coding 實戰，從提問到產出", "🎬")
    st.title("🔄 上堂回顧與 Q&A")

    st.subheader("📋 第一堂重點複習")
    col_r1, col_r2, col_r3 = st.columns(3)
    with col_r1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    border-radius: 15px; padding: 25px; color: white; min-height: 180px;">
            <h4 style="color: white; text-align:center;">🧩 Vibe Coding</h4>
            <hr style="border-color: rgba(255,255,255,0.3);">
            <p style="font-size:14px;">用自然語言描述意圖，讓 AI 幫你寫程式。核心公式：背景 + 目標 + 風格</p>
        </div>
        """, unsafe_allow_html=True)
    with col_r2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                    border-radius: 15px; padding: 25px; color: white; min-height: 180px;">
            <h4 style="color: white; text-align:center;">📸 照相任務進化</h4>
            <hr style="border-color: rgba(255,255,255,0.3);">
            <p style="font-size:14px;">語系在地化不只是翻譯，更是讓操作邏輯符合台灣習慣。</p>
        </div>
        """, unsafe_allow_html=True)
    with col_r3:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
                    border-radius: 15px; padding: 25px; color: white; min-height: 180px;">
            <h4 style="color: white; text-align:center;">🎯 拍貼機 Demo</h4>
            <hr style="border-color: rgba(255,255,255,0.3);">
            <p style="font-size:14px;">完整走過支付 → 拍照 → 背景板 → 列印的原型流程。</p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()
    st.subheader("❓ 上堂課後的疑問與發現")
    st.markdown("請分享你在上次課後嘗試操作時遇到的問題或新發現：")
    st.text_area("你的問題或心得", key="review_qa", height=120,
                 placeholder="例：我試著用 Prompt 請 AI 修改介面，但結果不如預期...")

    st.divider()
    st.subheader("🎯 第二堂課目標")
    st.markdown("""
    今天我們將進入**實戰體驗**階段：
    1. 實際操作拍貼機原型系統 Demo
    2. 看一個真實的 Vibe Coding 案例（帳號與權限系統）
    """)

elif current_section == "6. Vibe Coding 實戰案例":
    st.title("🎬 Vibe Coding 實戰案例：帳號與權限系統")

    st.markdown("""
    這個案例來自**真實專案開發過程**。我們會完整拆解一次 Vibe Coding 的流程：
    從「怎麼問」到「AI 怎麼拆解」到「最終執行了什麼」，讓你看到 AI Agent 實際上是如何工作的。
    """)

    tab_ask, tab_analyze, tab_result = st.tabs([
        "📝 第一步：怎麼問",
        "🔍 第二步：AI 如何拆解",
        "✅ 第三步：執行結果"
    ])

    # ======== Tab 1：怎麼問 ========
    with tab_ask:
        st.subheader("📝 實際的提問方式")
        st.markdown("以下是開發者**實際輸入給 AI Agent（Claude Code）的一段話**：")

        st.markdown("""
        <div style="background: #1e1e1e; border-left: 4px solid #0984e3; border-radius: 8px;
                    padding: 25px; color: #dfe6e9; font-size: 14px; line-height: 2; font-family: monospace;">
            <span style="color: #74b9ff;">❯</span> 我在會員頁登錄完之後，為什麼還會出現登錄的按鈕？另外我在 Profile 頁，我按儲存好像都沒有效果。
            另外，我的 0936-xxx-xxx 之前有管理者的權限，現在又沒有了。你幫我說明一下，我現在的會員登錄帳號有哪些不同的角色？<br><br>

            我希望要有以下幾種角色：<br>
            1. 系統角色<br>
            2. 管理人員角色<br>
            3. 一般用戶角色<br><br>

            針對帳號與登入機制，我希望：<br><br>

            <strong style="color: #ffeaa7;">1. 建立一個 Admin 帳號：</strong><br>
            &nbsp;&nbsp;&nbsp;這是一個具備無上權限的固定帳號，可以看到所有的功能。<br><br>

            <strong style="color: #ffeaa7;">2. 強化登入安全性：</strong><br>
            &nbsp;&nbsp;&nbsp;請建議如何避免被他人隨意登入。目前考慮兩種方式：<br>
            &nbsp;&nbsp;&nbsp;(a) 使用密碼登入<br>
            &nbsp;&nbsp;&nbsp;(b) 使用手機驗證（一定要透過手機 OTP 驗證才能進入）<br><br>

            <strong style="color: #ffeaa7;">3. 建立一個 Guest（訪客）帳號：</strong><br>
            &nbsp;&nbsp;&nbsp;我希望增加一個訪客功能。訪客雖然不能實際操作使用，但可以看到上課的畫面，
            瞭解我們上課的樣子，像是進入教室看老師對話，提供試用或瞭解的管道。
            這個 Guest 帳號應該是讓任何人就算沒有註冊，也可以先進行訪問使用。
        </div>
        """, unsafe_allow_html=True)

        st.markdown("")
        st.subheader("🔑 這段提問的關鍵技巧")

        col_t1, col_t2, col_t3 = st.columns(3)
        with col_t1:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #e17055 0%, #d63031 100%);
                        border-radius: 12px; padding: 20px; color: white; min-height: 180px;">
                <h4 style="color: white; text-align:center;">🐛 先報 Bug</h4>
                <hr style="border-color: rgba(255,255,255,0.3);">
                <p style="font-size: 13px;">先描述目前遇到的問題（登入按鈕、儲存無效、權限消失），讓 AI 理解現狀。</p>
            </div>
            """, unsafe_allow_html=True)
        with col_t2:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #0984e3 0%, #6c5ce7 100%);
                        border-radius: 12px; padding: 20px; color: white; min-height: 180px;">
                <h4 style="color: white; text-align:center;">🏗️ 再給架構</h4>
                <hr style="border-color: rgba(255,255,255,0.3);">
                <p style="font-size: 13px;">說明期望的角色分類（系統、管理、一般），讓 AI 知道設計方向。</p>
            </div>
            """, unsafe_allow_html=True)
        with col_t3:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #00b894 0%, #00cec9 100%);
                        border-radius: 12px; padding: 20px; color: white; min-height: 180px;">
                <h4 style="color: white; text-align:center;">📋 最後列需求</h4>
                <hr style="border-color: rgba(255,255,255,0.3);">
                <p style="font-size: 13px;">具體列出每個功能的細節（Admin、OTP、Guest），讓 AI 能一次規劃完整方案。</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("")
        st.info("💡 **核心觀念：** 一次把「問題 + 期望 + 細節」講清楚，AI 就能一次性規劃出完整的執行方案，而不是一步一步問來問去。")

    # ======== Tab 2：AI 如何拆解 ========
    with tab_analyze:
        st.subheader("🔍 AI 收到問題後的拆解過程")
        st.markdown("AI Agent 收到上面那段話後，自動辨識出**三類問題**和**三項新需求**，然後規劃成 8 個執行階段：")

        st.markdown("")
        col_bug, col_feat = st.columns(2)
        with col_bug:
            st.markdown("""
            <div style="background: #2d3436; border-radius: 12px; padding: 20px; color: white;">
                <h4 style="color: #ff7675;">🐛 辨識出的問題（3 個）</h4>
                <hr style="border-color: rgba(255,255,255,0.2);">
                <p>1. 登入後還顯示登入按鈕 → <strong>Auth Provider Bug</strong></p>
                <p>2. Profile 儲存無效 → <strong>儲存邏輯 Bug</strong></p>
                <p>3. 管理者權限消失 → <strong>角色判斷不一致</strong></p>
            </div>
            """, unsafe_allow_html=True)
        with col_feat:
            st.markdown("""
            <div style="background: #2d3436; border-radius: 12px; padding: 20px; color: white;">
                <h4 style="color: #74b9ff;">🆕 辨識出的新需求（3 個）</h4>
                <hr style="border-color: rgba(255,255,255,0.2);">
                <p>1. 三種角色分類 → <strong>角色系統設計</strong></p>
                <p>2. Admin + OTP 驗證 → <strong>安全登入機制</strong></p>
                <p>3. Guest 訪客模式 → <strong>免註冊體驗功能</strong></p>
            </div>
            """, unsafe_allow_html=True)

        st.divider()
        st.subheader("📋 AI 規劃的 8 個執行階段")
        st.markdown("AI 把這些問題與需求，按照**依賴順序**排列成執行計畫：")

        phases = [
            ("Phase 1-2", "角色基礎建設", "建立角色判斷工具函式 + 資料庫角色約束", "先打地基：定義 user / admin / superadmin 三種角色"),
            ("Phase 3", "Auth Provider 修復", "修正登入後 header 仍顯示登入按鈕的 Bug", "解決使用者回報的第一個問題"),
            ("Phase 4", "權限檢查統一", "統一 6 處權限判斷邏輯", "讓 superadmin 也能進入管理後台"),
            ("Phase 5", "Superadmin OTP 登入", "新增手機 OTP 兩步驟驗證", "Admin 帳號的安全強化"),
            ("Phase 6", "Superadmin 帳號建立", "建立自動建立/升級 Admin 帳號的 API", "讓系統管理員可以安全建立最高權限帳號"),
            ("Phase 7", "Guest 訪客體驗", "建立免登入的唯讀瀏覽頁面", "訪客可以看到上課畫面但不能操作"),
            ("Phase 8", "Profile 儲存修復", "修正儲存後沒有反應的 Bug", "解決使用者回報的第二個問題"),
        ]

        for i, (phase, title, action, reason) in enumerate(phases):
            with st.expander(f"{phase}：{title}", expanded=(i < 3)):
                col_do, col_why = st.columns([6, 4])
                with col_do:
                    st.markdown(f"**執行內容：** {action}")
                with col_why:
                    st.markdown(f"**為什麼這步：** {reason}")

        st.markdown("")
        st.warning("⚠️ **注意順序邏輯：** AI 不是隨便排的——先建角色基礎（Phase 1-2），才能修權限判斷（Phase 3-4），才能做 OTP（Phase 5）。這就是 AI Agent 的規劃能力。")

    # ======== Tab 3：執行結果 ========
    with tab_result:
        st.subheader("✅ 最終執行成果")
        st.markdown("AI Agent 自動完成了以下所有變更，以下是每個階段的具體產出：")

        result_data = [
            {
                "phase": "Phase 1-2：角色基礎",
                "files": ["src/lib/roles.ts", "supabase/migrations/005_add_role_constraint.sql"],
                "details": [
                    "`isAdminRole()` / `isSuperAdmin()` 工具函式",
                    "DB 約束：user / admin / superadmin 三種角色",
                ],
                "color": "#6c5ce7",
            },
            {
                "phase": "Phase 3：Auth Provider 修復",
                "files": ["src/components/providers/auth-provider.tsx"],
                "details": [
                    "`onAuthStateChange` 現在會重新查 role",
                    "Context 新增 role / isSuperAdmin",
                ],
                "color": "#0984e3",
            },
            {
                "phase": "Phase 4：權限檢查統一",
                "files": ["manage layout + 5 個 API route"],
                "details": [
                    "全改為 `isAdminRole()`",
                    "superadmin 也能進後台（共 6 處）",
                ],
                "color": "#00b894",
            },
            {
                "phase": "Phase 5：OTP 兩步驟登入",
                "files": ["src/app/(public)/login/actions.ts", "src/components/auth/login-form.tsx"],
                "details": [
                    "偵測 superadmin → 驗密碼 → 送 OTP → 驗證後登入",
                    "新增 OTP 輸入介面（4 碼 + 60 秒 cooldown + 重發）",
                ],
                "color": "#e17055",
            },
            {
                "phase": "Phase 6：Superadmin 帳號建立",
                "files": ["src/app/api/setup/superadmin/route.ts", ".env.local"],
                "details": [
                    "POST + SETUP_SECRET → 自動建立/升級帳號",
                    "新增 SUPERADMIN_PHONE / SUPERADMIN_PASSWORD / SETUP_SECRET 環境變數",
                ],
                "color": "#fdcb6e",
            },
            {
                "phase": "Phase 7：Guest 訪客體驗",
                "files": ["src/app/(public)/guest/[serviceCode]/page.tsx", "src/components/dashboard/learning-dashboard.tsx"],
                "details": [
                    "不需登入的唯讀課程頁",
                    "readonly 模式：隱藏聊天、顯示橘色 banner + 註冊按鈕",
                    "首頁 + 登入頁加「免費體驗」入口 → /guest/happy",
                ],
                "color": "#a29bfe",
            },
            {
                "phase": "Phase 8：Profile 儲存修復",
                "files": ["src/components/dashboard/profile-form.tsx"],
                "details": [
                    "儲存後 `reset(data)` + `router.refresh()`",
                ],
                "color": "#55efc4",
            },
        ]

        for item in result_data:
            st.markdown(f"""
            <div style="border-left: 4px solid {item['color']}; padding: 15px 20px; margin-bottom: 15px;
                        background: rgba(45,52,54,0.5); border-radius: 0 8px 8px 0;">
                <strong style="color: {item['color']}; font-size: 16px;">{item['phase']}</strong><br>
                <span style="color: #b2bec3; font-size: 13px;">📁 {' / '.join(item['files'])}</span>
                <ul style="margin-top: 8px; color: #dfe6e9;">
                    {''.join(f'<li style="font-size: 14px;">{d}</li>' for d in item['details'])}
                </ul>
            </div>
            """, unsafe_allow_html=True)

        st.divider()
        st.subheader("🧮 數據統計")
        col_s1, col_s2, col_s3, col_s4 = st.columns(4)
        with col_s1:
            st.metric("執行階段", "8 個 Phase")
        with col_s2:
            st.metric("修改檔案", "~15 個")
        with col_s3:
            st.metric("Bug 修復", "3 個")
        with col_s4:
            st.metric("新功能", "3 項")

        st.markdown("")
        st.success("""
        **重點回顧：** 一段自然語言的描述，AI Agent 自動完成了：
        - 分析問題根因
        - 規劃執行順序（考慮依賴關係）
        - 修改 15+ 個檔案
        - 修復 3 個 Bug + 建立 3 項新功能

        **這就是 Vibe Coding 的威力。**
        """)

elif current_section == "6.5. 代碼考古學":
    st.title("🏺 代碼考古學：讀懂現有系統")

    st.markdown("""
    要重構拍貼機系統，第一步不是「寫新的」，而是「**讀懂舊的**」。
    這堂課我們學習如何用 AI 幫你「考古」——把看不懂的源碼變成你看得懂的架構圖。
    """)

    tab_why, tab_how, tab_mermaid = st.tabs(["🤔 為什麼要考古", "🔍 AI 輔助解讀", "📊 架構圖實作"])

    with tab_why:
        st.markdown("### 不讀舊碼就改版，最常踩到的坑")

        pitfalls = [
            ("🕳️ 隱藏依賴", "舊系統裡可能有你沒注意到的硬體呼叫順序，改了 A 結果 B 壞了。"),
            ("🔤 編碼地雷", "簡體系統的字串編碼（GB2312）跟繁體（UTF-8）不同，直接改字會亂碼。"),
            ("⏱️ 時序陷阱", "投幣機的訊號要在 200ms 內回應，否則硬體會判定逾時，這種邏輯藏在深處。"),
            ("🔑 寫死的設定", "原廠可能把 API Key、IP 位址寫死在程式碼裡，不讀碼你根本找不到。"),
        ]

        for icon_title, desc in pitfalls:
            st.markdown(f"**{icon_title}**：{desc}")

        st.markdown("")
        st.warning("⚠️ **經驗法則：** 花 1 小時讀懂舊碼，能省下 10 小時的除錯時間。")

    with tab_how:
        st.markdown("### 用 AI 解讀你看不懂的程式碼")
        st.markdown("你不需要自己讀懂每一行，只需要會「問 AI」。以下是實用的提問範本：")

        prompts = [
            {
                "scenario": "拿到整個專案，不知從何看起",
                "prompt": "這是一個 PhotoBooth 拍貼機的系統源碼。請幫我分析專案結構，\n列出每個資料夾和主要檔案的用途，並標記哪些是核心業務邏輯。",
            },
            {
                "scenario": "看到一段看不懂的函式",
                "prompt": "請用繁體中文解釋這段程式碼在做什麼。\n請特別說明：1. 輸入和輸出 2. 有沒有跟硬體溝通 3. 可能的副作用",
            },
            {
                "scenario": "想知道資料怎麼流動",
                "prompt": "請追蹤從「使用者投幣」到「照片列印完成」的完整資料流。\n列出每一步經過哪個函式、哪個模組，用 Mermaid 流程圖表示。",
            },
        ]

        for p in prompts:
            with st.expander(f"情境：{p['scenario']}"):
                st.code(p["prompt"], language=None)

        st.info("💡 **訣竅：** 不要一次丟整個專案給 AI。先讓它看目錄結構，再針對重要檔案逐一深入。")

    with tab_mermaid:
        st.markdown("### 讓 AI 幫你畫架構圖（Mermaid）")
        st.markdown("Mermaid 是一種用文字描述圖表的語法，AI 特別擅長產出這種格式。")

        st.markdown("**範例：PhotoBooth 系統流程圖**")
        st.code("""graph TD
    A[使用者進入] --> B{投幣/掃碼}
    B -->|投幣| C[投幣機偵測金額]
    B -->|掃碼| D[QR Code 支付驗證]
    C --> E[金額足夠？]
    D --> E
    E -->|是| F[進入拍照模式]
    E -->|否| G[顯示餘額不足]
    F --> H[倒數計時拍照]
    H --> I[選擇背景/濾鏡]
    I --> J[合成照片]
    J --> K[送至印表機]
    K --> L[列印完成]
    L --> M[回到待機畫面]""", language="mermaid")

        st.markdown("**你可以這樣請 AI 幫你畫：**")
        st.code("""請根據我們剛才分析的程式碼，用 Mermaid 語法畫出：
1. 系統整體架構圖（哪些模組、如何連接）
2. 使用者操作流程圖（從進門到拿到照片）
3. 硬體通訊時序圖（投幣 → 拍照 → 列印的訊號順序）""", language=None)

        st.divider()
        st.markdown("#### 🎯 現場練習")
        st.markdown("如果你手上有現有系統的任何程式碼片段或截圖，現在就可以試試看：")
        code_input = st.text_area("貼上一段程式碼或描述系統的某個流程",
                                  key="archaeology_input", height=150,
                                  placeholder="例如：貼上投幣機的控制程式碼，或描述「客人拍完照之後發生了什麼事」")
        if code_input:
            st.info("👆 把這段內容複製到 Claude，請它用 Mermaid 畫出流程圖！")

elif current_section == "HW2. 課後練習":
    st.title("📝 課後練習：用 AI 完成一個小功能")

    st.markdown("這次的練習目標是**親手體驗 Vibe Coding**，讓你實際感受 AI 如何幫你寫程式。")

    st.divider()
    st.subheader("🎯 練習任務")
    st.markdown("""
    請選擇以下其中一個任務，用 Claude 或 ChatGPT 完成：

    **任務 A：修改拍貼機的一個功能**
    > 「請幫我修改拍貼機的歡迎畫面，加上我們公司的 Logo 和一段歡迎語。」

    **任務 B：做一個小工具**
    > 「請幫我做一個簡單的計算機，可以計算今天的營業額（輸入拍照次數 × 單價）。」

    **任務 C：描述你自己的一個需求**
    > 用上堂課學到的「背景 + 目標 + 風格」公式，描述一個你工作上需要的功能。
    """)

    st.divider()
    st.subheader("📋 練習重點")
    st.info("""
    1. **不需要寫程式** — 用自然語言描述即可
    2. **記錄你的對話** — 截圖保存你跟 AI 的對話過程
    3. **觀察 AI 的拆解方式** — 看它如何把你的需求拆成步驟
    """)

    st.subheader("📤 繳交作業")
    student2 = st.text_input("你的名字", key="hw2_name", placeholder="例：JD")
    hw2_file = st.file_uploader(
        "上傳對話截圖或 AI 產出的程式碼",
        type=["png", "jpg", "jpeg", "pdf", "txt", "py", "md"],
        key="hw2_upload",
    )
    if hw2_file and student2:
        path, gdrive_link = save_uploaded_file(hw2_file, "HW2", student2)
        st.success(f"✅ 作業已儲存！檔案：`{os.path.basename(path)}`")
        if gdrive_link:
            st.info(f"☁️ 已同步到 Google Drive")
    elif hw2_file and not student2:
        st.warning("請先填寫你的名字再上傳。")

# =====================================================
# 第三堂課：需求分析與架構規劃
# =====================================================

elif current_section == "R2. 上堂回顧與 Q&A":
    lesson_cover(3, "需求分析與架構規劃", "深掘真實痛點，學習系統性描述需求的方法", "🔍")
    st.title("🔄 上堂回顧：實戰體驗")

    st.subheader("📋 第二堂重點複習")
    st.markdown("""
    上堂課我們體驗了兩個重要的實戰案例：
    1. **拍貼機 Demo** — 完整走過收款 → 濾鏡 → 拍照 → 確認 → 格式 → 出圖的流程
    2. **帳號權限案例** — 看到一段自然語言如何讓 AI 自動完成 8 個階段的開發工作
    """)

    st.divider()
    st.subheader("❓ Q&A 與討論")
    st.text_area("記錄上堂課的問題或心得", key="r2_issues", height=100,
                 placeholder="例：拍貼機的流程跟我們實際的操作有什麼不同？")

    st.divider()
    st.subheader("📌 本堂課目標")
    st.markdown("""
    今天我們要學習：
    1. 深入分析真實業務痛點
    2. 練習用結構化方式描述系統需求
    3. 討論設備選型的決策方法
    """)

elif current_section == "7. 真實痛點深掘":
    st.title("🔍 真實痛點深掘")

    tab_a, tab_b = st.tabs(["🏛️ 文博會合規問題", "📊 ERP/POS 行政耗損"])

    with tab_a:
        st.subheader("為什麼現有系統無法參加政府活動？")

        col_problem, col_solution = st.columns(2)
        with col_problem:
            st.error("**現狀問題**")
            st.markdown("""
            * 系統介面含簡體字，不符合政府活動規範
            * 大陸廠商限制功能，無法依需求客製
            * 設備搬遷後需原廠技術支援才能重新設定
            * 支付系統僅支援大陸支付管道
            """)
        with col_solution:
            st.success("**解決方案**")
            st.markdown("""
            * 透過 Claude 全面掃描並替換簡體資源檔
            * 建立自有的設定檔管理流程
            * 整合台灣本地支付（LINE Pay、街口等）
            * 撰寫設備快速部署 SOP，不再依賴原廠
            """)

        st.divider()
        st.subheader("📝 合規檢查清單")
        checklist_items = [
            "所有使用者介面文字已轉為繁體中文",
            "操作用語已在地化（非單純簡轉繁）",
            "支付系統已串接台灣合法支付管道",
            "設備可由內部人員獨立完成部署與設定",
            "系統操作手冊已翻譯為繁體中文版",
        ]
        for item in checklist_items:
            st.checkbox(item, key=f"compliance_{item[:10]}")

    with tab_b:
        st.subheader("多平台重複操作的行政耗損")

        st.markdown("""
        <div style="background: #1a1a2e; border-radius: 15px; padding: 30px; color: white;">
            <h4 style="color: #e94560; text-align:center;">目前的日常作業流程</h4>
            <br>
            <div style="display:flex; justify-content:space-around; text-align:center;">
                <div>
                    <p style="font-size:36px;">📦</p>
                    <p><b>ERP 系統</b></p>
                    <p style="font-size:12px; color:#aaa;">庫存管理</p>
                </div>
                <div style="display:flex; align-items:center;"><p style="font-size:24px;">↔</p></div>
                <div>
                    <p style="font-size:36px;">🖥️</p>
                    <p><b>POS 系統</b></p>
                    <p style="font-size:12px; color:#aaa;">現場銷售</p>
                </div>
                <div style="display:flex; align-items:center;"><p style="font-size:24px;">↔</p></div>
                <div>
                    <p style="font-size:36px;">🛒</p>
                    <p><b>蝦皮 / Pinkoi</b></p>
                    <p style="font-size:12px; color:#aaa;">電商訂單</p>
                </div>
                <div style="display:flex; align-items:center;"><p style="font-size:24px;">↔</p></div>
                <div>
                    <p style="font-size:36px;">🌐</p>
                    <p><b>官方網站</b></p>
                    <p style="font-size:12px; color:#aaa;">品牌銷售</p>
                </div>
            </div>
            <br>
            <p style="text-align:center; color: #e94560; font-size:18px;">
                ⚠️ 同仁需在以上 4+ 個平台間重複登入、手動核對數據
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("")
        st.info("💡 **第二堂課後的下一步：** 利用 AI 協助設計自動化腳本，逐步串接這些平台的 API，減少人工重複作業。")

elif current_section == "13. QR Code 行動支付實作":
    st.title("💳 QR Code 行動支付實作")

    st.markdown("""
    根據專案規劃，PhotoBooth 的第一階段核心功能就是 **QR Code 行動支付**。
    以下是支付流程的互動模擬：
    """)

    if 'pay_stage' not in st.session_state: st.session_state.pay_stage = "idle"

    # 支付方式選擇
    st.subheader("Step 1：選擇支付方式")
    pay_method = st.radio("顧客選擇付款方式：", ["LINE Pay", "街口支付", "現金投幣"], horizontal=True)

    if pay_method in ["LINE Pay", "街口支付"]:
        st.subheader("Step 2：產生 QR Code")
        st.markdown(f"模擬產生 **{pay_method}** 的付款 QR Code：")

        # 用 Pillow 產生模擬 QR Code
        qr_img = Image.new("RGB", (200, 200), "white")
        draw = ImageDraw.Draw(qr_img)
        # 模擬 QR Code 圖案
        import random
        random.seed(42 if pay_method == "LINE Pay" else 99)
        for row in range(20):
            for col in range(20):
                if random.random() > 0.5:
                    x, y = 10 + col * 9, 10 + row * 9
                    draw.rectangle([x, y, x+8, y+8], fill="black")
        # 定位點
        for ox, oy in [(10, 10), (145, 10), (10, 145)]:
            draw.rectangle([ox, oy, ox+45, oy+45], fill="black")
            draw.rectangle([ox+5, oy+5, ox+40, oy+40], fill="white")
            draw.rectangle([ox+12, oy+12, ox+33, oy+33], fill="black")

        col_qr, col_info = st.columns([1, 2])
        with col_qr:
            st.image(qr_img, width=200)
        with col_info:
            if pay_method == "LINE Pay":
                color = "#00C300"
                st.markdown(f'<p style="color:{color}; font-size:24px; font-weight:bold;">LINE Pay</p>', unsafe_allow_html=True)
            else:
                color = "#FF6600"
                st.markdown(f'<p style="color:{color}; font-size:24px; font-weight:bold;">街口支付</p>', unsafe_allow_html=True)
            st.markdown("**金額：** NT$ 100")
            st.markdown("**商品：** PhotoBooth 拍照服務 x1")
            st.caption("請用手機掃描左方 QR Code 完成付款")

        st.subheader("Step 3：確認付款")
        if st.button(f"✅ 模擬 {pay_method} 付款成功"):
            st.session_state.pay_stage = "success"
            st.balloons()
            st.rerun()

    else:
        st.subheader("Step 2：投幣")
        st.markdown("請將紙鈔或硬幣投入機台：")
        if st.button("🪙 模擬投入 NT$ 100"):
            st.session_state.pay_stage = "success"
            st.balloons()
            st.rerun()

    if st.session_state.pay_stage == "success":
        st.success("🎉 付款成功！系統即將進入拍照流程...")
        st.markdown("""
        ---
        #### 💡 技術解析：這段流程需要哪些串接？
        | 項目 | 說明 |
        |---|---|
        | **支付 SDK** | LINE Pay API 或街口支付 API 的串接 |
        | **Webhook** | 接收付款成功通知的後端端點 |
        | **狀態管理** | 前端等待 → 付款中 → 成功的狀態切換 |
        | **錯誤處理** | 逾時、取消、金額不符的例外處理 |
        """)
        if st.button("🔄 重新模擬"):
            st.session_state.pay_stage = "idle"
            st.rerun()

elif current_section == "14.5. 異常處理 Vibe 化":
    st.title("🛡️ 異常處理 Vibe 化：讓錯誤訊息說人話")

    st.markdown("""
    系統出錯時，使用者看到的是什麼？如果是 `Error Code: 0x8004005`，沒有人知道該怎麼辦。
    **異常處理 Vibe 化**就是用自然語言描述需求，讓 AI 幫你把冷冰冰的錯誤訊息變成**親切的繁體中文引導**。
    """)

    tab_before_after, tab_scenarios, tab_practice = st.tabs([
        "🔄 Before vs After", "📋 常見異常情境", "🎯 實作練習"
    ])

    with tab_before_after:
        st.markdown("### 同一個錯誤，兩種體驗")

        error_pairs = [
            {
                "situation": "印表機卡紙",
                "before": "ERROR: Printer jam detected. Code: 0x0002",
                "after": "🖨️ 印表機卡紙了！\n\n請依以下步驟處理：\n1. 打開印表機上蓋\n2. 輕輕將卡住的紙張往外拉出\n3. 關上蓋子，系統會自動重新列印\n\n如需協助，請呼叫現場工作人員。",
            },
            {
                "situation": "網路斷線（支付失敗）",
                "before": "ConnectionError: Failed to reach payment gateway. Timeout after 30s.",
                "after": "📶 網路連線中斷\n\n目前無法完成行動支付。你可以：\n• 使用投幣方式付款（機台左側投幣口）\n• 稍等 30 秒後重新掃碼\n\n系統偵測到網路恢復後會自動提示你。",
            },
            {
                "situation": "相機無回應",
                "before": "cv2.error: Camera index 0 not available",
                "after": "📷 相機正在準備中...\n\n請稍候 10 秒。如果畫面仍未出現，\n請呼叫工作人員協助重新啟動相機。\n\n（系統已自動通知技術人員）",
            },
        ]

        for pair in error_pairs:
            st.markdown(f"#### {pair['situation']}")
            col_b, col_a = st.columns(2)
            with col_b:
                st.markdown(f"""
                <div style="background: #2d3436; border: 2px solid #d63031; border-radius: 8px;
                            padding: 15px; color: #ff7675; font-family: monospace; font-size: 13px;">
                    ❌ <strong>Before（原始錯誤）</strong><br><br>{pair['before']}
                </div>
                """, unsafe_allow_html=True)
            with col_a:
                st.markdown(f"""
                <div style="background: #2d3436; border: 2px solid #00b894; border-radius: 8px;
                            padding: 15px; color: #55efc4; font-size: 13px;">
                    ✅ <strong>After（Vibe 化）</strong><br><br>{pair['after'].replace(chr(10), '<br>')}
                </div>
                """, unsafe_allow_html=True)
            st.markdown("")

    with tab_scenarios:
        st.markdown("### PhotoBooth 常見異常情境清單")
        st.markdown("以下是實際營運中最常遇到的問題，每一個都需要有**使用者看得懂的引導訊息**。")

        scenarios = {
            "💰 收款相關": [
                "投幣機無法辨識硬幣（髒污或異幣）",
                "紙鈔機退鈔（鈔票皺摺或破損）",
                "QR Code 掃碼逾時（30 秒無回應）",
                "行動支付扣款成功但系統未收到通知",
            ],
            "📷 拍照相關": [
                "相機無法啟動（USB 連線中斷）",
                "拍照倒數時使用者離開感應區",
                "燈光模組故障（補光不足）",
                "連續拍照間隔過短導致相機未就緒",
            ],
            "🖨️ 列印相關": [
                "印表機離線（Wi-Fi 斷線）",
                "紙張用完",
                "墨水/色帶不足",
                "列印品質異常（模糊、偏色）",
            ],
            "🖥️ 系統相關": [
                "觸控螢幕無回應",
                "系統記憶體不足（長時間運行後）",
                "硬碟空間不足（照片累積）",
                "意外斷電後的自動恢復",
            ],
        }

        for category, items in scenarios.items():
            with st.expander(category, expanded=False):
                for item in items:
                    st.markdown(f"- {item}")

        st.info("""
        💡 **Vibe Coding 做法：** 不用自己寫每一條錯誤訊息。把這份清單交給 AI，說：
        「請針對以上每個異常情境，產出使用者友善的繁體中文提示訊息，語氣親切、步驟明確。」
        """)

    with tab_practice:
        st.markdown("### 實作：讓 AI 幫你寫異常處理")
        st.markdown("**建議 Prompt：**")
        st.code("""【背景】
我在開發 PhotoBooth 拍貼機系統（Streamlit + Python）。
系統需要在各種硬體異常時顯示使用者友善的繁體中文提示。

【目標】
請幫我建立一個 error_messages.py 模組：
1. 定義一個 ERROR_MESSAGES 字典，包含所有異常情境的提示訊息
2. 每條訊息包含：圖示 emoji、標題、說明步驟、是否需通知技術人員
3. 提供 show_error(error_code) 函式，在 Streamlit 中顯示友善提示
4. 訊息語氣親切，像是服務人員在旁邊引導

【風格】
繁體中文、台灣用語、語氣溫和但明確""", language=None)

        st.divider()
        st.markdown("#### 🧪 即時預覽")
        st.markdown("選擇一個情境，看看友善提示長什麼樣：")

        demo_error = st.selectbox("選擇異常情境", [
            "印表機卡紙", "網路斷線", "紙張用完", "相機無回應", "投幣無法辨識",
        ])

        demo_messages = {
            "印表機卡紙": ("🖨️", "印表機卡紙了", "請打開印表機上蓋，輕輕將卡住的紙張往外拉出，再關上蓋子。系統會自動重新列印您的照片。"),
            "網路斷線": ("📶", "網路連線暫時中斷", "行動支付暫時無法使用。您可以使用機台左側的投幣口付款，或稍等片刻讓系統自動重新連線。"),
            "紙張用完": ("📄", "相紙已用完", "很抱歉造成不便！工作人員正在補充相紙，請稍候約 2 分鐘。您的照片已儲存，補紙後會自動列印。"),
            "相機無回應": ("📷", "相機正在重新啟動", "請稍候 10 秒鐘。如果畫面仍未出現，請呼叫現場工作人員協助。"),
            "投幣無法辨識": ("🪙", "硬幣無法辨識", "請確認投入的是新台幣硬幣。如硬幣被退回，可能是因為表面髒污，請更換一枚再試。"),
        }

        emoji, title, msg = demo_messages[demo_error]
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #2d3436 0%, #636e72 100%);
                    border-radius: 15px; padding: 30px; text-align: center; color: white;
                    max-width: 500px; margin: 0 auto;">
            <p style="font-size: 48px; margin: 0;">{emoji}</p>
            <h3 style="color: white; margin: 10px 0;">{title}</h3>
            <p style="font-size: 14px; line-height: 1.8; color: #dfe6e9;">{msg}</p>
            <hr style="border-color: rgba(255,255,255,0.2); margin: 15px 0;">
            <p style="font-size: 12px; color: #b2bec3;">如需協助請呼叫現場工作人員</p>
        </div>
        """, unsafe_allow_html=True)

elif current_section == "15. 快閃店部署策略":
    st.title("🏪 快閃店部署策略")

    st.markdown("PhotoBooth 需要通過**快閃店（Pop-up Store）頻繁搬遷**的實地測試，因此部署策略至關重要。")

    st.divider()
    st.subheader("🗺️ 部署挑戰 vs 解決方案")

    challenges = [
        {
            "icon": "🌐", "title": "網路環境不穩定",
            "problem": "快閃店場地的 Wi-Fi 可能不可靠或根本沒有網路",
            "solution": "系統支援離線模式，核心拍照/列印功能不依賴網路；支付部分使用 4G/5G 行動熱點備援",
        },
        {
            "icon": "🔌", "title": "電力與空間限制",
            "problem": "場地插座位置不固定，空間大小每次不同",
            "solution": "設備採用 UPS 不斷電系統；軟體介面支援直立/橫向模式自動切換",
        },
        {
            "icon": "⏱️", "title": "快速架設需求",
            "problem": "每次搬遷後需要快速完成設備設定，不能等原廠技術支援",
            "solution": "建立一鍵部署腳本，開機自動啟動服務；設定檔外部化，換場只需改設定檔",
        },
        {
            "icon": "🛡️", "title": "設備安全",
            "problem": "公共場合設備可能被誤觸或惡意操作",
            "solution": "軟體鎖定 Kiosk 模式，僅顯示拍照介面；管理功能需密碼驗證",
        },
    ]

    for ch in challenges:
        with st.expander(f"{ch['icon']} {ch['title']}", expanded=False):
            col_p, col_s = st.columns(2)
            with col_p:
                st.error(f"**挑戰：** {ch['problem']}")
            with col_s:
                st.success(f"**對策：** {ch['solution']}")

    st.divider()
    st.subheader("🐳 Docker 快速部署流程")
    st.markdown("""
    <div style="display: flex; align-items: center; justify-content: center; gap: 0; flex-wrap: wrap; margin: 20px 0;">
        <div style="background: linear-gradient(135deg, #e74c3c, #c0392b); border-radius: 12px; padding: 20px 25px;
                    color: white; text-align: center; min-width: 160px;">
            <p style="font-size: 28px; margin: 0;">💻</p>
            <strong>開發環境</strong><br><span style="font-size: 12px; opacity: 0.8;">Streamlit</span>
            <hr style="border-color: rgba(255,255,255,0.3); margin: 8px 0;">
            <span style="font-size: 12px;">Jeff / JD</span>
        </div>
        <div style="font-size: 28px; padding: 0 15px; color: #b2bec3;">→</div>
        <div style="background: linear-gradient(135deg, #f39c12, #e67e22); border-radius: 12px; padding: 20px 25px;
                    color: white; text-align: center; min-width: 160px;">
            <p style="font-size: 28px; margin: 0;">🐳</p>
            <strong>Docker 封裝</strong><br><span style="font-size: 12px; opacity: 0.8;">映像打包</span>
            <hr style="border-color: rgba(255,255,255,0.3); margin: 8px 0;">
            <span style="font-size: 12px;">技術同事</span>
        </div>
        <div style="font-size: 28px; padding: 0 15px; color: #b2bec3;">→</div>
        <div style="background: linear-gradient(135deg, #27ae60, #2ecc71); border-radius: 12px; padding: 20px 25px;
                    color: white; text-align: center; min-width: 160px;">
            <p style="font-size: 28px; margin: 0;">🏪</p>
            <strong>快閃店設備</strong><br><span style="font-size: 12px; opacity: 0.8;">一鍵啟動</span>
            <hr style="border-color: rgba(255,255,255,0.3); margin: 8px 0;">
            <span style="font-size: 12px;">現場同仁</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.info("""
    **關鍵原則：** 穩定、小規模、針對細部需求微調，快速產出可驗收的成果。
    每次部署前跑一次自動化測試，確認核心流程（支付→拍照→列印）正常運作。
    """)

elif current_section == "_legacy_jd_prep":
    st.title("📋 JD 的第一步準備清單")

    st.markdown("由 Jeff 指導，JD 主導完成以下準備工作。勾選已完成的項目：")

    st.divider()
    st.subheader("🛠️ 工具與環境佈置（由 Jeff 指導）")

    tool_items = {
        "安裝 VS Code 編輯器": "前往 code.visualstudio.com 下載安裝",
        "安裝 Claude Code 官方插件": "在 VS Code 擴充套件搜尋 Claude Code 並安裝（claude.ai/code）",
        "安裝 Python 3.9+": "前往 python.org 下載，安裝時勾選「Add to PATH」",
        "安裝 Streamlit": "在終端機輸入 pip install streamlit",
        "確認 Git 版本控制已安裝": "在終端機輸入 git --version 確認",
    }

    for item, hint in tool_items.items():
        col_check, col_hint = st.columns([3, 7])
        with col_check:
            st.checkbox(item, key=f"tool_{item[:10]}")
        with col_hint:
            st.caption(f"💡 {hint}")

    st.divider()
    st.subheader("📑 權限與文件整理（由 JD 主導）")

    doc_items = {
        "取得 ERP 系統的 API 文件或匯出格式說明": "確認能匯出 CSV 或有 API 端點",
        "取得 POS 系統的串接規格": "向 POS 廠商索取 API 文件",
        "確認支付介面（LINE Pay / 街口）的商家申請狀態": "需要商家帳號才能串接",
        "整理現有 PhotoBooth 的硬體規格文件": "包含相機型號、印表機型號、通訊協定",
        "列出目前系統中所有簡體中文的畫面截圖": "方便 AI 比對與替換",
    }

    for item, hint in doc_items.items():
        col_check, col_hint = st.columns([3, 7])
        with col_check:
            st.checkbox(item, key=f"doc_{item[:10]}")
        with col_hint:
            st.caption(f"💡 {hint}")

    st.divider()
    st.subheader("📐 業務邏輯定義（由 JD 主導）")
    st.markdown("請 JD 繪製初步邏輯圖，包含以下三大區塊：")

    col_in, col_proc, col_out = st.columns(3)
    with col_in:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    border-radius: 15px; padding: 25px; color: white;">
            <h4 style="color: white; text-align:center;">📥 Input</h4>
            <hr style="border-color: rgba(255,255,255,0.3);">
            <p>- 使用者掃碼</p>
            <p>- 選取照片方案</p>
            <p>- 串接支付資訊</p>
        </div>
        """, unsafe_allow_html=True)
    with col_proc:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                    border-radius: 15px; padding: 25px; color: white;">
            <h4 style="color: white; text-align:center;">⚙️ Process</h4>
            <hr style="border-color: rgba(255,255,255,0.3);">
            <p>- UI 介面中文化</p>
            <p>- 去除簡體字殘留</p>
            <p>- 邏輯在地化調整</p>
        </div>
        """, unsafe_allow_html=True)
    with col_out:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
                    border-radius: 15px; padding: 25px; color: white;">
            <h4 style="color: white; text-align:center;">📤 Output</h4>
            <hr style="border-color: rgba(255,255,255,0.3);">
            <p>- 繁體中文介面</p>
            <p>- 列印成品輸出</p>
            <p>- 交易記錄儲存</p>
        </div>
        """, unsafe_allow_html=True)

elif current_section == "16. 數據儀表板願景":
    st.title("📊 數據儀表板願景")

    st.markdown("""
    PhotoBooth 重構只是第一步，最終目標是打造一個**整合式數據儀表板**，
    讓團隊不再需要在多個系統間切換，一個畫面掌握所有資訊。
    """)

    st.divider()
    st.subheader("🖥️ 儀表板模擬預覽")

    # 模擬即時數據
    import random
    random.seed(int(time.time()) // 10)

    # KPI 指標
    col_k1, col_k2, col_k3, col_k4 = st.columns(4)
    with col_k1:
        st.metric("今日拍照次數", f"{random.randint(30, 80)} 次", f"+{random.randint(5, 15)}")
    with col_k2:
        st.metric("今日營收", f"NT$ {random.randint(3000, 8000):,}", f"+{random.randint(500, 1500):,}")
    with col_k3:
        st.metric("蝦皮待出貨", f"{random.randint(5, 20)} 筆", f"{random.randint(-3, 3)}")
    with col_k4:
        st.metric("Pinkoi 待出貨", f"{random.randint(2, 10)} 筆", f"{random.randint(-2, 2)}")

    st.divider()

    # 模擬圖表
    import datetime
    col_chart1, col_chart2 = st.columns(2)

    with col_chart1:
        st.subheader("📈 近 7 日營收趨勢")
        chart_data = {
            "日期": [(datetime.date.today() - datetime.timedelta(days=i)).strftime("%m/%d") for i in range(6, -1, -1)],
            "PhotoBooth": [random.randint(2000, 6000) for _ in range(7)],
            "電商合計": [random.randint(3000, 8000) for _ in range(7)],
        }
        st.line_chart(chart_data, x="日期", y=["PhotoBooth", "電商合計"])

    with col_chart2:
        st.subheader("🥧 營收來源佔比")
        pie_data = {
            "來源": ["PhotoBooth", "蝦皮", "Pinkoi", "官網"],
            "金額": [random.randint(5000, 15000) for _ in range(4)],
        }
        st.bar_chart(pie_data, x="來源", y="金額")

    st.divider()
    st.subheader("🔮 未來整合藍圖")
    st.markdown("""
    | 階段 | 內容 | 預計時程 |
    |---|---|---|
    | **Phase 1** | PhotoBooth 繁體化 + QR Code 支付 | 第 1-2 週 |
    | **Phase 2** | 營收數據自動彙整儀表板 | 第 3-4 週 |
    | **Phase 3** | ERP/POS 數據串接 | 第 5-8 週 |
    | **Phase 4** | 電商平台訂單自動同步 | 第 9-12 週 |
    """)

    st.info("💡 **開發哲學：** 穩定、小規模、針對細部需求微調，快速產出可驗收的成果。不更動大架構，用 AI 的「小工具」模式逐步推進。")

elif current_section == "HW3. 課後練習":
    st.title("📝 課後練習：寫出你的系統需求描述")

    st.markdown("今天我們學了需求描述框架和設備評估方法。現在輪到你實際練習。")

    st.divider()
    st.subheader("🎯 練習任務")
    st.markdown("""
    **請完成以下兩項作業：**

    **作業 A：系統需求描述**
    用今天學到的「四個必答題」框架，寫出你自己系統的完整需求描述：
    1. 這是什麼？（用途與使用對象）
    2. 操作流程是什麼？
    3. 目前的現狀與痛點
    4. 期望達成什麼？

    **作業 B：硬體清點**
    把你們目前使用的所有硬體設備列出來，包含：
    - 品牌 / 型號
    - 連接方式（USB / Serial / Wi-Fi）
    - 目前有沒有 SDK 或驅動文件
    """)

    st.divider()
    st.subheader("📤 繳交作業")
    student3 = st.text_input("你的名字", key="hw3_name", placeholder="例：JD")
    hw3_file = st.file_uploader(
        "上傳需求描述文件或硬體清點表",
        type=["png", "jpg", "jpeg", "pdf", "txt", "docx", "md", "xlsx"],
        key="hw3_upload",
    )
    if hw3_file and student3:
        path, gdrive_link = save_uploaded_file(hw3_file, "HW3", student3)
        st.success(f"✅ 作業已儲存！檔案：`{os.path.basename(path)}`")
        if gdrive_link:
            st.info(f"☁️ 已同步到 Google Drive")
    elif hw3_file and not student3:
        st.warning("請先填寫你的名字再上傳。")
    st.caption("我們會用你的需求描述來做截圖復刻的實戰練習。")

# =====================================================
# 第四堂課：截圖復刻與在地化
# =====================================================

elif current_section == "R3. 上堂回顧與 Q&A":
    lesson_cover(4, "截圖復刻與在地化", "用截圖讓 AI 重建介面，將簡體全面轉為繁體", "🎨")
    st.title("✅ 準備清單驗收")

    st.markdown("在正式動手前，先確認上堂課分配的準備事項都已完成。")

    st.divider()
    st.subheader("🛠️ 環境檢查（現場確認）")

    env_checks = [
        ("VS Code 已安裝並能正常開啟", "在終端機輸入 code --version"),
        ("Claude Code 插件已安裝", "VS Code 左側邊欄應出現 Claude Code 圖示"),
        ("Python 3.9+ 已安裝", "在終端機輸入 python3 --version"),
        ("Streamlit 已安裝", "在終端機輸入 streamlit --version"),
        ("可以成功執行範例程式", "在終端機輸入 streamlit run course_app.py"),
    ]

    all_ok = True
    for item, hint in env_checks:
        col_c, col_h = st.columns([4, 6])
        with col_c:
            checked = st.checkbox(item, key=f"env_{item[:15]}")
            if not checked:
                all_ok = False
        with col_h:
            st.caption(f"驗證方式：`{hint}`")

    st.divider()
    st.subheader("📸 截圖素材檢查")

    screenshot_items = [
        "待機 / 歡迎頁面截圖",
        "支付頁面截圖",
        "拍照頁面截圖",
        "選版型 / 背景頁面截圖",
        "列印 / 完成頁面截圖",
        "設定 / 管理後台截圖（如有）",
    ]

    uploaded_count = 0
    for item in screenshot_items:
        col_c, col_u = st.columns([3, 7])
        with col_c:
            st.markdown(f"**{item}**")
        with col_u:
            f = st.file_uploader(f"上傳 {item}", type=["png", "jpg", "jpeg"], key=f"ss_{item[:6]}")
            if f:
                uploaded_count += 1

    st.divider()
    st.metric("截圖素材進度", f"{uploaded_count} / {len(screenshot_items)}")

    if all_ok and uploaded_count >= 3:
        st.success("🎉 準備充足，可以開始動手了！")
    elif uploaded_count >= 1:
        st.warning("⚠️ 素材不完整也沒關係，有幾張就先做幾張，後續再補。")
    else:
        st.info("請至少提供 1-2 張操作畫面截圖，作為復刻的依據。")

elif current_section == "10. 截圖轉程式實戰":
    st.title("🖼️ 截圖轉程式：看圖說話讓 AI 重建")

    st.markdown("""
    這是 Vibe Coding 的核心應用場景：**不需要原始碼，只要有畫面截圖，
    Claude Code 就能分析佈局、按鈕、文字、流程，重新建構出完整的程式。**
    """)

    st.divider()
    st.subheader("Step 1：上傳截圖")
    uploaded = st.file_uploader("上傳一張 PhotoBooth 的操作畫面截圖", type=["png", "jpg", "jpeg"])

    if uploaded:
        screenshot = Image.open(uploaded)
        col_img, col_prompt = st.columns([1, 1])

        with col_img:
            st.image(screenshot, caption="原始截圖", use_container_width=True)

        with col_prompt:
            st.subheader("Step 2：組合 Prompt")
            st.markdown("根據核心公式，我們組合一個讓 Claude Code 復刻這個畫面的 Prompt：")

            prompt_text = st.text_area(
                "你的 Prompt（可直接使用或修改）",
                value="""【背景】
我正在重構一台 PhotoBooth 拍貼機系統，原系統由大陸廠商開發，介面為簡體中文。
我使用 Python + Streamlit 作為新的前端框架。

【目標】
請根據我提供的截圖，用 Streamlit 重建這個頁面的介面與互動邏輯。
所有文字必須改為繁體中文，用語需在地化（例：摄像→照相、刷新→重新整理）。

【風格】
使用繁體中文，介面風格現代簡潔，配色可保留原設計或改為更適合台灣市場的配色。
按鈕要大且明顯，適合觸控螢幕操作。""",
                height=300,
            )

        st.divider()
        st.subheader("Step 3：在 Claude Code 中執行")
        st.markdown("將上面的 Prompt 複製到 VS Code 的 Claude Code 插件中，並附上截圖：")

        st.markdown("""
        ```
        操作步驟：
        1. 開啟 VS Code
        2. 啟動 Claude Code 插件（側邊欄圖示）
        3. 將截圖拖入對話框（或貼上圖片路徑）
        4. 貼上 Prompt 並送出
        5. Claude 會產生 .py 檔案
        6. 在終端機執行 streamlit run <檔名>.py 查看結果
        ```
        """)

        st.info("💡 **小撇步：** 如果第一次產出不滿意，直接告訴 Claude「按鈕再大一點」「顏色換成粉紅色」，它會自動修改。這就是 Vibe Coding 的迭代精神。")
    else:
        st.info("👆 請上傳一張操作畫面截圖，開始復刻實戰。")

        st.divider()
        st.subheader("📎 沒有截圖？用示範情境練習")
        st.markdown("選擇一個模擬情境，體驗截圖轉程式的流程：")

        demo_scenario = st.selectbox("選擇示範情境", [
            "（請先上傳截圖）",
            "模擬：簡體支付頁面",
            "模擬：簡體拍照頁面",
        ])

        if demo_scenario == "模擬：簡體支付頁面":
            # 產生模擬簡體截圖
            mock = Image.new("RGB", (400, 600), "#1a1a2e")
            draw = ImageDraw.Draw(mock)
            try:
                font_lg = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 28)
                font_sm = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 18)
            except (OSError, IOError):
                font_lg = ImageFont.load_default()
                font_sm = font_lg
            draw.text((120, 30), "支付页面", fill="white", font=font_lg)
            draw.rectangle([50, 100, 350, 180], fill="#e74c3c", outline="white", width=2)
            draw.text((110, 125), "投币支付", fill="white", font=font_lg)
            draw.rectangle([50, 220, 350, 300], fill="#27ae60", outline="white", width=2)
            draw.text((100, 245), "扫码支付", fill="white", font=font_lg)
            draw.text((80, 400), "请选择支付方式", fill="#888", font=font_sm)
            draw.text((100, 500), "当前状态: 待机中", fill="#666", font=font_sm)

            st.image(mock, caption="模擬：大陸廠商的簡體支付頁面", use_container_width=True)
            st.markdown("**練習目標：** 用 Prompt 請 Claude 將這個頁面改為繁體中文在地化版本。")

        elif demo_scenario == "模擬：簡體拍照頁面":
            mock = Image.new("RGB", (400, 600), "#1a1a2e")
            draw = ImageDraw.Draw(mock)
            try:
                font_lg = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 28)
                font_sm = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 18)
            except (OSError, IOError):
                font_lg = ImageFont.load_default()
                font_sm = font_lg
            draw.text((120, 30), "拍摄页面", fill="white", font=font_lg)
            draw.rectangle([75, 100, 325, 350], outline="#3498db", width=3)
            draw.text((130, 200), "摄像区域", fill="#3498db", font=font_lg)
            draw.text((100, 380), "已拍摄: 2/6 张", fill="#888", font=font_sm)
            # 進度條
            draw.rectangle([50, 430, 350, 450], fill="#333")
            draw.rectangle([50, 430, 150, 450], fill="#3498db")
            draw.rectangle([100, 480, 300, 550], fill="#3498db", outline="white", width=2)
            draw.text((140, 500), "拍照", fill="white", font=font_lg)

            st.image(mock, caption="模擬：大陸廠商的簡體拍照頁面", use_container_width=True)
            st.markdown("**練習目標：** 用 Prompt 請 Claude 將這個頁面改為繁體，並將「摄像」改為「照相」、「拍摄」改為「拍攝」。")

elif current_section == "11. 在地化調整實作":
    st.title("🇹🇼 在地化調整實作")

    st.markdown("復刻完畫面後，接下來做深度在地化——不只換字，還要調整邏輯和體驗。")

    st.divider()
    tab_text, tab_flow, tab_style = st.tabs(["📝 文字在地化", "🔄 流程在地化", "🎨 視覺在地化"])

    with tab_text:
        st.subheader("文字在地化：不只是簡轉繁")
        st.markdown("以下是常見的轉換範例，請練習組合 Prompt 讓 Claude 處理：")

        text_pairs = [
            ("摄像", "照相", "功能名稱"),
            ("刷新", "重新整理", "操作動作"),
            ("导航", "導引", "UI 元素"),
            ("打印机", "印表機", "硬體設備"),
            ("用户界面", "使用者介面", "技術術語"),
            ("确认", "確認", "按鈕文字"),
            ("取消", "取消", "按鈕文字（相同但確認字型）"),
            ("上传", "上傳", "操作動作"),
            ("信息", "訊息 / 資訊", "通知用語"),
            ("视频", "影片", "媒體類型"),
        ]

        col_cn, col_tw, col_cat = st.columns(3)
        with col_cn:
            st.markdown("**🇨🇳 簡體原文**")
        with col_tw:
            st.markdown("**🇹🇼 繁體在地化**")
        with col_cat:
            st.markdown("**📂 分類**")

        for cn, tw, cat in text_pairs:
            col_cn, col_tw, col_cat = st.columns(3)
            with col_cn:
                st.markdown(f"`{cn}`")
            with col_tw:
                st.markdown(f"**{tw}**")
            with col_cat:
                st.caption(cat)

        st.divider()
        st.markdown("**練習：** 將以下 Prompt 貼到 Claude Code 中，讓它自動掃描並替換：")
        st.code("""請掃描目前專案中所有 .py 檔案，找出簡體中文字串，
並依照台灣繁體中文的在地化習慣進行替換。
不只是簡繁轉換，還需要調整用語（如：摄像→照相、信息→訊息）。
替換後列出所有變更的對照表。""", language=None)

    with tab_flow:
        st.subheader("流程在地化：調整操作邏輯")
        st.markdown("有些操作流程在台灣的使用習慣不同，需要調整：")

        flow_changes = [
            {
                "title": "支付方式",
                "before": "支付宝 / 微信支付",
                "after": "LINE Pay / 街口支付 / 現金",
                "reason": "台灣消費者不使用大陸支付工具",
            },
            {
                "title": "預設語系",
                "before": "系統預設簡體中文，語系選單切換",
                "after": "直接繁體中文，移除語系切換（單一市場）",
                "reason": "減少不必要的操作步驟",
            },
            {
                "title": "客服聯繫",
                "before": "微信客服 / QQ 群組",
                "after": "LINE 官方帳號 / 電話",
                "reason": "台灣消費者習慣的聯繫管道不同",
            },
        ]

        for change in flow_changes:
            with st.expander(f"🔄 {change['title']}"):
                col_b, col_a = st.columns(2)
                with col_b:
                    st.error(f"**原始流程：** {change['before']}")
                with col_a:
                    st.success(f"**在地化後：** {change['after']}")
                st.caption(f"原因：{change['reason']}")

    with tab_style:
        st.subheader("視覺在地化：配色與風格調整")
        st.markdown("根據目標客群（台灣年輕女性為主），建議調整的視覺元素：")

        col_s1, col_s2 = st.columns(2)
        with col_s1:
            st.markdown("**建議配色方案**")
            colors = {
                "主色 — 櫻花粉": "#ffb7c5",
                "強調 — 蜜桃橘": "#ff8a65",
                "背景 — 奶茶色": "#f5e6d3",
                "文字 — 深咖啡": "#4e342e",
            }
            for name, color in colors.items():
                st.markdown(
                    f'<div style="display:flex; align-items:center; gap:10px;">'
                    f'<div style="width:40px; height:40px; background:{color}; border-radius:8px; border:1px solid #666;"></div>'
                    f'<span>{name} ({color})</span></div>',
                    unsafe_allow_html=True,
                )
                st.markdown("")

        with col_s2:
            st.markdown("**字體建議**")
            st.markdown("""
            * **標題：** PingFang TC Bold（蘋方繁體粗體）
            * **內文：** PingFang TC Regular
            * **數字/英文：** SF Pro Display
            * **按鈕文字大小：** 至少 18px（觸控友善）
            * **行距：** 1.6 倍以上（中文閱讀舒適度）
            """)

elif current_section == "14. 支付與列印串接規劃":
    st.title("🔗 支付與列印串接規劃")

    st.markdown("復刻完介面後，下一步就是讓它真的能動——串接支付系統和印表機。")

    st.divider()
    st.subheader("💳 支付串接架構")

    st.markdown("""
    <div style="margin: 20px 0;">
        <div style="display: flex; align-items: center; justify-content: center; gap: 0; flex-wrap: wrap;">
            <div style="background: linear-gradient(135deg, #0984e3, #74b9ff); border-radius: 12px; padding: 18px 22px;
                        color: white; text-align: center; min-width: 140px;">
                <p style="font-size: 24px; margin: 0;">🖥️</p>
                <strong>Streamlit</strong><br><span style="font-size: 11px;">前端介面</span>
            </div>
            <div style="font-size: 22px; padding: 0 12px; color: #b2bec3;">⇄</div>
            <div style="background: linear-gradient(135deg, #6c5ce7, #a29bfe); border-radius: 12px; padding: 18px 22px;
                        color: white; text-align: center; min-width: 140px;">
                <p style="font-size: 24px; margin: 0;">⚙️</p>
                <strong>後端 Server</strong><br><span style="font-size: 11px;">Webhook</span>
            </div>
            <div style="font-size: 22px; padding: 0 12px; color: #b2bec3;">⇄</div>
            <div style="background: linear-gradient(135deg, #00b894, #55efc4); border-radius: 12px; padding: 18px 22px;
                        color: white; text-align: center; min-width: 140px;">
                <p style="font-size: 24px; margin: 0;">💳</p>
                <strong>LINE Pay</strong><br><span style="font-size: 11px;">/ 街口 API</span>
            </div>
        </div>
        <div style="display: flex; justify-content: center; gap: 80px; margin-top: 8px;">
            <div style="text-align: center; color: #636e72; font-size: 18px;">↕</div>
            <div style="text-align: center; color: #636e72; font-size: 18px;">↕</div>
        </div>
        <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
            <div style="background: rgba(45,52,54,0.6); border: 2px solid #0984e3; border-radius: 12px;
                        padding: 15px 22px; color: #dfe6e9; text-align: center; min-width: 140px;">
                <p style="font-size: 24px; margin: 0;">📱</p>
                <strong>使用者手機</strong><br><span style="font-size: 11px;">掃 QR Code</span>
            </div>
            <div style="background: rgba(45,52,54,0.6); border: 2px solid #6c5ce7; border-radius: 12px;
                        padding: 15px 22px; color: #dfe6e9; text-align: center; min-width: 140px;">
                <p style="font-size: 24px; margin: 0;">🗄️</p>
                <strong>交易資料庫</strong><br><span style="font-size: 11px;">記錄 / 對帳</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("LINE Pay 串接要點", expanded=True):
        st.markdown("""
        | 項目 | 說明 |
        |---|---|
        | **申請** | 需有台灣公司統編，申請 LINE Pay 商家帳號 |
        | **Sandbox** | LINE Pay 提供測試環境，可用假金額測試全流程 |
        | **API 版本** | 建議使用 LINE Pay API v3 |
        | **關鍵端點** | Request（建立交易）、Confirm（確認付款）、Refund（退款） |
        | **Webhook** | 需建立公開的 HTTPS 端點接收付款結果通知 |
        """)

    with st.expander("街口支付串接要點"):
        st.markdown("""
        | 項目 | 說明 |
        |---|---|
        | **申請** | 向街口申請商家 SDK |
        | **整合方式** | 街口提供 QR Code 產生 API |
        | **注意事項** | 街口的 Sandbox 環境需另外申請 |
        """)

    st.divider()
    st.subheader("🖨️ 印表機串接架構")

    st.markdown("""
    <div style="display: flex; align-items: center; justify-content: center; gap: 0; flex-wrap: wrap; margin: 20px 0;">
        <div style="background: linear-gradient(135deg, #0984e3, #74b9ff); border-radius: 12px; padding: 18px 22px;
                    color: white; text-align: center; min-width: 140px;">
            <p style="font-size: 24px; margin: 0;">🖼️</p>
            <strong>Streamlit</strong><br><span style="font-size: 11px;">產生合成圖</span>
        </div>
        <div style="font-size: 22px; padding: 0 12px; color: #b2bec3;">→</div>
        <div style="background: linear-gradient(135deg, #e17055, #fab1a0); border-radius: 12px; padding: 18px 22px;
                    color: white; text-align: center; min-width: 140px;">
            <p style="font-size: 24px; margin: 0;">⚙️</p>
            <strong>列印服務模組</strong><br><span style="font-size: 11px;">Python</span>
        </div>
        <div style="font-size: 22px; padding: 0 12px; color: #b2bec3;">→</div>
        <div style="background: linear-gradient(135deg, #636e72, #b2bec3); border-radius: 12px; padding: 18px 22px;
                    color: white; text-align: center; min-width: 140px;">
            <p style="font-size: 24px; margin: 0;">🖨️</p>
            <strong>印表機</strong><br><span style="font-size: 11px;">USB / 網路</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("**需要在第四堂課前確認的資訊：**")
    printer_items = [
        "印表機的型號與品牌",
        "連接方式：USB / Wi-Fi / 藍牙 / 網路（IP）",
        "是否有官方 SDK 或驅動程式",
        "支援的列印格式（圖片直印 / ESC/POS 指令 / PDF）",
        "紙張規格（4x6 / 長條 / 自訂）",
    ]
    for item in printer_items:
        st.checkbox(item, key=f"printer_{item[:10]}")

elif current_section == "12. Before/After 成果驗收":
    st.title("🏆 Before / After 成果驗收")

    st.markdown("把今天復刻的成果跑起來，和原始截圖做 Before / After 對比。")

    st.divider()
    st.subheader("📸 上傳對比")

    col_before, col_after = st.columns(2)
    with col_before:
        st.markdown("#### Before（原始系統）")
        before_img = st.file_uploader("上傳原始畫面截圖", type=["png", "jpg", "jpeg"], key="before_upload")
        if before_img:
            st.image(Image.open(before_img), use_container_width=True)
        else:
            st.markdown("""
            <div style="background: #333; border: 2px dashed #666; border-radius: 12px;
                        height: 300px; display: flex; align-items: center; justify-content: center; color: #666;">
                上傳原始畫面截圖
            </div>
            """, unsafe_allow_html=True)

    with col_after:
        st.markdown("#### After（復刻成果）")
        after_img = st.file_uploader("上傳復刻後的畫面截圖", type=["png", "jpg", "jpeg"], key="after_upload")
        if after_img:
            st.image(Image.open(after_img), use_container_width=True)
        else:
            st.markdown("""
            <div style="background: #333; border: 2px dashed #666; border-radius: 12px;
                        height: 300px; display: flex; align-items: center; justify-content: center; color: #666;">
                上傳復刻後截圖
            </div>
            """, unsafe_allow_html=True)

    st.divider()
    st.subheader("📋 驗收檢查清單")
    review_items = [
        "所有簡體文字已轉為繁體中文",
        "用語已在地化（非單純簡繁轉換）",
        "佈局與原始畫面一致或更優",
        "按鈕可以正常點擊互動",
        "流程邏輯正確（支付→拍照→列印）",
        "在觸控螢幕上按鈕大小合適",
    ]
    passed = sum(1 for item in review_items if st.checkbox(item, key=f"review_{item[:10]}"))
    st.progress(passed / len(review_items))
    st.markdown(f"**通過 {passed}/{len(review_items)} 項**")

    if passed == len(review_items):
        st.success("🎉 全部通過！復刻成果驗收完成。")
        st.balloons()
    elif passed > len(review_items) // 2:
        st.warning("⚠️ 大部分通過，剩餘項目可在課後繼續調整。")


elif current_section == "HW4. 課後練習":
    st.title("📝 課後練習：截圖復刻你的系統頁面")

    st.markdown("今天學了截圖轉程式和在地化技巧，請在下堂課前完成以下練習。")

    st.divider()
    st.subheader("🎯 練習任務")
    st.markdown("""
    **用截圖復刻你現有系統的一個頁面：**

    1. 選擇你們拍貼機系統中的一個頁面（例如：歡迎畫面、支付頁面）
    2. 截圖後交給 Claude，請它用 Streamlit 復刻
    3. 將簡體用語改為繁體在地化版本
    4. 記錄過程中遇到的問題

    **進階挑戰：** 嘗試復刻兩個以上的頁面，並確認它們之間的流程串接。
    """)

    st.divider()
    st.subheader("📤 繳交作業")
    student4 = st.text_input("你的名字", key="hw4_name", placeholder="例：JD")
    hw4_file = st.file_uploader(
        "上傳復刻後的畫面截圖",
        type=["png", "jpg", "jpeg", "pdf"],
        key="hw4_upload",
    )
    if hw4_file and student4:
        path, gdrive_link = save_uploaded_file(hw4_file, "HW4", student4)
        st.success(f"✅ 作業已儲存！檔案：`{os.path.basename(path)}`")
        if gdrive_link:
            st.info(f"☁️ 已同步到 Google Drive")
    elif hw4_file and not student4:
        st.warning("請先填寫你的名字再上傳。")

    st.divider()
    st.subheader("📋 下堂課準備")
    st.info("""
    下堂課主題是**支付串接與部署策略**，請準備：
    1. **印表機型號** 與連接方式
    2. **投幣/紙鈔機的通訊介面**（Serial Port / GPIO）
    3. **網路環境資訊**（快閃店是否有固定 IP）
    """)

# =====================================================
# 第五堂課：支付串接與部署策略
# =====================================================

elif current_section == "R4. 上堂回顧與 Q&A":
    lesson_cover(5, "支付串接與部署策略", "串接 QR Code 行動支付，規劃快閃店部署方案", "💳")
    st.title("🔄 上堂回顧：截圖復刻與在地化")

    st.subheader("📋 第四堂成果確認")
    st.markdown("先確認上堂課的復刻成果目前狀態：")

    status_items = {
        "歡迎/待機頁面": ["未開始", "已復刻", "已在地化", "已驗收"],
        "支付頁面": ["未開始", "已復刻", "已在地化", "已驗收"],
        "拍照頁面": ["未開始", "已復刻", "已在地化", "已驗收"],
        "背景選擇頁面": ["未開始", "已復刻", "已在地化", "已驗收"],
        "列印/完成頁面": ["未開始", "已復刻", "已在地化", "已驗收"],
    }

    for page_name, options in status_items.items():
        col_name, col_status = st.columns([3, 7])
        with col_name:
            st.markdown(f"**{page_name}**")
        with col_status:
            st.radio(f"{page_name} 狀態", options, horizontal=True, key=f"status_{page_name}")

    st.divider()
    st.subheader("❓ 復刻過程中遇到的問題")
    st.text_area("記錄遇到的問題，今天一起討論解決", key="r3_issues", height=100,
                 placeholder="例：拍照頁面的相機預覽區域大小抓不準...")

elif current_section == "8. 需求描述與架構訓練":
    st.title("📝 需求描述與架構訓練")

    st.markdown("""
    在決定「用什麼設備」之前，最重要的一步是**把需求講清楚**。
    這一節我們練習如何用結構化的方式，向 AI 或技術夥伴描述一個系統的背景、現狀與目標。
    """)

    # ---- 為什麼需要練習描述 ----
    st.divider()
    st.subheader("🎯 為什麼「描述需求」是一門功課？")

    col_why1, col_why2 = st.columns(2)
    with col_why1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #e17055 0%, #d63031 100%);
                    border-radius: 12px; padding: 20px; color: white; min-height: 150px;">
            <h4 style="color: white;">❌ 常見問題</h4>
            <hr style="border-color: rgba(255,255,255,0.3);">
            <p style="font-size: 14px;">「幫我做一台拍貼機」</p>
            <p style="font-size: 14px;">「跟原本那台一樣就好」</p>
            <p style="font-size: 14px;">「我要能印照片的那種」</p>
            <p style="font-size: 13px; opacity: 0.8;">→ 太模糊，AI 或工程師無法判斷規格</p>
        </div>
        """, unsafe_allow_html=True)
    with col_why2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #00b894 0%, #00cec9 100%);
                    border-radius: 12px; padding: 20px; color: white; min-height: 150px;">
            <h4 style="color: white;">✅ 有效描述</h4>
            <hr style="border-color: rgba(255,255,255,0.3);">
            <p style="font-size: 14px;">「一台自助拍貼機，投幣後自動拍 6 張，<br>顧客在觸控螢幕選格式後列印，<br>同時提供 QR Code 下載電子檔。」</p>
            <p style="font-size: 13px; opacity: 0.8;">→ 有流程、有互動方式、有輸出物</p>
        </div>
        """, unsafe_allow_html=True)

    # ---- 描述框架教學 ----
    st.divider()
    st.subheader("📋 需求描述框架：四個必答題")

    st.markdown("當你要向 AI（或技術團隊）描述一個系統需求時，至少回答這四個問題：")

    framework = [
        ("1️⃣ 這是什麼？", "系統的用途與使用對象", "一台自助式 PhotoBooth 拍貼機，放在快閃店供消費者自助使用"),
        ("2️⃣ 操作流程是什麼？", "使用者從頭到尾的步驟", "投幣 → 自動拍 6 張（每 5 秒一張）→ 觸控螢幕選格式 → 列印 + QR Code 取電子檔"),
        ("3️⃣ 目前的現狀與痛點", "現在用什麼方案、哪裡不行", "現有系統是大陸廠商的 Android 方案，簡體介面無法參加政府活動，且硬體整合受限"),
        ("4️⃣ 期望達成什麼？", "改完之後要變怎樣", "繁體中文在地化、自主掌控硬體與軟體、能獨立維護與更換零件"),
    ]

    for title, subtitle, example in framework:
        with st.expander(f"{title} — {subtitle}", expanded=True):
            st.markdown(f"**範例：** {example}")

    # ---- 實戰練習：描述拍貼機系統 ----
    st.divider()
    st.subheader("✍️ 實戰練習：描述你的拍貼機系統")
    st.markdown("用上面的框架，試著完整描述我們正在開發的 PhotoBooth 系統：")

    desc_q1 = st.text_area("1. 這是什麼？（用途與使用對象）", key="desc_q1", height=80,
                            placeholder="例：一台放在快閃店的自助式拍貼機，目標客群是...")
    desc_q2 = st.text_area("2. 操作流程是什麼？（使用者的步驟）", key="desc_q2", height=100,
                            placeholder="例：顧客走到機台 → 投入紙鈔 → ...")
    desc_q3 = st.text_area("3. 目前的現狀與痛點", key="desc_q3", height=100,
                            placeholder="例：目前使用的是大陸廠商提供的系統，問題是...")
    desc_q4 = st.text_area("4. 期望達成什麼？", key="desc_q4", height=80,
                            placeholder="例：我們希望能自己控制軟硬體，做到...")

    # ---- 示範：完整的需求描述 ----
    st.divider()
    st.subheader("📄 範例：完整的需求描述（給 AI 或技術團隊）")
    st.markdown("以下是把四個問題整合後的完整描述，這也是我們實際跟 Claude 討論時使用的版本：")

    st.markdown("""
    <div style="background: #2d3436; border-left: 4px solid #74b9ff; border-radius: 8px;
                padding: 25px; color: #dfe6e9; font-size: 14px; line-height: 1.8;">
        <strong style="color: #74b9ff;">【系統背景】</strong><br>
        我們正在重構一台自助式 PhotoBooth 拍貼機。這台機器放在快閃店（Pop-up Store），
        供消費者自助拍照、選擇套圖樣式後列印帶走。目標客群是台灣的年輕消費者。<br><br>

        <strong style="color: #74b9ff;">【操作流程】</strong><br>
        一個主控制主機配備兩個螢幕輸出：<br>
        1. 顧客投入紙鈔後啟動（系統需接收紙鈔機的確認訊號）<br>
        2. 自動定時拍攝 6 張照片（每 5 秒一張，非手動按壓）<br>
        3. 拍完後在觸控螢幕上選擇背景板風格與列印版型（不滿意的照片可選擇重拍）<br>
        4. 確認後列印成品，同時產生 QR Code 讓顧客掃碼下載電子圖檔<br><br>

        <strong style="color: #74b9ff;">【現狀與痛點】</strong><br>
        現有系統由大陸廠商開發，使用 Android 裝置。介面為簡體中文，無法參加台灣政府活動（如文博會）。
        硬體整合受廠商限制，無法自行更換零件或客製功能。<br><br>

        <strong style="color: #74b9ff;">【期望目標】</strong><br>
        改為繁體中文在地化版本，使用 Linux + Python 開發，自主掌控軟硬體。
        能獨立維護、更換硬體模組、客製 UI，不再依賴原廠商。
    </div>
    """, unsafe_allow_html=True)

    st.markdown("")
    st.success("💡 **重點：** 這份描述就是接下來所有技術決策的基礎。描述得越清楚，AI 給的建議越精準，團隊溝通的成本也越低。")

    # ---- 從描述到架構：AI 回饋流程 ----
    st.divider()
    st.subheader("🔄 從需求描述到系統架構：AI 回饋流程")
    st.markdown("當你把需求描述交給 AI（如 Claude），它會依照以下步驟幫你分析：")

    steps = [
        ("📥 輸入", "你的需求描述", "把四個問題的答案整理成完整敘述"),
        ("🔍 分析", "AI 拆解需求", "辨識出：操作步驟、I/O 需求、硬體介面、軟體模組"),
        ("📐 架構", "AI 提出系統架構", "畫出主機、週邊設備、通訊方式的關係圖"),
        ("⚖️ 評估", "AI 比較方案", "根據場景條件（預算、穩定性、搬遷頻率）比較選項"),
        ("🎯 建議", "AI 給出推薦策略", "分階段建議：先用什麼驗證，再用什麼上線"),
    ]

    for i, (icon, title, desc) in enumerate(steps):
        col_icon, col_content = st.columns([1, 9])
        with col_icon:
            st.markdown(f"### {icon}")
        with col_content:
            st.markdown(f"**{title}**：{desc}")
        if i < len(steps) - 1:
            st.markdown("<div style='text-align:center; color:#636e72; font-size:20px;'>↓</div>", unsafe_allow_html=True)

    st.info("👉 **下一節** 我們就來實際走一遍這個流程——用剛才的需求描述，進行設備選型決策。")

elif current_section == "9. 設備選型決策討論":
    st.title("⚖️ 設備選型決策討論")

    st.markdown("""
    上一節我們學會了如何描述需求。這一節我們用那份需求描述，實際走一遍**設備選型的決策過程**。
    重點不只是「選了什麼」，而是「**為什麼這樣選**」——這個思考方法可以套用在任何硬體決策上。
    """)

    # ---- 第一段：操作流程確認 ----
    st.divider()
    st.subheader("📋 第一步：確認操作流程")
    st.markdown("我們先把一位顧客從走進來到拿到成品的完整流程拉出來：")

    flow_steps = [
        ("1️⃣ 收款", "顧客投入紙鈔，系統確認金額後啟動流程"),
        ("2️⃣ 定時拍攝 ×6", "系統自動倒數 5 秒拍一張，連續拍 6 張，不需人工按快門"),
        ("3️⃣ 選擇格式", "顧客在觸控螢幕上選擇背景板風格與列印版型"),
        ("4️⃣ 出圖", "合成影像、送出列印，同時產生 QR Code 供顧客下載電子檔"),
    ]

    flow_cols = st.columns(4)
    for i, (title, desc) in enumerate(flow_steps):
        with flow_cols[i]:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #2d3436 0%, #636e72 100%);
                        border-radius: 12px; padding: 20px; color: white; min-height: 160px;">
                <h4 style="color: #74b9ff; text-align:center;">{title}</h4>
                <hr style="border-color: rgba(255,255,255,0.2);">
                <p style="font-size: 14px;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    st.info("💡 **關鍵決策：** 拍攝改為定時自動拍攝（非手動按壓），每張間隔 5 秒。這決定了相機模組必須支援軟體觸發拍照。")

    # ---- 第二段：從流程推導 I/O 需求 ----
    st.divider()
    st.subheader("🔌 第二步：從流程推導 I/O 需求")
    st.markdown("根據上面的流程，我們可以列出主機需要的所有輸入/輸出介面：")

    io_data = [
        {"類別": "螢幕輸出 ×2", "介面": "HDMI ×2", "說明": "一個給顧客觸控操作、一個顯示引導畫面或即時預覽"},
        {"類別": "觸控螢幕輸入", "介面": "USB（觸控訊號）", "說明": "顧客選擇重拍、選格式、確認出圖"},
        {"類別": "滑鼠輸入", "介面": "USB", "說明": "維護 / 除錯用"},
        {"類別": "印表機", "介面": "USB", "說明": "熱昇華相片印表機，送出合成影像列印"},
        {"類別": "紙鈔接收器", "介面": "Serial（RS-232）或 USB", "說明": "接收投幣 / 紙鈔確認訊號"},
        {"類別": "相機", "介面": "USB", "說明": "需支援軟體觸發拍照（非僅預覽）"},
    ]

    st.markdown("| 類別 | 介面 | 說明 |")
    st.markdown("|------|------|------|")
    for row in io_data:
        st.markdown(f"| {row['類別']} | {row['介面']} | {row['說明']} |")

    st.warning("""
    ⚠️ **紙鈔機通訊注意：** 紙鈔機通常走 **RS-232 串口** 或 **MDB 協議**（自動販賣機國際標準）。
    如果主機沒有原生 COM Port，需要一個 USB-to-Serial 轉接器，或選用帶 GPIO 的主機直接讀取訊號。
    """)

    # ---- 第三段：主機方案比較 ----
    st.divider()
    st.subheader("⚖️ 第三步：主機方案比較")
    st.markdown("知道需要什麼 I/O 之後，我們來比較三種主機方案：")

    tab_pi, tab_nuc, tab_android = st.tabs(["🍓 Raspberry Pi 5", "💻 Intel NUC / 工控主機", "📱 Android（現狀）"])

    with tab_pi:
        st.markdown("#### Raspberry Pi 5")
        col_pro, col_con = st.columns(2)
        with col_pro:
            st.markdown("""
            **✅ 優點**
            - 成本最低（約 NT$2,500~3,500）
            - 雙 micro-HDMI 輸出
            - 4 個 USB Port（觸控 + 印表機 + 紙鈔機 + 相機）
            - **GPIO 可直接讀紙鈔機訊號**，省掉 USB-to-Serial
            - 社群資源豐富，Python 支援完整
            """)
        with col_con:
            st.markdown("""
            **⚠️ 限制**
            - 影像合成速度較慢（大圖可能要等數秒）
            - 印表機驅動相容性需逐一確認（CUPS on ARM）
            - SD 卡長期讀寫穩定性不如 SSD
            - 機櫃內散熱需額外處理
            """)
        st.info("🎯 **適合：** 原型驗證階段、預算有限、可接受處理速度稍慢的場景")

    with tab_nuc:
        st.markdown("#### Intel NUC / 工控迷你主機")
        st.markdown("品牌參考：Intel NUC、研華 (Advantech)、威強電 (IEI)")
        col_pro2, col_con2 = st.columns(2)
        with col_pro2:
            st.markdown("""
            **✅ 優點**
            - x86 架構，驅動相容性最佳
            - 雙 HDMI / DP 輸出標配
            - 可裝 SSD，系統穩定度高
            - 工控機型設計給 7×24 運行
            - 擴充 COM Port 容易（接紙鈔機）
            - 效能充裕，影像合成秒級完成
            """)
        with col_pro2:
            pass
        with col_con2:
            st.markdown("""
            **⚠️ 限制**
            - 成本較高（約 NT$6,000~12,000）
            - 體積比 Pi 大
            - 沒有原生 GPIO（需外接介面板）
            """)
        st.success("🎯 **適合：** 商用部署、快閃店頻繁搬遷、需長時間穩定運行的正式場景")

    with tab_android:
        st.markdown("#### Android 裝置（現有系統）")
        st.markdown("""
        這是目前大陸廠商採用的方案，但在我們的需求下有明顯限制：

        | 問題 | 說明 |
        |------|------|
        | 雙螢幕輸出 | Android 裝置普遍不支援雙螢幕獨立控制 |
        | 印表機驅動 | Android 印表機支援有限，多需廠商專屬 App |
        | 紙鈔機串口 | Android 裝置接 Serial Port 非常麻煩 |
        | 硬體整合自由度 | 整體自由度低，客製化困難 |
        """)
        st.error("🎯 **結論：** 不建議繼續使用。切換到 Linux 主機（Pi 或 NUC）可大幅提升硬體整合彈性。")

    # ---- 第四段：建議策略 ----
    st.divider()
    st.subheader("🎯 第四步：建議策略")

    st.markdown("""
    <div style="background: linear-gradient(135deg, #0984e3 0%, #6c5ce7 100%);
                border-radius: 15px; padding: 30px; color: white;">
        <h4 style="color: white;">分階段推進：先驗證，再上線</h4>
        <hr style="border-color: rgba(255,255,255,0.3);">
        <table style="width: 100%; color: white; font-size: 15px;">
            <tr>
                <td style="padding: 10px; vertical-align: top; width: 50%;">
                    <strong>📌 短期（原型驗證）</strong><br><br>
                    使用 <strong>Raspberry Pi 5</strong><br>
                    • 成本低，快速搭建原型<br>
                    • GPIO 直接讀紙鈔機訊號<br>
                    • 驗證完整流程可行性
                </td>
                <td style="padding: 10px; vertical-align: top; width: 50%;">
                    <strong>📌 中期（商用部署）</strong><br><br>
                    切換 <strong>Intel NUC / 工控主機</strong><br>
                    • 穩定性與驅動相容性是商用關鍵<br>
                    • 價差不大但省大量除錯時間<br>
                    • 軟體層完全共用，無需重寫
                </td>
            </tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("")
    st.info("💡 **關鍵：** 兩者都跑 Linux + Python，軟體層（Streamlit + 硬體控制模組）完全共用。切換主機時只需調整硬體驅動設定，不需要改程式邏輯。")

    # ---- 第五段：系統架構圖 ----
    st.divider()
    st.subheader("🗺️ 系統架構總覽")
    st.markdown("把以上分析整合起來，整台拍貼機的系統架構如下：")
    st.image("images/photobooth-infra.png", caption="PhotoBooth 系統架構總覽", use_container_width=True)

    st.divider()
    st.subheader("💬 討論：你們的場景")
    st.markdown("根據以上分析，思考以下問題：")
    q1 = st.text_area("你們目前的紙鈔機是什麼廠牌/型號？通訊方式是？", key="hw_eval_q1",
                       placeholder="例：ICT V7 紙鈔機，RS-232 介面...")
    q2 = st.text_area("快閃店搬遷頻率大約多久一次？對體積/重量有要求嗎？", key="hw_eval_q2",
                       placeholder="例：大概每 1-2 週換一個點...")
    q3 = st.text_area("除了上述設備，還有沒有其他週邊需要整合？", key="hw_eval_q3",
                       placeholder="例：LED 燈條控制、外接喇叭播放語音提示...")

elif current_section == "HW5. 課後練習":
    st.title("📝 課後練習：準備硬體規格文件")

    st.markdown("下堂課是最後一堂，主題是**硬體整合**。請在課前完成以下準備。")

    st.divider()
    st.subheader("🎯 練習任務")
    st.markdown("""
    **請收集並整理以下硬體資訊：**

    | 設備 | 需收集的資訊 |
    |------|-------------|
    | 📷 相機 | 品牌/型號、連接方式、解析度、SDK 文件 |
    | 🖨️ 印表機 | 品牌/型號、連接方式、紙張規格、驅動程式 |
    | 💰 紙鈔機 | 品牌/型號、通訊介面、訊號格式 |
    | 🖥️ 螢幕 | 尺寸、解析度、是否觸控 |

    **沒有文件也沒關係！** 如果硬體上有型號標籤，拍照即可。
    """)

    st.divider()
    st.subheader("📤 繳交作業")
    student5 = st.text_input("你的名字", key="hw5_name", placeholder="例：JD")
    hw5_file = st.file_uploader(
        "上傳硬體規格文件或設備照片",
        type=["png", "jpg", "jpeg", "pdf", "txt", "docx", "xlsx", "zip"],
        key="hw5_upload",
    )
    if hw5_file and student5:
        path, gdrive_link = save_uploaded_file(hw5_file, "HW5", student5)
        st.success(f"✅ 作業已儲存！檔案：`{os.path.basename(path)}`")
        if gdrive_link:
            st.info(f"☁️ 已同步到 Google Drive")
    elif hw5_file and not student5:
        st.warning("請先填寫你的名字再上傳。")
    st.caption("我們會用這些資訊進行整合架構設計。")

# =====================================================
# 第六堂課：硬體整合與總結
# =====================================================

elif current_section == "R5. 上堂回顧與 Q&A":
    lesson_cover(6, "硬體整合與總結", "收集硬體 SDK、設計整合架構、實機串接測試", "🔧")
    st.title("🔄 上堂回顧：支付串接與部署")

    st.subheader("📋 第五堂重點複習")
    st.markdown("""
    上堂課我們完成了：
    1. **QR Code 行動支付** — LINE Pay / 街口支付的串接邏輯
    2. **支付與列印串接規劃** — 軟硬體如何協同
    3. **快閃店部署策略** — 不同場地的網路與設備配置
    4. **數據儀表板願景** — 營業數據的整合方向
    """)

    st.divider()
    st.subheader("❓ Q&A 與討論")
    st.text_area("記錄上堂課的問題或心得", key="r5_issues", height=100,
                 placeholder="例：支付串接時 Webhook 回呼的流程還不太清楚...")

    st.divider()
    st.subheader("📌 本堂課目標")
    st.markdown("""
    今天是最後一堂課，我們要：
    1. 收集並整理所有硬體 SDK 規格
    2. 解析通訊協定
    3. 設計整合架構
    4. 現場實作一個硬體模組串接
    5. 總結整個課程，規劃後續行動
    """)

# =====================================================
# 第六堂課：硬體整合與總結
# =====================================================

elif current_section == "17. 硬體 SDK 規格收集":
    st.title("📦 硬體 SDK 規格收集")

    st.markdown("""
    要讓復刻的介面真正驅動硬體，我們需要先把所有硬體的規格和通訊方式搞清楚。
    請逐一填入或上傳目前 PhotoBooth 使用的硬體資訊。
    """)

    st.divider()

    devices = [
        {
            "name": "📷 相機模組",
            "fields": ["品牌/型號", "連接方式（USB / IP / CSI）", "解析度", "支援的拍照指令或 SDK"],
        },
        {
            "name": "🖨️ 印表機",
            "fields": ["品牌/型號", "連接方式（USB / Wi-Fi / 藍牙）", "紙張規格", "支援的列印指令（ESC/POS / 直接圖片 / 其他）"],
        },
        {
            "name": "💰 投幣/紙鈔機",
            "fields": ["品牌/型號", "通訊介面（Serial Port / GPIO / 其他）", "訊號格式（脈衝 / 封包）", "可辨識的幣別與面額"],
        },
        {
            "name": "💡 燈光控制",
            "fields": ["控制方式（GPIO / DMX / 繼電器）", "幾組燈光", "是否需要可調亮度"],
        },
        {
            "name": "🖥️ 觸控螢幕",
            "fields": ["尺寸", "解析度", "連接方式（HDMI / DSI）", "是否支援多點觸控"],
        },
    ]

    for device in devices:
        with st.expander(device["name"], expanded=False):
            for field in device["fields"]:
                st.text_input(f"{field}", key=f"hw_{device['name'][:3]}_{field[:10]}",
                              placeholder=f"請填入 {field}")
            st.file_uploader(f"上傳 {device['name']} 的規格書/SDK 文件",
                             type=["pdf", "zip", "doc", "docx", "txt"],
                             key=f"hwfile_{device['name'][:3]}")

    st.divider()
    st.info("💡 沒有文件也沒關係。如果硬體上有型號標籤，拍照上傳即可，Claude 可以協助搜尋對應的技術文件。")

elif current_section == "17.5. AI 加值應用實驗":
    st.title("✨ AI 加值應用實驗")

    st.markdown("""
    硬體串接完成後，接下來思考如何用 AI 為 PhotoBooth 創造**差異化價值**。
    這些功能不需要額外硬體，只需要軟體升級，就能讓拍貼體驗大幅提升。
    """)

    tab_beauty, tab_frame, tab_doc = st.tabs([
        "🪄 AI 自動美顏", "🖼️ 智慧相框生成", "📖 自動化文檔生成"
    ])

    with tab_beauty:
        st.markdown("### AI 自動美顏：讓每張照片都好看")

        st.markdown("""
        傳統拍貼機的美顏是「一刀切」——同一個濾鏡套所有人。
        AI 美顏可以根據每張臉的特徵**個別調整**，效果更自然。
        """)

        st.markdown("#### 可實現的美顏功能")
        beauty_features = [
            ("膚色均勻", "自動偵測膚色不均區域，輕微修正", "OpenCV + MediaPipe"),
            ("亮度補償", "根據臉部位置自動調整局部亮度", "PIL / OpenCV"),
            ("背景虛化", "人像清晰、背景自然模糊", "rembg + PIL"),
            ("自動裁切", "偵測人臉位置，確保構圖居中", "MediaPipe Face Detection"),
        ]

        for feat, desc, tech in beauty_features:
            col_f, col_d, col_t = st.columns([2, 5, 3])
            with col_f:
                st.markdown(f"**{feat}**")
            with col_d:
                st.markdown(desc)
            with col_t:
                st.caption(tech)

        st.divider()
        st.markdown("**建議 Prompt：**")
        st.code("""【背景】
我的 PhotoBooth 拍完照後，希望自動對照片做美顏處理。
目前使用 Python + PIL 處理影像。

【目標】
請幫我寫一個 beauty.py 模組：
1. 偵測照片中的人臉位置（用 MediaPipe）
2. 對膚色區域做輕微平滑處理（保持自然）
3. 自動調整亮度和對比度
4. 提供「自然」「精緻」「標準」三個等級選擇
5. 處理時間需在 2 秒內完成（拍貼機不能讓客人等太久）

【風格】
繁體中文註解，函式名稱用英文。""", language=None)

    with tab_frame:
        st.markdown("### 智慧相框生成：繁體中文主題相框")

        st.markdown("""
        讓 AI 根據活動主題，**自動生成符合情境的相框設計**。
        不再需要每次都請設計師重新做，AI 幾秒鐘就能產出。
        """)

        st.markdown("#### 相框生成情境範例")

        frame_examples = [
            {
                "event": "🌸 文博會",
                "prompt": "台灣文博會主題相框，融入台灣意象（天燈、101、珍奶），繁體中文標題『文博會紀念 2026』",
                "style": "文藝風、水彩質感",
            },
            {
                "event": "🎄 聖誕快閃",
                "prompt": "聖誕節主題相框，紅綠配色、雪花裝飾，底部寫『聖誕快樂 Merry Christmas』",
                "style": "可愛風、金色點綴",
            },
            {
                "event": "🏢 企業活動",
                "prompt": "企業年會相框，簡約專業風格，右下角放公司 Logo 位置，頂部寫『2026 年度盛會』",
                "style": "商務風、深藍色系",
            },
        ]

        for ex in frame_examples:
            with st.expander(f"{ex['event']}", expanded=False):
                st.markdown(f"**AI Prompt：**「{ex['prompt']}」")
                st.markdown(f"**風格：** {ex['style']}")

        st.divider()
        st.info("""
        💡 **實作方式：**
        - **簡單版：** 用 PIL 程式化生成邊框 + 文字（本地處理，速度快）
        - **進階版：** 串接 AI 圖片生成 API（如 DALL-E、Stable Diffusion），產出更精美的設計
        - **混合版：** AI 生成底圖 → PIL 加上文字和 Logo（兼顧品質與速度）
        """)

    with tab_doc:
        st.markdown("### 自動化文檔生成：讓 AI 幫你寫維護手冊")

        st.markdown("""
        系統開發完成後，最痛苦的事情就是**寫文件**。
        但有了 AI，你只需要提供系統資訊，它就能自動產出完整的維護手冊。
        """)

        st.markdown("#### AI 可以自動產出的文件")

        doc_types = [
            ("📘 操作手冊", "給現場操作人員看的", "每個畫面的截圖 + 操作步驟說明"),
            ("📗 維護手冊", "給技術維護人員看的", "硬體連接圖、故障排除 SOP、零件更換步驟"),
            ("📙 部署指南", "給 IT 人員看的", "安裝步驟、環境設定、網路需求、備份還原"),
            ("📕 API 文件", "給未來開發者看的", "每個模組的功能說明、參數列表、使用範例"),
        ]

        for icon_name, audience, content in doc_types:
            col_doc, col_aud, col_con = st.columns([2, 3, 5])
            with col_doc:
                st.markdown(f"**{icon_name}**")
            with col_aud:
                st.caption(audience)
            with col_con:
                st.markdown(content)

        st.divider()
        st.markdown("**建議 Prompt：**")
        st.code("""【背景】
我完成了一個 PhotoBooth 拍貼機系統，使用以下技術：
- 前端：Streamlit
- 硬體控制：Python（OpenCV 相機、pyserial 投幣機、CUPS 印表機）
- 支付：LINE Pay API + QR Code

【目標】
請根據這個系統架構，產出一份「現場操作手冊」：
1. 系統開機流程（按什麼順序啟動）
2. 每個畫面的操作說明（搭配截圖位置標記）
3. 常見問題排除（印表機卡紙、網路斷線等）
4. 每日結束營業的關機流程
5. 緊急狀況處理（斷電、設備故障）

【風格】
繁體中文、適合非技術人員閱讀、步驟編號清楚、
重要警告用紅色標記、每個步驟一句話不超過 20 字。""", language=None)

        st.divider()
        st.success("""
        💡 **文件不是寫完就好——它需要跟著系統更新。**
        每次改版後，把新的程式碼交給 AI，請它比對差異並更新文件。
        這樣維護手冊永遠是最新版本。
        """)

elif current_section == "18. 通訊協定解析":
    st.title("🔌 通訊協定解析")

    st.markdown("了解每個硬體「說什麼語言」，才能讓軟體正確下指令。")

    st.divider()
    tab_serial, tab_usb, tab_network = st.tabs(["📟 Serial Port", "🔌 USB", "🌐 網路 (HTTP/TCP)"])

    with tab_serial:
        st.subheader("Serial Port（常用於投幣機、紙鈔機）")
        st.markdown("""
        | 參數 | 常見設定 | 說明 |
        |---|---|---|
        | **Baud Rate** | 9600 / 115200 | 通訊速率 |
        | **Data Bits** | 8 | 資料位元 |
        | **Stop Bits** | 1 | 停止位元 |
        | **Parity** | None | 校驗位元 |
        | **Port** | /dev/ttyUSB0 (Linux) / COM3 (Windows) | 裝置路徑 |
        """)

        st.markdown("**Python 範例（pyserial）：**")
        st.code("""import serial

# 開啟 Serial Port
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

# 讀取投幣訊號
while True:
    data = ser.readline()
    if data:
        print(f"收到投幣訊號: {data.decode()}")
""", language="python")

        st.caption("💡 此範例需在實際連接硬體時執行，Streamlit Demo 中會用模擬方式替代。")

    with tab_usb:
        st.subheader("USB（常用於相機、印表機）")
        st.markdown("""
        | 裝置 | 通訊方式 | Python 套件 |
        |---|---|---|
        | **USB Webcam** | Video4Linux / DirectShow | `opencv-python` |
        | **USB 印表機** | USB 直連 / CUPS | `python-escpos` / `cups` |
        | **USB 讀卡機** | HID | `pyscard` |
        """)

        st.markdown("**相機擷取範例（OpenCV）：**")
        st.code("""import cv2

cap = cv2.VideoCapture(0)  # 0 = 第一台 USB 相機
ret, frame = cap.read()
if ret:
    cv2.imwrite("photo.jpg", frame)
cap.release()
""", language="python")

    with tab_network:
        st.subheader("網路（常用於 IP Camera、網路印表機）")
        st.markdown("""
        | 通訊方式 | 使用場景 | Python 套件 |
        |---|---|---|
        | **HTTP REST API** | IP Camera 截圖 / 雲端服務 | `requests` |
        | **TCP Socket** | 工業設備控制 | `socket` |
        | **MQTT** | IoT 感測器 | `paho-mqtt` |
        """)

        st.markdown("**IP Camera 截圖範例：**")
        st.code("""import requests

# 從 IP Camera 取得即時截圖
response = requests.get("http://192.168.1.100/capture",
                        auth=("admin", "password"))
with open("snapshot.jpg", "wb") as f:
    f.write(response.content)
""", language="python")

elif current_section == "19. 整合架構設計":
    st.title("🏗️ 整合架構設計")

    st.markdown("根據收集到的硬體資訊，設計一個軟硬體整合架構。")

    st.divider()
    st.subheader("🗺️ 系統架構總覽")

    st.markdown("""
    <div style="background: linear-gradient(135deg, #2d3436, #636e72); border-radius: 15px; padding: 25px; margin: 20px 0;
                border: 2px solid #6c5ce7;">
        <h4 style="text-align: center; color: #a29bfe; margin-top: 0;">PhotoBooth 主機</h4>
        <div style="display: flex; justify-content: center; gap: 15px; flex-wrap: wrap; margin-bottom: 15px;">
            <div style="background: #0984e3; border-radius: 8px; padding: 10px 18px; color: white; text-align: center;">
                🖥️ Streamlit<br><span style="font-size: 11px;">前端 UI</span>
            </div>
            <div style="background: #e17055; border-radius: 8px; padding: 10px 18px; color: white; text-align: center;">
                🔧 硬體控制<br><span style="font-size: 11px;">中間層</span>
            </div>
            <div style="background: #00b894; border-radius: 8px; padding: 10px 18px; color: white; text-align: center;">
                💳 支付服務<br><span style="font-size: 11px;">中間層</span>
            </div>
        </div>
        <div style="text-align: center; color: #b2bec3; margin: 8px 0;">▼</div>
        <div style="background: #6c5ce7; border-radius: 8px; padding: 10px; color: white; text-align: center;
                    max-width: 200px; margin: 0 auto 15px auto;">
            🐍 主控程式 (Python)
        </div>
        <div style="text-align: center; color: #b2bec3; margin: 8px 0;">▼</div>
        <div style="display: flex; justify-content: center; gap: 10px; flex-wrap: wrap;">
            <div style="background: rgba(255,255,255,0.1); border: 1px solid #74b9ff; border-radius: 8px;
                        padding: 10px 14px; color: #dfe6e9; text-align: center; font-size: 13px;">
                📷 相機<br><span style="font-size: 10px; color: #74b9ff;">USB</span>
            </div>
            <div style="background: rgba(255,255,255,0.1); border: 1px solid #fab1a0; border-radius: 8px;
                        padding: 10px 14px; color: #dfe6e9; text-align: center; font-size: 13px;">
                🖨️ 印表機<br><span style="font-size: 10px; color: #fab1a0;">USB/IP</span>
            </div>
            <div style="background: rgba(255,255,255,0.1); border: 1px solid #ffeaa7; border-radius: 8px;
                        padding: 10px 14px; color: #dfe6e9; text-align: center; font-size: 13px;">
                💰 投幣機<br><span style="font-size: 10px; color: #ffeaa7;">Serial</span>
            </div>
            <div style="background: rgba(255,255,255,0.1); border: 1px solid #55efc4; border-radius: 8px;
                        padding: 10px 14px; color: #dfe6e9; text-align: center; font-size: 13px;">
                💡 燈光<br><span style="font-size: 10px; color: #55efc4;">GPIO</span>
            </div>
            <div style="background: rgba(255,255,255,0.1); border: 1px solid #a29bfe; border-radius: 8px;
                        padding: 10px 14px; color: #dfe6e9; text-align: center; font-size: 13px;">
                🖥️ 觸控螢幕<br><span style="font-size: 10px; color: #a29bfe;">HDMI</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()
    st.subheader("📂 程式碼模組規劃")

    modules = [
        {"module": "app.py", "desc": "Streamlit 主程式（UI 介面）", "owner": "JD + Claude"},
        {"module": "hardware/camera.py", "desc": "相機控制模組（拍照、預覽）", "owner": "技術同事 + Claude"},
        {"module": "hardware/printer.py", "desc": "印表機控制模組（列印指令）", "owner": "技術同事 + Claude"},
        {"module": "hardware/coin.py", "desc": "投幣機控制模組（監聽訊號）", "owner": "技術同事 + Claude"},
        {"module": "hardware/light.py", "desc": "燈光控制模組（開關、亮度）", "owner": "技術同事"},
        {"module": "payment/linepay.py", "desc": "LINE Pay 串接模組", "owner": "JD + Claude"},
        {"module": "payment/jkopay.py", "desc": "街口支付串接模組", "owner": "JD + Claude"},
        {"module": "utils/image.py", "desc": "影像處理（背景合成、縮圖）", "owner": "Claude"},
        {"module": "config.yaml", "desc": "設定檔（可切換場地設定）", "owner": "JD"},
    ]

    st.markdown("| 檔案 | 功能 | 負責人 |")
    st.markdown("|---|---|---|")
    for m in modules:
        st.markdown(f"| `{m['module']}` | {m['desc']} | {m['owner']} |")

    st.divider()
    st.subheader("🧪 分工討論")
    st.markdown("根據上面的模組規劃，填入目前的分工狀態：")
    for m in modules:
        col_m, col_s = st.columns([4, 6])
        with col_m:
            st.markdown(f"`{m['module']}`")
        with col_s:
            st.select_slider(
                f"{m['module']} 進度",
                options=["未開始", "規格確認中", "開發中", "測試中", "完成"],
                key=f"mod_{m['module']}",
                label_visibility="collapsed",
            )

elif current_section == "20. 整合實作與測試":
    st.title("🧪 整合實作與測試")

    st.markdown("選擇一個硬體模組，現場用 Claude Code 產出串接程式碼並測試。")

    st.divider()
    target = st.radio("選擇要實作的模組：", [
        "📷 相機模組 — USB Webcam 拍照",
        "🖨️ 印表機模組 — 送出列印指令",
        "💰 投幣機模組 — 監聽 Serial Port",
    ])

    st.divider()
    if "相機" in target:
        st.subheader("📷 相機模組實作")
        st.markdown("**目標：** 讓 Streamlit 可以呼叫 USB 相機拍照並取得高解析度照片（不只是 Webcam 預覽）。")

        st.markdown("**建議 Prompt：**")
        st.code("""【背景】
我在開發 PhotoBooth 拍貼機，使用 Streamlit 做前端。
目前 st.camera_input 只能取得低解析度的 Webcam 預覽。

【目標】
請幫我寫一個 camera.py 模組：
1. 使用 OpenCV 控制 USB 相機（裝置 ID 從 config 讀取）
2. 提供 capture() 函式，回傳高解析度 PIL Image
3. 提供 preview() 函式，回傳即時預覽的低解析度串流
4. 拍照時自動觸發燈光（呼叫 light 模組）

【風格】
程式碼需有繁體中文註解，函式名稱用英文。""", language=None)

        st.info("💡 如果現場有接 USB 相機，可以直接測試。沒有的話，Claude 會自動產生模擬模式的程式碼。")

    elif "印表機" in target:
        st.subheader("🖨️ 印表機模組實作")
        st.markdown("**目標：** 將合成好的照片送至印表機列印。")

        st.markdown("**建議 Prompt：**")
        st.code("""【背景】
PhotoBooth 系統需要將合成好的拍貼照片送至印表機列印。
印表機型號：___（請填入）
連接方式：___（USB / 網路 IP）

【目標】
請幫我寫一個 printer.py 模組：
1. 提供 print_image(image_path, copies=1) 函式
2. 支援 4x6 和長條兩種紙張規格
3. 列印前自動調整圖片 DPI 為 300
4. 提供 get_status() 函式檢查印表機狀態（紙張/墨水）

【風格】
程式碼需有繁體中文註解，錯誤訊息用繁體中文。""", language=None)

    elif "投幣" in target:
        st.subheader("💰 投幣機模組實作")
        st.markdown("**目標：** 監聽投幣/紙鈔機的訊號，判斷投入金額。")

        st.markdown("**建議 Prompt：**")
        st.code("""【背景】
PhotoBooth 系統需要監聽投幣機/紙鈔機的 Serial Port 訊號。
通訊介面：Serial Port
Baud Rate：___（請填入）
投幣訊號格式：___（請填入，如：每個脈衝代表 10 元）

【目標】
請幫我寫一個 coin.py 模組：
1. 提供 start_listening() 開始監聽
2. 提供 get_balance() 取得目前投入金額
3. 金額到達設定值時觸發回呼函式
4. 提供模擬模式，方便在沒有硬體時測試

【風格】
程式碼需有繁體中文註解。""", language=None)

    st.divider()
    st.subheader("🧪 測試結果記錄")
    test_result = st.radio("測試結果：", ["尚未測試", "✅ 測試通過", "⚠️ 部分成功", "❌ 測試失敗"])
    if test_result in ["⚠️ 部分成功", "❌ 測試失敗"]:
        st.text_area("問題描述", key="test_issue",
                     placeholder="描述遇到的問題，例：印表機有回應但印出來是空白的...")

elif current_section == "21. 課程總結與後續規劃":
    st.title("🎓 第一階段總結：六堂課回顧與展望")

    st.subheader("🗺️ 前六堂課走了多遠？")

    milestones = [
        {"lesson": "第一堂", "title": "Vibe Coding 入門", "status": "概念理解 + 看到 Demo", "color": "#e74c3c"},
        {"lesson": "第二堂", "title": "實戰體驗", "status": "拍貼機原型 + 案例分析", "color": "#e67e22"},
        {"lesson": "第三堂", "title": "需求分析", "status": "痛點深掘 + 架構訓練", "color": "#f1c40f"},
        {"lesson": "第四堂", "title": "截圖復刻", "status": "UI 重建 + 在地化", "color": "#2ecc71"},
        {"lesson": "第五堂", "title": "支付串接", "status": "QR Code + 部署策略", "color": "#3498db"},
        {"lesson": "第六堂", "title": "硬體整合", "status": "SDK + 架構 + 串接", "color": "#9b59b6"},
    ]

    cols = st.columns(6)
    for i, m in enumerate(milestones):
        with cols[i]:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {m['color']}cc, {m['color']}88);
                        border-radius: 12px; padding: 15px 10px; color: white; min-height: 160px; text-align:center;">
                <h5 style="color: white; margin: 0;">{m['lesson']}</h5>
                <p style="font-size: 14px; margin: 5px 0;"><b>{m['title']}</b></p>
                <hr style="border-color: rgba(255,255,255,0.3); margin: 8px 0;">
                <p style="font-size: 11px; margin: 0;">{m['status']}</p>
            </div>
            """, unsafe_allow_html=True)

    st.divider()
    st.subheader("📊 目前專案完成度")

    phases = {
        "UI 介面復刻": 80,
        "文字在地化": 70,
        "支付串接": 30,
        "印表機串接": 20,
        "相機串接": 20,
        "投幣機串接": 10,
        "部署 SOP": 10,
    }

    for phase, pct in phases.items():
        col_label, col_bar = st.columns([3, 7])
        with col_label:
            st.markdown(f"**{phase}**")
        with col_bar:
            st.progress(pct / 100)
            st.caption(f"{pct}%")

    st.divider()
    st.subheader("🔮 後續六堂課預覽")

    st.markdown("""
    | 堂次 | 主題 | 月份 | 重點 |
    |------|------|------|------|
    | **第七堂** | 部署與 MVP 驗收 | 第二個月 | 定義 MVP 範圍、部署 SOP、現場實作 |
    | **第八堂** | GitHub 版本控制 | 第二個月 | Git 入門、GitHub 協作、AI 管理變更 |
    | **第九堂** | 測試迭代 | 第三個月 | 系統測試策略、問題追蹤、迭代修正 |
    | **第十堂** | 會員與社群 | 第三個月 | 會員系統、LINE 官方帳號、回購機制 |
    | **第十一堂** | 維護與商品 | 第三個月 | 自動監控告警、維護 SOP、周邊商品 |
    | **第十二堂** | 成果發表 | 第三個月 | 成果整理、Demo、未來路線圖 |
    """)

    st.divider()
    st.subheader("💬 階段性回饋")
    st.text_area("前六堂課下來，你最大的收穫是什麼？對後續六堂有什麼期待？",
                 key="final_feedback", height=120)

    st.markdown("")
    st.success("""
    🎉 **恭喜完成第一階段六堂課程！**

    你已經從「什麼是 Vibe Coding」走到「用 AI 串接真實硬體」。
    接下來的第二階段，我們將進入**部署、版控、測試、以及商業化功能**。

    記住開發哲學：**穩定、小規模、快速產出可驗收的成果。**
    """)

elif current_section == "HW6. 課後練習":
    st.title("📝 課後練習：完成硬體模組串接")

    st.markdown("課程已全部結束，但開發旅程才剛開始！以下是持續練習的方向。")

    st.divider()
    st.subheader("🎯 短期任務（1-2 週內）")
    st.markdown("""
    1. **完成至少一個硬體模組的串接測試**（相機、印表機、或紙鈔機，擇一）
    2. **在模擬環境跑一次完整流程**：收款 → 拍照 → 選格式 → 出圖
    3. **記錄遇到的問題**，整理成問題清單交給 Jeff 討論
    """)

    st.divider()
    st.subheader("📋 中期目標（3-8 週）")
    st.markdown("""
    | 週次 | 目標 |
    |------|------|
    | 第 1-2 週 | 完成所有頁面復刻 + 在地化驗收 |
    | 第 3 週 | LINE Pay Sandbox 串接測試 |
    | 第 4 週 | 印表機 + 相機實機串接 |
    | 第 5 週 | 投幣機串接 + 全流程整合測試 |
    | 第 6 週 | 快閃店實地部署測試 |
    | 第 7-8 週 | 修復問題 + 正式上線 |
    """)

    st.divider()
    st.subheader("📤 繳交成果")
    student6 = st.text_input("你的名字", key="hw6_name", placeholder="例：JD")
    hw6_file = st.file_uploader(
        "上傳硬體串接測試結果或問題清單",
        type=["png", "jpg", "jpeg", "pdf", "txt", "docx", "md", "py", "zip"],
        key="hw6_upload",
    )
    if hw6_file and student6:
        path, gdrive_link = save_uploaded_file(hw6_file, "HW6", student6)
        st.success(f"✅ 作業已儲存！檔案：`{os.path.basename(path)}`")
        if gdrive_link:
            st.info(f"☁️ 已同步到 Google Drive")
    elif hw6_file and not student6:
        st.warning("請先填寫你的名字再上傳。")

    st.divider()
    st.success("""
    💡 **持續使用 AI 的秘訣：**
    每次遇到問題，先用「背景 + 目標 + 風格」描述給 AI，讓它幫你分析和寫程式。
    你負責決策，AI 負責執行——這就是 Vibe Coding 的精髓。
    """)

# =====================================================
# 第七堂課：部署與 MVP 驗收
# =====================================================

elif current_section == "R6. 上堂回顧與 Q&A":
    lesson_cover(7, "部署與 MVP 驗收", "定義最小可行產品，建立可重複的部署流程", "🚀")
    st.title("🔄 上堂回顧：硬體整合")

    st.subheader("📋 第六堂成果確認")
    st.markdown("""
    | 項目 | 狀態 |
    |------|------|
    | 硬體 SDK 規格收集 | ✅ / ⬜ |
    | 通訊協定理解 | ✅ / ⬜ |
    | 整合架構設計 | ✅ / ⬜ |
    | 至少一個模組串接測試 | ✅ / ⬜ |
    """)

    hw_status = {}
    for item in ["硬體 SDK 規格收集", "通訊協定理解", "整合架構設計", "至少一個模組串接測試"]:
        hw_status[item] = st.checkbox(f"{item}", key=f"r6_{item}")

    completed = sum(hw_status.values())
    st.progress(completed / len(hw_status))
    if completed == len(hw_status):
        st.success("🎉 太棒了！全部完成，準備進入部署階段！")
    else:
        st.info(f"完成 {completed}/{len(hw_status)} 項。還沒完成的項目可以在本堂課結束前補齊。")

    st.divider()
    st.subheader("❓ 硬體串接遇到的問題")
    st.text_area("記錄問題，今天一起討論", key="r6_issues", height=100,
                 placeholder="例：投幣機的 Serial Port 讀不到訊號...")

elif current_section == "22. MVP 版本定義與範圍":
    st.title("🎯 MVP 版本定義與範圍")

    st.markdown("""
    **MVP（Minimum Viable Product）= 最小可行性產品**

    不是做「最少的功能」，而是做出「能讓客人完成一次完整體驗」的最小版本。
    """)

    st.divider()
    st.subheader("🔍 什麼算是 PhotoBooth 的 MVP？")

    st.markdown("""
    <div style="background: linear-gradient(135deg, #0984e3 0%, #6c5ce7 100%);
                border-radius: 15px; padding: 25px; color: white;">
        <h4 style="color: white; text-align: center;">MVP 核心流程</h4>
        <p style="text-align: center; font-size: 18px; letter-spacing: 2px;">
            💰 付款 → 📷 拍照 → 🖼️ 選背景 → 🖨️ 列印 → ✅ 完成
        </p>
        <hr style="border-color: rgba(255,255,255,0.3);">
        <p style="text-align: center; font-size: 13px; color: #dfe6e9;">
            客人從頭到尾不需要工作人員協助，就能完成整個流程
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("")
    st.subheader("📋 MVP 功能清單")

    mvp_features = {
        "✅ MVP 必須有": [
            "投幣/掃碼付款（至少支援一種）",
            "倒數計時自動拍照",
            "至少 3 款背景可選",
            "照片合成與排版",
            "自動列印",
            "繁體中文介面",
            "基本異常提示（卡紙、斷線）",
        ],
        "⏳ 第二版再做": [
            "AI 自動美顏",
            "會員系統與回購優惠",
            "多種列印版型選擇（超過 3 種）",
            "數據儀表板",
            "遠端監控",
        ],
        "🔮 未來規劃": [
            "AI 主題相框自動生成",
            "社群分享功能",
            "周邊商品購買",
            "多機台管理系統",
        ],
    }

    for category, items in mvp_features.items():
        with st.expander(category, expanded=category.startswith("✅")):
            for item in items:
                st.markdown(f"- {item}")

    st.divider()
    st.subheader("📐 驗收標準")
    st.markdown("""
    MVP 通過驗收的條件：

    | # | 驗收項目 | 測試方法 |
    |---|----------|---------|
    | 1 | 投幣後 3 秒內進入拍照畫面 | 實機計時 |
    | 2 | 拍照倒數準確（3、2、1） | 實機觀察 |
    | 3 | 照片合成不超過 5 秒 | 實機計時 |
    | 4 | 列印品質清晰可接受 | 肉眼檢查 |
    | 5 | 全流程無需人工介入 | 請非團隊成員實測 |
    | 6 | 異常時顯示中文提示，不會當機 | 模擬斷網/卡紙 |
    | 7 | 連續運作 2 小時無異常 | 壓力測試 |
    """)

elif current_section == "23. 部署工作流程":
    st.title("🚀 部署工作流程")

    st.markdown("從開發機到快閃店現場，需要一套可重複執行的部署 SOP。")

    st.divider()
    st.subheader("📦 部署三階段")

    stages = [
        {
            "icon": "🏠", "title": "Stage 1：開發環境",
            "desc": "在自己的電腦上開發和測試",
            "tasks": ["程式碼開發", "模擬硬體測試", "功能驗證"],
        },
        {
            "icon": "🧪", "title": "Stage 2：測試環境",
            "desc": "在實際硬體上做整合測試",
            "tasks": ["連接真實硬體", "全流程測試", "壓力測試（連續運作）"],
        },
        {
            "icon": "🏪", "title": "Stage 3：正式環境",
            "desc": "快閃店現場部署",
            "tasks": ["搬運與架設", "網路設定", "最終確認", "開始營業"],
        },
    ]

    cols = st.columns(3)
    for i, s in enumerate(stages):
        with cols[i]:
            st.markdown(f"""
            <div style="background: rgba(45,52,54,0.5); border-radius: 12px; padding: 20px;
                        min-height: 250px; border-top: 4px solid {'#e74c3c' if i == 0 else '#f39c12' if i == 1 else '#27ae60'};">
                <h3 style="text-align: center;">{s['icon']}</h3>
                <h4>{s['title']}</h4>
                <p style="font-size: 13px; color: #b2bec3;">{s['desc']}</p>
                <hr style="border-color: rgba(255,255,255,0.1);">
                {''.join(f'<p style="font-size: 13px;">☑️ {t}</p>' for t in s['tasks'])}
            </div>
            """, unsafe_allow_html=True)

    st.divider()
    st.subheader("📝 部署 SOP 檢查表")

    deploy_checklist = [
        ("出發前", ["確認程式碼為最新版本", "備份到 USB 隨身碟", "準備備用相紙和墨水", "確認所有線材齊全"]),
        ("到場後", ["架設硬體（螢幕、相機、印表機、投幣機）", "連接所有線路", "確認網路連線", "啟動系統並做一次完整測試"]),
        ("營業中", ["每 2 小時檢查相紙存量", "注意印表機溫度", "監控網路連線狀態", "記錄任何異常狀況"]),
        ("收攤後", ["關閉系統（先軟體、再硬體）", "備份當天照片", "記錄營業數據", "整理線材、安全包裝硬體"]),
    ]

    for phase, items in deploy_checklist:
        with st.expander(f"📋 {phase}", expanded=False):
            for item in items:
                st.checkbox(item, key=f"deploy_{phase}_{item[:8]}")

elif current_section == "24. 現場部署實作":
    st.title("🔧 現場部署實作")

    st.markdown("模擬一次完整的部署流程，確認你能獨立完成。")

    st.divider()
    st.subheader("🎬 部署模擬演練")

    st.markdown("依序完成以下步驟，每完成一步就打勾：")

    deploy_steps = [
        "1. 開啟終端機，確認 Python 環境正常",
        "2. 進入專案目錄，執行 `streamlit run app.py`",
        "3. 確認 Streamlit 畫面正常顯示",
        "4. 測試投幣/掃碼流程",
        "5. 測試拍照功能",
        "6. 測試照片合成與列印",
        "7. 模擬異常情境（拔網路線、關印表機）",
        "8. 確認異常提示正確顯示",
        "9. 恢復正常後系統能自動復原",
        "10. 連續運作 30 分鐘無異常",
    ]

    completed_steps = 0
    for step in deploy_steps:
        if st.checkbox(step, key=f"sim_{step[:10]}"):
            completed_steps += 1

    st.progress(completed_steps / len(deploy_steps))
    if completed_steps == len(deploy_steps):
        st.balloons()
        st.success("🎉 部署模擬演練完成！你已經具備獨立部署的能力。")

    st.divider()
    st.subheader("📸 部署紀錄")
    st.markdown("拍下你的部署現場，作為日後參考：")
    deploy_photo = st.file_uploader("上傳部署現場照片", type=["png", "jpg", "jpeg"], key="deploy_photo")
    if deploy_photo:
        st.image(deploy_photo, caption="部署現場紀錄", use_container_width=True)

elif current_section == "HW7. 課後練習":
    st.title("📝 課後練習：完成一次完整部署")

    st.markdown("在下堂課前，請完成以下任務。")

    st.divider()
    st.subheader("🎯 練習任務")
    st.markdown("""
    1. **在測試環境完成一次完整部署**（從啟動到收攤）
    2. **記錄部署過程中遇到的問題**，整理成問題清單
    3. **計時整個部署流程**，找出可以加速的環節
    4. **拍攝部署過程照片**，作為 SOP 文件的素材
    """)

    st.divider()
    st.subheader("📤 繳交作業")
    student7 = st.text_input("你的名字", key="hw7_name", placeholder="例：JD")
    hw7_file = st.file_uploader(
        "上傳部署紀錄或問題清單",
        type=["png", "jpg", "jpeg", "pdf", "txt", "docx", "md"],
        key="hw7_upload",
    )
    if hw7_file and student7:
        path, gdrive_link = save_uploaded_file(hw7_file, "HW7", student7)
        st.success(f"✅ 作業已儲存！檔案：`{os.path.basename(path)}`")
        if gdrive_link:
            st.info(f"☁️ 已同步到 Google Drive")
    elif hw7_file and not student7:
        st.warning("請先填寫你的名字再上傳。")

# =====================================================
# 第八堂課：GitHub 版本控制與協作
# =====================================================

elif current_section == "R7. 上堂回顧與 Q&A":
    lesson_cover(8, "GitHub 版本控制與協作", "學會用 Git 管理程式碼，不再害怕改壞回不去", "📚")
    st.title("🔄 上堂回顧：部署與 MVP")

    st.subheader("📋 第七堂成果確認")

    r7_items = ["MVP 功能清單確認", "部署 SOP 制定", "至少一次完整部署測試", "部署問題記錄與解決"]
    for item in r7_items:
        st.checkbox(item, key=f"r7_{item}")

    st.divider()
    st.subheader("❓ 部署遇到的問題")
    st.text_area("分享你的部署經驗", key="r7_issues", height=100,
                 placeholder="例：現場 Wi-Fi 太慢，支付驗證經常逾時...")

elif current_section == "25. Git 版本控制入門":
    st.title("📚 Git 版本控制入門")

    st.markdown("""
    寫程式最怕的事情：**改壞了卻回不去。**
    Git 就像是程式碼的「時光機」，讓你隨時可以回到任何一個版本。
    """)

    st.divider()
    tab_why_git, tab_concepts, tab_commands = st.tabs(["🤔 為什麼需要 Git", "📖 核心概念", "⌨️ 基本指令"])

    with tab_why_git:
        st.markdown("### 沒有版本控制的噩夢")

        st.markdown("""
        <div style="background: #2d3436; border: 2px solid #d63031; border-radius: 10px;
                    padding: 20px; color: #ff7675; font-family: monospace; font-size: 13px;">
            📂 PhotoBooth/<br>
            ├── app.py<br>
            ├── app_backup.py<br>
            ├── app_backup_0401.py<br>
            ├── app_v2.py<br>
            ├── app_v2_final.py<br>
            ├── app_v2_final_真的最終版.py<br>
            └── app_v2_final_真的最終版_JD修改.py<br>
            <br>
            😱 到底哪個才是最新的？
        </div>
        """, unsafe_allow_html=True)

        st.markdown("")
        st.markdown("""
        <div style="background: #2d3436; border: 2px solid #00b894; border-radius: 10px;
                    padding: 20px; color: #55efc4; font-family: monospace; font-size: 13px;">
            📂 PhotoBooth/<br>
            └── app.py &nbsp; ← 永遠只有一個檔案<br>
            <br>
            📜 Git 歷史紀錄：<br>
            &nbsp;&nbsp;#7 — 修正印表機逾時問題 (4/8)<br>
            &nbsp;&nbsp;#6 — 新增 QR Code 支付 (4/5)<br>
            &nbsp;&nbsp;#5 — 完成背景選擇功能 (4/3)<br>
            &nbsp;&nbsp;#4 — 在地化繁體中文 (4/1)<br>
            &nbsp;&nbsp;...<br>
            <br>
            ✅ 清清楚楚，隨時可以回到任何版本
        </div>
        """, unsafe_allow_html=True)

    with tab_concepts:
        st.markdown("### Git 的三個核心概念")

        concepts = [
            ("📸 Commit（提交）", "把目前的程式碼「拍照存檔」。每次存檔都要寫一段說明。",
             "就像遊戲的存檔點，隨時可以讀取。"),
            ("🌿 Branch（分支）", "開一條「平行宇宙」來做實驗，不影響主線。",
             "想試新功能？開一條分支，成功了再合併回來。"),
            ("☁️ Remote（遠端）", "把程式碼存到雲端（GitHub），多人協作 + 備份。",
             "電腦壞了也不怕，程式碼在雲端安全保管。"),
        ]

        for title, desc, analogy in concepts:
            st.markdown(f"#### {title}")
            st.markdown(desc)
            st.caption(f"💡 比喻：{analogy}")
            st.markdown("")

    with tab_commands:
        st.markdown("### 日常會用到的 Git 指令")
        st.markdown("你不需要記住所有指令，只要會這幾個就夠了：")

        commands = [
            ("git status", "查看目前有哪些檔案被修改了", "查看狀態"),
            ("git add .", "把所有修改的檔案加入「準備提交」的清單", "加入清單"),
            ("git commit -m \"說明\"", "提交（存檔），附上這次改了什麼", "存檔"),
            ("git push", "把本機的提交上傳到 GitHub", "上傳"),
            ("git pull", "把 GitHub 上的最新版本下載到本機", "下載"),
            ("git log --oneline", "查看提交歷史紀錄", "查看歷史"),
        ]

        for cmd, desc, short in commands:
            col_cmd, col_desc = st.columns([4, 6])
            with col_cmd:
                st.code(cmd, language="bash")
            with col_desc:
                st.markdown(f"**{short}** — {desc}")

        st.info("💡 **用 AI 幫你記：** 忘記指令沒關係，直接問 Claude「我想把程式碼上傳到 GitHub，要打什麼指令？」")

elif current_section == "26. GitHub 協作流程":
    st.title("🤝 GitHub 協作流程")

    st.markdown("把專案放到 GitHub 之後，你就有了**備份、版本紀錄、團隊協作**三大好處。")

    st.divider()
    st.subheader("🚀 第一次上傳專案到 GitHub")

    st.markdown("**Step by Step：**")

    steps = [
        ("1. 建立 GitHub 帳號", "到 github.com 註冊（免費）"),
        ("2. 建立新的 Repository", "點 New Repository → 命名為 `photobooth` → 選 Private（私人）"),
        ("3. 在本機初始化 Git", "`git init` → `git add .` → `git commit -m \"初始版本\"`"),
        ("4. 連結到 GitHub", "`git remote add origin https://github.com/你的帳號/photobooth.git`"),
        ("5. 上傳", "`git push -u origin main`"),
    ]

    for title, desc in steps:
        st.markdown(f"**{title}**")
        st.markdown(f"　{desc}")

    st.divider()
    st.subheader("🔄 日常工作流程")

    st.markdown("""
    ```
    1. 開始工作前 → git pull（取得最新版本）
    2. 寫程式、修改功能
    3. 完成後 → git add . → git commit -m "說明"
    4. 上傳 → git push
    5. 回到步驟 1
    ```
    """)

    st.info("""
    💡 **建議 Prompt：**
    「我剛修改了 app.py 的投幣偵測邏輯，請幫我寫一個適當的 git commit 訊息。」
    AI 會根據你的程式碼變更，自動產出清楚的提交說明。
    """)

elif current_section == "27. 用 AI 管理程式碼變更":
    st.title("🤖 用 AI 管理程式碼變更")

    st.markdown("讓 AI 幫你做版本控制中最煩人的事：**寫提交說明、比較差異、解決衝突。**")

    st.divider()

    tab_commit, tab_diff, tab_conflict = st.tabs(["📝 自動寫 Commit Message", "🔍 程式碼差異比較", "⚔️ 解決合併衝突"])

    with tab_commit:
        st.markdown("### 讓 AI 幫你寫 Commit Message")
        st.markdown("好的提交說明 = **做了什麼 + 為什麼做**")

        st.markdown("**不好的例子：**")
        st.code("git commit -m \"update\"", language="bash")
        st.code("git commit -m \"fix bug\"", language="bash")

        st.markdown("**好的例子：**")
        st.code("git commit -m \"修正投幣機在連續投幣時金額計算錯誤的問題\"", language="bash")
        st.code("git commit -m \"新增 QR Code 掃碼支付功能（LINE Pay Sandbox）\"", language="bash")

        st.markdown("")
        st.markdown("**建議 Prompt：**")
        st.code("""我剛修改了以下檔案，請幫我寫一個 git commit message：
- app.py: 修改了投幣偵測的邏輯，改用中斷而非輪詢
- hardware/coin.py: 新增 interrupt_handler() 函式
- config.yaml: 新增投幣機的中斷設定

要求：繁體中文、一行標題 + 詳細說明""", language=None)

    with tab_diff:
        st.markdown("### 用 AI 看懂程式碼差異")
        st.markdown("當你不確定改了什麼，可以請 AI 幫你分析：")

        st.code("""請幫我分析以下 git diff 的內容，用繁體中文說明：
1. 改了什麼
2. 為什麼可能要這樣改
3. 有沒有潛在的風險""", language=None)

        st.info("💡 Claude Code 內建 `/diff` 指令，可以直接分析當前的程式碼變更。")

    with tab_conflict:
        st.markdown("### 合併衝突不用怕")
        st.markdown("當兩個人改了同一個地方，Git 會標記衝突。這時候請 AI 幫你：")

        st.code("""以下是一個 git merge 衝突，請幫我解決：
- 我的版本：改了投幣金額判斷為 >= 50
- 對方的版本：改了投幣金額判斷為 >= 30
- 正確做法應該是什麼？請幫我合併並解釋原因""", language=None)

elif current_section == "HW8. 課後練習":
    st.title("📝 課後練習：把專案上傳到 GitHub")

    st.markdown("今天學了 Git 和 GitHub，現在輪到你實際操作。")

    st.divider()
    st.subheader("🎯 練習任務")
    st.markdown("""
    1. **建立 GitHub 帳號**（如果還沒有的話）
    2. **建立一個新的 Repository**（命名為 `photobooth`，設為 Private）
    3. **把目前的專案上傳到 GitHub**
    4. **做一個小修改**（例如改歡迎畫面的文字），然後 commit + push
    5. **到 GitHub 網頁確認**你的程式碼和提交記錄都在上面

    **進階挑戰：** 請 Claude 幫你寫 `.gitignore` 和 `README.md`
    """)

    st.divider()
    st.subheader("📤 繳交作業")
    student8 = st.text_input("你的名字", key="hw8_name", placeholder="例：JD")
    hw8_file = st.file_uploader(
        "上傳 GitHub 頁面截圖（顯示你的 repo 和 commit 記錄）",
        type=["png", "jpg", "jpeg", "pdf"],
        key="hw8_upload",
    )
    if hw8_file and student8:
        path, gdrive_link = save_uploaded_file(hw8_file, "HW8", student8)
        st.success(f"✅ 作業已儲存！檔案：`{os.path.basename(path)}`")
        if gdrive_link:
            st.info(f"☁️ 已同步到 Google Drive")
    elif hw8_file and not student8:
        st.warning("請先填寫你的名字再上傳。")

# =====================================================
# 第九堂課：測試迭代與品質優化
# =====================================================

elif current_section == "R8. 上堂回顧與 Q&A":
    lesson_cover(9, "測試迭代與品質優化", "找出所有問題、逐一修好，建立品質標準", "🧪")
    st.title("🔄 上堂回顧：GitHub 版本控制")

    st.subheader("📋 第八堂成果確認")
    for item in ["GitHub 帳號建立", "Repository 建立", "專案已上傳", "完成至少一次 commit + push"]:
        st.checkbox(item, key=f"r8_{item}")

    st.divider()
    st.subheader("❓ 版控遇到的問題")
    st.text_area("分享你的版控經驗", key="r8_issues", height=100,
                 placeholder="例：push 的時候一直要我輸入密碼...")

elif current_section == "28. 系統測試策略":
    st.title("🧪 系統測試策略")

    st.markdown("""
    MVP 做出來了，但「能動」不代表「能用」。
    進入第三個月，我們的核心任務是：**找出所有問題，逐一修好。**
    """)

    st.divider()
    st.subheader("🔬 三層測試法")

    test_layers = [
        {
            "name": "🔧 單元測試", "color": "#e74c3c",
            "what": "測試每個小模組能不能獨立運作",
            "examples": ["相機模組：能不能成功拍一張照片？", "印表機模組：能不能送出列印指令？", "投幣模組：能不能正確偵測金額？"],
        },
        {
            "name": "🔗 整合測試", "color": "#f39c12",
            "what": "測試模組之間串在一起能不能正常運作",
            "examples": ["投幣完 → 能不能正確觸發拍照？", "拍照完 → 能不能正確送去合成？", "合成完 → 能不能正確列印？"],
        },
        {
            "name": "👤 使用者測試", "color": "#27ae60",
            "what": "請真實使用者操作，觀察他們遇到什麼問題",
            "examples": ["客人看得懂操作介面嗎？", "流程順不順暢？有沒有卡住的地方？", "拿到照片的表情如何？"],
        },
    ]

    for layer in test_layers:
        st.markdown(f"""
        <div style="border-left: 4px solid {layer['color']}; padding: 15px 20px; margin-bottom: 15px;
                    background: rgba(45,52,54,0.3); border-radius: 0 8px 8px 0;">
            <strong style="color: {layer['color']}; font-size: 16px;">{layer['name']}</strong>
            <p style="color: #dfe6e9; margin: 5px 0;">{layer['what']}</p>
        </div>
        """, unsafe_allow_html=True)
        for ex in layer["examples"]:
            st.markdown(f"　　- {ex}")

    st.divider()
    st.subheader("📋 測試紀錄表")
    st.markdown("每次測試都要記錄結果，方便追蹤問題。")

    st.markdown("""
    | 測試項目 | 預期結果 | 實際結果 | 通過？ | 備註 |
    |---------|---------|---------|--------|------|
    | 投幣 50 元 | 進入拍照畫面 | | | |
    | 拍照倒數 | 3-2-1 拍照 | | | |
    | 背景選擇 | 顯示 3 款可選 | | | |
    | 照片合成 | 5 秒內完成 | | | |
    | 自動列印 | 照片清晰 | | | |
    | 拔網路線 | 顯示中文提示 | | | |
    """)

elif current_section == "29. 迭代修正工作坊":
    st.title("🔄 迭代修正工作坊")

    st.markdown("""
    發現問題後，用 Vibe Coding 的方式快速修正。
    **流程：發現問題 → 描述給 AI → 審核方案 → 修正 → 重新測試**
    """)

    st.divider()
    st.subheader("📝 問題追蹤板")
    st.markdown("把測試中發現的問題記錄在這裡，逐一解決：")

    if "issues" not in st.session_state:
        st.session_state.issues = []

    col_input, col_priority = st.columns([6, 4])
    with col_input:
        new_issue = st.text_input("新問題描述", key="new_issue", placeholder="例：拍照時燈光太暗")
    with col_priority:
        priority = st.selectbox("優先度", ["🔴 高（影響核心流程）", "🟡 中（影響體驗）", "🟢 低（可之後處理）"], key="issue_priority")

    if st.button("➕ 新增問題") and new_issue:
        st.session_state.issues.append({"desc": new_issue, "priority": priority, "status": "待處理"})

    if st.session_state.issues:
        st.markdown("---")
        for i, issue in enumerate(st.session_state.issues):
            col_p, col_d, col_s = st.columns([2, 5, 3])
            with col_p:
                st.markdown(issue["priority"][:2])
            with col_d:
                st.markdown(issue["desc"])
            with col_s:
                new_status = st.selectbox(
                    f"狀態 #{i+1}", ["待處理", "處理中", "已解決"],
                    key=f"issue_status_{i}",
                    index=["待處理", "處理中", "已解決"].index(issue["status"]),
                )
                st.session_state.issues[i]["status"] = new_status

    st.divider()
    st.subheader("💡 用 AI 快速修正的技巧")
    st.markdown("""
    **描述問題的範本：**
    ```
    【問題】拍照時螢幕上的倒數計時會閃爍
    【重現步驟】投幣 → 選背景 → 進入拍照 → 倒數時螢幕閃爍
    【環境】Windows 10 + Chrome + Streamlit 1.30
    【期望】倒數數字平穩顯示，不閃爍
    ```

    把這段貼給 Claude，它會幫你分析原因並提出修正方案。
    """)

elif current_section == "HW9. 課後練習":
    st.title("📝 課後練習：完成一輪完整測試")

    st.markdown("本週的任務是把 MVP 做一次完整的測試，找出所有問題。")

    st.divider()
    st.subheader("🎯 練習任務")
    st.markdown("""
    1. **對照測試紀錄表**，逐項測試每個功能
    2. **記錄所有發現的問題**，標記優先度
    3. **至少修正一個問題**，用 Git commit 記錄修正內容
    4. **請一個非團隊成員**操作一次完整流程，記錄他們的反應
    """)

    st.divider()
    st.subheader("📤 繳交作業")
    student9 = st.text_input("你的名字", key="hw9_name", placeholder="例：JD")
    hw9_file = st.file_uploader(
        "上傳測試紀錄或問題清單",
        type=["png", "jpg", "jpeg", "pdf", "txt", "docx", "md", "xlsx"],
        key="hw9_upload",
    )
    if hw9_file and student9:
        path, gdrive_link = save_uploaded_file(hw9_file, "HW9", student9)
        st.success(f"✅ 作業已儲存！檔案：`{os.path.basename(path)}`")
        if gdrive_link:
            st.info(f"☁️ 已同步到 Google Drive")
    elif hw9_file and not student9:
        st.warning("請先填寫你的名字再上傳。")

# =====================================================
# 第十堂課：會員系統與社群經營
# =====================================================

elif current_section == "R9. 上堂回顧與 Q&A":
    lesson_cover(10, "會員系統與社群經營", "建立會員關係、經營官方帳號、設計回購機制", "👥")
    st.title("🔄 上堂回顧：測試迭代")

    st.subheader("📋 第九堂成果確認")
    for item in ["完成完整測試一輪", "問題清單已建立", "至少修正一個問題", "使用者測試完成"]:
        st.checkbox(item, key=f"r9_{item}")

    st.divider()
    st.subheader("📊 目前 Bug 狀態")
    col_open, col_fixed = st.columns(2)
    with col_open:
        open_bugs = st.number_input("待修問題數", min_value=0, value=0, key="open_bugs")
    with col_fixed:
        fixed_bugs = st.number_input("已修問題數", min_value=0, value=0, key="fixed_bugs")

    if open_bugs + fixed_bugs > 0:
        st.progress(fixed_bugs / (open_bugs + fixed_bugs))
        st.caption(f"修復率：{fixed_bugs}/{open_bugs + fixed_bugs}")

elif current_section == "30. 會員關係建立與維護":
    st.title("👥 會員關係建立與維護")

    st.markdown("""
    拍貼機不只是「一次性消費」。透過會員系統，你可以：
    - **認識你的客人** — 知道誰是回頭客、什麼時段最多人
    - **創造回購動機** — 集點、優惠券、會員專屬背景
    - **建立長期關係** — 推播活動訊息、生日優惠
    """)

    st.divider()
    tab_system, tab_flow, tab_retention = st.tabs(["🏗️ 會員系統架構", "📱 註冊流程設計", "🔄 回購機制"])

    with tab_system:
        st.markdown("### 會員系統最小架構")

        st.markdown("""
        ```
        📱 客人掃 QR Code
            ↓
        🌐 LINE 官方帳號加好友
            ↓
        📋 自動建立會員資料
            ↓
        💰 消費紀錄自動累積
            ↓
        🎁 達標自動發送獎勵
        ```
        """)

        st.info("""
        💡 **為什麼用 LINE 而不是自己做 App？**
        - 台灣人幾乎都有 LINE，不用額外下載
        - LINE 官方帳號免費額度就夠小型營運使用
        - 推播訊息直接送到客人手機
        """)

    with tab_flow:
        st.markdown("### 會員註冊流程（無痛版）")
        st.markdown("客人不需要填任何表單，只要掃碼加好友就完成：")

        flow_steps = [
            ("📷 拍照完成後", "螢幕顯示 QR Code：「掃碼加好友，免費領取電子版照片」"),
            ("📱 客人掃碼", "自動加入 LINE 官方帳號"),
            ("🤖 自動回覆", "歡迎訊息 + 發送電子版照片連結"),
            ("📊 後台記錄", "自動建立會員：LINE 暱稱、首次消費日期、消費金額"),
        ]

        for step, desc in flow_steps:
            st.markdown(f"**{step}**")
            st.markdown(f"　{desc}")

        st.warning("⚠️ **隱私注意：** 不要收集不必要的個資。LINE 暱稱 + 消費記錄就夠用了。")

    with tab_retention:
        st.markdown("### 回購機制設計")

        retention_ideas = [
            ("🎫 集點卡", "每次消費累積 1 點，滿 5 點免費拍一次", "簡單有效，客人有明確目標"),
            ("🎂 生日優惠", "生日月份享半價（需加入 LINE 官方帳號）", "增加加好友的誘因"),
            ("🖼️ 會員專屬背景", "每月推出會員限定背景/相框", "創造持續回來的理由"),
            ("👫 揪團優惠", "兩人同行第二位半價", "客人自帶新客人"),
        ]

        for icon_name, desc, why in retention_ideas:
            with st.expander(icon_name):
                st.markdown(f"**做法：** {desc}")
                st.markdown(f"**效果：** {why}")

elif current_section == "31. 官方帳號與社群經營":
    st.title("📣 官方帳號與社群經營")

    st.markdown("拍貼機的商業價值不只在機台上，**社群是延伸戰場**。")

    st.divider()
    tab_internal, tab_merchandise = st.tabs(["🏢 內部社群經營", "🛍️ 周邊商品功能"])

    with tab_internal:
        st.markdown("### 經營 LINE 官方帳號")

        st.markdown("#### 📅 內容行事曆建議")
        calendar = [
            ("每週", "分享客人拍照趣事（需徵得同意）、最新背景預覽"),
            ("每月", "會員專屬優惠、新品/新場地預告"),
            ("活動前", "快閃店地點＆日期公告、限定背景預覽"),
            ("活動後", "活動照片精選、感謝訊息、下次活動預告"),
        ]

        for freq, content in calendar:
            col_f, col_c = st.columns([2, 8])
            with col_f:
                st.markdown(f"**{freq}**")
            with col_c:
                st.markdown(content)

        st.divider()
        st.markdown("#### 🤖 自動化訊息（用 AI 生成）")
        st.code("""【背景】
我經營一個 PhotoBooth 拍貼機的 LINE 官方帳號。

【目標】
請幫我生成以下自動回覆訊息（繁體中文、語氣活潑親切）：
1. 新好友歡迎訊息
2. 消費後感謝訊息（附電子照片領取連結）
3. 集點滿 5 點的通知訊息
4. 一個月沒消費的喚回訊息
5. 生日祝福訊息""", language=None)

    with tab_merchandise:
        st.markdown("### 周邊商品功能規劃")
        st.markdown("把拍貼照片延伸成實體商品，創造額外營收。")

        products = [
            ("🧲 客製磁鐵", "把拍貼照片印成冰箱磁鐵", "成本低、製作快、客人愛收藏"),
            ("🔑 鑰匙圈", "壓克力鑰匙圈 + 拍貼照片", "適合快閃店現場販售"),
            ("📱 手機殼", "客製化手機殼（需搭配外部廠商）", "單價高、利潤好"),
            ("📮 明信片", "把拍貼照片印成明信片，現場可寄出", "適合觀光景點"),
            ("🎁 貼紙組", "一組 6 張迷你貼紙", "成本最低、適合年輕客群"),
        ]

        for icon_name, desc, note in products:
            col_p, col_d, col_n = st.columns([2, 5, 3])
            with col_p:
                st.markdown(f"**{icon_name}**")
            with col_d:
                st.markdown(desc)
            with col_n:
                st.caption(note)

        st.divider()
        st.info("""
        💡 **MVP 思維用在周邊商品：**
        先從「貼紙組」開始（成本最低、製作最快），驗證客人有購買意願後，
        再逐步加入其他商品。不要一次全做。
        """)

elif current_section == "HW10. 課後練習":
    st.title("📝 課後練習：設計你的會員方案")

    st.markdown("根據今天的課程，設計一份適合你的會員與社群經營方案。")

    st.divider()
    st.subheader("🎯 練習任務")
    st.markdown("""
    1. **決定會員系統的建立方式**（LINE 官方帳號 / 其他）
    2. **設計一個回購機制**（集點？生日優惠？會員專屬？）
    3. **規劃第一個月的社群內容**（至少 4 則貼文主題）
    4. **選一款周邊商品**做為試賣品項

    可以請 AI 幫你發想和細化方案。
    """)

    st.divider()
    st.subheader("📤 繳交作業")
    student10 = st.text_input("你的名字", key="hw10_name", placeholder="例：JD")
    hw10_file = st.file_uploader(
        "上傳會員方案或社群經營規劃",
        type=["png", "jpg", "jpeg", "pdf", "txt", "docx", "md"],
        key="hw10_upload",
    )
    if hw10_file and student10:
        path, gdrive_link = save_uploaded_file(hw10_file, "HW10", student10)
        st.success(f"✅ 作業已儲存！檔案：`{os.path.basename(path)}`")
        if gdrive_link:
            st.info(f"☁️ 已同步到 Google Drive")
    elif hw10_file and not student10:
        st.warning("請先填寫你的名字再上傳。")

# =====================================================
# 第十一堂課：維護自動化與周邊商品
# =====================================================

elif current_section == "R10. 上堂回顧與 Q&A":
    lesson_cover(11, "維護自動化與周邊商品", "讓機台自己告訴你它需要什麼，拓展商品線", "⚙️")
    st.title("🔄 上堂回顧：會員與社群")

    st.subheader("📋 第十堂成果確認")
    for item in ["會員系統方案確定", "回購機制設計完成", "社群內容規劃", "周邊商品品項選定"]:
        st.checkbox(item, key=f"r10_{item}")

    st.divider()
    st.text_area("分享你的會員方案構想", key="r10_share", height=100)

elif current_section == "32. 維護流程自動化":
    st.title("⚙️ 維護流程自動化")

    st.markdown("""
    機台在外面跑，你不可能 24 小時盯著看。
    **自動化維護 = 讓機台自己告訴你它需要什麼。**
    """)

    st.divider()
    tab_monitor, tab_alert, tab_sop = st.tabs(["📊 自動監控", "🔔 異常告警", "📋 維護 SOP 自動化"])

    with tab_monitor:
        st.markdown("### 機台健康監控儀表板")
        st.markdown("讓 AI 幫你建一個簡單的監控頁面，即時掌握每台機台的狀態。")

        monitor_items = [
            ("🖨️ 相紙存量", "剩餘張數 / 低於 20 張時告警"),
            ("🌡️ 機台溫度", "CPU / 印表機溫度 / 超過 60°C 告警"),
            ("📶 網路狀態", "連線/斷線 / 延遲超過 500ms 告警"),
            ("💾 硬碟空間", "剩餘容量 / 低於 1GB 告警"),
            ("📷 相機狀態", "正常/離線 / 連拍失敗率"),
            ("💰 營收統計", "今日拍照次數 / 營收金額"),
        ]

        cols = st.columns(3)
        for i, (name, desc) in enumerate(monitor_items):
            with cols[i % 3]:
                st.markdown(f"""
                <div style="background: rgba(45,52,54,0.5); border-radius: 10px; padding: 15px;
                            margin-bottom: 10px; min-height: 100px;">
                    <p style="font-size: 16px; margin: 0;">{name}</p>
                    <p style="font-size: 12px; color: #b2bec3; margin: 5px 0 0 0;">{desc}</p>
                </div>
                """, unsafe_allow_html=True)

    with tab_alert:
        st.markdown("### 異常告警通知設定")
        st.markdown("當機台出問題時，自動發通知到你的手機。")

        alert_channels = [
            ("LINE Notify", "免費、設定簡單、即時推播到 LINE", "推薦 ⭐"),
            ("Email", "適合記錄，但即時性差", "備用"),
            ("LINE 官方帳號", "可以順便通知客人機台狀態", "進階"),
        ]

        for channel, desc, tag in alert_channels:
            st.markdown(f"**{channel}** — {desc}　`{tag}`")

        st.divider()
        st.markdown("**建議 Prompt：**")
        st.code("""【背景】
我的 PhotoBooth 系統需要在異常時自動發送通知到我的 LINE。

【目標】
請幫我用 LINE Notify 實作告警通知：
1. 當相紙剩餘低於 20 張時通知
2. 當網路斷線超過 30 秒時通知
3. 當印表機報錯時通知（附錯誤代碼）
4. 每日營業結束時發送當日統計摘要

【風格】
通知訊息用繁體中文，簡短明瞭。""", language=None)

    with tab_sop:
        st.markdown("### 定期維護 SOP")

        st.markdown("#### 📅 日常維護（每日營業前）")
        daily = ["檢查相紙存量", "確認印表機墨水/色帶", "測試網路連線", "執行一次完整測試拍照", "清潔觸控螢幕和鏡頭"]
        for item in daily:
            st.markdown(f"- {item}")

        st.markdown("#### 📅 週維護")
        weekly = ["清理硬碟暫存照片", "檢查系統更新", "備份資料到外部硬碟", "檢查所有線材是否鬆脫"]
        for item in weekly:
            st.markdown(f"- {item}")

        st.markdown("#### 📅 月維護")
        monthly = ["深度清潔所有硬體", "更換耗材（色帶/相紙補充）", "匯出月報資料", "檢討異常紀錄、優化系統"]
        for item in monthly:
            st.markdown(f"- {item}")

elif current_section == "33. 周邊商品功能規劃":
    st.title("🛍️ 周邊商品功能規劃")

    st.markdown("把「拍照留念」延伸成「帶走商品」，創造更多營收。")

    st.divider()
    st.subheader("📐 商品功能的系統設計")

    st.markdown("""
    在拍貼機的流程中加入商品選購環節：

    ```
    📷 拍照完成
        ↓
    🖼️ 預覽照片
        ↓
    ┌─────────────────────────────┐
    │  🖨️ 列印照片（基本方案）      │ ← 原有流程
    │  🧲 加購磁鐵 (+$50)          │ ← 新增
    │  🔑 加購鑰匙圈 (+$80)        │ ← 新增
    │  🎁 加購貼紙組 (+$30)        │ ← 新增
    └─────────────────────────────┘
        ↓
    💰 顯示總金額 → 付款
        ↓
    🎉 製作 & 取貨
    ```
    """)

    st.divider()
    st.subheader("💰 商品定價參考")

    pricing = [
        ("拍貼照片（基本）", "$50-80", "$5-10", "85%+"),
        ("迷你貼紙組 x6", "$30-50", "$5-8", "80%+"),
        ("客製磁鐵", "$50-80", "$15-20", "70%+"),
        ("壓克力鑰匙圈", "$80-120", "$20-30", "70%+"),
        ("明信片", "$30-50", "$5-10", "80%+"),
    ]

    st.markdown("| 商品 | 建議售價 | 估計成本 | 毛利率 |")
    st.markdown("|------|---------|---------|--------|")
    for name, price, cost, margin in pricing:
        st.markdown(f"| {name} | {price} | {cost} | {margin} |")

    st.divider()
    st.info("""
    💡 **實作優先順序：**
    1. 先做「貼紙組」— 只需要調整列印排版，不需額外設備
    2. 再做「磁鐵」— 需要磁鐵片 + 護貝機，成本可控
    3. 最後做「鑰匙圈」— 需要壓克力切割機或外包
    """)

elif current_section == "HW11. 課後練習":
    st.title("📝 課後練習：建立你的維護計畫")

    st.markdown("設計一份完整的維護計畫和周邊商品試做。")

    st.divider()
    st.subheader("🎯 練習任務")
    st.markdown("""
    1. **設定 LINE Notify 告警**（或選擇其他通知方式）
    2. **制定日/週/月維護 SOP**，列印貼在機台旁
    3. **選一款周邊商品試做**，計算實際成本
    4. **設計加購流程的 UI 草稿**（可以用紙筆畫，拍照上傳）
    """)

    st.divider()
    st.subheader("📤 繳交作業")
    student11 = st.text_input("你的名字", key="hw11_name", placeholder="例：JD")
    hw11_file = st.file_uploader(
        "上傳維護計畫、商品試做照片、或 UI 草稿",
        type=["png", "jpg", "jpeg", "pdf", "txt", "docx", "md"],
        key="hw11_upload",
    )
    if hw11_file and student11:
        path, gdrive_link = save_uploaded_file(hw11_file, "HW11", student11)
        st.success(f"✅ 作業已儲存！檔案：`{os.path.basename(path)}`")
        if gdrive_link:
            st.info(f"☁️ 已同步到 Google Drive")
    elif hw11_file and not student11:
        st.warning("請先填寫你的名字再上傳。")

# =====================================================
# 第十二堂課：成果發表與未來路線圖
# =====================================================

elif current_section == "R11. 上堂回顧與 Q&A":
    lesson_cover(12, "成果發表與未來路線圖", "整理三個月成果，展望自主營運的未來", "🎓")
    st.title("🔄 上堂回顧：維護與商品")

    st.subheader("📋 第十一堂成果確認")
    for item in ["告警通知設定完成", "維護 SOP 制定", "周邊商品試做", "加購流程 UI 草稿"]:
        st.checkbox(item, key=f"r11_{item}")

    st.divider()
    st.text_area("分享你的維護或商品試做經驗", key="r11_share", height=100)

elif current_section == "34. 成果發表準備":
    st.title("🎓 成果發表準備")

    st.markdown("十二堂課走到這裡，是時候整理成果，做一次正式的成果發表。")

    st.divider()
    st.subheader("🗺️ 我們走了多遠？")

    milestones_12 = [
        {"month": "第一個月", "title": "基礎建設", "items": ["Vibe Coding 入門", "環境部署", "UI 復刻與在地化", "支付串接"]},
        {"month": "第二個月", "title": "硬體整合", "items": ["硬體 SDK 串接", "部署 SOP", "GitHub 版控", "MVP 驗收"]},
        {"month": "第三個月", "title": "優化與擴展", "items": ["測試迭代", "會員系統", "維護自動化", "周邊商品"]},
    ]

    cols = st.columns(3)
    for i, m in enumerate(milestones_12):
        with cols[i]:
            color = ["#e74c3c", "#f39c12", "#27ae60"][i]
            items_html = "".join(f"<p style='font-size:13px; margin:3px 0;'>✅ {item}</p>" for item in m["items"])
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}33 0%, {color}11 100%);
                        border-radius: 12px; padding: 20px; border-top: 4px solid {color};
                        min-height: 220px;">
                <h4 style="color: {color};">{m['month']}</h4>
                <p><strong>{m['title']}</strong></p>
                {items_html}
            </div>
            """, unsafe_allow_html=True)

    st.divider()
    st.subheader("📊 專案完成度總覽")

    phases_12 = {
        "UI 介面復刻": 90,
        "文字在地化": 90,
        "支付串接": 70,
        "印表機串接": 60,
        "相機串接": 60,
        "投幣機串接": 50,
        "部署 SOP": 80,
        "會員系統": 40,
        "維護自動化": 30,
        "周邊商品": 20,
    }

    for phase, pct in phases_12.items():
        col_label, col_bar = st.columns([3, 7])
        with col_label:
            st.markdown(f"**{phase}**")
        with col_bar:
            st.progress(pct / 100)
            st.caption(f"{pct}%")

    st.divider()
    st.subheader("📝 成果發表大綱")
    st.markdown("""
    準備一份 10 分鐘的成果發表，包含：

    | 段落 | 時間 | 內容 |
    |------|------|------|
    | 開場 | 1 分鐘 | 專案背景與目標 |
    | 技術歷程 | 3 分鐘 | 從零開始到 MVP 的過程 |
    | 現場 Demo | 3 分鐘 | 實機演示完整流程 |
    | 數據成果 | 1 分鐘 | 測試數據、效率提升 |
    | 未來規劃 | 2 分鐘 | 下一步要做什麼 |
    """)

elif current_section == "35. 未來路線圖":
    st.title("🔮 未來路線圖")

    st.markdown("課程結束不是終點，而是自主營運的起點。")

    st.divider()
    st.subheader("📅 課程後 3 個月行動計畫")

    roadmap = [
        {
            "period": "第 1 個月（穩定期）",
            "color": "#3498db",
            "goals": [
                "完成所有硬體模組串接",
                "實際快閃店部署至少 2 次",
                "收集使用者回饋、修正問題",
                "建立穩定的維護 SOP",
            ],
        },
        {
            "period": "第 2 個月（成長期）",
            "color": "#e67e22",
            "goals": [
                "上線會員系統（LINE 官方帳號）",
                "推出第一款周邊商品（貼紙組）",
                "建立數據儀表板，追蹤營運指標",
                "開始經營社群內容",
            ],
        },
        {
            "period": "第 3 個月（擴展期）",
            "color": "#27ae60",
            "goals": [
                "導入 AI 美顏功能",
                "擴展周邊商品品項",
                "考慮第二台機台部署",
                "整理技術文件，培訓團隊成員",
            ],
        },
    ]

    for r in roadmap:
        st.markdown(f"""
        <div style="border-left: 4px solid {r['color']}; padding: 15px 20px; margin-bottom: 15px;
                    background: rgba(45,52,54,0.3); border-radius: 0 8px 8px 0;">
            <strong style="color: {r['color']}; font-size: 16px;">{r['period']}</strong>
        </div>
        """, unsafe_allow_html=True)
        for goal in r["goals"]:
            st.markdown(f"　　- {goal}")

    st.divider()
    st.subheader("💡 持續使用 AI 的方向")

    ai_applications = [
        ("🧑‍💻 程式開發", "功能新增、Bug 修復、程式碼重構"),
        ("📊 數據分析", "營收分析、客群分析、定價優化"),
        ("📝 內容生成", "社群貼文、行銷文案、活動企劃"),
        ("🎨 設計產出", "相框設計、宣傳海報、商品視覺"),
        ("📖 文件撰寫", "操作手冊、維護指南、提案簡報"),
    ]

    for icon_name, examples in ai_applications:
        col_ai, col_ex = st.columns([3, 7])
        with col_ai:
            st.markdown(f"**{icon_name}**")
        with col_ex:
            st.markdown(examples)

    st.divider()
    st.markdown("")
    st.success("""
    🎉 **恭喜完成十二堂課程！**

    你已經從「什麼是 Vibe Coding」走到「獨立營運一台智慧拍貼機」。

    記住我們的開發哲學：
    **穩定、小規模、快速產出可驗收的成果。**

    有任何問題隨時找 Jeff，Claude Code 也隨時待命！🚀
    """)

elif current_section == "HW12. 課後練習":
    st.title("📝 最終作業：成果整理與發表")

    st.markdown("最後一堂課了。整理你的成果，準備正式發表。")

    st.divider()
    st.subheader("🎯 練習任務")
    st.markdown("""
    1. **準備成果發表簡報**（10 分鐘內）
    2. **確認實機 Demo 可正常運作**
    3. **整理專案的 GitHub README**，讓其他人看得懂
    4. **寫下你的學習心得和未來計畫**
    """)

    st.divider()
    st.subheader("💬 學習心得")
    st.text_area("十二堂課下來，你最大的收穫是什麼？未來想繼續學什麼？",
                 key="final_feedback_12", height=150)

    st.divider()
    st.subheader("📤 繳交作業")
    student12 = st.text_input("你的名字", key="hw12_name", placeholder="例：JD")
    hw12_file = st.file_uploader(
        "上傳成果簡報或學習心得",
        type=["png", "jpg", "jpeg", "pdf", "txt", "docx", "md", "pptx"],
        key="hw12_upload",
    )
    if hw12_file and student12:
        path, gdrive_link = save_uploaded_file(hw12_file, "HW12", student12)
        st.success(f"✅ 作業已儲存！檔案：`{os.path.basename(path)}`")
        if gdrive_link:
            st.info(f"☁️ 已同步到 Google Drive")
    elif hw12_file and not student12:
        st.warning("請先填寫你的名字再上傳。")

# =====================================================
# 教師後台
# =====================================================

elif current_section == "📋 作業繳交追蹤":
    st.title("📋 作業繳交追蹤")

    st.markdown("一覽所有學員的作業繳交狀態。資料來源：`uploads/homework/` 資料夾。")

    hw_dir = os.path.join(os.path.dirname(__file__), "uploads", "homework")
    hw_labels = {
        "HW1": "與 AI 對話產出規格書",
        "HW2": "用 AI 完成一個小功能",
        "HW3": "系統需求描述",
        "HW4": "截圖復刻系統頁面",
        "HW5": "硬體規格文件",
        "HW6": "硬體模組串接",
        "HW7": "完整部署測試",
        "HW8": "GitHub 上傳專案",
        "HW9": "完整測試一輪",
        "HW10": "會員方案設計",
        "HW11": "維護計畫",
        "HW12": "成果發表",
    }

    if os.path.exists(hw_dir):
        # 收集所有學員名單
        all_students = set()
        hw_data = {}
        for hw_name in hw_labels:
            hw_path = os.path.join(hw_dir, hw_name)
            hw_data[hw_name] = []
            if os.path.exists(hw_path):
                for f in os.listdir(hw_path):
                    parts = f.split("_")
                    student = parts[0] if len(parts) >= 3 else "未知"
                    timestamp = f"{parts[1]}_{parts[2]}" if len(parts) >= 3 else ""
                    all_students.add(student)
                    hw_data[hw_name].append({"student": student, "time": timestamp, "file": f})

        if all_students:
            st.divider()
            st.subheader("📊 繳交總覽")

            # 統計卡片
            total_hw = len(hw_labels)
            total_students = len(all_students)
            total_submissions = sum(len(v) for v in hw_data.values())

            col_s, col_h, col_t = st.columns(3)
            with col_s:
                st.metric("學員人數", total_students)
            with col_h:
                st.metric("作業堂數", total_hw)
            with col_t:
                st.metric("總繳交數", total_submissions)

            st.divider()
            st.subheader("📋 各堂作業繳交明細")

            # 繳交矩陣表格
            header = "| 學員 |" + "|".join(f" {k} " for k in hw_labels) + "|"
            separator = "|---|" + "|".join("---" for _ in hw_labels) + "|"
            st.markdown(header)
            st.markdown(separator)

            for student in sorted(all_students):
                row = f"| **{student}** |"
                for hw_name in hw_labels:
                    submitted = any(d["student"] == student for d in hw_data[hw_name])
                    row += " ✅ |" if submitted else " ⬜ |"
                st.markdown(row)

            st.divider()
            st.subheader("📂 作業檔案詳細列表")

            for hw_name, label in hw_labels.items():
                files = hw_data[hw_name]
                with st.expander(f"{hw_name}：{label}（{len(files)} 份）"):
                    if files:
                        for f_info in sorted(files, key=lambda x: x["time"], reverse=True):
                            col_n, col_t, col_f = st.columns([2, 3, 5])
                            with col_n:
                                st.markdown(f"**{f_info['student']}**")
                            with col_t:
                                t = f_info["time"]
                                if len(t) >= 15:
                                    display_t = f"{t[:4]}/{t[4:6]}/{t[6:8]} {t[9:11]}:{t[11:13]}"
                                else:
                                    display_t = t
                                st.caption(display_t)
                            with col_f:
                                st.caption(f_info["file"])
                    else:
                        st.caption("尚無人繳交")
        else:
            st.info("📭 目前還沒有學員繳交作業。")
    else:
        st.info("📭 尚未有任何作業上傳紀錄。作業會在學員上傳後出現在這裡。")

elif current_section == "📈 課程進度總覽":
    st.title("📈 課程進度總覽")

    st.markdown("追蹤整體課程的執行進度與規劃狀態。")

    st.divider()
    st.subheader("🗓️ 十二堂課程進度")

    course_progress = [
        {"lesson": "第一堂", "title": "Vibe Coding 入門", "month": "第一個月", "status": "completed"},
        {"lesson": "第二堂", "title": "實戰體驗與案例", "month": "第一個月", "status": "completed"},
        {"lesson": "第三堂", "title": "需求分析與架構規劃", "month": "第一個月", "status": "completed"},
        {"lesson": "第四堂", "title": "截圖復刻與在地化", "month": "第一個月", "status": "completed"},
        {"lesson": "第五堂", "title": "支付串接與部署策略", "month": "第二個月", "status": "in_progress"},
        {"lesson": "第六堂", "title": "硬體整合與總結", "month": "第二個月", "status": "in_progress"},
        {"lesson": "第七堂", "title": "部署與 MVP 驗收", "month": "第二個月", "status": "planned"},
        {"lesson": "第八堂", "title": "GitHub 版本控制與協作", "month": "第二個月", "status": "planned"},
        {"lesson": "第九堂", "title": "測試迭代與品質優化", "month": "第三個月", "status": "planned"},
        {"lesson": "第十堂", "title": "會員系統與社群經營", "month": "第三個月", "status": "planned"},
        {"lesson": "第十一堂", "title": "維護自動化與周邊商品", "month": "第三個月", "status": "planned"},
        {"lesson": "第十二堂", "title": "成果發表與未來路線圖", "month": "第三個月", "status": "planned"},
    ]

    status_icons = {"completed": "✅", "in_progress": "🔄", "planned": "📅"}
    status_labels = {"completed": "已完成", "in_progress": "進行中", "planned": "規劃中"}

    # 進度統計
    completed = sum(1 for c in course_progress if c["status"] == "completed")
    st.progress(completed / len(course_progress))
    st.caption(f"已完成 {completed} / {len(course_progress)} 堂課")

    st.divider()

    # 按月份分組
    for month in ["第一個月", "第二個月", "第三個月"]:
        month_courses = [c for c in course_progress if c["month"] == month]
        month_completed = sum(1 for c in month_courses if c["status"] == "completed")
        st.markdown(f"#### {month}（{month_completed}/{len(month_courses)} 完成）")

        for c in month_courses:
            icon = status_icons[c["status"]]
            label = status_labels[c["status"]]
            col_icon, col_lesson, col_title, col_status = st.columns([1, 2, 5, 2])
            with col_icon:
                st.markdown(icon)
            with col_lesson:
                st.markdown(f"**{c['lesson']}**")
            with col_title:
                st.markdown(c["title"])
            with col_status:
                st.caption(label)
        st.markdown("")

    st.divider()
    st.subheader("📊 專案模組完成度")
    st.markdown("根據實際開發進度更新（教師手動調整）：")

    module_progress = {
        "UI 介面復刻": 80,
        "文字在地化": 70,
        "支付串接": 30,
        "印表機串接": 20,
        "相機串接": 20,
        "投幣機串接": 10,
        "部署 SOP": 40,
        "GitHub 版控": 50,
        "會員系統": 0,
        "維護自動化": 0,
        "周邊商品": 0,
    }

    for mod, pct in module_progress.items():
        col_label, col_bar = st.columns([3, 7])
        with col_label:
            st.markdown(f"**{mod}**")
        with col_bar:
            st.progress(pct / 100)
            st.caption(f"{pct}%")

    st.divider()
    st.info("💡 進度數據目前為靜態設定。未來可串接 GitHub commit 紀錄或資料庫，自動更新進度。")
