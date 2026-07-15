"""Shared Foundry client and agent factory for all pattern samples."""
import os

from agent_framework.foundry import FoundryChatClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

load_dotenv()

PROJECT_ENDPOINT = os.environ["FOUNDRY_PROJECT_ENDPOINT"]
MODEL = os.environ.get("FOUNDRY_MODEL_DEPLOYMENT", "gpt-5-mini")


def get_client(model: str | None = None) -> FoundryChatClient:
    """One chat client per model deployment; agents are cheap views on top."""
    return FoundryChatClient(
        project_endpoint=PROJECT_ENDPOINT,
        model=model or MODEL,
        credential=DefaultAzureCredential(),
    )


def make_agent(client: FoundryChatClient, name: str, instructions: str):
    return client.as_agent(name=name, instructions=instructions)


def print_event(event) -> None:
    """Uniform, readable output for streamed workflow events."""
    kind = type(event).__name__
    text = getattr(event, "text", None) or getattr(event, "output", None)
    if text:
        print(f"\n--- {kind} ---\n{text}")
