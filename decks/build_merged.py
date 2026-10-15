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
        runs[0].find(qn("a:t")).text = "Global storytelling and ESG narrative territories"
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
        p0.runs[0].text = "Global sustainability narrative: storytelling and ESG territories"
        for hl in p0._p.iter(qn("a:highlight")):
            hl.getparent().remove(hl)
        sh.width = Inches(9.5)
        for t in ["Key insight and the four territories", "Competitors: automotive players",
                  "Remarkable cases: global storytelling", "Remarkable cases: ESG topics",
                  "Positioning map", "Stellantis today and narrative architecture", "Take-outs"]:
            p = tf.add_paragraph()
            p.level = 1
            r = p.add_run()
            r.text = t
            fmt_run(r, 14, TEXT, False, font=LIGHT)
notes(agenda, "One research area, recalibrated on four narrative territories. The sub-items are the sections of the deck.")

# ---------------------------------------------------------------- 3 divider
for sh in divider.shapes:
    if sh.is_placeholder and sh.placeholder_format.idx == 13:
        sh.text_frame.paragraphs[0].runs[0].text = "GLOBAL SUSTAINABILITY NARRATIVE"
    elif sh.is_placeholder and sh.placeholder_format.idx == 21:
        sh.text_frame.paragraphs[0].runs[0].text = "1"
    elif sh.name == "Text 35":
        ps = sh.text_frame.paragraphs
        ps[0].runs[0].text = "KEY QUESTION"
        ps[2].runs[0].text = ("How do leading players tell their overall sustainability story, and how do they "
                              "prove it on the four ESG territories that matter for Stellantis?")
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


# ---------------------------------------------------------------- key insight
sK = new_slide(LAYOUT_BAR, "Key insight")
text(sK, 0.67, 1.2, 11.6, 1.3, [("The best players do not have the smartest slogan. They have one organising idea repeated everywhere, "
                                 "and they prove it territory by territory with a measurable, recurring proof.", 22, NAVY, True, False)], name="Statement")
ki = [("01", "One grid, everywhere", "Hub, KPIs, report, governance and local sites use the same dimensions (VW, Toyota)."),
      ("02", "Impact areas, not dates", "Frameworks built on impact areas survived the 2024-26 target changes; those built on an end date did not."),
      ("03", "A proof per territory", "A monthly payment, a patent given away, tonnes of CO₂ per car, a quarterly score: never an adjective alone.")]
for i, (n, h, b) in enumerate(ki):
    x = 0.67 + i * 4.07
    box(sK, x, 3.0, 3.85, 2.75, name=f"Card {n}")
    text(sK, x + 0.3, 3.3, 3.25, 2.3, [{"runs": [(n, 28, ORANGE, True, False)], "after": 10},
                                       {"runs": [(h, 18, NAVY, True, False)], "after": 8},
                                       {"runs": [(b, 15, TEXT, False, False)]}], name=f"Card {n} text")
notes(sK, "This deck merges two lenses: overall corporate storytelling (organising idea, hub architecture, consistency over time) and the four ESG narrative territories (Fair Transition, Customer Trust, Environmental Transformation, Transparency & Accountability).")


# ---------------------------------------------------------------- player cards (logo area left for the real logo)
def player_slide(header, side, cases, labels, note):
    s = new_slide(LAYOUT_BAR, header)
    vertical_label(s, side)
    for i, c in enumerate(cases):
        x = 0.66 + i * 4.07
        text(s, x + 0.1, 1.08, 3.7, 0.6, [(c["logo"], 22, NAVY, True, False)], anchor=MSO_ANCHOR.MIDDLE,
             align=PP_ALIGN.CENTER, name=f"Logo placeholder {c['logo']}")
        box(s, x, 1.75, 3.9, 5.12, name=f"Card {i+1}")
        big = len(labels) == 2
        paras = [{"runs": [("Title", 12, ORANGE, True, False)], "after": 1},
                 {"runs": [(c["title"], 14, NAVY, True, False)], "after": 10}]
        for key, lab in labels:
            paras.append({"runs": [(lab, 12, ORANGE, True, False)], "after": 1})
            paras.append({"runs": [(c[key], 13 if big else 11.5, TEXT, False, False)], "after": 10})
        paras[-1]["after"] = 0
        text(s, x + 0.25, 1.95, 3.4, 4.5, paras, name=f"Card {i+1} text")
        text(s, x + 1.2, 6.52, 2.48, 0.25, [(c["tag"], 10, NAVY, False, True)], align=PP_ALIGN.RIGHT, name=f"Hashtag {i+1}")
    notes(s, note)
    return s


COMP = [("story", "Global storytelling"), ("esg", "ESG territories"), ("matters", "Why it matters for Stellantis")]

