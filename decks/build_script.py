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

keep = s
sldIdLst = prs.slides._sldIdLst
for sid in list(sldIdLst):
    if prs.part.related_part(sid.rId) is not keep.part:
        prs.part.drop_rel(sid.rId)
        sldIdLst.remove(sid)
prs.save(OUT)
print("saved", OUT)
