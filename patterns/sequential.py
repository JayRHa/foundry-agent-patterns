"""Sequential pattern: writer -> reviewer -> finalizer pipeline.

Each agent consumes the output of the previous one. Use when the task has a
natural, fixed order. Latency adds up per step, so keep the chain short.

Usage: python patterns/sequential.py "Write a summary of our rollout plan."
"""
import asyncio
import sys

from agent_framework.orchestrations import SequentialBuilder

from shared import get_client, make_agent, print_event


async def main(task: str) -> None:
    client = get_client()

    writer = make_agent(client, "writer",
        "You write a clear first draft for the given task. Plain language, short sentences.")
    reviewer = make_agent(client, "reviewer",
        "You review the draft you receive. Fix factual gaps, tighten the text, keep the voice.")
    finalizer = make_agent(client, "finalizer",
        "You produce the final version from the reviewed draft. Output only the final text.")

    workflow = SequentialBuilder(participants=[writer, reviewer, finalizer]).build()

    async for event in workflow.run(task, stream=True):
        print_event(event)


if __name__ == "__main__":
    task = sys.argv[1] if len(sys.argv) > 1 else "Write a short summary of what Microsoft Foundry is."
    asyncio.run(main(task))
