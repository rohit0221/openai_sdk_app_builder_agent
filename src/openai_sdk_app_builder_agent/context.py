# src/openai_sdk_app_builder_agent/context.py

from dataclasses import dataclass, field
from typing import Dict, Any

@dataclass
class AppBuilderContext:
    """
    Memory container for the App Builder Agent.
    Stores user details, app idea, clarifications, answers, and facts discovered during the session.
    """
    user_id: str
    rough_idea: str
    facts: Dict[str, Any] = field(default_factory=dict)
