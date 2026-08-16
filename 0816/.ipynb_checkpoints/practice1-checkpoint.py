# 導入 Google 的 Gemini API 客戶端函式庫
from google import genai
# 導入 dotenv，用來讀取 .env 檔案中的環境變數（例如 API 金鑰）
from dotenv import load_dotenv

# 載入 .env 檔案中的環境變數
load_dotenv()

# 建立 Gemini API 客戶端（會自動從環境變數取得 API 金鑰）
client = genai.Client()

# 呼叫 Gemini API，建立一次對話互動
interaction = client.interactions.create(
    model="gemini-3.5-flash",  # 指定要使用的模型名稱
    input="天空為什麼是藍的"     # 傳送給模型的使用者提問
)

# 印出模型回覆的文字內容
print(interaction.output_text)