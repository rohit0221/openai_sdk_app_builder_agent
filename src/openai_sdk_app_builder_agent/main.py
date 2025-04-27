# main.py

import asyncio
from dataclasses import dataclass
import uuid
from dotenv import load_dotenv
import os
from agents import Runner
from agents.run import RunContextWrapper
from openai_sdk_app_builder_agent.agents.app_builder_orchestrator_agent import orchestrator_agent

# Load environment variables
load_dotenv()

# Read MAX_WORDS env variable, fallback to 100 if not set
MAX_WORDS = int(os.getenv("MAX_WORDS", 100))

# Define context (in this case, user input) as a dataclass
@dataclass
class UserInputContext:
    rough_idea: str
    uid: int

async def main():
    # Get user input (rough app idea)
    user_input = input(f"Enter your rough app idea (Output limited to {MAX_WORDS} words): ")

    # Wrap the user input in a context object
    user_id = str(uuid.uuid4())
    user_input_context = UserInputContext(rough_idea=user_input,uid=user_id)

    # Create the RunContextWrapper with user input as context
    context_wrapper = RunContextWrapper([user_input_context])

    # Run the Root Agent with the context
    result = await Runner.run(
        starting_agent=orchestrator_agent,
        input=user_input,  # Pass user input as input
        context=context_wrapper  # Pass the context to keep the state
    )

    # Print the final agent response
    print(f"\nAgent Response (limited to {MAX_WORDS} words):\n", result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
