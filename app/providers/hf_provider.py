import os, requests
import re

HF_API_KEY = os.getenv("HF_API_KEY")
HF_MODEL = os.getenv("HF_MODEL", "distilbert-base-uncased-finetuned-sst-2-english")

def classify_with_hf(text: str) -> tuple[str, float]:
    """
    Simple rule-based fraud detection for demonstration.
    In a real application, you would use a proper fraud detection model.
    """
    # Allow demo mode without API key
    # if not HF_API_KEY:
    #     raise RuntimeError("HF_API_KEY not set")
    
    # Simple rule-based fraud detection
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
            fraud_score += 0.2
    
    # Check for multiple transactions or rapid succession
    if re.search(r'(\d+)\s*(transactions?|purchases?)', text_lower):
        fraud_score += 0.3
    
    # Normalize score to 0-1 range
    fraud_score = min(1.0, fraud_score)
    
    # Determine label
    if fraud_score > 0.5:
        label = "FRAUD"
    else:
        label = "LEGIT"
    
    return label, fraud_score
