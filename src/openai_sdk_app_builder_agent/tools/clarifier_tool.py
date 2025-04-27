# tools/clarifier_tool.py

from agents import function_tool
from openai import AsyncOpenAI
import os
from dotenv import load_dotenv

# Load .env variables (for OPENAI_API_KEY)
load_dotenv()

# Initialize OpenAI client
openai_client = AsyncOpenAI()

@function_tool
async def clarify_app_idea(rough_idea: str) -> str:
    """
    Given a rough app idea, generate 2–3 smart clarifying questions using LLM.
    """
    prompt = (
        "You are a professional product designer.\n"
        "Given the following rough app idea, generate 2–3 clarifying questions to better understand it.\n"
        "Be concise, number your questions, and keep total under 75 words.\n\n"
        f"App Idea: {rough_idea}\n\n"
        "Questions:"
    )
    
    response = await openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You generate clarifying questions for app ideas."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
    )

    clarifying_questions = response.choices[0].message.content.strip()
    return clarifying_questions
