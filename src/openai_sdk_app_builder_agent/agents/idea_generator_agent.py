# agents/idea_generator_agent.py

from agents import Agent
from openai_sdk_app_builder_agent.context import AppBuilderContext

idea_generator_agent = Agent[AppBuilderContext](
    name="Idea Generator Agent",
    instructions=(
        "You are a product strategist. "
        "Given a clarified app idea (user inputs + clarifications), generate a refined, polished App Concept. "
        "Summarize it cleanly: target audience, purpose, 3-5 key features. "
        "Keep output concise (under 200 words)."
    ),
    model="gpt-4o-mini",
)
