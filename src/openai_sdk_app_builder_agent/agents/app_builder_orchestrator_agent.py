# agents/app_builder_orchestrator_agent.py

from dotenv import load_dotenv
import os
from agents import Agent, function_tool, RunContextWrapper
from openai_sdk_app_builder_agent.agents.clarifier_agent import clarifier_agent
from openai_sdk_app_builder_agent.agents.idea_generator_agent import idea_generator_agent
from openai_sdk_app_builder_agent.context import AppBuilderContext

# Load environment variables
load_dotenv()

# Read MAX_WORDS env variable, fallback to 100 if not set
MAX_WORDS = int(os.getenv("MAX_WORDS", 100))

# --- Tool: Decide if idea is ready ---
@function_tool
async def decide_next_step(wrapper: RunContextWrapper[AppBuilderContext], user_response: str) -> str:
    """
    Decide whether the user response sufficiently clarifies the app idea.
    If it is still vague, respond 'clarify'.
    If it is clear enough, respond 'generate'.
    """
    idea_text = user_response.lower()
    if any(keyword in idea_text for keyword in ["health", "finance", "education", "kids", "seniors", "platform", "features"]):
        return "generate"
    return "clarify"

# --- Orchestrator Agent ---
orchestrator_agent = Agent[AppBuilderContext](
    name="App Builder Orchestrator Agent",
    instructions=(
        f"You orchestrate the app building flow.\n"
        "First, pass the user idea to the Clarifier Agent to ask smart clarifying questions.\n"
        "Then, after the user answers, decide if the idea is ready.\n"
        "If ready, handoff to the Idea Generator Agent to polish the app concept.\n"
        "Always use the `decide_next_step` tool after getting user input.\n"
        f"Keep responses short (approx {MAX_WORDS} words)."
    ),
    model="gpt-4o-mini",
    handoffs=[clarifier_agent, idea_generator_agent],
    tools=[decide_next_step],
)