sA = player_slide("Competitors · Automotive (1/3)", "ESG Narrative", [
    dict(logo="Volkswagen Group", title="One grid that runs site, report and Board pay",
         story="regenerate+: four dimensions (Nature, Our People, Society, Business) with 3 Top-KPIs each; the same grid runs the hub, the Progress Report, the external council and pay.",
         esg="Transparency: Decarbonization Index in the Board bonus. Fair Transition contradictory: ID.Polo at €24,995 next to 35,000 jobs cut. Supply-chain exposure (Xinjiang).",
         matters="Adopt the skeleton, then add what VW lacks: its own voice and an explicit link to FaSTLAne 2030.",
         tag="#OneGridEverywhere"),
    dict(logo="Mercedes-Benz Group", title="The deepest hub, from promise to single model",
         story="One path, five layers: overview, six strategic areas, Ambition 2039, a 360° Environmental Check per model, investor metrics.",
         esg="Customer Trust: Traffic Safety and Digital Trust as ESG pillars. Transparency: Climate Transition Action Plan versioned every year (2023-2026).",
         matters="A public transition plan linked from the 2050 page, as EmpCo will require, and data trust as an ESG topic.",
         tag="#LayeredHub"),
    dict(logo="BMW Group", title="One product carries the whole transformation",
         story="Neue Klasse and the Debrecen plant tell CO₂, circularity and supply chain through one car and one place; “carbon neutral” became “fossil-free”.",
         esg="Environmental: 0.1 t CO₂ in production per iX3, about one third secondary material, −35% supply-chain CO₂e. Transparency: fleet CO₂ weighted 25% in long-term pay.",
         matters="The model for STLA One and the Pomigliano E-Car: one object that unites the whole transformation.",
         tag="#OneProductOneStory")], COMP,
    "VW: progress figures (Decarbonization Index 46.3 t CO2e per vehicle in 2025) from secondary sources; hub visuals not verified. Mercedes: six areas are hard to remember and Ambition 2039 is built on a date. BMW: pay split (about 37%/3%) to re-check. Visuals: volkswagen-group.com/en/sustainability-15772; group.mercedes-benz.com/sustainability; BMW Neue Klasse press materials.")

sB = player_slide("Competitors · Automotive (2/3)", "ESG Narrative", [
    dict(logo="Renault Group", title="Sustainability in the brand menu and in the monthly payment",
         story="The Future is NEUTRAL sits under “brands & entities” next to Renault, Dacia and Alpine, with revenue and margin targets (over €2.3bn, over 10% by 2030, self-reported).",
         esg="Fair Transition: Twingo from €19,490, social leasing €130-139/month, Flins Re-Factory. Customer Trust: Fireman Access patents licensed free to the industry.",
         matters="The closest competitor, strong on three territories. SUSTAINera and the ë-C3 at €94/month can answer it.",
         tag="#CircularityAsBusiness"),
    dict(logo="Volvo Cars", title="Safety given away, a reset explained",
         story="Safety as brand DNA for decades; one integrated Annual and Sustainability Report.",
         esg="Customer Trust: seatbelt patent shared, E.V.A. crash data (women 71% more likely to be injured). Environmental: EX90 battery passport with QR. Transparency: 2024 target reset explained with causes, net zero 2040 kept.",
         matters="The template for an open safety gesture and for the missing “why 2050” message.",
         tag="#SafetyForAll"),
    dict(logo="Toyota", title="Environmental Challenge 2050: eleven years, same frame",
         story="Six numbered challenges since 2015: impact areas, not deadlines. The same icon set travels across UK, US, Lebanese and dealer sites.",
         esg="Customer Trust: 10-year hybrid battery warranty. Fair Transition contested: “multi-pathway” read as an alibi; rated worst on climate lobbying (InfluenceMap).",
         matters="Dateless, iconic dimensions survive target changes; a multi-energy plan still needs proof, not a slogan.",
         tag="#ImpactAreasNotDates")], COMP,
    "Renault: Re-Factory figures dated 2021-22; no independent test of the “minutes instead of hours” fire claim; Transparency is its weakest territory. Volvo: 55m+ reach of E.V.A. is self-reported. Toyota: 2026 global hub not verified; NGO criticism of multi-pathway from Greenpeace and InfluenceMap.")

