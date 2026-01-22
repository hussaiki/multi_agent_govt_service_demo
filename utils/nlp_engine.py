import re

def detect_language(text: str) -> str:
    """
    Simple language detection for Malayalam/English.
    In a real system, this would use a more robust model or LLM.
    """
    # Malayalam unicode range: 0D00-0D7F
    malayalam_pattern = re.compile(r'[\u0D00-\u0D7F]+')
    if malayalam_pattern.search(text):
        return "malayalam"
    return "english"

def preprocess_text(text: str) -> str:
    """
    Basic text cleaning.
    """
    return text.strip()
