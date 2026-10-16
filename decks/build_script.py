import os
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "helpers.py")).read())

s = new_slide(LAYOUT_BAR, "Stellantis Motor Citizens · Script")
text(s, 0.67, 1.05, 12.0, 0.5, [{"runs": [("International Volunteering Day", 22, NAVY, True, False), ("  ·  December 5th", 22, ORANGE, True, False)]}], name="Title")

B, N = True, False
def L(*parts, after=5):
    return {"runs": [(t, 12, NAVY if b else TEXT, b, False) for t, b in parts], "after": after}

cols = [
 ("01", "Opening", None, [
   L(("Making a difference starts with ", N), ("people", B)),
   L(("People who ", N), ("care", B)),
   L(("People who ", N), ("take action", B)),
   L(("People who ", N), ("give their time to help others", B))]),
 ("02", "Core", None, [
   L(("At Stellantis, this spirit comes to life through ", N), ("Motor Citizens", B)),
   L(("Our global employee volunteering program", N)),
   L(("It connects our people with local projects and organizations where their skills can make a difference", N), after=9),
   L(("From supporting young people", N)),
   L(("To protecting the environment", N)),
   L(("To sharing knowledge and experience", N), after=9),
   L(("Every action starts with a simple idea:", N)),
   L(("We can all contribute.", B))]),
 ("03", "Employee cuts", "Nice to have", [
   {"runs": [("EMPLOYEE 1", 11, ORANGE, True, False)], "after": 1},
   {"runs": [("“I wanted to give something back to my community.”", 12, TEXT, False, True)], "after": 10},
   {"runs": [("EMPLOYEE 2", 11, ORANGE, True, False)], "after": 1},
   {"runs": [("“It’s a chance to share what I know and learn something new.”", 12, TEXT, False, True)], "after": 10},
   {"runs": [("EMPLOYEE 3", 11, ORANGE, True, False)], "after": 1},
   {"runs": [("“And to see the difference we can make, together.”", 12, TEXT, False, True)]}]),
 ("04", "Ending", None, [
   L(("Because making a difference", N)),
   L(("doesn’t take just one person", N)),
   L(("It takes ", N), ("all of us.", B), after=14)]),
]
w, gap, y = 2.9, 0.13, 1.8
for i, (n, h, tag, paras) in enumerate(cols):
    x = 0.67 + i * (w + gap)
    end = h == "Ending"
    box(s, x, y, w, 4.95, fill=WHITE, line=BORDER, name=f"Scene {n}")
    label_box(s, x, y, w, 0.55, "", fill=NAVY, shape=MSO_SHAPE.RECTANGLE, name=f"Scene {n} head")
    text(s, x + 0.2, y + 0.05, w - 0.4, 0.45, [{"runs": [(n + "  ", 14, ORANGE, True, False), (h, 14, WHITE, True, False)]}],
         anchor=MSO_ANCHOR.MIDDLE, name=f"Scene {n} title")
    if tag:
        label_box(s, x + w - 1.35, y + 0.65, 1.2, 0.28, tag, fill=PEACH, color=ORANGE, size=9, bold=True,
                  shape=MSO_SHAPE.ROUNDED_RECTANGLE, name=f"Scene {n} tag")
    text(s, x + 0.22, y + (1.05 if tag else 0.8), w - 0.44, 3.4, paras, name=f"Scene {n} text")
    if end:
        label_box(s, x + 0.22, y + 3.85, w - 0.44, 0.75, "", fill=NAVY, shape=MSO_SHAPE.ROUNDED_RECTANGLE, name="End card")
        text(s, x + 0.3, y + 3.9, w - 0.6, 0.65, [{"runs": [("Stellantis", 12, WHITE, False, False)]},
                                                  {"runs": [("Motor Citizens", 16, WHITE, True, False)]}],
             anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER, name="End card text")
notes(s, "Script for the International Volunteering Day (5 December) video on Motor Citizens, Stellantis' global employee volunteering program. Structure: opening, core message, optional employee cuts, ending with the Stellantis Motor Citizens end card.")