sC = player_slide("Competitors · Automotive (3/3)", "ESG Narrative", [
    dict(logo="Polestar", title="The car with a label and an honest vocabulary",
         story="A Product Sustainability Declaration per model, online and in Spaces; an editorial report with its own name (“The Beep Report”).",
         esg="Environmental: minerals “traced vs mapped”, per-car footprint 31.7 t (−31%). Transparency: public LCA method; discloses +24% absolute emissions; Polestar 0 moved to 2035.",
         matters="A label and a vocabulary that hold under EmpCo and anticipate the 2027 battery passport.",
         tag="#TracedVsMapped"),
    dict(logo="Hyundai · Kia", title="Award-winning platforms, thinner proof",
         story="Hyundai “Progress for Humanity” and IONIQ Forest (1m+ trees, 13 countries, Cannes Lions 2025-26); Kia trunk liner from Ocean Cleanup plastic, with a QR code.",
         esg="Fair Transition weak: EV3 “affordable” at €35,990. Transparency: Hyundai at 40% supply-chain disclosure (Lead the Charge).",
         matters="Borrow the creativity of long platforms and objects; add what they lack: impact in CO₂, not trees or kilos.",
         tag="#PlatformNeedsProof"),
    dict(logo="BYD", title="A memorable slogan without depth",
         story="“Cool the Earth by 1°C”: the most memorable organising idea of the sample, with little depth behind it on the hub.",
         esg="Fair Transition: price only (Dolphin Surf €22,990 at launch). Environmental: 46.6 Mt “avoided” claim. Transparency: 0% supply-chain disclosure.",
         matters="The risk case: a slogan without proof is exactly what EmpCo now makes risky.",
         tag="#SloganVsProof")], COMP,
    "Polestar figures self-reported. Hyundai/Kia: battery warranty data from secondary sources; IONIQ Forest engagement metrics not published. BYD: Blade Battery nail test dated and not independently replicated; BYD hub not verified.")

REM = [("why", "Why it works"), ("matters", "Why it matters for Stellantis")]

sD = player_slide("Remarkable · Global storytelling", "Remarkable cases", [
    dict(logo="Microsoft", title="Promise, proof, people, depth",
         why="Four 2030 commitments, one big proof number and one sub-page each, then the CSO's voice, stories and a reports hub. It owns the bad news in the first person: emissions up about 25% in 2025, with the cause.",
         matters="The model for the first two layers of a hub, and the register for 2050: name the setback before the press does.",
         tag="#PromiseProofPeople"),
    dict(logo="Schneider Electric", title="A score out of 10 that survives a change of plan",
         why="SSI 2021-25 closed at 8.86/10; Impact 2030 restarts the scale (3.69 at H1 2026 vs 4.20 target). Published quarterly with results; pillars written as business missions; linked to incentives.",
         matters="A “Stellantis Impact Score” restarting with FaSTLAne turns the new plan into a chapter, not a retreat.",
         tag="#OneScore"),
    dict(logo="Patagonia", title="“Work in Progress”: candour as a brand trait",
         why="A purpose, an act that proves it (“Earth is now our only shareholder”) and an impact report with missed targets on the cover (footprint +2%). First for GlobeScan/ERM experts in 2025.",
         matters="One lesson: name the step back, explain why, reaffirm the path. The tone itself is not transferable.",
         tag="#RadicalCandour")], REM,
    "Microsoft: the only hub read directly (October 2026); criticism over a gas deal with Chevron. Schneider: weight in bonuses not verified. Patagonia: figures self-reported; candour works only when backed by an act. Counter-example: Unilever's quiet 2024 target cuts.")

REM2 = [("why", "Why it works"), ("matters", "Why it matters for Stellantis")]
sE = player_slide("Remarkable · ESG topics", "Remarkable cases", [
    dict(logo="Enel", title="Fair Transition: just transition as a report with KPIs",
         why="Futur-e converts 23 Italian coal plants and a mining area; a dedicated Just Transition Report tracks people redeployed after reskilling (about 55%, 110 hours each in 2021).",
         matters="Italian, industrial, transferable to the ICE-to-EV shift at Mirafiori, Pomigliano, Melfi, Termoli: a joint ESG and HR format.",
         tag="#JustTransitionReport"),
    dict(logo="Miele", title="Customer Trust: “longevity is the ultimate sustainability”",
         why="Machines tested for 5,000 cycles, about 20 years of use, reviewed by Fraunhofer, with an honest note that this is not a guarantee.",
         matters="Durability told as sustainability, with a test and a caveat: a model for SUSTAINera parts and Spoticar battery certificates.",
         tag="#DurabilityIsSustainability"),
    dict(logo="Holcim", title="Environmental Transformation: green product lines that grow",
         why="ECOPact, ECOPlanet and ECOCycle are brands with a share of sales (31% and 36%) and 8 Mt recycled, reported next to the financial results.",
         matters="Template for SUSTAINera as a brand with a revenue-share KPI, instead of “up to 80%” claims.",
         tag="#GreenRevenue")], REM2,
    "Enel caveat: redeployment share fell to about 30% in 2023, the rest retired; figures dated. Miele figures self-reported. Holcim figures self-reported. Transparency & Accountability remarkable cases are on the storytelling slide (Microsoft, Schneider, Patagonia).")
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
order = [cover, agenda, divider, sK, s4, sA, sB, sC, sD, sE, s5, s6, s11, s12, takeout]
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
