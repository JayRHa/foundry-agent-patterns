"""Group chat pattern: a moderated discussion between agents.

An orchestrator picks who speaks next (round-robin here; a custom
selection_func or an LLM orchestrator_agent also work). Every response is
broadcast to all participants to keep context in sync - token usage grows
with each turn, so keep the group small.

Usage: python patterns/group_chat.py "Should we block personal devices from enrollment?"
"""
import asyncio
import sys

from agent_framework.orchestrations import GroupChatBuilder

from shared import get_client, make_agent, print_event

MAX_TURNS = 6


async def main(task: str) -> None:
    client = get_client()

    advocate = make_agent(client, "advocate",
        "You argue in favor of the proposal. One short, concrete argument per turn.")
    critic = make_agent(client, "critic",
        "You argue against the proposal. One short, concrete counter-argument per turn.")
    moderator = make_agent(client, "moderator",
        "You summarize the discussion so far and, on your final turn, give a clear recommendation.")

    workflow = GroupChatBuilder(
        participants=[advocate, critic, moderator],
        termination_condition=lambda conversation: len(conversation) >= MAX_TURNS,
    ).build()

    async for event in workflow.run(task, stream=True):
        print_event(event)


if __name__ == "__main__":
    task = sys.argv[1] if len(sys.argv) > 1 else "Should we allow AI agents to auto-remediate device issues?"
    asyncio.run(main(task))
