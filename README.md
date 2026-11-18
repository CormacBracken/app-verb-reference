# app-verb-reference

An offline Spanish verb reference for Android, currently in specification and toolchain verification. Production app implementation has not started.

Completed planning and verification artifacts:

- [Domain glossary](CONTEXT.md)
- [Interaction prototype](prototypes/verb-reference.html): open directly in a browser; illustrative, unverified fixtures, not the production corpus.
- [Toolchain research](research/toolchain.md)
- [Spanish inventory research](research/spanish-inventory.md)
- [Frequency-source comparison](research/frequency-source.md)
- [CORPES inspection](research/corpes-inspection.md) and [inspection script](research/inspect_corpes.py)
- [Toolchain reproduction instructions](toolchain-smoke/README.md) and [verification results](toolchain-smoke/VERIFICATION.md), with the disposable Expo harness, locked dependencies, Maestro flows, and text evidence.
- [Subagent tool-access diagnosis](docs/diagnostics/subagent-tool-access.md)

Beads is the canonical decision tracker: run `bd show app-vs7` for the wayfinder map. [The issue export](.beads/issues.jsonl) checkpoints issues, comments, and dependencies; it is a passive snapshot, not a full Dolt database backup or the remote synchronization mechanism.

The research and toolchain artifacts were consolidated from sibling worktrees and the local `toolchain-smoke` directory on 18 November 2026. Original artifacts remain in place. Historical reports and issue comments retain their original absolute paths and observations; use the relative links above for the committed copies.

Installed tools, caches, dependencies, generated native projects/builds, screenshots, and the raw CORPES download are not included. The smoke harness is source and evidence, not a ready-installed toolchain: its `env.sh` expects tooling installed alongside it. Follow its reproduction instructions and adjust local paths when needed. To rerun the corpus inspection, supply the original TSV matching the checksum documented in the report:

```bash
python research/inspect_corpes.py /path/to/diccionario_frecuencias_corpes_alfa.tsv
```
