# Decisions

Every coding or scoring decision not already covered by the coding frame or the rubric is entered here, dated, before it is applied. The frame or rubric is then updated so the next case is covered.

## 2026-09-16: repository created from spec

Repository created from `docs/PLF_Repo_Spec_For_ClaudeCode.md`. The pass threshold is set in `standard/rubric.md` and fixed before any scoring: all seven dimensions assessable, no dimension at 0, total at least 9 of 14, and a product is not assessable at three or more NA. The product cap is 15 to 20 dairy products plus AI4Animals as a comparator, following point 8 of Part 1 of the resources doc.

## 2026-09-16: scaffold choices the spec left open

**Corpus kept out of git entirely.** The spec's `.gitignore` excluded only PDF and HTML files, but several corpus files are pasted Markdown, including the Aeon essay, the EA Forum posts and legal text, and some of that is copyrighted. `.gitignore` now excludes everything in `corpus/` except `corpus/README.md`.

**The crosswalk is a full grid.** It holds one row per indicator per scheme for every indicator in `data/indicators.csv`. An empty requirement_text means that scheme does not require the indicator, and audit_method is then left empty. Without these rows the second query, indicators instrumented but required by no scheme, would have nowhere to be recorded.

**The three queries as `scripts/stats.py` computes them.** The shortlist is yes for every row of an indicator that at least one product measures directly and that FARM v5 requires. Instrumented but not required is yes for every row of an indicator that at least one product measures directly or by proxy and that no scheme requires. Required but manual only is decided per row: that scheme requires the indicator, audits it by visual inspection, and some product measuring it has external validation. I made it per row rather than per indicator because a certifier acts on its own scheme.

**NA versus 0 on validation evidence and disclosure.** Both criteria are about what has been published, so finding nothing published scores 0, not NA. NA on these two is kept for a product that cannot be identified precisely enough to search. On logging, lineage, access and tamper evidence, silence in the documentation is NA. This will shape the headline numbers and should be shown to Kevin with the rubric.

**Headline numbers exclude the comparator.** AI4Animals is scored but reported on its own line.

**Reliability agreement is computed.** `scripts/stats.py` fills agree_a_a and agree_a_b from the coder columns, so they are never typed by hand.

**Plan text in Markdown.** `docs/PLF_Audit_Standard_Plan.md` is a text extraction of the .docx, with a header note saying where the resources doc supersedes it (Berckmans 2022 citation, GlobalGAP, product cap).

**Open, to decide before scoring.** `legal_required_somewhere` depends on whether a product is sold in the EU, and `data/products.csv` has no column for that. It also needs a rule for when access_ownership is NA. Both need a decision here before week 4.

## 2026-09-16: corpus assembled

Twenty nine of thirty two expected source files downloaded into `corpus/`, each one checked to confirm it is the document it claims to be. Versions captured: RSPCA dairy standards April 2026 and the matching justification, Global Animal Partnership dairy v2.0 issued 1 June 2026, Certified Humane dairy Edition 23, ICAR Section 11 version October 2020, Welfare Quality dairy cows protocol version 3.2, February 2024. The Stygar supplementary product table is a spreadsheet, not a PDF, so it is saved as `stygar_2021_supplementary.xlsx`.

Missing and needing a browser: the FARM Animal Care Version 5 manual and the ISO/TS 34700 abstract, both blocked by bot protection, and van Erp-van der Kooij and Rutter 2020, which is paywalled with the repository copy restricted. None of these blocks were worked around. Provenance of each copy is recorded in `corpus/README.md`, because several came from repository mirrors rather than the publisher.

Recorded from the saved ICAR page in `notes/duplication_check.md`: three validated systems, all milk composition or yield, none welfare. That is the factual basis for the claim in CLAUDE.md, and it holds as of today.

## 2026-09-16: how indicators.csv was built

