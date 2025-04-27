# src/openai_sdk_app_builder_agent/main.py

import asyncio
import uuid
from agents import Runner
from openai_sdk_app_builder_agent.agents.app_builder_orchestrator_agent import orchestrator_agent
from openai_sdk_app_builder_agent.context import AppBuilderContext
from agents.items import MessageOutputItem

async def main():
    # Step 1: Get rough idea from user
    rough_idea = input("Enter your rough app idea: ")
    user_id = f"user-{uuid.uuid4().hex[:8]}"

    # Step 2: Initialize session
    context = AppBuilderContext(user_id=user_id, rough_idea=rough_idea)
    input_items = []  # This will store conversation history

    while True:
        # Step 3: Run agent
        result = await Runner.run(
            starting_agent=orchestrator_agent,
            input=input_items if input_items else rough_idea,
            context=context
        )

        # Step 4: Append new items to input history
        input_items = result.to_input_list()

        # Step 5: Look at last output — decide if agent expects user input
        last_item = None
        for item in reversed(result.new_items):
            if isinstance(item, MessageOutputItem):
                last_item = item
                break

        if last_item is None:
            print("[Agent]: No message output from agent. Ending session.")
            break

        # Step 6: Show agent's output to user
        agent_message = last_item.raw_item.content
        print(f"\n[Agent]: {agent_message}\n")

        # Step 7: Ask user for next input
        user_response = input("[You]: ")
        input_items.append({"role": "user", "content": user_response})

asyncio.run(main())
