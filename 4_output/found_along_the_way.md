# Found along the way

While building the crosswalk, the source documents were read line by line, and some of them turned out to disagree with themselves, with each other, or with the web as it is today. This page lists those things in plain words. None of them is a welfare finding. They are findings about the sources: where a reader of the same documents could trip, and what this project did about each one.

Each entry says where the problem is, what does not match, what the project did, and whether it changes any answer in the Excel file. Page numbers are PDF page numbers, the number your PDF viewer shows, with the printed number in brackets where they differ. Short quotes copy the source exactly, spelling slips included. Every entry was checked again against its file in [1_sources](../1_sources) on 15 October 2026.

## 1. The product links in the Stygar spreadsheet

**Where.** The spreadsheet the Stygar team published with their 2021 review ([1_sources/stygar_2021_supplementary.xlsx](../1_sources/stygar_2021_supplementary.xlsx), sheet "Appendix table 1", column INTERNET LINK) gives a web link for each of its 129 products. This project did not write these links; it copied them, and products.csv uses the same links for its 17 Stygar products.

**What we found.** On 15 October 2026 every link was opened again. 20 still open a page that names the product, and 20 more do after redirecting to a new address. 32 open the wrong page: a dealer's page, a page that no longer names the product, a parked domain or an unrelated site. 57 are broken. For example, the WellCow bolus link (row 2) now redirects to an error page on the design firm's site.

Some old addresses now belong to someone else, so the 2021 link leads to a site that has nothing to do with the product. On the day checked, the old Agersens address (row 7) went to an unrelated restaurant site, the old EIO Diagnostics address (row 44) to an unrelated pizza site, and the old Workswell camera address (rows 127 and 128) to an unrelated spam site. The eCow address (row 43) went to a domain resale service, and the Smartbow address (row 117) was a domain for sale. Take care when opening the 2021 links in these rows.

**Where the maker's page is today.** For each product, the maker's current page was searched for, and accepted only on the maker's own site, never a reseller, a news story or an archive copy. 61 products have a current page that names them. 18 have only a related page: one that names the product family or a likely successor but not this exact model, such as a page for Lely Calm that does not name the Calm Compact + (row 87). For 21 the maker's site is live but the product is not on it, for 14 only the maker's home page was found, and for 15 no maker site was found at all.

**Links that point somewhere other than the maker.** Several 2021 links did not point to the maker even then. Six point to a dealer, a marketplace, a third party file or a third party profile: StepMatrix (row 18) to a BouMatic dealer, the BouMatic calf feeder (row 19) to a dealer, the DeLaval Activity Meter System (row 30) to a dealer, CowScout S (row 66) to a GEA brochure hosted on another company's site, the SAC FDS3 feeding station (row 115) to a trade marketplace page, and VitalHerd (row 125) to a company profile on an investment site. The Heatime Pro+ link (row 12) points to the page of a sister product, the Heatime HR system.

**Rows that look mixed up.** Row 116 is named "RDS Futureline MAX", which is the name SAC gives its milking robot in row 114, yet it is listed under the company Sensolus as a GPS collar, "A location tracker on animals". Row 80, "Calf Star", is listed under Holm & Laue; its link opens the shop of Calf Star, which sells Holm & Laue's CalfExpert feeders, and its page describes "The Calf Star Double Jug".

**What we did.** The new table [2_research/product_links.csv](../2_research/product_links.csv) records, for every product, what the 2021 link opens today, the maker's current page where one was found, and the words on that page that name the product. The Product list sheet of the Excel file shows the same next to the 2021 link. The rule is [rules.md](../2_research/rules.md), rule 4.10.

**Does it change an answer?** No. The grades and counts read the products' stated aims in the spreadsheet, not their web pages. The links matter to a reader who wants to see a product, and they show how fast this market moves: in five years, most of the 2021 links stopped leading to the product.

## 2. Stygar and colleagues 2021, the paper and its spreadsheet

**One study coded two ways.** In Table 1 (PDF 6), study 27 (Nielsen and colleagues) sits in the independent validation column on the IceQube and IceTag row, and in the self validation column on the CowScout Leg row. The spreadsheet ("Appendix table 2", row 28) codes it "External self-validation". The project noted this on products P016 and P013 and rests P016 on studies 21, 26 and 28, so no answer changes.

