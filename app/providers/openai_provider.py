import os, json, requests, re

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

def classify_with_openai(text: str) -> tuple[str, float]:
    # Demo mode - simulate OpenAI response
    if not OPENAI_API_KEY:
        # Simple rule-based demo for OpenAI
        fraud_indicators = [
            r'\$(\d{4,})',  # Large amounts (>$1000)
            r'(midnight|3am|4am|5am)',  # Unusual hours
            r'(urgent|emergency|asap)',  # Urgency keywords
            r'(wire|transfer|bitcoin|crypto)',  # High-risk payment methods
            r'(overseas|international|foreign)',  # International transactions
        ]
        
        text_lower = text.lower()
        fraud_score = 0.0
        
        for pattern in fraud_indicators:
            if re.search(pattern, text_lower):
                fraud_score += 0.15  # Lower weight for demo
        
        # Check for multiple transactions
        if re.search(r'(\d+)\s*(transactions?|purchases?)', text_lower):
            fraud_score += 0.2
        
        fraud_score = min(1.0, fraud_score)
        label = "FRAUD" if fraud_score > 0.4 else "LEGIT"
        
        return label, fraud_score
    url = "https://api.openai.com/v1/chat/completions"
    headers = {"Authorization": f"Bearer {OPENAI_API_KEY}"}
    payload = {
        "model": OPENAI_MODEL,
        "response_format": {"type": "json_object"},
        "messages": [
            {
                "role": "system",
                "content": (
                    "Classify a financial transaction as FRAUD or LEGIT with a risk score from 0 to 1. "
                    "Return strictly JSON: {\\\"label\\\": \\\"FRAUD|LEGIT\\\", \\\"score\\\": <float>}"
                ),
            },
            {"role": "user", "content": text},
        ],
        "temperature": 0.0
    }
    resp = requests.post(url, headers=headers, json=payload, timeout=20)
    resp.raise_for_status()
    data = resp.json()
    content = data["choices"][0]["message"]["content"]
    obj = json.loads(content)
    label = str(obj.get("label", "LEGIT")).upper()
    score = float(obj.get("score", 0.0))
    if label not in {"FRAUD", "LEGIT"}:
        label = "LEGIT"
    score = max(0.0, min(1.0, score))
    return label, score
