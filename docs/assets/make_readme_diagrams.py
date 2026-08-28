#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate the two README diagrams (light + dark) for tns-as-st-me.

Writes only into docs/assets/.
"""
import os

OUT = "/home/tobias/Projects/tns-as-st-me/docs/assets"
FONT = "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"

THEMES = {
    "light": dict(
        ink="#0b0b0b", ink2="#52514e", ink3="#898781",
        hair="rgba(11,11,11,0.10)", hair2="rgba(11,11,11,0.07)",
        card="rgba(11,11,11,0.035)", ghost="rgba(11,11,11,0.085)",
        tri="rgba(11,11,11,0.024)",
        proved="#0ca30c", sketch="#2a78d6", conj="#eb6834", refut="#d03b3b",
    ),
    "dark": dict(
        ink="#ffffff", ink2="#c3c2b7", ink3="#898781",
        hair="rgba(255,255,255,0.10)", hair2="rgba(255,255,255,0.07)",
        card="rgba(255,255,255,0.045)", ghost="rgba(255,255,255,0.10)",
        tri="rgba(255,255,255,0.032)",
        proved="#0ca30c", sketch="#3987e5", conj="#d95926", refut="#d03b3b",
    ),
}

NB = " "


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def math(parts, size, fill, x, y, anchor="start", weight="400"):
    """parts: list of (text, kind), kind in '', 'sub', 'sup'.

    Boundary spaces are turned into explicit dx offsets so that no renderer
    can collapse them away; interior spaces become non-breaking spaces.
    """
    sub_dy, sup_dy = round(size * 0.30, 2), round(-size * 0.42, 2)
    small = round(size * 0.80, 2)
    spw = size * 0.29
    cur = 0.0
    pending = 0
    runs = []
    for txt, kind in parts:
        s = txt.lstrip(" ")
        pending += len(txt) - len(s)
        body = s.rstrip(" ")
        trailing = len(s) - len(body)
        if not body:
            pending += trailing
            continue
        tgt = {"": 0.0, "sub": sub_dy, "sup": sup_dy}[kind]
        dy = round(tgt - cur, 2)
        cur = tgt
        a = []
        if pending:
            a.append('dx="%s"' % round(pending * spw, 2))
        if dy:
            a.append('dy="%s"' % dy)
        a.append('font-size="%s"' % (small if kind else size))
        runs.append("<tspan %s>%s</tspan>" % (" ".join(a), esc(body.replace(" ", NB))))
        pending = trailing
    return ('<text x="%s" y="%s" font-size="%s" font-weight="%s" fill="%s" '
            'text-anchor="%s">%s</text>' % (x, y, size, weight, fill, anchor, "".join(runs)))


def text(s, x, y, size, fill, weight="400", anchor="start", ls=None, style=""):
    a = ""
    if ls is not None:
        a += ' letter-spacing="%s"' % ls
    if style:
        a += ' font-style="%s"' % style
    return ('<text x="%s" y="%s" font-size="%s" font-weight="%s" fill="%s" '
            'text-anchor="%s"%s>%s</text>' % (x, y, size, weight, fill, anchor, a, esc(s)))


def two_tone(x, y, size, head, tail, c_head, c_tail, anchor="start", ls=None, gap=5):
    """head in the strong ink, tail in the muted ink, separated by an explicit dx."""
    a = ' letter-spacing="%s"' % ls if ls is not None else ""
    t = ""
    if tail:
        t = ('<tspan dx="%s" fill="%s" font-weight="400">%s</tspan>'
             % (gap, c_tail, esc(tail.replace(" ", NB))))
    return ('<text x="%s" y="%s" font-size="%s" font-weight="600" text-anchor="%s"%s>'
            '<tspan fill="%s">%s</tspan>%s</text>'
            % (x, y, size, anchor, a, c_head, esc(head), t))


def dot(cx, cy, color, r=4.4):
    return '<circle cx="%s" cy="%s" r="%s" fill="%s"/>' % (cx, cy, r, color)


def card(x, y, w, h, T, rx=10):
    return ('<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s" '
            'stroke="%s" stroke-width="1"/>' % (x, y, w, h, rx, T["card"], T["hair"]))


def arrowmarker(mid, col):
    return ('<marker id="%s" viewBox="0 0 10 10" refX="9.4" refY="5" markerWidth="5" '
            'markerHeight="5" orient="auto">'
            '<path d="M0.4,0.7 L9.4,5 L0.4,9.3 L2.4,5 Z" fill="%s"/></marker>' % (mid, col))


def header(w, h, tid):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" '
            'height="%d" role="img" aria-labelledby="%s">' % (w, h, w, h, tid))


# ------------------------------------------------------------------ diagram 1
def triangle(theme):
    T = THEMES[theme]
    W, H = 900, 668
    o = [header(W, H, "irt")]
    o.append('<title id="irt">The 1D lattice infrared triangle. Corner A, asymptotic '
             'symmetry: PROVED for general compact G. Corner B, memory effect: PROVED, '
             'conditional on D26 and D27. Corner C, soft theorem: CONJECTURE in general, '
             'exact and PROVED at n equals 2. Directed edges: A to C is CONJECTURE, '
             'C to B is SKETCH blocked on lemma ACE-LD, B to A is SKETCH awaiting the '
             'moment map.</title>')
    o.append("<defs>")
    o.append(arrowmarker("t-conj", T["conj"]))
    o.append(arrowmarker("t-sk", T["sketch"]))
    # everything except the three card footprints
    o.append('<clipPath id="t-cut"><path clip-rule="evenodd" d="M0,0 H900 V668 H0 Z '
             'M280,76 h340 v150 h-340 Z M30,396 h290 v150 h-290 Z '
             'M580,396 h290 v150 h-290 Z"/></clipPath>')
    o.append("</defs>")
    o.append('<g font-family="%s">' % FONT)

    # ---- geometry (mirror-symmetric about x = 450) ----
    AX0, AX1, AY0 = 280, 620, 76      # corner A card  (w 340, h 150)
    CX0, CX1, CY0 = 30, 320, 396      # corner C card  (w 290, h 150)
    BX0, BX1 = 580, 870               # corner B card  (w 290, h 150)

    # soft triangular field, with the three card footprints clipped away
    o.append('<polygon points="450,151 175,471 725,471" fill="%s" '
             'clip-path="url(#t-cut)"/>' % T["tri"])

    o.append('<line x1="382.9" y1="229.0" x2="242.8" y2="392.2" stroke="%s" '
             'stroke-width="2" stroke-dasharray="7 5" stroke-linecap="round" '
             'marker-end="url(#t-conj)"/>' % T["conj"])
    o.append('<line x1="325" y1="471" x2="575" y2="471" stroke="%s" stroke-width="2" '
             'stroke-linecap="round" marker-end="url(#t-sk)"/>' % T["sketch"])
    o.append('<line x1="657.9" y1="393.0" x2="517.8" y2="229.8" stroke="%s" '
             'stroke-width="2" stroke-linecap="round" marker-end="url(#t-sk)"/>' % T["sketch"])

    o.append(text("The 1D lattice infrared triangle", 450, 36, 19, T["ink"], "600", "middle"))

    def corner(x0, x1, y0, letter, status, col, qual, name, tag, note):
        w = x1 - x0
        g = [card(x0, y0, w, 150, T)]
        g.append(text(letter, x1 - 20, y0 + 54, 54, T["ghost"], "700", "end"))
        g.append(dot(x0 + 26, y0 + 22, col))
        g.append(two_tone(x0 + 38, y0 + 26, 11, status, qual, T["ink2"], T["ink3"],
                          "start", 0.6))
        g.append(text(name, x0 + 22, y0 + 55, 17, T["ink"], "600"))
        g.append(math(tag, 13.5, T["ink2"], x0 + 22, y0 + 83))
        g.append(text(note, x0 + 22, y0 + 107, 11.5, T["ink3"]))
        return "".join(g)

    o.append(corner(
        AX0, AX1, AY0, "A", "PROVED", T["proved"], "· general compact G",
        "Asymptotic symmetry",
        [("A", ""), ("eff", "sub"), (" = G / N", ""), ("α", "sub"),
         ("    ·    [ω", ""), ("α", "sub"), ("] ∈ H", ""), ("2", "sup"),
         ("(H", ""), ("α", "sub"), (", U(1))", "")],
        "charges on the MPS manifold · kinks: double cosets"))

    o.append(corner(
        CX0, CX1, CY0, "C", "CONJECTURE", T["conj"], "· exact at n = 2",
        "Soft theorem",
        [("∂", ""), ("k", "sub"), ("s", "sub"), (" δ", ""), ("phys", "sub"),
         (" |", ""), ("0", "sub"), (" = sgn(v", ""), ("h", "sub"), (" − v", ""),
         ("s", "sub"), (") / S", "")],
        "empirically confirmed · proof under review"))

    o.append(corner(
        BX0, BX1, CY0, "B", "PROVED", T["proved"], "· conditional (D26, D27)",
        "Memory effect",
        [("δx = −(2s)", ""), ("−1", "sup"), (" Σ", ""), ("ν", "sub"), (" ν p", ""),
         ("ν", "sub"), ("    ·    ν ∈ Z", "")],
        "channel-free · needs no scattering input"))

    # ---- edge labels ----
    o.append(text("A ⇒ C", 272, 302, 13, T["ink"], "600", "end"))
    o.append(dot(282, 319, T["conj"], 4.2))
    o.append(two_tone(272, 323, 11, "CONJECTURE", "· ML1, ML3, ML6 open",
                      T["ink2"], T["ink3"], "end", 0.5))

    o.append(text("B ⇒ A", 628, 302, 13, T["ink"], "600", "start"))
    o.append(dot(618, 319, T["sketch"], 4.2))
    o.append(two_tone(628, 323, 11, "SKETCH", "· awaiting the moment map",
                      T["ink2"], T["ink3"], "start", 0.5))

    o.append(text("C ⇒ B", 450, 432, 13, T["ink"], "600", "middle"))
    o.append(dot(345, 449, T["sketch"], 4.2))
    o.append(two_tone(357, 453, 11, "SKETCH", "· blocked on lemma ACE-LD",
                      T["ink2"], T["ink3"], "start", 0.5))

    # ---- rule, legend, caption ----
    o.append('<line x1="30" y1="574" x2="870" y2="574" stroke="%s" stroke-width="1"/>'
             % T["hair2"])
    lx = 211
    for word, tail, col, adv in (("PROVED", "", T["proved"], 100),
                                 ("SKETCH", "— conditional or partial", T["sketch"], 248),
                                 ("CONJECTURE", "— open", T["conj"], 0)):
        o.append(dot(lx, 596, col, 4.2))
        o.append(two_tone(lx + 12, 600, 11, word, tail, T["ink2"], T["ink3"], "start", 0.5))
        lx += adv

    o.append(text("symmetry quantizes; the ansatz supplies the kinematics; "
                  "dynamics only picks the values.",
                  450, 630, 12.5, T["ink2"], "400", "middle", None, "italic"))
    o.append(text("statuses verbatim from claims/CLAIMS.md · edges from theory/TRIANGLE.md §6",
                  450, 652, 11, T["ink3"], "400", "middle"))

    o.append("</g></svg>")
    return "\n".join(o)


# ------------------------------------------------------------------ diagram 2
def loop(theme):
    T = THEMES[theme]
    W, H = 900, 506
    o = [header(W, H, "avl")]
    o.append('<title id="avl">The adversarial verification loop. Stage 1, target brief '
             'with a pre-registered falsifier and frozen red and green gates. Stage 2, '
             'two provers from different model families, sealed from each other. Stage 3, '
             'adversarial critics who recompute rather than referee. Stage 4, '
             'adjudication across lanes. Stage 5, the claims DAG ratchet. A dashed '
             'feedback arrow returns from adjudication to the provers for repair '
             'rounds.</title>')
    o.append("<defs>")
    o.append(arrowmarker("l-step", T["ink2"]))
    o.append(arrowmarker("l-back", T["ink3"]))
    o.append("</defs>")
    o.append('<g font-family="%s">' % FONT)

    o.append(text("The adversarial verification loop", 450, 36, 19, T["ink"], "600", "middle"))
    o.append(text("rk-light — a claim is PROVED only after an independent recomputation "
                  "fails to break it", 450, 58, 11.5, T["ink3"], "400", "middle"))

    stages = [
        ("1", "Target brief", ["pre-registered", "falsifier; red and", "green gates frozen"]),
        ("2", "Two provers", ["different model", "families, sealed", "from each other"]),
        ("3", "Adversarial critics", ["recompute, never", "referee prose;", "hunt counterexamples"]),
        ("4", "Adjudication", ["cross-lane compare;", "one binding verdict", "per round"]),
        ("5", "Claims DAG", ["four statuses,", "one-way ratchet:", "no silent upgrades"]),
    ]
    x0s = [31, 203, 375, 547, 719]
    CW, CY0, CH = 150, 86, 122
    for (num, name, subs), x0 in zip(stages, x0s):
        o.append(card(x0, CY0, CW, CH, T, 9))
        o.append('<circle cx="%s" cy="%s" r="9.5" fill="none" stroke="%s" '
                 'stroke-width="1"/>' % (x0 + 25, CY0 + 24, T["hair"]))
        o.append(text(num, x0 + 25, CY0 + 28, 11, T["ink2"], "700", "middle"))
        o.append(text(name, x0 + 16, CY0 + 57, 12.5, T["ink"], "600"))
        for i, s in enumerate(subs):
            o.append(text(s, x0 + 16, CY0 + 80 + 14.5 * i, 11, T["ink3"]))
    for x0 in x0s[:-1]:
        o.append('<line x1="%s" y1="147" x2="%s" y2="147" stroke="%s" stroke-width="2" '
                 'stroke-linecap="round" marker-end="url(#l-step)"/>'
                 % (x0 + CW + 4, x0 + CW + 19, T["ink2"]))

    o.append('<path d="M 622 208 V 230 Q 622 240 612 240 H 288 Q 278 240 278 230 V 214" '
             'fill="none" stroke="%s" stroke-width="2" stroke-dasharray="5 5" '
             'marker-end="url(#l-back)"/>' % T["ink3"])
    o.append(text("repair round — every objection is accepted or refuted, in writing",
                  450, 262, 11, T["ink3"], "400", "middle"))

    ev = [
        (31, "OBJECTION TRAJECTORY", "6 → 2 MAJOR",
         ["S2 lane, two hostile rounds · 0 FATAL;",
          "the r2 critic re-derived 14 of 15 repairs.",
          "The memory lane ran 6 → 3 → 1 → repaired."]),
        (319, "FALSIFIER, PRE-REGISTERED", "1.0217",
         ["the soft slope law at S = 1, measured",
          "out of sample (exact 1); the S = 1/2",
          "calibration gave 1.9929 against 2."]),
        (607, "CORPUS DAMAGE FOUND", "×3 recomputations",
         ["ML4-Ward (9), 2nd display: a PROVED row.",
          "Critics broke it for n ≥ 2. Rescoped,",
          "erratum added, audit opened."]),
    ]
    EY0, EW, EH = 292, 262, 124
    for x0, label, stat, lines in ev:
        o.append(card(x0, EY0, EW, EH, T, 9))
        o.append(text(label, x0 + 18, EY0 + 27, 11, T["ink3"], "600", "start", 1.0))
        o.append(text(stat, x0 + 18, EY0 + 58, 21, T["ink"], "700"))
        for i, s in enumerate(lines):
            o.append(text(s, x0 + 18, EY0 + 82 + 14.5 * i, 11, T["ink2"]))

    o.append('<line x1="30" y1="440" x2="870" y2="440" stroke="%s" stroke-width="1"/>'
             % T["hair2"])
    o.append(text("claims DAG statuses", 198, 466, 11, T["ink3"], "400", "start"))
    lx = 330
    for word, col, adv in (("PROVED", T["proved"], 92),
                           ("SKETCH", T["sketch"], 92),
                           ("CONJECTURE", T["conj"], 123),
                           ("REFUTED", T["refut"], 0)):
        o.append(dot(lx, 462, col, 4.2))
        o.append(text(word, lx + 12, 466, 11, T["ink2"], "600", "start", 0.5))
        lx += adv
    o.append(text("every number above is recorded in theory/verdicts/ and HANDOFF.md",
                  450, 490, 11, T["ink3"], "400", "middle"))

    o.append("</g></svg>")
    return "\n".join(o)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for th in ("light", "dark"):
        with open(os.path.join(OUT, "triangle-%s.svg" % th), "w") as f:
            f.write(triangle(th) + "\n")
        with open(os.path.join(OUT, "adversarial-loop-%s.svg" % th), "w") as f:
            f.write(loop(th) + "\n")
    print("wrote 4 files to", OUT)
