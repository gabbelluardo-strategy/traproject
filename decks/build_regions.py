import os
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "helpers.py")).read())

s = new_slide(LAYOUT_BAR, "ESG TOPICS, LOCAL ADAPTATION")
title(s, "One Narrative, Adapted by Global Markets", y=1.0, size=24)
text(s, 0.67, 1.6, 12.0, 0.6, [{"runs": [
    ("Facts will be anchored in current ESG facts provided by Stellantis, along with the FaSTlane 2030 strategic plan through a consistent message, carried through different ways according to the region", 13, TEXT, False, False)]}], name="Lead")

regions = [
 ("EUROPE", "“Are you keeping your promises?”",
  "Sustainability is a regulatory and political matter. We answer with proof: CO₂ compliance, affordable EVs, the future of our plants, circularity. Every claim needs to hold up under CSRD and the new EU rules on green claims.",
  "Watch out for: anything that sounds like a slogan", None),
 ("NORTH & SOUTH AMERICA", "“What does this mean for American jobs?”",
  "The word “ESG” closes doors. The same investments speak for themselves when told through plants, jobs, efficiency and customer choice.",
  "Watch out for: going silent, as it can carry risks and paranoia.",
  "South America: flex-fuel and bio-hybrid as a local climate solution, industrial jobs"),
 ("ASIA", "“Can you make green mobility affordable here?”",
  "Social impact matters as much as climate. Lead with access to mobility, local production and skills, and partnerships like Leapmotor.",
  "Watch out for: exporting a European message that doesn’t fit.", None),
]
w, gap, y, h = 3.9, 0.15, 2.3, 3.6
for i, (reg, q, body, watch, extra) in enumerate(regions):
    x = 0.67 + i * (w + gap)
    box(s, x, y, w, h, fill=WHITE, line=BORDER, name=f"{reg} card")
    label_box(s, x, y, w, 0.5, reg, fill=NAVY, size=14, bold=True, shape=MSO_SHAPE.RECTANGLE, name=f"{reg} head")
    paras = [{"runs": [(q, 13, ORANGE, True, True)], "after": 8},
             {"runs": [(body, 11.5, TEXT, False, False)], "after": 8}]
    wl, wr = watch.split(": ", 1)
    paras.append({"runs": [(wl + ": ", 11.5, ORANGE, True, False), (wr, 11.5, TEXT, False, False)], "after": 8})
    if extra:
        el, er = extra.split(": ", 1)
        paras.append({"runs": [(el + ": ", 11.5, NAVY, True, False), (er, 11.5, TEXT, False, False)]})
    text(s, x + 0.22, y + 0.68, w - 0.44, h - 0.8, paras, name=f"{reg} text")

yp = 6.05
paths = [[("Path 1: ", False), ("Discovering he right energy for every road.", True),
          (" It presents our multi-energy strategy as a promise to customers, rather than something we need to defend.", False)],
         [("Path 2: ", False), ("The progress you can measure.", True),
          (" Fewer promises, more evidence, more meaning with a short set of KPIs to report consistently.", False)]]
pw = (12.0 - 0.15) / 2
for i, runs in enumerate(paths):
    x = 0.67 + i * (pw + 0.15)
    box(s, x, yp, pw, 0.8, fill=TINT, line=None, radius=0.12, name=f"Path {i+1} box")
    text(s, x + 0.25, yp + 0.06, pw - 0.5, 0.68, [{"runs": [(t, 11.5, NAVY if b else TEXT, b, False) for t, b in runs]}],
         anchor=MSO_ANCHOR.MIDDLE, name=f"Path {i+1} text")

keep = s
sldIdLst = prs.slides._sldIdLst
for sid in list(sldIdLst):
    if prs.part.related_part(sid.rId) is not keep.part:
        prs.part.drop_rel(sid.rId)
        sldIdLst.remove(sid)
prs.save(OUT)
print("saved", OUT)
