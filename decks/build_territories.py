import os
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "helpers.py")).read())

STRONG_F, MED_F, WEAK_F, NONE_F = RGBColor(0xC9, 0xD2, 0xF0), TINT, PEACH, RGBColor(0xF7, 0xF7, 0xF9)

# ---------------------------------------------------------------- 1 cover
for sh in cover.shapes:
    if sh.has_text_frame and sh.text_frame.text.startswith("ESG"):
        last = sh.text_frame.paragraphs[-1]
        newp = copy.deepcopy(last._p)
        last._p.addnext(newp)
        runs = newp.findall(qn("a:r"))
        for r in runs[1:]:
            newp.remove(r)
        runs[0].find(qn("a:t")).text = "Narrative territories: how leading players position"
        rPr = runs[0].find(qn("a:rPr"))
        rPr.set("sz", "1800"); rPr.set("b", "0"); rPr.set("cap", "none")
        sb = newp.find(qn("a:pPr")).find(qn("a:spcBef"))
        sb.clear()
        from lxml import etree as _e
        _e.SubElement(sb, qn("a:spcPts")).set("val", "1400")
        sh.top = sh.top - Inches(0.35)
        sh.height = sh.height + Inches(0.35)
    elif sh.has_text_frame and sh.text_frame.text.strip() == "2026":
        sh.text_frame.paragraphs[0].runs[0].text = "October 2026"
notes(cover, "Recalibrated benchmark: the global sustainability narrative read through four narrative territories (Fair Transition, Customer Trust, Environmental Transformation, Transparency & Accountability). For each player: which activities, and how they tell them.")

# ---------------------------------------------------------------- 2 agenda
for sh in list(agenda.shapes):
    if sh.has_text_frame and sh.text_frame.text.startswith("Da trad"):
        sh._element.getparent().remove(sh._element)
    elif sh.has_text_frame and sh.text_frame.text == "AMBITI DI RICERCA":
        sh.text_frame.paragraphs[0].runs[0].text = "RESEARCH AREAS"
    elif sh.has_text_frame and sh.text_frame.text.strip() == "Lorem":
        tf = sh.text_frame
        p0 = tf.paragraphs[0]
        p0.runs[0].text = "Global sustainability narrative: four narrative territories"
        for hl in p0._p.iter(qn("a:highlight")):
            hl.getparent().remove(hl)
        sh.width = Inches(9.5)
        for t in ["The four territories", "Positioning map of the players", "Fair Transition", "Customer Trust",
                  "Environmental Transformation", "Transparency & Accountability",
                  "Stellantis today and narrative architecture", "Take-outs"]:
            p = tf.add_paragraph()
            p.level = 1
            r = p.add_run()
            r.text = t
            fmt_run(r, 14, TEXT, False, font=LIGHT)
notes(agenda, "One research area, recalibrated on four narrative territories. The sub-items are the sections of the deck.")

# ---------------------------------------------------------------- 3 divider
for sh in divider.shapes:
    if sh.is_placeholder and sh.placeholder_format.idx == 13:
        sh.text_frame.paragraphs[0].runs[0].text = "NARRATIVE TERRITORIES"
    elif sh.is_placeholder and sh.placeholder_format.idx == 21:
        sh.text_frame.paragraphs[0].runs[0].text = "1"
    elif sh.name == "Text 35":
        ps = sh.text_frame.paragraphs
        ps[0].runs[0].text = "KEY QUESTION"
        ps[2].runs[0].text = ("Where do leading players stand on the four narrative territories, "
                              "with which activities, and how do they tell them?")
        sh.width = Inches(6.4)
notes(divider, "Players analysed: Volkswagen, Mercedes-Benz, BMW, Renault, Volvo Cars, Polestar, Toyota, Hyundai/Kia, BYD; beyond automotive: Schneider Electric, Microsoft, Patagonia, Apple, IKEA, Enel, Holcim. Plus Stellantis today.")

