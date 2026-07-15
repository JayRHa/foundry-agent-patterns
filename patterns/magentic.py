"""Magentic pattern: a manager agent plans, delegates and tracks progress.

Based on the Magentic-One research. The manager keeps a task ledger, selects
the next agent, detects stalls and replans. Most powerful pattern, least
predictable cost - ALWAYS set max_round_count and max_stall_count.

Usage: python patterns/magentic.py "Compare update ring strategies for a 5000 device tenant."
"""
import asyncio
import sys

from agent_framework.orchestrations import MagenticBuilder

from shared import get_client, make_agent, print_event


async def main(task: str) -> None:
    client = get_client()

    researcher = make_agent(client, "researcher",
        "You research facts and options for the given sub-task and report findings as bullets.")
    analyst = make_agent(client, "analyst",
        "You analyze findings, compare options and give a reasoned recommendation.")
    manager = make_agent(client, "manager",
        "You are the orchestration manager. Plan, delegate, track progress, synthesize.")

    workflow = MagenticBuilder(
        participants=[researcher, analyst],
        manager_agent=manager,
        intermediate_output_from=[researcher, analyst],
        max_round_count=10,   # hard ceiling on manager rounds
        max_stall_count=3,    # replan after 3 rounds without progress
        max_reset_count=2,
    ).build()

    async for event in workflow.run(task, stream=True):
        print_event(event)


if __name__ == "__main__":
    task = sys.argv[1] if len(sys.argv) > 1 else "Design a pilot plan for AI agents in IT support."
    asyncio.run(main(task))
