<!-- jr-brand:start -->
<div align="center">
  <a href="https://jannikreinhard.com/">
    <img src="https://raw.githubusercontent.com/JayRHa/.github/main/assets/readme/learning.svg" alt="Jannik Reinhard — AI, Cloud and Endpoint Management" width="100%">
  </a>
  <h1>Microsoft Foundry Agent Patterns</h1>
  <p><strong>Runnable Microsoft Agent Framework orchestration patterns (sequential, concurrent, group chat, handoff, magentic) wired to Microsoft Foundry.</strong></p>
  <p>
  <a href="https://jannikreinhard.com/"><img src="https://img.shields.io/badge/Website-0A5FC0?style=flat-square&amp;logo=wordpress&amp;logoColor=white" alt="Website"></a>
  <a href="https://github.com/JayRHa"><img src="https://img.shields.io/badge/GitHub-081427?style=flat-square&amp;logo=github&amp;logoColor=white" alt="GitHub"></a>
  <a href="https://www.linkedin.com/in/jannik-r/"><img src="https://img.shields.io/badge/LinkedIn-0795FF?style=flat-square&amp;logo=linkedin&amp;logoColor=white" alt="LinkedIn"></a>
  <a href="https://x.com/jannik_reinhard"><img src="https://img.shields.io/badge/X-081427?style=flat-square&amp;logo=x&amp;logoColor=white" alt="X"></a>
  <a href="https://www.youtube.com/@ModernDevMgmt/featured"><img src="https://img.shields.io/badge/YouTube-0A5FC0?style=flat-square&amp;logo=youtube&amp;logoColor=white" alt="YouTube"></a>
</p>
  <p><sub>Book · Sample · Pattern · Python · Practical by design</sub></p>
</div>
<!-- jr-brand:end -->

## Overview

Runnable examples for the five Microsoft Agent Framework orchestration patterns,
wired to **Microsoft Foundry** — sequential, concurrent, group chat, handoff and
magentic. One file per pattern, no framework ceremony, ready to adapt.

> Microsoft retired connected agents (classic) and is retiring the Foundry portal
> workflow designer on December 1, 2026. The durable way to build multi-agent
> solutions is the [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/)
> — that is what these samples use.

## What Is in Here

| File | Pattern | Use it when |
|------|---------|-------------|
| `patterns/sequential.py` | Pipeline | The task has a fixed order (draft → review → finalize) |
| `patterns/concurrent.py` | Fan-out | You want independent perspectives in parallel |
| `patterns/group_chat.py` | Moderated discussion | Agents must react to each other |
| `patterns/handoff.py` | Full control transfer | Triage to a specialist that owns the task |
| `patterns/magentic.py` | Manager + specialists | Open-ended, complex problems |
| `patterns/shared.py` | — | Foundry client + agent factory used by all samples |

## Prerequisites

- Python 3.10+
- A Microsoft Foundry project with a deployed chat model (e.g. `gpt-5-mini`)
- Azure CLI login (`az login`) or any other `DefaultAzureCredential` source
- Your user needs the **Foundry User** role on the project

## Quickstart

```bash
git clone https://github.com/JayRHa/foundry-agent-patterns.git
cd foundry-agent-patterns
pip install -r requirements.txt

cp .env.example .env   # fill in your project endpoint + model deployment

python patterns/sequential.py "Write a short summary of our Intune rollout plan."
```

Every sample prints the intermediate agent outputs, so you can watch the
orchestration happen instead of only seeing the final answer.

## Pattern cheat sheet

- **Sequential** — latency adds up per step; keep chains short.
- **Concurrent** — tokens multiply by agent count; aggregate deliberately.
- **Group chat** — every response is broadcast to all participants; context
  grows fast, keep the group at 3–4 agents.
- **Handoff** — routing quality depends entirely on the one-sentence agent
  descriptions; write them like tool descriptions.
- **Magentic** — the manager replans on stalls. Always set `max_round_count`
  and `max_stall_count`, or the token bill will surprise you.

## Human in the loop

All patterns support pausing for approval. The samples keep it simple, but for
anything that changes production systems, mark the tool accordingly:

```python
@tool(approval_mode="always_require")
def create_ticket(...): ...
```

## Related

- Blog: [jannikreinhard.com](https://jannikreinhard.com) — deep dive on
  multi-agent orchestration in Microsoft Foundry
- [Agent Framework orchestration docs](https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/)

## Disclaimer

Community samples, not an official Microsoft project. The Agent Framework and
Foundry APIs move fast — pin your versions and test before production use.

## License

MIT — see [LICENSE](LICENSE).

<!-- jr-brand-footer:start -->

---

<div align="center">
  <p><sub>Built and maintained by <a href="https://jannikreinhard.com/">Jannik Reinhard</a> · Microsoft MVP for Security and AI Platform.</sub></p>
  <p><a href="https://www.buymeacoffee.com/jannikreinf">Support the open-source work</a></p>
  <p><strong>Stay healthy, Cheers Jannik</strong></p>
</div>

<!-- jr-brand-footer:end -->
