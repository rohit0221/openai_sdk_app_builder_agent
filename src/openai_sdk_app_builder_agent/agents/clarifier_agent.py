# agents/clarifier_agent.py

from dotenv import load_dotenv
import os
from agents import Agent
from openai_sdk_app_builder_agent.tools.clarifier_tool import clarify_app_idea  # Import the Clarifier Tool

# Load environment variables
load_dotenv()

# Read MAX_WORDS env variable, fallback to 100 if not set
MAX_WORDS = int(os.getenv("MAX_WORDS"))

# Define the Clarifier Sub-Agent
clarifier_agent = Agent(
    name="Clarifier Agent",
    instructions=(
        f"Your job is to ask clarifying questions to better understand rough app ideas provided by users. "
        f"Use the 'clarify_app_idea' tool to generate smart, concise questions, limited to {MAX_WORDS} words."
    ),
    tools=[clarify_app_idea],
    model="gpt-4o-mini",
)
