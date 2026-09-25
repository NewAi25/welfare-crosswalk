---
name: audit
description: Run the pre push audit for the welfare crosswalk repository. Mechanical checks first, then the research-auditor agent verifies every claim and every data row in the unpushed changes against the corpus, the live web and the rules in standard/definitions.md. Pushing is allowed only on AUDIT PASS, and the result is logged in notes/audit_log.md.
---

# Pre push audit

Nothing in this repository is pushed until it has passed this audit. A crosswalk that ships one wrong reference number loses the trust every other cell depends on.

## Procedure

1. From the repository root, run the mechanical gates and stop if any fails:

   ```
   python scripts/validate_csv.py
   python scripts/check_corpus.py --local
   python scripts/stats.py
   ```

   If corpus files were added or replaced in this batch, also run the full network check, `python scripts/check_corpus.py`, and record any new manifest rows first.

2. Collect the change set: `git diff origin/master --stat` and `git diff origin/master`. For data files, list the row ids that changed so the auditor checks each one.

3. Launch the `research-auditor` agent with the diff or the row list and wait for it. Do not audit in the main session; the point is a second reader with no memory of writing the rows.

4. Read the report. If the first line is `AUDIT: FAIL`, fix every WRONG, UNSUPPORTED and rule breach in the files, log any rule change in `notes/decisions.md` and `standard/definitions.md`, commit, and go back to step 1. Do not argue with the auditor in the log; fix or remove the claim.

5. On `AUDIT: PASS`, append an entry to `notes/audit_log.md` with the date, the commit hash audited, the number of claims or rows checked, the counts of wrong, unsupported and imprecise, and a one line summary. Commit that entry with the message `Audit: PASS for <short hash>`.

6. Push. `gh auth switch --user NewAi25`, push, `gh auth switch --user manisha-oz`.

7. Manisha's spot check of ten rows against the rendered PDF pages, after the push and before the next batch starts. Findings are corrected with a decisions entry and re-audited.

## What the auditor must be given

The diff or row list, and nothing else. Do not pass it a summary of what the changes say; it would audit the summary rather than the files.

## Scope

Everything under `data/`, `standard/`, `notes/`, `writeup/`, `docs/`, `results/`, `corpus/README.md` and `corpus/manifest.csv`. Changes only to `scripts/` or `.claude/` still need the mechanical gates but not the agent, unless the change alters how a value is computed, in which case the agent checks that the computation still matches `standard/definitions.md`.
