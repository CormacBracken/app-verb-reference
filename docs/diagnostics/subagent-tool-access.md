# Subagent tool access investigation

Investigated 17 November 2026. Beads: **Investigate missing tool access in spawned subagents** (`app-gqe`).

## Finding

In this conversation, full-history subagents consistently reported no callable tools. Fresh-context subagents successfully invoked shell and web tools. Using `fork_turns: "none"` is a verified workaround. No configuration was changed.

This narrows the symptom to the history-inheritance path. It does not establish whether the defect is missing tool-schema provisioning or an agent failure to recognize the available schemas. Failed probes produced self-reports, not a server-side manifest or rejected tool call; the parent cannot directly inspect the child model request.

## Reproduction and evidence

The original research dispatch used the default full-history fork and returned immediately claiming no tools, without any tool results. Diagnosis used tiny probes rather than retrying the research task.

| Probe | History | Result |
| --- | --- | --- |
| `tool_access_probe` | Explicit `none` | `functions.exec` printed `subagent-probe-ok`; nested `exec_command` ran `pwd`, exit 0. |
| `inherited_tool_probe` | Default `all` | Reported no callable namespaces; no shell or code tool invocation. |
| `inherited_probe_repeat` | Explicit `all` | Reported absent tool definitions again; no tool invocation. |
| Follow-up to `tool_access_probe` | Retained fresh context | Printed `fresh-repeat-ok`; `pwd` exited 0; `ALL_TOOLS` included `exec_command` and `web__run`. |
| `fresh_tool_probe_second` | Explicit `none` | Shell `pwd` exited 0 and web tool opened the official multi-agent documentation. |

All successful `pwd` calls returned `/home/cormac/Projects/verb-reference`. No probe changed files or launched descendants. No model overrides were used. The compared initial probes differed in history mode and marker text, and asked the same capability question. Fresh probes also succeeded after being told about the inherited probes' failure, so merely mentioning the failure did not reproduce it.

Minimal reproduction at the collaboration tool boundary:

```json
{
  "task_name": "probe_all",
  "fork_turns": "all",
  "message": "Diagnostic only: call functions.exec with text(await tools.exec_command({cmd:'pwd',max_output_tokens:100})); Report actual results or absent callable definitions. Do not edit files or spawn agents."
}
```

Replay with a new task name and change only `fork_turns` to `none`. This session's observed result is failure for `all`, success for `none`. The invocation is a `collaboration.spawn_agent` tool call, not a shell command; the app repository has no seam for invoking this session's collaboration runtime from a test script.

## Hypotheses and limits

Ranked before repeat probes:

1. Tool definitions are lost along the full-history inheritance path. Repeated differential results support this, but the underlying request is inaccessible.
2. Inherited conversation content causes tool-recognition failure. Not eliminated: fresh context removes both history and any defect in its serialization. Fresh probes mentioning the failure still worked.
3. Intermittent provisioning unrelated to history. Less consistent with the repeated results, but this small sample cannot rule it out completely.

The accessible repository `.codex/config.toml` contains only `[features] hooks = true`; no agent-specific configuration was found there. Selected global feature/agent/sandbox/approval fields yielded no configured values. The discoverable CLI reports `codex-cli 0.162.0-alpha.17.2`, bundled with the VS Code extension. That identifies a local executable, not proof that it owns this chat's subagent provisioning. No credentials or complete private configuration were printed.

[OpenAI's Responses multi-agent documentation](https://developers.openai.com/api/docs/guides/responses-multi-agent) states that agents share the configured tools. It is more relevant to the exposed collaboration tools than the different Agents API documentation cited in the initial discussion. Neither source establishes the cause of this particular failure.

## Workaround and next diagnostic boundary

Create fresh-context subagents and supply explicit task requirements, skill paths, repository path, constraints and required return format. Have each perform a tiny real tool call before assigning substantial work. Fresh contexts do not receive the conversation history, so essential context must be passed explicitly.

The native tool request/response payload or a runtime-side trace comparing the `all` and `none` child manifests is needed to distinguish provisioning from model interpretation. This is outside the controls exposed in this chat. No speculative config toggle, permissions widening, CLI upgrade, or restart was applied. The underlying bug remains open; investigation is complete to the accessible boundary.
