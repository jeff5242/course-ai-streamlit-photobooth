import streamlit as st
import time
import io
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# 設定頁面配置
st.set_page_config(layout="wide", page_title="AI 領航員：Vibe Coding 實戰教學")

# --- 自定義樣式 ---
st.markdown("""
    <style>
    .stTabs [data-baseweb="tab-list"] { gap: 20px; }
    .stTabs [data-baseweb="tab"] { height: 50px; font-size: 18px; font-weight: bold; }
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
        "15. 快閃店部署策略",
        "16. 數據儀表板願景",
        "HW5. 課後練習",
    ])
else:
    current_section = st.sidebar.radio("課程章節", [
        "R5. 上堂回顧與 Q&A",
        "17. 硬體 SDK 規格收集",
        "18. 通訊協定解析",
        "19. 整合架構設計",
        "20. 整合實作與測試",
        "21. 課程總結與後續規劃",
        "HW6. 課後練習",
    ])

# =====================================================
# 第一堂課
# =====================================================

if current_section == "0. 啟航：計畫願景":
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
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    border-radius: 15px; padding: 40px 20px; text-align: center; color: white;">
            <p style="font-size: 48px; margin: 0;">🔄</p>
            <h3 style="margin: 10px 0; color: white;">數位轉型</h3>
            <p style="font-size: 14px; opacity: 0.9;">被動使用 ➜ AI 驅動 ➜ 自主掌控</p>
        </div>
        """, unsafe_allow_html=True)
        st.caption("系統轉型示意圖")

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

    tab1, tab2, tab3 = st.tabs(["💡 核心概念", "⚔️ 能與不能", "🎯 Prompt 實戰練習"])

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
    st.subheader("📤 繳交方式")
    st.info("請將 AI 產出的規格書文件（截圖或文字檔）帶來下堂課，我們會一起檢視並討論。")

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

    st.subheader("📤 繳交方式")
    st.markdown("請將對話截圖或 AI 產出的程式碼帶來下堂課分享。")

# =====================================================
# 第三堂課：需求分析與架構規劃
# =====================================================

elif current_section == "R2. 上堂回顧與 Q&A":
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
    ```
    ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
    │  開發環境     │     │  Docker 封裝 │     │  快閃店設備   │
    │  (Streamlit) │ ──→ │  (映像打包)   │ ──→ │  (一鍵啟動)   │
    └─────────────┘     └─────────────┘     └─────────────┘
         Jeff/JD             技術同事              現場同仁
    ```
    """)

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
    st.info("📤 請將作業帶來下堂課，我們會用你的需求描述來做截圖復刻的實戰練習。")

# =====================================================
# 第四堂課：截圖復刻與在地化
# =====================================================

elif current_section == "R3. 上堂回顧與 Q&A":
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
    ```
    ┌──────────┐    ┌──────────────┐    ┌────────────┐
    │ Streamlit │───→│  後端 Server  │───→│ LINE Pay   │
    │ 前端介面   │←───│  (Webhook)   │←───│ / 街口 API  │
    └──────────┘    └──────────────┘    └────────────┘
         ↕                 ↕
    ┌──────────┐    ┌──────────────┐
    │ 使用者手機 │    │  交易資料庫   │
    │ 掃 QR Code│    │  (記錄/對帳)  │
    └──────────┘    └──────────────┘
    ```
    """)

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
    ```
    ┌──────────┐    ┌──────────────┐    ┌────────────┐
    │ Streamlit │───→│ 列印服務模組  │───→│  印表機     │
    │ 產生合成圖 │    │ (Python)     │    │ (USB/網路)  │
    └──────────┘    └──────────────┘    └────────────┘
    ```
    """)

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

    st.code("""