# ---------------------------------------------------------------- 4 framework
s4 = new_slide(LAYOUT_BAR, "The four territories")
title(s4, "Four territories, one test: turn a value into a measurable proof")
terr = [("01", "Fair Transition", "Affordability, accessibility, electrification, reskilling"),
        ("02", "Customer Trust", "Quality, safety, durability, privacy, customer experience"),
        ("03", "Environmental Transformation", "Decarbonisation, circularity, supply chain"),
        ("04", "Transparency & Accountability", "Results, progress and transparency beyond reporting")]
for i, (n, h, b) in enumerate(terr):
    x = 0.67 + i * 3.05
    box(s4, x, 1.95, 2.85, 2.85, name=f"Territory {n}")
    text(s4, x + 0.25, 2.2, 2.4, 2.5, [{"runs": [(n, 28, ORANGE, True, False)], "after": 10},
                                       {"runs": [(h, 16, NAVY, True, False)], "after": 8},
                                       {"runs": [(b, 13, TEXT, False, False)]}], name=f"Territory {n} text")
box(s4, 0.67, 5.1, 11.95, 1.15, fill=NAVY, line=None, name="What wins")
text(s4, 0.95, 5.25, 11.4, 0.9, [{"runs": [("What wins in every territory: ", 15, ORANGE, True, False),
                                           ("a recurring, measurable proof tied to a concrete object (a monthly payment, a patent given away, tonnes of CO₂ per car, a quarterly score), not a slogan.", 15, WHITE, False, False)]}],
     anchor=MSO_ANCHOR.MIDDLE, name="What wins text")
notes(s4, "Players that stay on value claims (“multi-pathway”, “affordable” without an orderable price, “avoided” emissions) get challenged. Since 27 September 2026 the EU Empowering Consumers Directive also requires proof behind generic and future claims.")

