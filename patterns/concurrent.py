"""Concurrent pattern: three specialists look at the same input in parallel.

Use when you want independent perspectives (fan-out) and aggregate afterwards.
Cost note: tokens multiply by agent count.

Usage: python patterns/concurrent.py "We plan to enforce MFA for all admins next month."
"""
import asyncio
import sys

from agent_framework.orchestrations import ConcurrentBuilder

from shared import get_client, make_agent, print_event


async def main(task: str) -> None:
    client = get_client()

    security = make_agent(client, "security_review",
        "Assess the given change from a security perspective. List risks and mitigations.")
    licensing = make_agent(client, "licensing_review",
        "Assess the given change from a licensing and cost perspective.")
    user_impact = make_agent(client, "user_impact_review",
        "Assess the given change from an end-user impact perspective. Be concrete.")

    workflow = ConcurrentBuilder(participants=[security, licensing, user_impact]).build()

    async for event in workflow.run(task, stream=True):
        print_event(event)


if __name__ == "__main__":
    task = sys.argv[1] if len(sys.argv) > 1 else "We roll out Windows 11 26H2 to all devices in October."
    asyncio.run(main(task))