┌─────────────────────────────────────────────────┐
│                   控制主機                        │
│  (Raspberry Pi 5 / Intel NUC)                   │
│  OS: Linux    Runtime: Python                    │
│                                                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐       │
│  │ 拍貼軟體  │  │ 支付監聽  │  │ 印表機驅動│       │
│  │(Streamlit)│  │(紙鈔機)  │  │(CUPS/USB)│       │
│  └────┬─────┘  └────┬─────┘  └─────┬────┘       │
│       │              │              │             │
│  ─────┴──────────────┴──────────────┴─────       │
│                      │                            │
│  I/O 介面            │                            │
│  ┌───────┬───────┬───┴───┬─────────┬───────┐    │
│  │HDMI×2 │USB×3  │Serial │  USB    │ GPIO  │    │
│  │螢幕輸出│觸控/鼠 │紙鈔機  │ 印表機  │(Pi用) │    │
│  └───┬───┘└───┬──┘└───┬──┘└───┬────┘└──┬───┘    │
└──────┼────────┼───────┼───────┼────────┼────────┘
       │        │       │       │        │
  ┌────┴───┐┌───┴──┐┌───┴──┐┌──┴───┐┌───┴────┐
  │螢幕×2  ││觸控  ││紙鈔  ││印表機││紙鈔訊號│
  │(操作+  ││+ 滑鼠││接收器││(熱昇 ││(GPIO  │
  │ 預覽)  ││      ││      ││ 華)  ││ 備用) │
  └────────┘└──────┘└──────┘└──────┘└───────┘
    """, language=None)

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
    st.info("📤 請帶來下堂課，我們會用這些資訊進行整合架構設計。")

# =====================================================
# 第六堂課：硬體整合與總結
# =====================================================

elif current_section == "R5. 上堂回顧與 Q&A":
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
    ```
    ┌────────────────────────────────────────────────────────┐
    │                    PhotoBooth 主機                      │
    │                                                        │
    │  ┌──────────┐  ┌──────────┐  ┌──────────┐             │
    │  │ Streamlit │  │ 硬體控制  │  │ 支付服務  │             │
    │  │ 前端 UI   │  │ 中間層    │  │ 中間層    │             │
    │  └────┬─────┘  └────┬─────┘  └────┬─────┘             │
    │       │              │              │                   │
    │       └──────────────┼──────────────┘                   │
    │                      │                                  │
    │              ┌───────┴───────┐                          │
    │              │  主控程式      │                          │
    │              │  (Python)     │                          │
    │              └───────┬───────┘                          │
    │                      │                                  │
    │    ┌─────────┬───────┼───────┬──────────┐              │
    │    │         │       │       │          │              │
    │  ┌─┴──┐  ┌──┴──┐ ┌──┴──┐ ┌──┴──┐  ┌───┴───┐         │
    │  │相機 │  │印表機│ │投幣機│ │燈光  │  │觸控螢幕│         │
    │  │USB  │  │USB/IP│ │Serial│ │GPIO │  │HDMI   │         │
    │  └────┘  └─────┘ └─────┘ └─────┘  └───────┘         │
    └────────────────────────────────────────────────────────┘
    ```
    """)

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
    st.title("🎓 四堂課總結與後續規劃")

    st.subheader("🗺️ 我們走了多遠？")

    milestones = [
        {"lesson": "第一堂", "title": "Vibe Coding 入門", "status": "概念理解 + 看到 Demo"},
        {"lesson": "第二堂", "title": "實戰規劃", "status": "痛點分析 + 準備清單 + QR Code 模擬"},
        {"lesson": "第三堂", "title": "截圖復刻", "status": "動手用 Claude Code 重建介面"},
        {"lesson": "第四堂", "title": "硬體整合", "status": "SDK 收集 + 架構設計 + 串接實作"},
    ]

    cols = st.columns(4)
    for i, m in enumerate(milestones):
        with cols[i]:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                        border-radius: 15px; padding: 20px; color: white; min-height: 180px; text-align:center;">
                <h4 style="color: white;">{m['lesson']}</h4>
                <p style="font-size: 16px;"><b>{m['title']}</b></p>
                <hr style="border-color: rgba(255,255,255,0.3);">
                <p style="font-size: 13px;">{m['status']}</p>
            </div>
            """, unsafe_allow_html=True)

    st.divider()
    st.subheader("📊 專案完成度總覽")

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
    st.subheader("🔮 後續行動計畫")

    st.markdown("""
    | 時程 | 行動 | 負責人 |
    |---|---|---|
    | **第 1-2 週** | 完成所有頁面復刻 + 在地化驗收 | JD + Jeff |
    | **第 3 週** | LINE Pay Sandbox 串接測試 | JD + Claude |
    | **第 4 週** | 印表機 + 相機實機串接 | 技術同事 + Claude |
    | **第 5 週** | 投幣機串接 + 全流程整合測試 | 全員 |
    | **第 6 週** | 快閃店實地部署測試 | 全員 |
    | **第 7-8 週** | 修復問題 + 正式上線 | 全員 |
    """)

    st.divider()
    st.subheader("💬 JD 的感想與回饋")
    st.text_area("六堂課下來，你最大的收穫是什麼？還有什麼想繼續學的？",
                 key="final_feedback", height=120)

    st.markdown("")
    st.success("""
    🎉 **恭喜完成六堂課程！**

    你已經從「什麼是 Vibe Coding」走到「用 AI 串接真實硬體」。
    記住開發哲學：**穩定、小規模、快速產出可驗收的成果。**

    有任何問題隨時找 Jeff，Claude Code 也隨時待命！
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
    st.success("""
    💡 **持續使用 AI 的秘訣：**
    每次遇到問題，先用「背景 + 目標 + 風格」描述給 AI，讓它幫你分析和寫程式。
    你負責決策，AI 負責執行——這就是 Vibe Coding 的精髓。
    """)
