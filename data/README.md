# Data dictionary

Four CSV files with fixed headers, checked by `scripts/validate_csv.py`. The rules that fill each column are in `standard/definitions.md`. An empty cell means something specific, given per file.

## indicators.csv

Copied from plf-audit (see `docs/decisions_from_plf_audit.md` for how it was built) plus one column.

| Column | Values | Meaning |
|---|---|---|
| indicator_id | I001 onwards | Identifier used by the other files |
| efsa_consequence, efsa_abm | text | The EFSA 2023 welfare consequence and animal based measure |
| wq_principle, wq_criterion, wq_measure | text | The Welfare Quality principle, criterion and measure |
| maroto_molina_technology, maroto_molina_feasible | text; yes, partial, no, not_covered | What Maroto Molina 2020 identify for the measure |
| notes | text | Source table, join basis, open questions |
| tier | joined, efsa_only, wq_only | Filled by scripts/stats.py: which sources list the indicator |

Empty means: EFSA columns empty on a Welfare Quality only row, and the reverse; wq_measure alone empty for thermal comfort, where Welfare Quality defines no measure.

## products.csv

Copied from plf-audit with three notes cells edited to remove the predecessor's plans (see decisions.md, 25 September). The 20 products plus the AI4Animals comparator; 17 carry Stygar validation levels, the 3 ICAR systems and the comparator are not in Stygar's appendix.

| Column | Values | Meaning |
|---|---|---|
| product_id | P001 onwards | Identifier used in sensor_coverage.csv product_ids |
| vendor, product | text | Company as it trades today, product as the vendor names it |
| sensor_type | collar_accelerometer, ear_tag, bolus, camera, milking_system, other | Main sensing hardware; other covers leg tags, the load cell plate and milk analysers |
| measures_claimed | text | The stated aim, copied from the Stygar appendix for Stygar rows |
| species, country | text | |
| stygar_listed | yes, no | In the Stygar appendix of 129 |
| stygar_validation | none, external_self, external_independent, not_listed | Stygar's finding: none means listed with no external study; external_self means every cited study had a developer or company author; external_independent means at least one had none; not_listed means not in the appendix |
| icar_validated | yes, no | On the ICAR validated sensor systems list |
| source | stygar, icar, market_scan, course | How the product entered the predecessor's list; market_scan is kept in the enum for the copied file, no market scan happens here |
| marketing_url, manual_url, devdocs_url, patent_urls | URLs | marketing_url is the Stygar 2021 link, not re-verified; the other three are empty and stay empty in this scope |
| comparator | yes, no | yes only for AI4Animals |
| notes | text | Provenance and the reference numbers behind the validation value |

## sensor_coverage.csv

One row per indicator, column 2 of the crosswalk.

| Column | Values | Meaning |
|---|---|---|
| indicator_id | an id in indicators.csv | |
| ai_grade | validated_commercial, commercial_unvalidated, research_only, none, unsure | Sensor coverage, definitions factor 1 |
| product_ids | ids from products.csv, space separated | The products behind the grade; required for the two commercial grades |
| stygar_trait | text | The Stygar Table 2 trait or appendix aim wording that matched |
| stygar_refs | reference numbers, space separated | The validation studies from Stygar Table 1; required for validated_commercial |
| maroto_feasible | yes, partial, no, not_covered | Copied from indicators.csv for the row |
| hardware_class | routine_data, farm_fixed, animal_mounted, sample_or_procedure, none, unsure | Definitions factor 2 |
| market_breadth | whole number | Filled by scripts/market_breadth.py from the keywords |
| market_keywords | keywords separated by ; | The keywords matched against the appendix AIM column |
| evidence_note | text | Where each value was read: file, page, table, row |
| notes | text | Alternatives, candidates for unsure rows |

Empty means: market_breadth empty until market_breadth.py has run; product_ids and stygar_refs empty only on grades that do not require them.

## crosswalk.csv

One row per indicator per scheme, column 3. An indicator no scheme requires still gets four rows by rule; the validator does not enforce grid completeness, so stats.py prints the row count and the extraction session checks it is 57 times 4.

| Column | Values | Meaning |
|---|---|---|
| indicator_id | an id in indicators.csv | |
| scheme | RSPCA_Assured, FARM_v5, GAP_dairy, Certified_Humane | |
| requirement_text | verbatim | The requirement that names the indicator; empty when the scheme does not require it |
| section_ref, page | text | Where in the scheme document; required when requirement_text is filled |
| numeric_threshold | text | Any number the requirement sets, exactly as written |
| audit_method | visual_inspection, records_review, sensor_accepted, unspecified | How the scheme checks it; filled only with a requirement |
| industry_naming | named_with_threshold, named, related_resource, not_named | FARM_v5 rows only, definitions factor 4 |
| notes | text | Related resource requirements, justification document reasoning, alternatives |

Empty means: requirement_text empty means the scheme does not require the indicator, and audit_method is then empty too; industry_naming is empty on every non FARM row.

## results/

Written by `scripts/stats.py`, never edited by hand. `adoption_table.csv` has every indicator with the five factors, their 0 to 3 points, the heuristic sum and the rank. `instrumented_not_required.csv` and `required_manual_only.csv` are the two item #13 views.
