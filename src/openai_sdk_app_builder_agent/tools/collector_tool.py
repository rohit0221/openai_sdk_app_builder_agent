# src/openai_sdk_app_builder_agent/tools/collector_tool.py

from agents import function_tool, RunContextWrapper
from openai_sdk_app_builder_agent.context import AppBuilderContext

@function_tool
async def collect_user_answers(wrapper: RunContextWrapper[AppBuilderContext], user_answers: str) -> str:
    """
    Collect user's answers to clarifying questions and store them into context.
    """
    wrapper.context.facts["clarification_answers"] = user_answers
    return "Thanks! Your clarifications have been saved. We'll move forward based on this."
