# src/openai_sdk_app_builder_agent/agents/clarification_collector_agent.py

from agents import Agent
from openai_sdk_app_builder_agent.context import AppBuilderContext
from openai_sdk_app_builder_agent.tools.collector_tool import collect_user_answers

clarification_collector_agent = Agent[AppBuilderContext](
    name="Clarification Collector Agent",
    instructions="You collect and save user responses to clarification questions. Update context facts.",
    tools=[collect_user_answers],
)
