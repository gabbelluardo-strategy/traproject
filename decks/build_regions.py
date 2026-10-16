import os
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "helpers.py")).read())

s = new_slide(LAYOUT_BAR, "ESG topics, local adaptation")
title(s, "One narrative, adapted by global markets", y=1.0, size=24)
text(s, 0.67, 1.6, 12.0, 0.6, [{"runs": [
    ("Facts are anchored in current ESG data provided by Stellantis and in the FaSTLAne 2030 strategic plan: ", 13, TEXT, False, False),
    ("one consistent message, carried in different ways by region.", 13, NAVY, True, False)]}], name="Lead")

regions = [
 ("Europe", "“Are you keeping your promises?”",
  "Sustainability is a regulatory and political matter. We answer with proof: CO₂ compliance, affordable EVs, the future of our plants, circularity. Every claim must hold up under CSRD and the new EU rules on green claims.",
  None, "Anything that sounds like a slogan."),
 ("North & South America", "“What does this mean for American jobs?”",
  "The word “ESG” closes doors. The same investments speak for themselves when told through plants, jobs, efficiency and customer choice.",
  ("South America: ", "flex-fuel and Bio-Hybrid as a local climate solution, with industrial jobs."),
  "Going silent: silence carries its own risks and fuels suspicion."),
 ("Asia", "“Can you make green mobility affordable here?”",
  "Social impact matters as much as climate. Lead with access to mobility, local production and skills, and partnerships like Leapmotor.",
  None, "Exporting a European message that doesn’t fit."),
]
w, gap, y, h = 3.9, 0.15, 2.25, 3.62
for i, (reg, q, body, extra, watch) in enumerate(regions):
    x = 0.67 + i * (w + gap)
    box(s, x, y, w, h, fill=WHITE, line=BORDER, name=f"{reg} card")
    label_box(s, x, y, w, 0.5, reg.upper(), fill=NAVY, size=14, bold=True, shape=MSO_SHAPE.RECTANGLE, name=f"{reg} head")
    paras = [{"runs": [("Stakeholder question", 10, GREY, True, False)], "after": 1},
             {"runs": [(q, 13, ORANGE, True, True)], "after": 8},
             {"runs": [("How we answer", 10, GREY, True, False)], "after": 1},
             {"runs": [(body, 11, TEXT, False, False)], "after": 5}]
    if extra:
        paras.append({"runs": [(extra[0], 11, NAVY, True, False), (extra[1], 11, TEXT, False, False)]})
    text(s, x + 0.22, y + 0.65, w - 0.44, h - 1.35, paras, name=f"{reg} text")
    box(s, x + 0.15, y + h - 0.68, w - 0.3, 0.55, fill=PEACH, line=None, radius=0.15, name=f"{reg} watch box")
    text(s, x + 0.3, y + h - 0.66, w - 0.6, 0.51, [{"runs": [("Watch out: ", 11, ORANGE, True, False), (watch, 11, TEXT, False, False)]}],
         anchor=MSO_ANCHOR.MIDDLE, name=f"{reg} watch")

# two narrative paths
yp = 6.02
text(s, 0.67, yp, 1.5, 0.8, [{"runs": [("Two narrative paths", 12, NAVY, True, False)]}], anchor=MSO_ANCHOR.MIDDLE, name="Paths label")
paths = [("Path 1", "Discovering the right energy for every road.",
          "It presents our multi-energy strategy as a promise to customers, rather than something we need to defend."),
         ("Path 2", "The progress you can measure.",
          "Fewer promises, more evidence, more meaning, with a short set of KPIs reported consistently.")]
pw = (12.0 - 1.55 - 0.15) / 2
for i, (lab, head, body) in enumerate(paths):
    x = 2.22 + i * (pw + 0.15)
    box(s, x, yp, pw, 0.8, fill=TINT, line=None, radius=0.12, name=f"{lab} box")
    label_box(s, x + 0.15, yp + 0.22, 0.8, 0.36, lab, fill=NAVY, size=10, bold=True, shape=MSO_SHAPE.ROUNDED_RECTANGLE, name=f"{lab} chip")
    text(s, x + 1.1, yp + 0.08, pw - 1.25, 0.7, [{"runs": [(head + " ", 11.5, NAVY, True, False), (body, 11, TEXT, False, False)]}],
         anchor=MSO_ANCHOR.MIDDLE, name=f"{lab} text")
notes(s, "One narrative, three regional entry points. Europe: proof under CSRD and EmpCo. Americas: plants, jobs, efficiency and choice rather than the word ESG; South America leads with flex-fuel and Bio-Hybrid. Asia: access, local production, skills and partnerships such as Leapmotor. Two candidate narrative paths for the group story.")

keep = s
sldIdLst = prs.slides._sldIdLst
for sid in list(sldIdLst):
    if prs.part.related_part(sid.rId) is not keep.part:
        prs.part.drop_rel(sid.rId)
        sldIdLst.remove(sid)
prs.save(OUT)
print("saved", OUT)