**Product names spelt differently.** The paper writes "Stepmetrix (54)" (Table 2, PDF 7) and the spreadsheet "StepMatrix" (row 18), whose own link ends in stepmetrix. Other names also differ between the paper and the spreadsheet: eCow Farmer bolus and eBolus (row 43), CowScout Leg and CowScout S (row 66), Track A Cow and Track a))) Cow (row 46), HerdInsight and HerdInsights (row 76), one Table 1 row for IceQube and IceTag against two spreadsheet rows (48 and 49), and three AfiAct names against one spreadsheet row, AfiAct II (row 3). A word search for one spelling misses the other. Each match is stated in products.csv or in the sensor row that uses it. No grade changes.

**A tested product with no row under its name.** Table 2 names the "Lely-on-line California mastitis test (43)", but no spreadsheet row has that name. It was matched to Lely MQC-C (row 91), the only Lely row with a validation flag (decision log, 3 October 2026). This match sets the device class of clinical mastitis (I006) and names MQC-C as the candidate product for the two somatic cell count rows.

**A cell count study filed under mastitis.** The same study 43 is filed under mastitis detection in Table 2, while page 8 says "real-time milk analyzers agreed moderately with SCC (43)" and its title is about online somatic cell count. Because the tables do not settle which counts, the two somatic cell count rows (I057, I058) are unsure (decision log, 9 October 2026). Kevin's lists do not move, because RSPCA Assured requires both.

**Validated technologies with no spreadsheet row.** Tables 1 and 2 name tested technologies that have no row in the spreadsheet's list of 129, among them Lely's activity system (study 42), the KB 3/04 bolus (study 52) and the Optris camera (study 55). Since grades only credit products in the list, these are not credited. This rules out one reading for thermal comfort (I039).

**On sale, says the paper; not in the list.** Page 10 says of thermal cameras and boluses for thermal comfort, "Both options are available on the market". Every thermal camera in the spreadsheet states another aim, such as udder health or lameness, and none names thermal comfort or body temperature. Under the project's rule that a product counts only for what its stated aim names, thermal comfort's device class is the worn sensor, not the camera (decision log, 30 September 2026).

**Spelling slips that hide words from a search.** "pastur activity" (row 48) is missed by a search for pasture; "meassurement" (rows 40 and 41) by a search for measurement; "wellbing" (row 3) by a search for wellbeing; "gat pressure" (row 18) is gait pressure. The company Workswell is written "Workshell" (rows 127 and 128), though their own links read workswell. No count changes. The pasture and gait cases are noted in the rows that use them.

What was not found: the counts in the paper match the spreadsheet. It lists 129 products, 18 of them with a validation flag, as the paper says.

## 3. Maroto Molina and colleagues 2020

**A measure the current protocol dropped.** Their Table 1 (page 2) lists coughing. The Welfare Quality protocol version 3.2 notes the "suppression of coughing measurement". The project follows version 3.2, so coughing (I042) was removed (decision log, 2 October 2026), and the count of Welfare Quality only indicators went from 27 to 26.

**One principle, two names.** Table 1 says "Good behaviour", while the paper's own heading on page 3 and Welfare Quality 3.2 say "Appropriate behaviour". Four rows were renamed to match. No answer changes.

**A cited study that does not match its claim.** Page 3 says image analysis was tested in pigs with respiratory problems, citing Chen and colleagues 2013. The reference (page 5) is a laboratory biosensor based on imaging ellipsometry that detects a virus, not a camera on animals. The device class for hampered respiration (I045) follows the paper's words, and the row says so.

## 4. The Welfare Quality protocol, version 3.2

**Printed page numbers run one behind.** PDF page 22 is printed 21, and so on. Since 30 September 2026 every page is cited as the PDF page with the printed one in brackets.

**A coughing column survives.** The recording sheet on PDF 63 (printed 62) still has a column for coughing, which the version note says was dropped. This supports removing I042.

**Two pasture measures, two labels.** Access to an outdoor loafing area or pasture (PDF 29, printed 28) is labelled a management based measure, and access to pasture (PDF 38, printed 37) a resource based measure, though both ask the farm manager the same questions about days and hours on pasture. The table follows each label as printed.

**Version labels.** The first pages carry the header "Version 3.0" and later pages "3.2". The overview on PDF 22 spells "integument alternations".

## 5. EFSA 2023, the opinion on dairy cows

