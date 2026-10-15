# Found along the way

While building the crosswalk, the source documents were read closely, and some of them turned out to disagree with themselves, with each other, or with the web as it is today. This page lists those things in plain words. None of them is a welfare finding. They are findings about the sources: where a reader of the same documents could trip, and what this project did about each one.

Each entry says where the problem is, what does not match, what the project did, and whether it changes any answer in the Excel file. Page numbers are PDF page numbers, the number your PDF viewer shows, with the printed number in brackets where they differ. Short quotes copy the source exactly, spelling slips included. Section 1 rests on the web pages as they were on 15 October 2026; every other entry was checked again against its file in [1_sources](../1_sources) on that day.

## 1. The product links in the Stygar spreadsheet

**Where.** The spreadsheet the Stygar team published with their 2021 review ([1_sources/stygar_2021_supplementary.xlsx](../1_sources/stygar_2021_supplementary.xlsx), sheet "Appendix table 1", column INTERNET LINK) gives a web link for each of its 129 products. This project did not write these links; it copied them, and products.csv uses the same links for its 17 Stygar products.

**What we found.** On 15 October 2026 every link was opened again. 16 still open a maker's page that names the exact product, and 19 more do after being sent on to a new address (a redirect). 38 open the wrong page: a page that does not name the product or names only its family, a dealer's or other third party page, a parked domain (an address held for sale, with no content of its own) or an unrelated site. 56 are broken. For example, the WellCow bolus link (row 2) now ends on an error page of the design firm's site. In all, 94 of the 129 links no longer lead to the product, often because a maker moved its pages, sometimes because the product or the company is gone.

Some old addresses now send visitors to sites that have nothing to do with the product. On the day checked, the old Agersens address (row 7) led to an unrelated restaurant site, and the old EIO Diagnostics address (row 44, whose 2021 link itself gives an error) and the old Workswell camera address (rows 127 and 128) led to unrelated gambling pages. The eCow address (row 43) led to a domain resale service, and the Smartbow address (row 117) was a domain for sale. Take care when opening the 2021 links in these rows.

**Where the maker's page is today.** For each product, the maker's current page was searched for. A page was accepted only on the maker's own site, the site of a company that sells the product under its own name, or a site the maker's own old address now sends visitors to, never a reseller, a news story or an archive copy. 63 products have a current page that names them. 21 have only a related page: one that names the product family or a likely successor but not this exact model, such as a page for Lely Calm that does not name the Calm Compact + (row 87). For 30 the maker's site is live, often only its home page, but the product is not named on it, and for 15 no maker site was found at all.

**Links that point somewhere other than the maker.** Several 2021 links did not point to the maker even then. Seven point to a dealer, a seller, a marketplace, a third party file or a third party profile: StepMatrix (row 18) to a BouMatic dealer, the BouMatic calf feeder (row 19) to a dealer, the DeLaval Activity Meter System (row 30) to a dealer, CowScout S (row 66) to a GEA brochure kept on another company's site, Calf Star (row 80) to a shop that sells Holm & Laue feeders, the SAC FDS3 feeding station (row 115) to a trade marketplace page, and VitalHerd (row 125) to a company profile on an investment site. The Heatime Pro+ link (row 12) points to the page of a sister product, the Heatime HR system.

**Rows that look mixed up.** Row 116 is named "RDS Futureline MAX", which is the name SAC gives its milking robot in row 114, yet it is listed under the company Sensolus as a GPS collar, "A location tracker on animals". Row 80, "Calf Star", is listed under Holm & Laue; its link opens the shop of Calf Star, which sells Holm & Laue's CalfExpert feeders, and its page describes "The Calf Star Double Jug".

**What we did.** The new table [2_research/product_links.csv](../2_research/product_links.csv) records, for every product, what the 2021 link opens today, the maker's current page where one was found, and the words on that page that name the product. The Product list sheet of the Excel file shows the same next to the 2021 link. The rule is [rules.md](../2_research/rules.md), rule 4.10.

**Does it change an answer?** No. The grades and counts read the products' stated aims in the spreadsheet, not their web pages. The links matter to a reader who wants to see a product.

## 2. Stygar and colleagues 2021, the paper and its spreadsheet

