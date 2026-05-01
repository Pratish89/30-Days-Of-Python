"""Optional OpenAI-powered summary generator."""

from __future__ import annotations

import os

from dotenv import load_dotenv
from openai import OpenAI

from stock_agent.ai.prompts import build_summary_prompt
from stock_agent.models import StockAnalysis


def generate_ai_summary(analysis: StockAnalysis, model: str = "gpt-4o-mini") -> str:
    """Generate an AI summary if OPENAI_API_KEY is set."""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set. Add it to your .env file.")

    client = OpenAI(api_key=api_key)
    prompt = build_summary_prompt(analysis)
    response = client.responses.create(
        model=model,
        input=prompt,
    )
    return response.output_text.strip()
