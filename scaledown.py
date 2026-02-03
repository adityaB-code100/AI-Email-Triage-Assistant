import os
import requests
from dotenv import load_dotenv

load_dotenv()

SCALEDOWN_API_KEY = os.getenv("SCALEDOWN_API_KEY")

if not SCALEDOWN_API_KEY:
    raise ValueError("❌ SCALEDOWN_API_KEY not found in .env")

SCALEDOWN_URL = "https://api.scaledown.xyz/compress/raw/"

def compress_with_scaledown(context: str, prompt: str) -> str:
    """
    Compress context + prompt using ScaleDown official API
    """
    payload = {
        "context": context,
        "prompt": prompt,
        "compression_rate": "auto"
    }

    headers = {
        "x-api-key": SCALEDOWN_API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(
        SCALEDOWN_URL,
        headers=headers,
        json=payload,
        timeout=30
    )

    if response.status_code != 200:
        print("⚠️ ScaleDown compression failed, using original context")
        return context + "\n" + prompt

    data = response.json()

    # ScaleDown usually returns optimized_prompt or compressed_prompt
    return data.get("optimized_prompt") or data.get("compressed_prompt")
