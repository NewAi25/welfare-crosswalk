---
name: audit
description: Run the pre push audit for the welfare crosswalk repository. Mechanical checks first, then the research-auditor agent verifies every claim and every table row in the unpushed changes against 1_sources, the live web and the rules in 2_research/rules.md. Pushing is allowed only on AUDIT PASS, and the result is logged in 2_research/audit_log.md.
---

# Pre push audit

Nothing in this repository is pushed until it has passed this audit. A crosswalk that ships one wrong study number loses the trust every other cell depends on.

## Procedure

1. Commit the batch first, staging files by name, so the audit and the push gate test exactly what will be pushed.

2. From the repository root, with `PYTHONIOENCODING=utf-8`, run the mechanical checks and stop if any fails:

   ```
   python 3_code/check_tables.py
   python 3_code/check_sources.py --local
   python 3_code/count_vendors.py
   python 3_code/build_output.py --check
   ```

   check_tables.py checks the four tables. check_sources.py --local checks every source file against its fingerprint in 1_sources/manifest.csv. count_vendors.py compares every stored vendors_naming_it with a fresh count and changes nothing. build_output.py --check confirms the Excel file in 4_output matches the tables; if it fails, run `python 3_code/build_output.py`, commit the rebuilt file and start again.

   If source files were added or replaced in this batch, record them first (`python 3_code/check_sources.py --record --only <file>`) and then run the full check with the network, `python 3_code/check_sources.py --only <file>`.

3. Collect the change set: `git diff origin/master --stat` and `git diff origin/master`. For tables, list the row ids that changed so the auditor checks each one.

4. Launch the `research-auditor` agent with the diff or the row list and wait for it. Do not audit in the main session; the point is a second reader with no memory of writing the rows.

5. Read the report. If the first line is `AUDIT: FAIL`, fix every WRONG, UNSUPPORTED, OVERSTATED and rule breach in the files. Log any rule change in `2_research/decision_log.md` and in `2_research/rules.md` with a new version and change log row. Rebuild the Excel file if a table changed, commit, and go back to step 2. Do not argue with the auditor in the log; fix or remove the claim.

6. On `AUDIT: PASS`, add a row to the table in `2_research/audit_log.md`: the date, the commit audited as a 7 character hash (`git rev-parse --short=7 HEAD`), the number of claims or rows checked, the counts of wrong, unsupported and imprecise, `PASS` in the Result column, and a one line summary. Commit only that file, with the message `Audit: PASS for <short hash>`. The push gate accepts a row with PASS in its Result column for the commit being pushed, or for its parent when the commit being pushed changes nothing but the audit log. It refuses to push any commit other than the one checked out.

7. Push: `gh auth switch --user NewAi25`, `git push`, `gh auth switch --user manisha-oz`. The push gate in 3_code/hooks/pre-push runs the checks again and refuses the push without the PASS row.

8. Manisha spot checks ten rows of the batch against the source pages, after the push and before the next batch starts. Each spot check is logged in decision_log.md with its date and the rows read; one that is not logged is never described as done. Anything she finds is corrected with a decision_log.md entry and audited again.

## What the auditor must be given

The diff or row list, and nothing else. Do not pass it a summary of what the changes say; it would audit the summary rather than the files.

## Scope

Every folder: 1_sources (manifest.csv, README.md, the kevin_*.md files), 2_research, 4_output, the top level README.md and CLAUDE.md, and .claude/. A change only to 3_code still needs the mechanical checks but not the agent, unless it alters how a value is computed or checked, in which case the agent checks that the code still matches 2_research/rules.md.