# ---------------------------------------------------------------- slide 2: requested material
r = new_slide(LAYOUT_BAR, "Stellantis Motor Citizens · Requested material")
text(r, 0.67, 1.05, 12.0, 0.5, [{"runs": [("What we need from Stellantis to produce the video", 22, NAVY, True, False)]}], name="Title")
# left card: program material
xL, wL, yT, hT = 0.67, 4.95, 1.8, 4.95
box(r, xL, yT, wL, hT, fill=WHITE, line=BORDER, name="Material card")
label_box(r, xL, yT, wL, 0.55, "", fill=NAVY, shape=MSO_SHAPE.RECTANGLE, name="Material head")
text(r, xL + 0.2, yT + 0.05, wL - 0.4, 0.45, [{"runs": [("01  ", 14, ORANGE, True, False), ("Motor Citizens program material", 14, WHITE, True, False)]}],
     anchor=MSO_ANCHOR.MIDDLE, name="Material title")
mat = [("Program overview", "purpose, how it works, countries involved"),
       ("Key facts and figures", "volunteers, hours, projects, latest year available"),
       ("Projects and partners", "examples by area: young people, environment, sharing skills"),
       ("Photo and video footage", "past activities, with usage rights"),
       ("Brand assets", "Motor Citizens logo, visual guidelines, approved wording"),
       ("Existing communication", "intranet articles, social posts, internal videos"),
       ("Contacts", "program owner and local coordinators for filming")]
paras = []
for h, b in mat:
    paras.append({"runs": [(h, 12, NAVY, True, False), (": " + b, 11.5, TEXT, False, False)], "after": 8, "bullet": True})
text(r, xL + 0.25, yT + 0.8, wL - 0.5, hT - 1.0, paras, name="Material list")
# right card: employee interviews
xR, wR = xL + wL + 0.15, 12.0 - wL - 0.15 + 0.01
box(r, xR, yT, wR, hT, fill=WHITE, line=BORDER, name="Interview card")
label_box(r, xR, yT, wR, 0.55, "", fill=NAVY, shape=MSO_SHAPE.RECTANGLE, name="Interview head")
text(r, xR + 0.2, yT + 0.05, wR - 0.4, 0.45, [{"runs": [("02  ", 14, ORANGE, True, False), ("Employee interviews", 14, WHITE, True, False)]}],
     anchor=MSO_ANCHOR.MIDDLE, name="Interview title")
label_box(r, xR + wR - 2.35, yT + 0.65, 2.2, 0.28, "Draft: questions to co-write", fill=PEACH, color=ORANGE, size=9, bold=True,
          shape=MSO_SHAPE.ROUNDED_RECTANGLE, name="Draft tag")
text(r, xR + 0.25, yT + 0.68, wR - 2.8, 0.6, [{"runs": [("Who and how: ", 11, NAVY, True, False),
     ("3 volunteers, different countries, roles and project types; about 20 min each; signed release forms.", 11, TEXT, False, False)]}], name="Interview setup")
qs = [("Can you introduce yourself: your name, your role and where you work?", ""),
      ("Which Motor Citizens project did you join, and what did you do?", ""),
      ("Why did you decide to volunteer?", "cut 1"),
      ("Which of your skills did you bring, and what did you learn?", "cut 2"),
      ("What difference did you see for the people or the community you helped?", "cut 3"),
      ("What was the moment that stayed with you the most?", ""),
      ("What would you say to a colleague thinking about volunteering?", ""),
      ("Motor Citizens in one word?", "")]
qp = []
for i, (q, cut) in enumerate(qs, 1):
    runs = [(f"{i}.  ", 13, ORANGE, True, False), (q, 13, TEXT, False, False)]
    if cut:
        runs.append(("   → " + cut, 10, ORANGE, True, True))
    qp.append({"runs": runs, "after": 10})
text(r, xR + 0.25, yT + 1.45, wR - 0.5, hT - 1.6, qp, name="Interview questions")
notes(r, "Requested material for the International Volunteering Day video. The arrows map interview questions to the three employee cuts in the script (cut 1: give something back; cut 2: share what I know and learn; cut 3: the difference we can make, together). Questions are a draft to be finalised together; deadlines and named contacts to be agreed with the Stellantis team.")

keep = (s, r)
sldIdLst = prs.slides._sldIdLst
for sid in list(sldIdLst):
    if prs.part.related_part(sid.rId) not in (keep[0].part, keep[1].part):
        prs.part.drop_rel(sid.rId)
        sldIdLst.remove(sid)
prs.save(OUT)
print("saved", OUT)