**One study coded two ways.** In Table 1 (PDF 6), study 27 (Nielsen and colleagues) sits in the column for tests by someone independent of the maker on the IceQube and IceTag row, and in the column for tests done with the maker on the CowScout Leg row. The spreadsheet ("Appendix table 2", row 28) codes it "External self-validation". The project noted this on products P016 and P013 and rests P016 on studies 21, 26 and 28, so no answer changes.

**Product names spelt differently.** The paper writes "Stepmetrix (54)" (Table 2, PDF 7) and the spreadsheet "StepMatrix" (row 18), whose own link ends in stepmetrix. Other names also differ between the paper and the spreadsheet: eCow Farmer bolus and eBolus (row 43), CowScout Leg and CowScout S (row 66), Track A Cow and Track a))) Cow (row 46), HerdInsight and HerdInsights (row 76), one Table 1 row for IceQube and IceTag against two spreadsheet rows (48 and 49), and three Afimilk names against one spreadsheet row, AfiAct II (row 3). A word search for one spelling misses the other. Each match is stated in products.csv or in the sensor row that uses it. No grade changes.

**A tested product with no row under its name.** Table 2 names the "Lely-on-line California mastitis test (43)", but no spreadsheet row has that name. It was matched to Lely MQC-C (row 91), the only Lely row marked as tested (decision log, 3 October 2026). MQC-C is among the candidates behind the kind of device recorded for clinical mastitis (I006), and the candidate tested product for the two somatic cell count rows.

**A cell count study filed under mastitis.** The same study 43 is filed under mastitis detection in Table 2, while page 8 says "real-time milk analyzers agreed moderately with SCC (43)" and its title is about online somatic cell count. Because the tables do not settle which counts, the two somatic cell count rows (I057, I058) are unsure (decision log, 9 October 2026). Kevin's lists do not move, because RSPCA Assured requires both.

**Validated technologies with no spreadsheet row.** Tables 1 and 2 name tested technologies that have no row in the spreadsheet's list of 129, among them Lely's activity system (study 42), the KB 3/04 bolus (study 52) and the Optris camera (study 55). Since grades only credit products in the list, these are not credited. This rules out one reading for thermal comfort (I039).

**On sale, says the paper; not in the list.** Page 10 says of thermal cameras and boluses for thermal comfort, "Both options are available on the market". Every thermal camera in the spreadsheet states another aim, such as udder health or lameness, and none names thermal comfort or body temperature. Under the project's rule that a product counts only for what its stated aim names, the device recorded for thermal comfort is a worn sensor, not a camera (decision log, 30 September 2026).

**Spelling slips that hide words from a search.** "pastur activity" (row 48) is missed by a search for pasture; "meassurement" (rows 40 and 41) by a search for measurement; "wellbing" (row 3) by a search for wellbeing; "gat pressure" (row 18) is gait pressure. The company Workswell is written "Workshell" (rows 127 and 128), though their own links read workswell. No count changes. The pasture and gait cases are noted in the rows that use them.

What was not found: the counts in the paper match the spreadsheet. It lists 129 products, 18 of them marked as tested by an outside study, as the paper says.

## 3. Maroto Molina and colleagues 2020

**A measure the current protocol dropped.** Their Table 1 (page 2) lists coughing. The Welfare Quality protocol version 3.2 notes the "suppression of coughing measurement". The project follows version 3.2, so coughing (I042) was removed (decision log, 2 October 2026), and the count of Welfare Quality only indicators went from 27 to 26.

**One principle, two names.** Table 1 says "Good behaviour", while the paper's own heading on page 3 and Welfare Quality 3.2 say "Appropriate behaviour". Four rows were renamed to match. No answer changes.

**A cited study that does not match its claim.** Page 3 says image analysis was tested in pigs with respiratory problems, citing Chen and colleagues 2013. The reference (page 5) is a laboratory biosensor based on imaging ellipsometry that detects a virus, not a camera on animals. The device class for hampered respiration (I045) follows the paper's words, and the row says so.

## 4. The Welfare Quality protocol, version 3.2

**Printed page numbers run one behind.** PDF page 22 is printed 21, and so on. Since 30 September 2026 every page is cited as the PDF page with the printed one in brackets.

**A coughing column survives.** The recording sheet on PDF 63 (printed 62) still has a column for coughing, which the version note says was dropped. This supports removing I042.

**Two pasture measures, two labels.** Access to an outdoor loafing area or pasture (PDF 29, printed 28) is labelled a management based measure, and access to pasture (PDF 38, printed 37) a resource based measure, though both ask the farm manager similar questions about days and hours on pasture. The table follows each label as printed.