The indicator set is the union of two published sources, not a selection I made. It holds the 30 animal based measures EFSA 2023 lists in its ABM tables for the five welfare consequences (Tables 16, 17, 18, 27, 31, 32, 33, 42 and 46) and the 31 measures of the Welfare Quality dairy protocol, which Maroto Molina reproduce in their Table 1. That gives 57 rows. Welfare Quality defines no measure for thermal comfort, so that row carries the criterion with an empty measure.

An EFSA measure and a Welfare Quality measure are joined into one row only where EFSA itself cites Welfare Quality for the definition, or where the two names are identical. That rule produced 6 joins. Everything else stays unjoined, because deciding that two differently named measures are the same thing is a welfare science judgement and not mine to make. The joins I am least sure about are in kevin_questions.md.

The maroto_molina_feasible column codes technology readiness as the paper describes it, not whether the measure matters. Yes means they identify commercially available technology. Partial means research level technology, technology needing adaptation, or a substitute measure they propose. No means they say sensors cannot provide the measure. Not_covered means the paper does not discuss it, which is true of most EFSA only measures. Counts today: 9 yes, 25 partial, 2 no, 21 not_covered.

## 2026-09-16: how products.csv was built

Twenty products plus the AI4Animals comparator. Seventeen are dairy sensor products from the Stygar 2021 appendix, chosen to cover every sensor type in the schema and to favour vendors that publish documentation, with eight of the eighteen products Stygar flags as having validation studies included. Three are the systems on the ICAR validated list. That is at the top of the 15 to 20 range agreed in Part 1 of the resources doc.

The ICAR three are in the register even though they are milk analysers rather than welfare products. Whether an ICAR validated system makes a welfare claim at all is a finding, and if the answer is no, that is worth reporting.

Two schema frictions, both recorded rather than fixed. The sensor_type enum has no value for a leg mounted accelerometer or a load cell plate, so those four products are coded other with the real mounting in notes. And stygar_validation set to external means the product is flagged in the Stygar appendix as having validation studies; their appendix table 1 does not split self validation from independent validation product by product, although their headline figure is 18 externally validated of 129. Before any of this is used as evidence in the register, that distinction has to be resolved from their Table 2, and the coding frame rule on evidence_cited depends on it.

Marketing URLs are the ones Stygar published in 2021 and have not been re-verified. The market scan re-verifies each one and adds manual, developer documentation and patent links.

## 2026-09-16: Stygar validation split resolved, enum changed

The earlier entry said the Stygar appendix does not split self validation from independent validation per product. The appendix does not, but Table 1 of the paper does, with reference numbers in two columns, and the supplementary Table 2 codes every study. Stygar define both levels as external validation on herds not used for development; self validation means at least one author was involved in developing the technology or represents the company, independent validation means none was.

Because that distinction maps directly onto the coding frame (rule 5, vendor staff authorship makes evidence vendor_internal), the stygar_validation enum in products.csv and scripts/validate_csv.py is now none, external_self, external_independent, not_listed. The value internal is dropped because Stygar did not review internal validation, and the value external is split. This deviates from the repo spec schema and is recorded here for that reason.

Per product, from the reference numbers in Table 1 matched to Table 2 by DOI: AfiAct II refs 21 to 24 all independent; CowManager refs 21, 39, 40, 41 independent and ref 17 self; IceQube and IceTag refs 21, 26 and 28 independent, with Table 1 and the supplementary table disagreeing on whether ref 27 is independent or self; Smartbow ref 21 independent; DeLaval BCS ref 48 independent; eCow refs 50, 51 independent; Stepmetrix ref 54 independent; GEA CowScout ref 27 only, self validation, and Table 1 names the validated product CowScout Leg while the appendix row says CowScout S. P013 is renamed to cover both and coded external_self until the market scan confirms the current names. A product with any independent study is coded external_independent.

## 2026-09-16: audit gate and corpus manifest

