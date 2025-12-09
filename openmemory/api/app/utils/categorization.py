import logging
from typing import List

from app.utils.prompts import MEMORY_CATEGORIZATION_PROMPT
from dotenv import load_dotenv
import os
import json
from google import genai
from google.genai import types
# from openai import OpenAI # Removed for Gemini exclusivity

from pydantic import BaseModel
from tenacity import retry, stop_after_attempt, wait_exponential

load_dotenv()


class MemoryCategories(BaseModel):
    categories: List[str]


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=15))
def get_categories_for_memory(memory: str) -> List[str]:
    provider = os.getenv("LLM_PROVIDER", "gemini")
    
    try:
        if provider == "gemini":
            client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))
            
            response = client.models.generate_content(
                model=os.getenv("LLM_MODEL", "gemini-3-pro-preview"),

                contents=memory,
                config=types.GenerateContentConfig(
                    system_instruction=MEMORY_CATEGORIZATION_PROMPT,
                    response_mime_type="application/json",
                    response_schema=MemoryCategories
                )
            )
            parsed = response.parsed
            if parsed:
                 return [cat.strip().lower() for cat in parsed.categories]
            return []
            
        # if provider == "openai":
        #    raise ValueError("OpenAI provider is not supported in this Gemini-exclusive version.")

    except Exception as e:
        logging.error(f"[ERROR] Failed to get categories: {e}")
        try:
            logging.debug(f"[DEBUG] Raw response: {completion.choices[0].message.content}")
        except Exception as debug_e:
            logging.debug(f"[DEBUG] Could not extract raw response: {debug_e}")
        raise
