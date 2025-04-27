# agents/app_builder_orchestrator_agent.py

from dotenv import load_dotenv
import os
from agents import Agent 
from openai_sdk_app_builder_agent.agents.clarifier_agent import clarifier_agent
from openai_sdk_app_builder_agent.context import AppBuilderContext

# Load environment variables
load_dotenv()

# Read MAX_WORDS env variable, fallback to 100 if not set
MAX_WORDS = int(os.getenv("MAX_WORDS", 100))

# Root Agent that orchestrates the flow
orchestrator_agent = Agent[AppBuilderContext](
    name="App Builder Orchestrator Agent",
    instructions=(
        f"You help users build apps. If the idea is too vague, hand it off to the Clarifier Agent for more details. "
        f"Limit your response to approximately {MAX_WORDS} words."
    ),
    model="gpt-4o-mini",
    handoffs=[clarifier_agent],  # Handoff to Clarifier Agent if needed
)