**A table that runs on without a caption.** Table 27 appears to end on PDF 43, but its last two measures sit at the top of PDF 44 under a bare header row, with no "continued" label. They were added as I058 and I059, which took the EFSA set from 30 to 32 indicators (decision log, 2 October 2026).

**A repeated caption.** Table 18 (PDF 33) carries a caption about claw conditions or claw diseases, like the table before it, although it lists hock and knee alterations.

**Scales credited to Welfare Quality that it does not use.** EFSA describes body condition as "a scoring from 1 to 5 (Welfare Quality, 2009)" (Table 46, PDF 75), but Welfare Quality scores body condition 0, 1 or 2. EFSA's hock and knee scales (Table 18, PDF 33) are said to come from Welfare Quality, which has one lesion count over five body regions and no separate hock or knee scale. EFSA's 3 point lameness scale (Table 16, PDF 32) matches only one of Welfare Quality's two lameness measures; the tied stall measure scores 0 or 2. The notes of I023, I004, I005 and I001 explain how the rows were joined. No answer changes.

**Feasibility reasons the market contradicts.** EFSA rates lying time low on feasibility because "Validated activity monitors are not widely available on farm yet" (Table 33, PDF 54), while Stygar list commercial monitors validated for lying. The table keeps EFSA's rating, as EFSA wrote it, and the I012 and I008 rows note the difference.

**Ratings written as sentences.** EFSA gives sensitivity, specificity and feasibility in prose. For two measures it gives no level word, and for two it gives two levels. These are coded not stated (I003, I058) and mixed (I017, I018) (decision log, 8 October 2026).

## 6. ICAR

The ICAR list page gives the Ekomilk analyser's parameters as "SCC and milk parameters", with no limit. Its test report (pages 12 and 13) says the somatic cell count met ICAR's accuracy limit only between 0 and 500,000 cells per ml. The report also calls the instrument "Horizon Limited" on page 3, while its title says Horizon Unlimited. No answer changes, because this product is outside the 2021 baseline.

## 7. The certification schemes

**Mortality counted narrowly.** Global Animal Partnership's mortality limit "excludes Culls" (PDF 25, printed 15), and culls include euthanised animals. Certified Humane records "All sudden deaths, disease outbreaks, and humane killings of unfit cattle" (PDF 37, printed 28). Both are narrower than Welfare Quality's mortality, so both rows are unsure (open questions, 8 October 2026). RSPCA Assured requires mortality, so Kevin's lists do not move.

**Mastitis standards numbered two ways.** On Global Animal Partnership's PDF 42 (printed 32), the four mastitis thresholds are numbered 7.D.3 to 7.D.6, but the text also refers to "the thresholds listed in 7.D.5-7.D.8". The row cites the numbering of the standards themselves.

**Should inside must.** Certified Humane's E 34 a (PDF 25, printed 16) says udder, teats and flanks "should be clean" inside a standard worded with must, under a milking parlour heading that may not cover farms milking in tie stalls. Both cleanliness rows it could name are unsure.

**One score over a span of the body.** RSPCA Assured scores cleanliness "only including the hind quarters to coronary band and udder" (PDF 98, printed 96), one combined score. Hind quarters is Welfare Quality's own name for the flank and upper leg area, so that row is required; whether the span includes the lower legs is not settled, so that row is unsure.

**Page numbers.** In each scheme document the printed page numbers differ from the PDF page numbers by a different amount, and Global Animal Partnership numbers its first pages in roman numerals. Every scheme row gives both.

## 8. Kevin's Slack reply

Kevin's reply quotes three of Manisha's questions without quotation marks, so "My recommendation is dairy" reads as his. [1_sources/README.md](../1_sources/README.md) says which words are his.

## 9. Our own corrections

The project's own mistakes are not listed here as findings about the sources. The audits caught them, and each is corrected in a dated entry of [decision_log.md](../2_research/decision_log.md); the audit rounds are listed in [audit_log.md](../2_research/audit_log.md). For example: rumination was first called the most validated trait, though Stygar rank non active behaviour first (29 September 2026); two counts of product aims were first taken from the wrong spreadsheet columns (30 September 2026); and a summary on the front page first said three schemes require body condition, when all four do (12 October 2026). While this page was written, one more was found: the lameness row had silently corrected the spreadsheet's "gat pressure" to gait in a quote, and now quotes it as printed.