# ---------------------------------------------------------------- 5 heat map
s5 = new_slide(LAYOUT_BAR, "Positioning map")
title(s5, "Who occupies which territory, and with what", y=1.05, size=20)
H = [
 ("Volkswagen", ("M", "ID.Polo €24,995; 35k jobs cut"), ("M", "Integrity, inward-facing"), ("M", "regenerate+, raw materials report"), ("M", "CO₂ index in Board bonus")),
 ("Mercedes-Benz", ("-", ""), ("S", "Traffic Safety + Digital Trust ESG"), ("M", "Low-CO₂ steel and aluminium"), ("S", "Yearly versioned transition plan")),
 ("BMW", ("M", "Debrecen training centre"), ("-", ""), ("S", "Neue Klasse: 0.1 t CO₂/car"), ("M", "Fleet CO₂ in long-term pay")),
 ("Renault", ("S", "Twingo, social leasing, Flins"), ("S", "Firefighter patent, free licence"), ("S", "The Future Is NEUTRAL"), ("W", "External ratings table only")),
 ("Volvo Cars", ("-", ""), ("S", "Seatbelt patent, E.V.A."), ("M", "EX90 battery passport"), ("M", "2024 reset explained")),
 ("Polestar", ("-", ""), ("-", ""), ("S", "Product label, traced vs mapped"), ("S", "Public LCA method per model")),
 ("Toyota", ("W", "“Multi-pathway” contested"), ("M", "10-year hybrid battery warranty"), ("M", "Battery 3R, Challenge 2050"), ("W", "Worst on climate lobbying")),
 ("Hyundai/Kia", ("W", "EV3 “affordable” at €35,990"), ("M", "Battery warranties"), ("M", "Ocean Cleanup, IONIQ Forest"), ("M", "Supply-chain disclosure 40%")),
 ("BYD", ("M", "Dolphin Surf €22,990, price only"), ("M", "Blade Battery nail test"), ("W", "46.6 Mt “avoided” claim"), ("W", "0% supply-chain disclosure")),
 ("Schneider Electric", ("S", "Access to Energy, 1m trained"), ("-", ""), ("S", "−56% CO₂ at top suppliers"), ("S", "Quarterly impact score")),
 ("Microsoft", ("S", "$4bn reskilling (Elevate)"), ("-", ""), ("M", "Supplier clause, Scope 3 up"), ("S", "Admits +25% emissions")),
 ("Patagonia", ("-", ""), ("S", "Ironclad Guarantee, repairs"), ("S", "Footprint Chronicles map"), ("S", "“Work in Progress” report")),
 ("Apple", ("-", ""), ("S", "“Privacy. That's iPhone.”"), ("S", "30% recycled, recycled cobalt"), ("M", "Watch claim banned in court")),
 ("IKEA", ("S", "“Not a premium add-on”, −10%"), ("-", ""), ("S", "Renewables for suppliers"), ("M", "Footprint delay disclosed")),
 ("Enel", ("S", "Futur-e, Just Transition Report"), ("-", ""), ("-", ""), ("-", "")),
 ("Holcim", ("-", ""), ("-", ""), ("S", "ECOPact/ECOPlanet share of sales"), ("M", "ECO KPIs next to results")),
 ("Stellantis", ("M", "ë-C3 €94/month, E-Car <€15k"), ("W", "US recalls, privacy; quality reset"), ("M", "SUSTAINera, Reuse +51%"), ("W", "CSRD only, no reset story")),
]
LV = {"S": ("Strong", STRONG_F), "M": ("Medium", MED_F), "W": ("Weak", WEAK_F), "-": ("Not found", NONE_F)}
cols = ["Player", "Fair Transition", "Customer Trust", "Environmental Transformation", "Transparency & Accountability"]
widths = [1.75, 2.55, 2.55, 2.55, 2.55]
rh = 0.275
tbl = s5.shapes.add_table(len(H) + 1, 5, Inches(0.67), Inches(1.5), Inches(sum(widths)), Inches(rh * (len(H) + 1))).table
for j, w in enumerate(widths):
    tbl.columns[j].width = Inches(w)
for i in range(len(H) + 1):
    tbl.rows[i].height = Inches(rh)
    for j in range(5):
        c = tbl.cell(i, j)
        c.margin_left = c.margin_right = Inches(0.06)
        c.margin_top = c.margin_bottom = Inches(0.01)
        c.vertical_anchor = MSO_ANCHOR.MIDDLE
        c.fill.solid()
        tf = c.text_frame
        tf.text = ""
        p = tf.paragraphs[0]
        if i == 0:
            c.fill.fore_color.rgb = NAVY
            r = p.add_run(); r.text = cols[j]; fmt_run(r, 10, WHITE, True)
            continue
        row = H[i - 1]
        stl = row[0] == "Stellantis"
        if j == 0:
            c.fill.fore_color.rgb = PEACH if stl else WHITE
            r = p.add_run(); r.text = row[0]; fmt_run(r, 10, ORANGE if stl else NAVY, True)
        else:
            lv, act = row[j]
            name, fill = LV[lv]
            c.fill.fore_color.rgb = fill
            r = p.add_run(); r.text = name + (": " if act else ""); fmt_run(r, 9, NAVY if lv != "-" else GREY, lv != "-")
            if act:
                r2 = p.add_run(); r2.text = act; fmt_run(r2, 9, TEXT, False)
footnote(s5, "Qualitative reading by the research team, not a rating. “Not found” = not found in our sources, not absent. Mostly self-reported figures.")
notes(s5, "Strong = quantified proof points and a recognisable format. Medium = partial or contradicted. Weak = mainly value claims or contested. Where the report used an intermediate level (e.g. medium-strong) the map shows the first term; nuances are in the written report. Renault Transparency set to Weak on a single signal (external ratings table on its site).")