Two mechanisms added after a wrong attribution slipped into a document shared with Kevin. First, corpus/manifest.csv records the exact URL and SHA256 of every corpus file, and scripts/check_corpus.py re-fetches each URL and confirms the bytes match, so every link in corpus/README.md is live and points at exactly the document that was read. Second, nothing is pushed without a passing audit: the research-auditor agent in .claude/agents/ checks every factual claim in the unpushed diff against the corpus and the live web, the /audit skill in .claude/skills/ runs the procedure, notes/audit_log.md records each result, and .githooks/pre-push refuses a push whose commit has no PASS entry.

## 2026-09-16: corrections from the first audit

The research-auditor agent returned FAIL on the first run over this batch. Every finding was checked against the source and corrected, and the earlier entries above were edited in place where they stated a wrong number, with this entry as the record of what changed.

The EU PLF blueprint has Guarino as first author: Guarino, Norton, Berckmans, Vranken and Berckmans 2017, Animal Frontiers 7(1) 12 to 17, confirmed from page 1 of the PDF and from Crossref. The planning documents in docs/ and the earlier fixed citation list in CLAUDE.md shortened it to Berckmans 2017. CLAUDE.md, rubric.md, corpus/README.md and duplication_check.md now carry the full author list. The docs/ files are left as shared with Kevin and are superseded on this point.

EFSA Table 46 lists eleven ABMs, not ten; blood calcium levels within days post calving (Hypocal-sc) was missed and is now I056. The EFSA count is 30, the file has 57 rows.

The bulk milk somatic cell count join (I007) broke the stated join rule, since EFSA cites no Welfare Quality definition and the names differ. It is split: I007 is the EFSA bulk tank measure, I057 the Welfare Quality individual cow measure, and the question of whether they are one indicator stays with Kevin. Joins are now 6.

Four rows (I008, I009, I010, I015) had EFSA wording or an extrapolation in the Maroto Molina technology column. They are now not_covered. Feasibility counts are 9 yes, 25 partial, 2 no, 21 not_covered.

The corpus count was wrong: 29 of 32 files are present, not 26 of 29; the three ICAR reports had been left out of the count. The Welfare Quality protocol file is version 3.2 of February 2024, not the 2009 edition. Welfare Quality reads somatic cell count from individual cow milk records, not herd records. EFSA and Welfare Quality use different body condition scales. For IceQube, Stygar Table 1 and their supplementary table disagree on ref 27. Cainthus was acquired by Ever.Ag in 2022; the current Lely robot is the Astronaut A5 Next; the AI4Animals talk is not in the corpus.

## 2026-09-16: second audit, documentation batch

The auditor failed the documentation batch on one wrong claim: Elliott and Werkheiser's framework has five audiences and five kinds of content, not four and four; the four is the number of parts of the framework. Corrected in the reading order. It also found that the auditor's own role file still shortened the blueprint citation to Berckmans 2017, which would have made it flag the correct citation as wrong in future; corrected. Six imprecise statements were tightened: Tuyttens threat 4 is about focusing on the measurable rather than the most meaningful indicators, not about meaningless indicators (also corrected in rubric.md); the Welfare Quality protocol names its fourth principle Appropriate behaviour while the CSV follows Maroto Molina's Table 1 naming; the sensor_type value other covers more than leg tags and load cells; Brolis and Panazoo countries come from vendor websites, not the ICAR reports; the claims validator enforces fewer columns than the coding frame requires; and page references for the Welfare Quality protocol, the ICAR checklist and the RSPCA health section were made exact.

Two changes follow from the audit rather than from a wrong claim. corpus/manifest.csv is now committed, because a reader of the repository could not otherwise walk the verification trail the README describes; the source documents themselves stay uncommitted. And the ISO/TS 34700 summary was retrieved by reading the public catalogue page and the Online Browsing Platform preview in a browser, since iso.org refuses scripted requests. Only the informative sections are public and only those were copied. One corpus file remains missing, van Erp and Rutter 2020. The FARM manual was fetched after the auditor found the PDF URL answers a scripted request that carries a browser user agent and referer; the product page alone returns 403. It is 164 pages, Version 5, July 2024 to June 2027, and hash verified. The ISO summary carries manifest status browser_only, which the checker handles by hashing the local file and skipping the network fetch.
