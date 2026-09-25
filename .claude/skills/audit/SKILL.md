---
name: audit
description: Run the pre push audit for the welfare crosswalk repository. Mechanical checks first, then the research-auditor agent verifies every factual claim in the unpushed changes against the corpus and the live web. Pushing is allowed only on AUDIT PASS, and the result is logged in notes/audit_log.md.
---

# Pre push audit

Nothing in this repository is pushed until it has passed this audit. The rule exists because a research repository that ships one wrong citation loses the trust that all its other numbers depend on.

## Procedure

1. From the repository root, run the mechanical gates and stop if either fails:

   ```
   python scripts/validate_csv.py
   python scripts/check_corpus.py --local
   ```

   If corpus files were added or replaced in this batch, run the full network check as well: `python scripts/check_corpus.py`. Every URL in `corpus/manifest.csv` must be live and serve the same bytes.

2. Collect the change set: `git diff origin/master --stat` and `git diff origin/master`. If the diff is large, list the changed files and let the auditor read them whole.

3. Launch the `research-auditor` agent with the diff or file list and wait for it. Do not run the audit yourself in the main session; the point is a second reader with no memory of writing the text.

4. Read the report. If the first line is `AUDIT: FAIL`, fix every WRONG and UNSUPPORTED claim in the files, log any decision this forces in `notes/decisions.md`, commit, and go back to step 1. Do not argue with the auditor in the log; fix or remove the claim.

5. On `AUDIT: PASS`, append an entry to `notes/audit_log.md` with the date, the commit hash audited (`git rev-parse HEAD`), the number of claims checked, the number IMPRECISE, and a one line summary. Commit that entry with the message `Audit: PASS for <short hash>`.

6. Only now push. Switch the GitHub account first: `gh auth switch --user NewAi25`, push, then `gh auth switch --user manisha-oz`.

## What the auditor must be given

The diff, plus a pointer to `CLAUDE.md` for the fixed citation list. Nothing else. In particular do not pass it your own summary of what the changes say, because then it audits the summary and not the files.

## Scope

Everything under `data/`, `standard/`, `notes/`, `writeup/`, `docs/`, `corpus/README.md` and `corpus/manifest.csv`. Changes only to `scripts/`, `logger/` or `.claude/` still need the mechanical gates but not the agent.
