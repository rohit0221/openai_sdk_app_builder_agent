# main.py

import asyncio
from dotenv import load_dotenv
import os
from agents import Agent, Runner
from openai_sdk_app_builder_agent.agents.app_builder_orchestrator_agent import orchestrator_agent

# Load environment variables
load_dotenv()

# Read MAX_WORDS env variable, fallback to 100 if not set
MAX_WORDS = int(os.getenv("MAX_WORDS", 100))  # Fallback to 100 if not set

async def main():
    user_input = input(f"Enter your rough app idea (Output limited to {MAX_WORDS} words): ")  # User input
    result = await Runner.run(orchestrator_agent, user_input)  # Root agent runs
    print(f"\nAgent Response (limited to {MAX_WORDS} words):\n", result.final_output)  # Corrected f-string

if __name__ == "__main__":
    asyncio.run(main())