**Version labels.** The first pages carry the header "Version 3.0" and later pages "3.2". The overview on PDF 22 spells "integument alternations".

## 5. EFSA 2023, the opinion on dairy cows

**A table that runs on without a caption.** Table 27 appears to end on PDF 43, but its last two measures sit at the top of PDF 44 under a bare header row, with no "continued" label. They were added as I058 and I059, which took the EFSA set from 30 to 32 indicators (decision log, 2 October 2026).

**A repeated caption.** Table 18 (PDF 33) carries a caption about claw conditions or claw diseases, like the table before it, although it lists hock and knee alterations.

**Scales credited to Welfare Quality that differ from it.** EFSA describes body condition as "a scoring from 1 to 5 (Welfare Quality, 2009)" (Table 46, PDF 75), but Welfare Quality scores body condition 0, 1 or 2. EFSA's hock and knee scales (Table 18, PDF 33) are said to come from Welfare Quality, which counts hairless patches and lesions per body region, scored as a total, with no separate hock or knee scale. EFSA's 3 point lameness scale (Table 16, PDF 32) matches only one of Welfare Quality's two lameness measures; the tied stall measure scores 0 or 2. The notes of I023, I004, I005 and I001 explain how the rows were joined. No answer changes.

**A feasibility reason to read beside the market list.** EFSA rates lying time low on feasibility because "Validated activity monitors are not widely available on farm yet" (Table 33, PDF 54), while Stygar list commercial monitors tested for lying. The two statements are about different things: EFSA's about how many farms have such monitors, Stygar's about what is on sale. The table keeps EFSA's rating as EFSA wrote it; the I012 row notes the difference, and I008 notes the same for steps (Table 31).

**Ratings written as sentences.** EFSA gives sensitivity, specificity and feasibility in prose. For two measures it gives no level word, and for two it gives two levels. These are coded not stated (I003, I058) and mixed (I017, I018) (decision log, 8 October 2026).

## 6. ICAR

The ICAR list page gives the Ekomilk analyser's parameters as "SCC and milk parameters", with no limit. Its test report (pages 12 and 13) says the somatic cell count met ICAR's accuracy limit only between 0 and 500,000 cells per ml. The report also calls the instrument "Horizon Limited" on page 3, while its title says Horizon Unlimited. No answer changes, because this product is outside the 2021 baseline.

## 7. The certification schemes

**Mortality counted narrowly.** Global Animal Partnership's mortality limit "excludes Culls" (PDF 26, printed 16), and its definition of culls includes euthanised animals (PDF 25, printed 15). Certified Humane records "All sudden deaths, disease outbreaks, and humane killings of unfit cattle" (PDF 37, printed 28). Both are narrower than Welfare Quality's mortality, so both rows are unsure (open questions, 8 October 2026). RSPCA Assured requires mortality, so Kevin's lists do not move.

**Mastitis standards numbered two ways.** On Global Animal Partnership's PDF 42 (printed 32), the four mastitis thresholds are numbered 7.D.3 to 7.D.6, but the text also refers to "the thresholds listed in 7.D.5-7.D.8". The row cites the numbering of the standards themselves.

**Should inside must.** Certified Humane's E 34 a (PDF 25, printed 16) says udder, teats and flanks "should be clean" inside a standard worded with must, under a milking parlour heading that may not cover farms milking in tie stalls. Both cleanliness rows it could name are unsure.

**One score over a span of the body.** RSPCA Assured scores cleanliness "only including the hind quarters to coronary band and udder" (PDF 98, printed 96), one combined score. Hind quarters is Welfare Quality's own name for the flank and upper leg area, so that row is required; whether the span includes the lower legs is not settled, so that row is unsure.

**Page numbers.** In three of the four scheme documents the printed page numbers differ from the PDF page numbers, by a different amount in each, and Global Animal Partnership numbers its first pages in roman numerals. Every scheme row gives both.

## 8. Kevin's Slack reply

Kevin's reply quotes three of Manisha's questions without quotation marks, so "My recommendation is dairy" reads as his. [1_sources/README.md](../1_sources/README.md) says which words are his.

## 9. Our own corrections

