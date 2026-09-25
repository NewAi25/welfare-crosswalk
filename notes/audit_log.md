# Audit log

One entry per push. An entry is written only after the research-auditor agent has returned AUDIT: PASS on the unpushed changes and both mechanical checks (`scripts/validate_csv.py`, `scripts/check_corpus.py --local`) exit 0. The pre push hook in `.githooks/pre-push` refuses a push whose commit has no PASS entry here. The predecessor repository's three audits are in its own log.

| Date | Commit audited | Claims checked | Wrong | Unsupported | Imprecise | Result | Summary |
|---|---|---|---|---|---|---|---|
