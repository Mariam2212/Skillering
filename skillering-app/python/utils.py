"""
utils.py
--------
Utility module for external API setup in the Focus Zone project.

This file:
- Loads environment variables from a `.env` file using `python-dotenv`.
- Configures the Gemini AI API key for use in other modules.
- Provides a single function:
    1. `setup_api()` → Initializes the API key for `google.generativeai`.
- Ensures that all AI-related modules (focus plan, skill suggestions, etc.) can use the Gemini API securely without hardcoding keys.
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai

def setup_api():
    load_dotenv()
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
