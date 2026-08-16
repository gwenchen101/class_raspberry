from pathlib import Path

from google import genai
from dotenv import load_dotenv


load_dotenv(Path(__file__).with_name(".env"))

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="裝設太陽光電板對環境的影響為何"
)

print(interaction.output_text)