# ---------------------------------------------------------------- 6 readings
s6 = new_slide(LAYOUT_BAR, "Positioning map")
title(s6, "What the map tells us")
reads = [("No player is strong everywhere", "Renault, Schneider Electric and Patagonia are strong on three territories; nobody on four."),
         ("No carmaker owns Transparency", "Only Mercedes (versioned transition plan) and Polestar (public LCA method) are strong: the space is still open."),
         ("Fair Transition is least crowded", "Premium carmakers barely use it, and FaSTLAne 2030 gives Stellantis the most natural material: price and European plants."),
         ("Customer Trust is the exposure", "The territory where Stellantis is most vulnerable today: a claim without proof would backfire.")]
for i, (h, b) in enumerate(reads):
    x = 0.67 + (i % 2) * 6.1
    y = 1.95 + (i // 2) * 2.15
    box(s6, x, y, 5.9, 1.95, name=f"Reading {i+1}")
    label_box(s6, x + 0.3, y + 0.3, 0.75, 0.75, f"0{i+1}", fill=NAVY, size=18, bold=True, shape=MSO_SHAPE.OVAL, name=f"Reading {i+1} badge")
    text(s6, x + 1.3, y + 0.3, 4.35, 1.5, [{"runs": [(h, 16, NAVY, True, False)], "after": 6},
                                           {"runs": [(b, 14, TEXT, False, False)]}], name=f"Reading {i+1} text")
notes(s6, "Readings from the positioning map. They frame why Fair Transition should lead the Stellantis story and why Transparency & Accountability is an open space.")


# ---------------------------------------------------------------- territory case slides
def territory_slide(header, cases, note):
    s = new_slide(LAYOUT_BAR, header)
    vertical_label(s, "Narrative territories")
    for i, c in enumerate(cases):
        x = 0.66 + i * 4.07
        box(s, x, 1.62, 3.9, 5.25, name=f"Card {i+1}")
        label_box(s, x, 1.13, 3.08, 0.41, c["logo"], size=14, name=f"Logo {i+1}")
        text(s, x + 0.22, 1.82, 3.46, 4.6, [
            {"runs": [("Title", 10, ORANGE, True, False)], "after": 1},
            {"runs": [(c["title"], 12, NAVY, True, False)], "after": 9},
            {"runs": [("What they do", 10, ORANGE, True, False)], "after": 1},
            {"runs": [(c["what"], 10.5, TEXT, False, False)], "after": 9},
            {"runs": [("How they tell it", 10, ORANGE, True, False)], "after": 1},
            {"runs": [(c["how"], 10.5, TEXT, False, False)], "after": 9},
            {"runs": [("Why it matters for Stellantis", 10, ORANGE, True, False)], "after": 1},
            {"runs": [(c["matters"], 10.5, TEXT, False, False)]}], name=f"Card {i+1} text")
        text(s, x + 1.2, 6.53, 2.48, 0.25, [(c["tag"], 10, NAVY, True, True)], align=PP_ALIGN.RIGHT, name=f"Hashtag {i+1}")
    notes(s, note)
    return s


s7 = territory_slide("Territory 1 · Fair Transition", [
    dict(logo="Renault Group", title="Electric for all, told from the plant to the monthly payment",
         what="Twingo E-Tech from €19,490; French social leasing 2026 at €130-139/month; 700 Flins staff moved to the Re-Factory with up to 450 training hours [2021-22].",
         how="One chain (customer, worker, territory) with a number on every link: launch, leasing offer, blog stories with workers' faces.",
         matters="Same segments and markets. Stellantis already has the lower payment (ë-C3 at €94/month) but does not tell it as a group story.",
         tag="#PlantToPayment"),
    dict(logo="Enel", title="Just transition as a dedicated report with KPIs",
         what="Futur-e: 23 Italian coal plants and one mining area; about 55% of leavers redeployed after reskilling, 110 hours each [2021].",
         how="A Just Transition Report separate from the sustainability report, alternating KPIs and workers' stories.",
         matters="Italian, industrial and transferable to the ICE-to-EV shift at Mirafiori, Pomigliano, Melfi and Termoli: a joint ESG and HR format.",
         tag="#JustTransitionReport"),
    dict(logo="Schneider Electric", title="Access and skills, with targets beaten",
         what="Access to Energy reached 61 million people against a 50 million target; over 1 million people trained in energy management.",
         how="Reported as part of the quarterly impact score next to financial results; targets and outcomes side by side.",
         matters="Shows how reskilling and access become a recurring, audited number instead of a one-off story.",
         tag="#SkillsAsKPI")],
    "Volkswagen sits in the risks: declared prices (ID.Polo €24,995) and a “socially responsible” 35,000-job cut, contradicted by Dresden and Osnabrück. IKEA is the simplest message: sustainability is “not a premium add-on”, with average prices down 10%. Enel caveat: redeployment share fell to about 30% in 2023, the rest retired. Visuals: automobile-propre.com social leasing Renault 2026; en.blogrenault.com Flins Re-Factory; Enel Just Transition Report 2023 PDF.")

s8 = territory_slide("Territory 2 · Customer Trust", [
    dict(logo="Volvo Cars", title="Safety given away to the whole industry",
         what="1959 three-point seatbelt patent shared; E.V.A. (2019) opened data from 43,000+ crashes: women 71% more likely to be injured.",
         how="Safety as brand DNA and as an equity story; open data library and campaign (55m+ people reached, self-reported).",
         matters="Giving something away, with a number attached, builds trust faster than any quality claim.",
         tag="#SafetyForAll"),
    dict(logo="Renault Group", title="A firefighter patent licensed for free",
         what="Fireman Access (7 patents) free to the industry since February 2025, improvements shared back; QRescue codes; 5,000+ firefighters trained in 21 countries.",
         how="Told through first responders, not customers: safety as a public good.",
         matters="The closest, most uncomfortable benchmark. Stellantis could answer with a rescue platform across all 14 brands and powertrains.",
         tag="#OpenSafety"),
    dict(logo="Mercedes-Benz", title="Traffic safety and digital trust as ESG pillars",
         what="Traffic Safety and Digital Trust are two of six strategic areas in the 2025 sustainability statement, presented to investors by a board member.",
         how="Inside the sustainability strategy and IR materials, not on a separate privacy page.",
         matters="The only carmaker making data trust an ESG pillar: a model for a Stellantis “Data Promise”, once practices are verified.",
         tag="#DigitalTrust")],
    "Also strong: Miele (durability tested for 20 years of use, with an honest legal caveat), Patagonia (Ironclad Guarantee), Apple (“Privacy. That's iPhone.”). Sector context: Mozilla 2023 found all 25 car brands reviewed failing on privacy; FTC order against GM/OnStar (January 2026). Renault's “minutes instead of hours” fire claim has no independent test found.")

s9 = territory_slide("Territory 3 · Environmental Transformation", [
    dict(logo="BMW", title="One product carries the whole transformation",
         what="Neue Klasse iX3: 0.1 t CO₂ in production at fossil-free Debrecen; about one third secondary material; 50% secondary Co/Li/Ni in Gen6 cells; −35% supply-chain CO₂e.",
         how="Numbers per car, told through the product launch and the plant; wording moved from “carbon neutral” to “fossil-free”.",
         matters="Model for STLA One and the Pomigliano E-Car: one object that unites CO₂, circularity and supply chain.",
         tag="#OneProductOneStory"),
    dict(logo="Polestar", title="The car with a label and an honest vocabulary",
         what="Sustainability declaration per model; minerals “traced vs mapped”; per-car footprint 31.7 t (−31%) while absolute emissions rose 24%.",
         how="Nutrition-style label in Spaces and online; public LCA method; bad news disclosed with the good.",
         matters="A label and a vocabulary that hold under EmpCo and anticipate the 2027 battery passport.",
         tag="#TracedVsMapped"),
    dict(logo="Holcim", title="Sustainability as product lines that grow",
         what="ECOPact, ECOPlanet and ECOCycle: share of sales (31% and 36%) and 8 Mt recycled, linked to profitability.",
         how="Branded green ranges reported next to the financial results.",
         matters="Template for SUSTAINera as a brand with a revenue-share KPI, instead of “up to 80%” claims.",
         tag="#GreenRevenue")],
    "Also strong: Apple (30% recycled material, recycled cobalt in batteries; but the Frankfurt court ruling on the Apple Watch “CO₂-neutral” claim shows the limit of offsets) and Schneider's Zero Carbon Project (−56% operational CO₂ at its top 1,000 suppliers). Figures mostly self-reported.")

s10 = territory_slide("Territory 4 · Transparency & Accountability", [
    dict(logo="Schneider Electric", title="An impact score every quarter, next to the accounts",
         what="SSI 2021-25 closed at 8.86/10; Impact 2030 restarts the scale: 3.69 at H1 2026 against a 4.20 target; linked to incentives.",
         how="One number with public sub-indicators, published with quarterly results and renewed each plan.",
         matters="A “FaSTLAne Impact Score” would turn the plan change into a new chapter, not a retreat.",
         tag="#OneScore"),
    dict(logo="Mercedes-Benz", title="A transition plan with the year in its title",
         what="Climate Transition Action Plan published every year (2023-2026): −90% production by 2039, −80% use, −70% value chain, net zero by 2049 (vs 2019).",
         how="Stand-alone, versioned PDF linked from the hub and investor pages.",
         matters="What EmpCo demands behind a “net zero 2050” claim; Stellantis should add the independent review Mercedes lacks.",
         tag="#VersionedPlan"),
    dict(logo="Volvo · Microsoft", title="Bad news in the first person, with cause and new route",
         what="Volvo 2024: dropped the all-electric 2030 target, named the causes, kept net zero 2040. Microsoft: emissions +25% in 2025, cause explained.",
         how="CEO line and press release (Volvo); report narrative and leadership letter (Microsoft).",
         matters="The template for the missing “why 2050” letter from Stellantis' CEO and CSO.",
         tag="#OwnTheSetback")],
    "Also relevant: BMW discloses a fleet CO₂ target weighted 25% in its long-term incentive and its 2024 misses; Polestar publishes the LCA method per model; Google dropped its carbon-neutral claim in 2024 and admits it is getting harder. BMW pay split and the Microsoft quote need re-checking.")

# ---------------------------------------------------------------- 11 Stellantis today
s11 = new_slide(LAYOUT_BAR, "Stellantis today")
title(s11, "More proof points than story, scattered across brands and countries")
st = [("Fair Transition", "Medium, high potential", MED_F,
       ["ë-C3 at €94/month, lowest French social leasing 2026", "E-Car under €15k at Pomigliano from 2028", "Douvrin 400-hour battery course; 6,000 Motor Citizens volunteers"],
       ["Fragmented, no group hub", "No group KPI on people reskilled", "Belvidere reopening delayed to 2028"]),
      ("Customer Trust", "Weak, exposed", PEACH,
       ["Quality reset: ~2,000 engineers [secondary]", "SUSTAINera remanufactured parts, Spoticar", "Mobilisights consent principles"],
       ["2026 US recalls (844k vehicles, camera)", "Privacy allegations in Texas v. Allstate/Arity (Stellantis not a defendant)"]),
      ("Environmental Transformation", "Medium", MED_F,
       ["−43% Scope 1-2, −26% Scope 1-3 vs 2021", "SUSTAINera Reuse +51%, Repair +48%", "500 MW solar on 27 European sites"],
       ["No symbol object, no per-unit metric", "“Up to” claims; 2038 pages online", "Indonesian nickel letter from 25 NGOs"]),
      ("Transparency & Accountability", "Weak", PEACH,
       ["CSRD statements 2024 and 2025", "Climate Policy Report on the reset"],
       ["No first-person “why 2050”", "No versioned plan with independent review", "No recurring scorecard or visible CO₂-pay link"])]
for i, (h, lvl, fill, pros, gaps) in enumerate(st):
    x = 0.67 + i * 3.05
    box(s11, x, 1.85, 2.85, 4.75, name=f"Stellantis {i+1}")
    label_box(s11, x, 1.85, 2.85, 0.75, h, fill=NAVY, size=12, bold=True, shape=MSO_SHAPE.RECTANGLE, name=f"Stellantis {i+1} head")
    label_box(s11, x + 0.2, 2.75, 2.45, 0.32, lvl, fill=fill, color=NAVY, size=10, bold=True, shape=MSO_SHAPE.ROUNDED_RECTANGLE, name=f"Stellantis {i+1} level")
    paras = [{"runs": [("Proof points", 10, ORANGE, True, False)], "after": 2}]
    paras += [{"runs": [(p_, 10, TEXT, False, False)], "after": 3, "bullet": True} for p_ in pros]
    paras += [{"runs": [("Gaps", 10, ORANGE, True, False)], "after": 2}]
    paras += [{"runs": [(g, 10, TEXT, False, False)], "after": 3, "bullet": True} for g in gaps]
    text(s11, x + 0.2, 3.25, 2.45, 3.25, paras, name=f"Stellantis {i+1} text")
footnote(s11, "Recall and J.D. Power figures beyond Reuters to be verified on NHTSA; allegations in Texas not proven. stellantis.com could not be opened directly.")
notes(s11, "Sensitive items to present factually: the Texas attorney general's January 2025 suit is against Allstate and its subsidiary Arity and alleges data purchases from several carmakers including Stellantis brands; Stellantis is not a defendant and the outcome is unverified. Italian competition authority (AGCM) probes on Stellantis, Tesla, BYD and VW closed in late 2025 with binding commitments and no fines. Stellantis replied to the Indonesian NGOs that it has no joint venture or formal collaboration on the smelter.")

# ---------------------------------------------------------------- 12 architecture
s12 = new_slide(LAYOUT_BAR, "Narrative architecture")
title(s12, "One promise, four kinds of proof: make the transition affordable and prove it with numbers", size=18)
rows = [("Stakeholder", "Lead territory", "Support territory", "Main proof", "Format"),
        ("Investors", "Transparency & Accountability", "Environmental Transformation", "Versioned transition plan, impact score, SUSTAINera KPIs", "Investor Day, half-year results"),
        ("Customers", "Customer Trust", "Fair Transition", "Orderable price and payment, Data Promise, battery certificate", "Product pages, configurator, dealers"),
        ("Employees", "Fair Transition", "Customer Trust (quality)", "Reskilling hours, people trained, Shares to Win", "Intranet, plant stories, ambassadors"),
        ("Regulators, NGOs", "Transparency & Accountability", "Environmental Transformation", "EmpCo-ready plan, critical minerals page", "Corporate hub, public answers"),
        ("Markets", "Varies by market", "", "France social leasing; Italy Pomigliano; US quality and UAW; Brazil Bio-Hybrid", "Local versions of the same index")]
widths = [1.6, 2.4, 2.4, 3.6, 2.0]
tbl = s12.shapes.add_table(len(rows), 5, Inches(0.67), Inches(1.95), Inches(sum(widths)), Inches(0.62 * len(rows))).table
for j, w in enumerate(widths):
    tbl.columns[j].width = Inches(w)
for i, row in enumerate(rows):
    tbl.rows[i].height = Inches(0.62 if i else 0.4)
    for j, val in enumerate(row):
        c = tbl.cell(i, j)
        c.fill.solid()
        c.fill.fore_color.rgb = NAVY if i == 0 else (TINT if i % 2 == 0 else WHITE)
        c.margin_left = c.margin_right = Inches(0.08)
        c.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf = c.text_frame
        tf.text = ""
        r = tf.paragraphs[0].add_run()
        r.text = val
        fmt_run(r, 10.5, WHITE if i == 0 else (NAVY if j == 0 else TEXT), bold=(i == 0 or j == 0))
box(s12, 0.67, 6.0, 12.0, 0.75, fill=PEACH, line=None, name="HR role")
text(s12, 0.9, 6.08, 11.6, 0.6, [{"runs": [("HR Communication leads, not supports: ", 12, ORANGE, True, False),
                                           ("reskilling becomes a public counter, Motor Citizens gives the faces, Shares to Win lets the people who build the affordable car co-own it.", 12, TEXT, False, False)]}],
     anchor=MSO_ANCHOR.MIDDLE, name="HR role text")
notes(s12, "The promise is our proposal, to be validated with the ESG and HR Communication teams. Shares to Win participation and conditions need internal verification (the ~11% figure is secondary).")

# ---------------------------------------------------------------- 13 take-outs
for sh in takeout.shapes:
    if sh.is_placeholder and sh.placeholder_format.idx == 13:
        sh.text_frame.paragraphs[0].runs[0].text = "TAKE-OUTS"
    elif sh.is_placeholder and sh.placeholder_format.idx == 21:
        sh.text_frame.paragraphs[0].runs[0].text = "1"
    elif sh.name == "Text 35":
        tf = sh.text_frame
        p0 = tf.paragraphs[0]
        p0.runs[0].text = "Fair Transition leads, Transparency & Accountability is the backbone, Customer Trust and Environmental Transformation supply the product proof."
        p0.runs[0].font.size = Pt(18)
        p0.runs[0].font.color.rgb = NAVY
        p0.runs[0].font.bold = True
        for extra in tf.paragraphs[1:]:
            extra._p.getparent().remove(extra._p)
        p0.space_after = Pt(14)
        for t in ["One object, one number, one person behind every story.",
                  "Never an adjective without proof: no “affordable” without price, no “just” without a KPI.",
                  "Rhythm over volume: a stable half-year index beats a longer report.",
                  "Bad news first and in the first person: 2050, Belvidere, recalls.",
                  "One group frame, many brand and market proofs."]:
            p = tf.add_paragraph()
            r = p.add_run()
            r.text = t
            fmt_run(r, 14, TEXT, False)
            p.space_after = Pt(7)
            pPr = p._p.get_or_add_pPr()
            pPr.set("marL", str(Emu(Inches(0.25))))
            pPr.set("indent", str(-Emu(Inches(0.25))))
            etree_sub(pPr, "a:buChar").set("char", "•")
        sh.width = Inches(7.0)
        sh.height = Inches(3.8)
notes(takeout, "Before client use, verify: US recall and J.D. Power figures, status of the Texas case, AGCM commitments, Indonesian nickel position, live 2038 pages, SUSTAINera 2025 revenues, reskilling and Shares to Win KPIs, ESG pay metrics, ESG content of the FaSTLAne Investor Day deck, and capture the visuals by hand.")

# ---------------------------------------------------------------- order & cleanup
order = [cover, agenda, divider, s4, s5, s6, s7, s8, s9, s10, s11, s12, takeout]
sldIdLst = prs.slides._sldIdLst
id_by_part = {prs.part.related_part(s.rId): s for s in list(sldIdLst)}
for drop in (blank, cards_tpl):
    sid = id_by_part[drop.part]
    prs.part.drop_rel(sid.rId)
    sldIdLst.remove(sid)
for s in order:
    sid = id_by_part[s.part]
    sldIdLst.remove(sid)
    sldIdLst.append(sid)
prs.save(OUT)
print("saved", OUT)