The project's own mistakes are not listed here as findings about the sources. The audits caught them, and each is corrected in a dated entry of [decision_log.md](../2_research/decision_log.md); the audit rounds are listed in [audit_log.md](../2_research/audit_log.md). For example: rumination was first called the most validated trait, though Stygar rank non active behaviour first (29 September 2026); two counts of product aims were first taken from the wrong spreadsheet columns (30 September 2026); and a summary on the front page first said three schemes require body condition, when all four do (12 October 2026). While this page was written, one more was found: the lameness row (I001, where_to_check) gave the StepMatrix aim as gait pressure, where the spreadsheet prints gat pressure; it now gives the aim as printed.

## 10. What happened to some of the companies

Checking the product links showed that many of the companies behind the 2021 products have closed, been bought or renamed. None of this is used in any table, grade or count; it explains why a link fails. These facts come from outside sources, not from the documents in 1_sources, so each one names its source, which was read on 15 October 2026. Where the source is weak or says less than the note it replaces, the entry says so.

**Well Cow (WellCow bolus, row 2).** The company WELL COW LIMITED (company number 04733004) was dissolved by voluntary strike off on 22 September 2020, after applying on 3 February 2020; no liquidation is recorded. Source: the UK companies register, Companies House, [filing history](https://find-and-update.company-information.service.gov.uk/company/04733004/filing-history): "Final Gazette dissolved via voluntary strike-off". A case study by TTP, one of its shareholders, describes the bolus and names "the Roslin Foundation, TTP and the Genomia Fund" as the main shareholders ([TTP](https://ttp.com/case-studies/well-cow-monitoring-the-gut-health-of-dairy-cows-with-an-ingestible-bolus)).

**GEA CowView (row 64).** GEA added an optional cow positioning function to CowScout in July 2021: "Existing GEA CowScout systems can be retrofitted with the positioning function" ([GEA trade press release, 29 July 2021](https://www.gea.com/en/news/trade-press/2021/gea-farm-technologies-cowscout/)). No GEA page found says that CowView was withdrawn or replaced; the release does not mention CowView, and gea-cowview.com no longer answers.

**LIC automation (Saber Milk, Protrack BCS and Protrack SCC, rows 92 to 94).** LIC, the Livestock Improvement Corporation of New Zealand, sold its automation business to MSD Animal Health in June 2021. LIC's announcement to the stock exchange says it "has completed the divestment of its automation business" ([NZX, 14 June 2021](https://www.nzx.com/announcements/373886)); its release of 8 June 2021 names Protrack ([Scoop](https://www.scoop.co.nz/stories/BU2106/S00133.htm)), and trade press names the "Saber and Protrack technology solutions" ([Agriland, 8 June 2021](https://www.agriland.co.uk/farming-news/saber-deal-sealed-msd-acquires-lic-automation/)).

**Bayer and Cowdition (row 14).** Bayer launched the free body condition scoring app Cowdition in 2016 ([FarmingUK, 14 March 2016](https://www.farminguk.com/news/bayer-launches-free-body-condition-scoring-app-to-identify-at-risk-cows_39021.html)). Elanco "closed the acquisition of Bayer Animal Health" on 3 August 2020 ([Elanco release filed with the US Securities and Exchange Commission](https://www.sec.gov/Archives/edgar/data/1739104/000110465920089668/tm2026229d1_ex99-1.htm)). No source was found that says what became of Cowdition.

**Cattlewatch (row 23).** A startup database lists a company, Herd-itt, with former names including CattleWatch, as "Non Active, Dec 2025 ceased to operate" ([Startupim](https://startupim.com/company/cattlewatch)). This is a weak source: the profile cites none, and no company statement, register entry or news report was found. Its domain is now parked.

**EIO Diagnostics (FirstLook Mastitis system, row 44).** The product was called FirstLook Mastitis in 2019 ([Douglas Magazine, 4 April 2019](https://douglasmagazine.com/?p=13431)). Some later company profiles use the name UdderHealth, but no source was found that says one name replaced the other. The company's domain now sends visitors to an unrelated site.

**Agersens (eShepherd, row 7).** Gallagher bought Agersens, the developer of eShepherd: "Agersens, is now part of Gallagher Group under a strategic change of ownership" ([Gallagher](https://am.gallagher.com/News/Virtual-fencing-leader-Agersens-acquired-by-Gallagher)); trade press dates the deal to June 2021 ([Beef Central, 14 June 2021](https://www.beefcentral.com/?p=190952)).

**Smartbow (row 117).** Zoetis lists "Our acquisition of Smartbow, a developer of dairy cow monitoring systems and electronic ear tags" among its 2018 transactions ([Zoetis proxy statement, filed with the US Securities and Exchange Commission, 2 April 2019](https://www.sec.gov/Archives/edgar/data/1555280/000119312519095103/d683828ddef14a.htm)). smartbow.com is now a domain for sale.

**Allflex, SCR and Heatime (rows 10 to 12).** Merck, known outside North America as MSD, completed its purchase of Antelliq Corporation, the parent of Allflex, on 1 April 2019 ([Merck release](https://www.merck.com/news/merck-completes-acquisition-of-antelliq-corporation-to-become-leader-in-emerging-digital-technology-for-livestock-and-companion-animals/)). Allflex had agreed to buy SCR Engineers, the maker of Heatime, in December 2014 ([Progressive Dairy, 12 December 2014](https://agproud.com/articles/48614-allflex-acquires-global-livestock-monitoring-company-scr-engineers-ltd)). An Allflex case study calls Heatime the predecessor of SenseHub: a farm "installed an Allflex SenseHub™ system after using its predecessor Heatime®" ([Allflex, April 2021](https://www.allflex.global/wp-content/uploads/2021/07/Halvor-Midtsundstad_Allflex_MSD_A4_low.pdf)).

**IceRobotics (IceTag and IceQube, rows 48 and 49).** "Peacock Technology has completed the acquisition of IceRobotics" ([Peacock Technology news, 2022](https://www.peacocktechnology.com/en/news/peacock-technology-acquires-icerobotics-to-expand-offering-to-dairy-sector)). Peacock now sells a leg sensor called IDS i-QUBE with CowAlert; no page says it is the IceQube under a new name, and IceTag is not mentioned.

**GrowSafe (row 74).** Vytelle and GrowSafe Systems, both owned by the Wheatsheaf Group, announced in July 2020 that they were combining under the Vytelle name. The original release ([Business Wire, 14 July 2020](https://www.businesswire.com/news/home/20200714005208/en/Vytelle-GrowSafe-Combine-Create-Leader-Bovine-Biotechnology)) refused scripted access; a newsletter of 18 July 2020 reports "The merger of Vytelle & GrowSafe" ([Prime Future](https://primefuture.substack.com/p/prime-future-013-three-structural)). growsafe.com now sends visitors to vytelle.com.

**SAC (rows 114 and 115).** BouMatic bought the SAC Group in October 2021: "SAC will operate as a fully owned subsidiary of BouMatic" ([BouMatic, 18 October 2021](https://boumatic.com/ca_en/news/boumatic-acquisition-sac/)). sacmilking.com now sends visitors to BouMatic.

**Cainthus (Alus Nutrition, row 22).** Ever.Ag announced on 21 June 2022 that it "has acquired Cainthus, a company that offers artificial intelligence- enabled cameras" ([release as reposted by Dairy Producer](https://dairyproducer.com/ever-ag-accelerates-growth-broadens-on-farm-dairy-solutions-with-acquisition-of-cainthus)). cainthus.com now leads to an Ever.Ag page that does not name Cainthus or Alus.

**Ida (Connecterra, row 25).** "Datamars has acquired the sensor business of Connecterra known as 'Ida for Farmers'", and took a majority share in Connecterra ([joint press release](https://www.agproud.com/ext/resources/directories/files/Datamars-and-Connecterra-Join-Forces-Press-Release.pdf); reported on 1 March 2023 by [Silicon Canals](https://siliconcanals.com/connecterra-datamars-strategic-partnership-enterprise-ai/)).

**Corrections to our own notes.** Earlier notes in product_links.csv said Well Cow was out of business, that positioning is now sold under CowScout, that Allflex was bought by MSD, that LIC sold its automation business to MSD, that Bayer Animal Health went to Elanco, that Cattlewatch became Herd-itt and ceased, that FirstLook became UdderHealth, and that Gallagher and Zoetis bought Agersens and Smartbow. They were removed from the table because no page it cites shows them. The sources above confirm most of them and narrow several: Well Cow was struck off voluntarily, not liquidated; MSD bought Allflex's parent, Antelliq; GEA added positioning to CowScout, but no source says CowView was replaced; the Herd-itt closure rests on one weak database entry; and no source says FirstLook was renamed UdderHealth.
