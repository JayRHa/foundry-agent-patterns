"""Handoff pattern: a triage agent passes FULL control to a specialist.

Unlike the old agent-as-tools model (connected agents), a handoff transfers
ownership of the task - the specialist answers the user directly. Routing
quality depends entirely on the one-sentence descriptions, so write them
like tool descriptions.

Usage: python patterns/handoff.py "My laptop is not compliant since yesterday."
"""
import asyncio
import sys

from agent_framework.orchestrations import HandoffBuilder

from shared import get_client, make_agent, print_event


async def main(task: str) -> None:
    client = get_client()

    triage = make_agent(client, "triage",
        "You are first-level support. Decide which specialist should own the request "
        "and hand off. Do not answer the request yourself.")
    device_agent = make_agent(client, "device_specialist",
        "You own device management questions: compliance, enrollment, policies. "
        "Solve the request end to end.")
    identity_agent = make_agent(client, "identity_specialist",
        "You own identity questions: sign-in, MFA, Conditional Access. "
        "Solve the request end to end.")

    workflow = (
        HandoffBuilder(participants=[triage, device_agent, identity_agent])
        .with_start_agent(triage)
        .add_handoff(triage, [device_agent, identity_agent])
        .build()
    )

    async for event in workflow.run(task, stream=True):
        print_event(event)


if __name__ == "__main__":
    task = sys.argv[1] if len(sys.argv) > 1 else "A user cannot pass MFA on a new phone."
    asyncio.run(main(task))
