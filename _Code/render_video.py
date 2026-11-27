"""
High-Definition Video Rendering Engine (1080p Full HD)
Linear Algebra and Calculus (M3) - Educational Animation
Student: Ritesh Kumar | URN: e25b070681
Topic: Eigenvalues and Eigenvectors: The Invariant Directions of Space
Voice Narration: Ritesh Kumar (Original Hinglish Voice Recording)
Visual Enhancements: 3Blue1Brown Unit Circle to Ellipse Morphing, STIX Math Typesetting & Synced Subtitles
"""
import math
import os
import subprocess
import time
from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1920, 1080
FPS = 24

# Color Palette
BG_COLOR = (10, 14, 24)        # Deep obsidian slate
PANEL_BG = (19, 25, 41)        # Dark navy card
INNER_BG = (13, 19, 32)        # Deeper card container
BORDER_COLOR = (38, 48, 72)    # Subtle border
CYAN = (0, 210, 211)           # Electric Cyan (v1, lambda=3)
CYAN_DIM = (0, 150, 155)
GOLD = (255, 175, 25)          # Radiant Gold (v2, lambda=1)
GOLD_DIM = (185, 125, 10)
CORAL = (255, 82, 99)          # Vivid Coral (generic vector)
PURPLE = (162, 155, 254)       # Soft Purple (matrix space)
WHITE = (255, 255, 255)
LIGHT_GRAY = (226, 232, 240)
MUTED_GRAY = (148, 163, 184)
GRID_LINE = (26, 34, 50)
AXIS_COLOR = (74, 85, 104)

# Font Paths & Safe Fallback Loader
AVENIR_FONT = "/System/Library/Fonts/Avenir Next.ttc"
HELVETICA_FALLBACK = "/System/Library/Fonts/Helvetica.ttc"
STIX_MATH = "/System/Library/Fonts/Supplemental/STIXTwoMath.otf"
ARIAL_UNICODE_FALLBACK = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"
STIX_ITALIC = "/System/Library/Fonts/Supplemental/STIXTwoText-Italic.ttf"


def load_font(paths, size, index=0):
    """Loads the first available TrueType/OpenType font from fallback candidates."""
    for path in paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size, index=index)
            except OSError:
                return ImageFont.truetype(path, size)
    return ImageFont.load_default()


# Load System Typography Fonts
FONT_HERO = load_font([AVENIR_FONT, HELVETICA_FALLBACK], 60, index=0)       # Bold
FONT_TITLE = load_font([AVENIR_FONT, HELVETICA_FALLBACK], 38, index=0)      # Bold
FONT_SUBTITLE = load_font([AVENIR_FONT, HELVETICA_FALLBACK], 25, index=2)   # Demi Bold
FONT_BODY = load_font([AVENIR_FONT, HELVETICA_FALLBACK], 21, index=7)       # Regular
FONT_BODY_SM = load_font([AVENIR_FONT, HELVETICA_FALLBACK], 18, index=5)    # Medium
FONT_BADGE = load_font([AVENIR_FONT, HELVETICA_FALLBACK], 15, index=2)      # Demi Bold
FONT_LABEL = load_font([AVENIR_FONT, HELVETICA_FALLBACK], 17, index=5)      # Medium
FONT_ITALIC_SM = load_font([STIX_ITALIC, HELVETICA_FALLBACK], 24)

# Academic Math Typography Fonts (STIXTwoMath)
FONT_MATH_HERO = load_font([STIX_MATH, ARIAL_UNICODE_FALLBACK], 72)
FONT_MATH_TITLE = load_font([STIX_MATH, ARIAL_UNICODE_FALLBACK], 38)
FONT_MATH_LG = load_font([STIX_MATH, ARIAL_UNICODE_FALLBACK], 42)
FONT_MATH_MD = load_font([STIX_MATH, ARIAL_UNICODE_FALLBACK], 29)
FONT_MATH_MD_SUP = load_font([STIX_MATH, ARIAL_UNICODE_FALLBACK], 18)
FONT_MATH_SM = load_font([STIX_MATH, ARIAL_UNICODE_FALLBACK], 21)
FONT_MATH_BADGE = load_font([STIX_MATH, ARIAL_UNICODE_FALLBACK], 16)
FONT_MATH_SM_SUP = load_font([STIX_MATH, ARIAL_UNICODE_FALLBACK], 14)


DEFAULT_DURATIONS = {
    "scene1_hook": 39.082,
    "scene2_intro": 49.550,
    "scene3_visual": 80.079,
    "scene4_math": 74.411,
    "scene5_eigenbasis": 62.461,
    "scene6_summary": 28.186,
}


def read_durations():
    durations = dict(DEFAULT_DURATIONS)
    if os.path.exists("assets/audio/durations.txt"):
        with open("assets/audio/durations.txt") as f:
            for line in f:
                if ":" in line:
                    k, v = line.strip().split(":")
                    durations[k] = float(v)
    return durations


def draw_centered_text(draw, cx, y, text, font, fill):
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    draw.text((cx - tw / 2, y), text, font=font, fill=fill)


def draw_math_text(draw, xy, text, font, fill, sup_font=None):
    """Renders math text safely, converting unsupported Unicode transpose '\u1d40' into a raised 'T'."""
    x, y = xy
    if "\u1d40" not in text:
        draw.text((x, y), text, font=font, fill=fill)
        return
    if sup_font is None:
        sup_font = FONT_MATH_SM_SUP if font == FONT_MATH_SM else FONT_MATH_MD_SUP
    parts = text.split("\u1d40")
    curr_x = x
    for idx, part in enumerate(parts):
        if part:
            draw.text((curr_x, y), part, font=font, fill=fill)
            curr_x += draw.textlength(part, font=font)
        if idx < len(parts) - 1:
            draw.text((curr_x + 1, y - 4), "T", font=sup_font, fill=fill)
            curr_x += draw.textlength("T", font=sup_font) + 2


def draw_pill(draw, bbox, fill_rgba, outline_rgb, text, font, text_fill, radius=10, width=1):
    x0, y0, x1, y1 = bbox
    draw.rounded_rectangle(bbox, radius=radius, fill=fill_rgba, outline=outline_rgb, width=width)
    tb = draw.textbbox((0, 0), text, font=font)
    tw = tb[2] - tb[0]
    th = tb[3] - tb[1]
    tx = (x0 + x1) / 2 - tw / 2
    ty = (y0 + y1) / 2 - th / 2 - tb[1]
    draw.text((tx, ty), text, font=font, fill=text_fill)


def draw_status_heading(draw, x, y, is_ok, heading_text, font, color):
    """Draws a crisp vector check/cross icon badge followed by heading text."""
    r = 12
    cx, cy = x + r, y + 14
    if is_ok:
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 210, 211, 35), outline=color, width=2)
        draw.line([(cx - 5, cy), (cx - 1, cy + 5), (cx + 6, cy - 5)], fill=color, width=2)
    else:
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 82, 99, 35), outline=color, width=2)
        draw.line([(cx - 5, cy - 5), (cx + 5, cy + 5)], fill=color, width=2)
        draw.line([(cx - 5, cy + 5), (cx + 5, cy - 5)], fill=color, width=2)
    draw_math_text(draw, (x + 34, y), heading_text, font, color)


def draw_header_footer(draw, scene_idx, total_scenes, scene_title, t, total_t):
    # Top Bar
    draw.rectangle([0, 0, WIDTH, 64], fill=(15, 21, 35))
    draw.line([(0, 64), (WIDTH, 64)], fill=BORDER_COLOR, width=1)

    # Left Badge (proper RGBA glass tint)
    draw_pill(
        draw, [28, 14, 356, 50],
        fill_rgba=(0, 210, 211, 28), outline_rgb=CYAN,
        text="M3  •  LINEAR ALGEBRA & CALCULUS", font=FONT_BADGE, text_fill=CYAN, radius=8
    )

    # Center Topic
    draw_centered_text(draw, WIDTH / 2, 17, "EIGENVALUES & EIGENVECTORS", FONT_SUBTITLE, WHITE)

    # Right Attribution Pill (No URN on screen/header)
    draw_pill(
        draw, [WIDTH - 320, 14, WIDTH - 28, 50],
        fill_rgba=(255, 175, 25, 28), outline_rgb=GOLD,
        text="Presented by Ritesh Kumar", font=FONT_BADGE, text_fill=GOLD, radius=8
    )

    # Bottom Bar
    draw.rectangle([0, HEIGHT - 54, WIDTH, HEIGHT], fill=(15, 21, 35))
    draw.line([(0, HEIGHT - 54), (WIDTH, HEIGHT - 54)], fill=BORDER_COLOR, width=1)

    # Progress Bar
    draw.rectangle([0, HEIGHT - 6, WIDTH, HEIGHT], fill=(25, 33, 50))
    prog = min(1.0, max(0.0, t / max(0.001, total_t)))
    prog_w = int(WIDTH * prog)
    if prog_w > 0:
        draw.rectangle([0, HEIGHT - 6, prog_w, HEIGHT], fill=CYAN)

    draw.text((30, HEIGHT - 39), f"Scene {scene_idx} of {total_scenes}: {scene_title}", font=FONT_LABEL, fill=LIGHT_GRAY)
    time_txt = f"Time: {t:.1f}s / {total_t:.1f}s"
    tw = draw.textlength(time_txt, font=FONT_LABEL)
    draw.text((WIDTH - 30 - tw, HEIGHT - 39), time_txt, font=FONT_LABEL, fill=MUTED_GRAY)


def draw_vector(draw, p0, p1, color, width=4, label=None, label_color=WHITE, label_offset=(12, -14)):
    draw.line([p0, p1], fill=color, width=width)
    dx = p1[0] - p0[0]
    dy = p1[1] - p0[1]
    length = math.hypot(dx, dy)
    if length > 5:
        ux, uy = dx / length, dy / length
        arrow_len = 15
        arrow_width = 7.5
        px, py = p1[0], p1[1]
        p_left = (px - arrow_len * ux + arrow_width * uy, py - arrow_len * uy - arrow_width * ux)
        p_right = (px - arrow_len * ux - arrow_width * uy, py - arrow_len * uy + arrow_width * ux)
        draw.polygon([p1, p_left, p_right], fill=color)

    if label:
        lx = p1[0] + label_offset[0]
        ly = p1[1] + label_offset[1]
        draw_math_text(draw, (lx, ly), label, FONT_MATH_SM, label_color)


# ----------------- SCENE RENDERERS -----------------

def render_scene1_frame(t, total_t):
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img, "RGBA")
    draw_header_footer(draw, 1, 6, "Opening & The Hidden Stability of Space", t, total_t)

    if t < 7.2:
        pulse = 0.5 + 0.5 * math.sin(t * 2.6)
        border_col = (int(20 + pulse * 30), int(185 + pulse * 45), int(210 + pulse * 45), 220)
        draw.rounded_rectangle([150, 96, 1770, 992], radius=28, fill=PANEL_BG, outline=border_col, width=2)

        # Top Centered Concept Pill
        draw_pill(
            draw, [695, 126, 1225, 166],
            fill_rgba=(0, 210, 211, 28), outline_rgb=CYAN,
            text="LINEAR ALGEBRA  •  GEOMETRIC INTUITION", font=FONT_BADGE, text_fill=CYAN, radius=10
        )

        # Hero Title & Poetic Subtitle
        draw_centered_text(draw, 960, 188, "EIGENVALUES & EIGENVECTORS", FONT_HERO, WHITE)

        # Sleek tricolor accent divider bar
        draw.line([(680, 268), (870, 268)], fill=CYAN, width=3)
        draw.line([(876, 268), (1044, 268)], fill=GOLD, width=3)
        draw.line([(1050, 268), (1240, 268)], fill=PURPLE, width=3)

        draw_centered_text(
            draw, 960, 282,
            "The Invariant Axes & Hidden Architecture of Linear Transformations",
            FONT_SUBTITLE, LIGHT_GRAY
        )

        # ---- LEFT HERO SHOWCASE CARD: The Golden Equation ----
        draw.rounded_rectangle([205, 342, 955, 868], radius=20, fill=INNER_BG, outline=BORDER_COLOR, width=1)
        draw.text((242, 368), "THE INVARIANCE PRINCIPLE", font=FONT_BADGE, fill=CYAN)

        # Formula Glass Box
        draw.rounded_rectangle([240, 405, 920, 560], radius=16, fill=(10, 16, 28, 255), outline=(0, 210, 211, 95), width=2)

        # Draw color-coded "A v = λ v" centered in formula box
        segs = [
            ("A ", WHITE, FONT_MATH_HERO),
            ("v", CYAN, FONT_MATH_HERO),
            ("  =  ", LIGHT_GRAY, FONT_MATH_HERO),
            ("λ ", GOLD, FONT_MATH_HERO),
            ("v", CYAN, FONT_MATH_HERO),
            ("   (v ≠ 0)", MUTED_GRAY, FONT_MATH_MD),
        ]
        total_w = sum(draw.textlength(s, font=f) for s, _, f in segs)
        fx = 580 - total_w / 2
        for txt, col, fnt in segs:
            y_adj = 434 if fnt == FONT_MATH_HERO else 468
            draw.text((fx, y_adj), txt, font=fnt, fill=col)
            fx += draw.textlength(txt, font=fnt)

        # Conceptual Meaning
        draw.text((245, 586), "When a linear transformation stretches, shears, or rotates", font=FONT_BODY, fill=LIGHT_GRAY)
        draw.text((245, 617), "space, most vectors are knocked off their original span line.", font=FONT_BODY, fill=LIGHT_GRAY)
        draw.text((245, 648), "Eigenvectors preserve direction — scaling purely by λ.", font=FONT_BODY, fill=CYAN)

        # 3 Sleek Pillar Micro-Cards
        pillars = [
            ("v", "Invariant Axis", "0° rotation under A", CYAN),
            ("λ", "Eigenvalue", "Pure scale multiplier", GOLD),
            ("det(A−λI)=0", "Eigen-Spectrum", "Characteristic root", PURPLE),
        ]
        for idx, (sym, title, desc, col) in enumerate(pillars):
            px0 = 240 + idx * 232
            px1 = px0 + 216
            draw.rounded_rectangle([px0, 706, px1, 838], radius=14, fill=(19, 26, 43, 255), outline=(col[0], col[1], col[2], 110), width=1)
            draw.line([(px0 + 18, 707), (px1 - 18, 707)], fill=col, width=3)
            sym_font = FONT_MATH_MD if len(sym) <= 2 else FONT_MATH_SM
            sym_y = 720 if len(sym) <= 2 else 726
            draw.text((px0 + 16, sym_y), sym, font=sym_font, fill=col)
            draw.text((px0 + 16, 766), title, font=FONT_BODY_SM, fill=WHITE)
            draw.text((px0 + 16, 796), desc, font=FONT_BADGE, fill=MUTED_GRAY)

        # ---- RIGHT HERO SHOWCASE CARD: Live Animated Eigen-Field Preview ----
        draw.rounded_rectangle([985, 342, 1715, 868], radius=20, fill=INNER_BG, outline=BORDER_COLOR, width=1)
        draw.text((1022, 368), "LIVE GEOMETRIC EIGEN-FIELD", font=FONT_BADGE, fill=GOLD)
        draw_math_text(draw, (1475, 365), "A = [[2, 1], [1, 2]]", FONT_MATH_SM, MUTED_GRAY)

        # Coordinate viewport
        draw.rounded_rectangle([1018, 405, 1682, 838], radius=16, fill=(10, 15, 26, 255), outline=(38, 48, 72, 180), width=1)
        pcx, pcy = 1350, 616
        pscale = 60

        for k in range(-4, 5):
            gx = pcx + k * pscale
            draw.line([(gx, pcy - 3 * pscale), (gx, pcy + 3 * pscale)], fill=(25, 33, 50), width=1)
        for k in range(-3, 4):
            gy = pcy + k * pscale
            draw.line([(pcx - 4 * pscale, gy), (pcx + 4 * pscale, gy)], fill=(25, 33, 50), width=1)
        draw.line([(pcx - 4 * pscale, pcy), (pcx + 4 * pscale, pcy)], fill=AXIS_COLOR, width=2)
        draw.line([(pcx, pcy - 3 * pscale), (pcx, pcy + 3 * pscale)], fill=AXIS_COLOR, width=2)

        # Smooth breathing morph between Unit Circle (s=0) and Eigen-Ellipse (s=1)
        s = 0.5 - 0.5 * math.cos(t * 0.95)
        n_pts = 72
        for k in range(n_pts):
            th0 = 2 * math.pi * k / n_pts
            th1 = 2 * math.pi * (k + 1) / n_pts
            # Faint original circle
            draw.line([
                (pcx + math.cos(th0) * pscale, pcy - math.sin(th0) * pscale),
                (pcx + math.cos(th1) * pscale, pcy - math.sin(th1) * pscale)
            ], fill=(60, 74, 98, 130), width=1)
            # Morphing ellipse
            x0, y0 = math.cos(th0), math.sin(th0)
            x1, y1 = math.cos(th1), math.sin(th1)
            mx0 = (1 - s) * x0 + s * (2 * x0 + y0)
            my0 = (1 - s) * y0 + s * (x0 + 2 * y0)
            mx1 = (1 - s) * x1 + s * (2 * x1 + y1)
            my1 = (1 - s) * y1 + s * (x1 + 2 * y1)
            draw.line([
                (pcx + mx0 * pscale, pcy - my0 * pscale),
                (pcx + mx1 * pscale, pcy - my1 * pscale)
            ], fill=(0, 210, 211, 175), width=2)

        # Glowing invariant lines y = x (Cyan) and y = -x (Gold)
        draw.line([(pcx - 2.9 * pscale, pcy + 2.9 * pscale), (pcx + 2.9 * pscale, pcy - 2.9 * pscale)], fill=(0, 210, 211, 70), width=5)
        draw.line([(pcx - 2.9 * pscale, pcy - 2.9 * pscale), (pcx + 2.9 * pscale, pcy + 2.9 * pscale)], fill=(255, 175, 25, 70), width=5)

        # Generic vector morphing off-axis (Coral)
        gx_val = 1.0 + s * 1.0
        gy_val = 0.0 + s * 1.0
        draw_vector(draw, (pcx, pcy), (pcx + pscale, pcy), (130, 140, 160), width=2)
        draw_vector(draw, (pcx, pcy), (pcx + gx_val * pscale, pcy - gy_val * pscale), CORAL, width=3)

        # Invariant Eigenvectors v1 (Cyan) and v2 (Gold)
        v1_len = 0.85 + 1.45 * s
        draw_vector(draw, (pcx, pcy), (pcx + v1_len * pscale, pcy - v1_len * pscale), CYAN, width=5, label="v₁ (λ₁=3)", label_color=CYAN, label_offset=(10, -24))
        draw_vector(draw, (pcx, pcy), (pcx - 1.15 * pscale, pcy - 1.15 * pscale), GOLD, width=4, label="v₂ (λ₂=1)", label_color=GOLD, label_offset=(-96, -24))

        # Mini Legend at bottom of preview box
        draw.text((1045, 804), "— Invariant Major Axis (y=x)", font=FONT_BADGE, fill=CYAN)
        draw.text((1295, 804), "— Minor Axis (y=-x)", font=FONT_BADGE, fill=GOLD)
        draw.text((1490, 804), "— Generic Vector", font=FONT_BADGE, fill=CORAL)

        # ---- BOTTOM ATTRIBUTION BAR (Minimal & Premium, NO URN / Weight / Duration) ----
        draw.rounded_rectangle([205, 892, 1715, 960], radius=14, fill=(13, 19, 32, 230), outline=BORDER_COLOR, width=1)
        draw_centered_text(
            draw, 960, 913,
            "Presented by  Ritesh Kumar    •    Visual Intuition  |  Algebraic Proof  |  Diagonalization",
            FONT_SUBTITLE, GOLD
        )

    else:
        cx, cy = 520, 560
        scale = 75

        for k in range(-5, 6):
            x = cx + k * scale
            draw.line([(x, cy - 5 * scale), (x, cy + 5 * scale)], fill=GRID_LINE, width=1)
            y = cy + k * scale
            draw.line([(cx - 5 * scale, y), (cx + 5 * scale, y)], fill=GRID_LINE, width=1)
        draw.line([(cx - 5 * scale, cy), (cx + 5 * scale, cy)], fill=AXIS_COLOR, width=2)
        draw.line([(cx, cy - 5 * scale), (cx, cy + 5 * scale)], fill=AXIS_COLOR, width=2)

        t_phase = t - 7.2
        colors_list = [CORAL, CYAN, GOLD, PURPLE, (52, 152, 219), (230, 126, 34)]
        for i, col in enumerate(colors_list):
            base_angle = (i * math.pi / 3.0) + 0.8 * math.sin(t_phase * 1.5 + i)
            base_r = 2.2 + 0.8 * math.cos(t_phase * 1.2 + i * 2)
            vx = base_r * math.cos(base_angle)
            vy = base_r * math.sin(base_angle)
            px = cx + vx * scale
            py = cy - vy * scale
            draw_vector(draw, (cx, cy), (px, py), col, width=3)

        draw.text((cx - 210, cy + 5.25 * scale), "Generic vectors tumble & rotate chaotically", font=FONT_BODY_SM, fill=MUTED_GRAY)

        draw.rounded_rectangle([1020, 105, 1845, 965], radius=20, fill=PANEL_BG, outline=BORDER_COLOR, width=1)
        draw.text((1060, 136), "THE MOTIVATION", font=FONT_BADGE, fill=CYAN)
        draw.text((1060, 165), "Why Invariant Directions Matter", font=FONT_TITLE, fill=WHITE)

        apps = [
            ("1. Structural Resonance", "Bridges & structures have natural vibrational modes.\nThese resonant frequencies ω² are eigenvalues of [M]⁻¹[K].\nFinding them prevents catastrophic collapse (Tacoma Narrows).", CYAN),
            ("2. Google PageRank", "Google models the entire World Wide Web as a giant\nconnection matrix P. The importance of web pages is the\nstationary eigenvector satisfying P v = 1 v.", GOLD),
            ("3. Principal Component Analysis (PCA)", "Compresses 4K video, big data, and facial recognition.\nEigenvectors of the data covariance matrix identify the\naxes of maximum variance.", PURPLE)
        ]

        for i, (head, desc, col) in enumerate(apps):
            y0 = 248 + i * 204
            y1 = y0 + 180
            draw.rounded_rectangle([1060, y0, 1805, y1], radius=14, fill=INNER_BG, outline=col, width=1)
            draw.text((1090, y0 + 20), head, font=FONT_SUBTITLE, fill=col)
            draw_math_text(draw, (1090, y0 + 66), desc, FONT_MATH_SM, LIGHT_GRAY)

        draw_pill(
            draw, [1060, 872, 1805, 938],
            fill_rgba=(0, 210, 211, 25), outline_rgb=CYAN,
            text="◆ Core Question: In a storm of distortion, which directions stay invariant?",
            font=FONT_MATH_SM, text_fill=CYAN, radius=10
        )

    return img


def render_scene2_frame(t, total_t):
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img, "RGBA")
    draw_header_footer(draw, 2, 6, "Concept Introduction: The Golden Equation", t, total_t)

    draw.rounded_rectangle([200, 106, 1720, 390], radius=20, fill=PANEL_BG, outline=CYAN, width=2)
    draw_pill(
        draw, [780, 132, 1140, 172],
        fill_rgba=(0, 210, 211, 28), outline_rgb=CYAN,
        text="THE GOLDEN EQUATION", font=FONT_BADGE, text_fill=CYAN, radius=8
    )

    draw_centered_text(draw, 960, 198, "A v  =  λ v ,    where  v ≠ 0", FONT_MATH_HERO, WHITE)
    draw_centered_text(
        draw, 960, 310,
        "Matrix multiplication collapses into simple scalar scaling along direction v",
        FONT_SUBTITLE, LIGHT_GRAY
    )

    params = [
        ("Matrix A", "n × n Linear Transformation", CYAN),
        ("Eigenvector v", "Special non-zero direction in ℝⁿ", GOLD),
        ("Eigenvalue λ", "Pure scalar scaling multiplier ∈ ℝ", PURPLE)
    ]
    for i, (name, role, col) in enumerate(params):
        x0 = 200 + i * 520
        x1 = x0 + 480
        draw.rounded_rectangle([x0, 418, x1, 530], radius=14, fill=INNER_BG, outline=col, width=1)
        draw_math_text(draw, (x0 + 26, 438), name, FONT_SUBTITLE, col)
        draw_math_text(draw, (x0 + 26, 482), role, FONT_MATH_SM, LIGHT_GRAY)

    # Split Screen Comparison
    draw.rounded_rectangle([200, 560, 930, 962], radius=16, fill=PANEL_BG, outline=CORAL, width=1)
    draw_status_heading(draw, 232, 586, False, "Generic Vector x  (A x ≠ λ x)", FONT_SUBTITLE, CORAL)

    gcx, gcy = 565, 780
    gscale = 60
    draw.line([(gcx - 150, gcy), (gcx + 150, gcy)], fill=AXIS_COLOR, width=1)
    draw.line([(gcx, gcy - 150), (gcx, gcy + 150)], fill=AXIS_COLOR, width=1)
    draw_vector(draw, (gcx, gcy), (gcx + 1.8 * gscale, gcy), (180, 180, 180), width=3, label="x", label_color=MUTED_GRAY)
    draw_vector(draw, (gcx, gcy), (gcx + 1.8 * gscale, gcy - 1.2 * gscale), CORAL, width=4, label="A x", label_color=CORAL)
    draw_math_text(draw, (232, 902), "• Changes BOTH length and direction (Δθ ≠ 0°).", FONT_MATH_SM, LIGHT_GRAY)
    draw_math_text(draw, (232, 928), "• Vector is knocked off its original span line.", FONT_MATH_SM, MUTED_GRAY)

    draw.rounded_rectangle([990, 560, 1720, 962], radius=16, fill=PANEL_BG, outline=CYAN, width=1)
    draw_status_heading(draw, 1022, 586, True, "Eigenvector v  (A v = λ v)", FONT_SUBTITLE, CYAN)

    ecx, ecy = 1355, 780
    draw.line([(ecx - 150, ecy), (ecx + 150, ecy)], fill=AXIS_COLOR, width=1)
    draw.line([(ecx, ecy - 150), (ecx, ecy + 150)], fill=AXIS_COLOR, width=1)
    draw.line([(ecx - 140, ecy + 140), (ecx + 140, ecy - 140)], fill=(0, 210, 211, 90), width=2)
    draw_vector(draw, (ecx, ecy), (ecx + 0.8 * gscale, ecy - 0.8 * gscale), CYAN_DIM, width=3, label="v", label_color=LIGHT_GRAY)
    draw_vector(draw, (ecx, ecy), (ecx + 2.0 * gscale, ecy - 2.0 * gscale), CYAN, width=5, label="A v = λ v", label_color=CYAN)
    draw_math_text(draw, (1022, 902), "• Strictly preserves direction (Δθ = 0°).", FONT_MATH_SM, LIGHT_GRAY)
    draw_math_text(draw, (1022, 928), "• Undergoes pure scalar stretching or shrinking by λ.", FONT_MATH_SM, MUTED_GRAY)

    return img


def render_scene3_frame(t, total_t):
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img, "RGBA")
    draw_header_footer(draw, 3, 6, "Geometric Intuition: Invariant Lines & Ellipse", t, total_t)

    cx, cy = 530, 560
    scale = 75

    # Background Grid
    for k in range(-5, 6):
        x = cx + k * scale
        draw.line([(x, cy - 5 * scale), (x, cy + 5 * scale)], fill=GRID_LINE, width=1)
        y = cy + k * scale
        draw.line([(cx - 5 * scale, y), (cx + 5 * scale, y)], fill=GRID_LINE, width=1)
    draw.line([(cx - 5 * scale, cy), (cx + 5 * scale, cy)], fill=AXIS_COLOR, width=2)
    draw.line([(cx, cy - 5 * scale), (cx, cy + 5 * scale)], fill=AXIS_COLOR, width=2)

    # 3Blue1Brown Unit Circle
    n_pts = 72
    circ_pts = [
        (cx + math.cos(2 * math.pi * k / n_pts) * scale, cy - math.sin(2 * math.pi * k / n_pts) * scale)
        for k in range(n_pts + 1)
    ]
    for k in range(n_pts):
        draw.line([circ_pts[k], circ_pts[k + 1]], fill=(75, 90, 118), width=1)

    # Transformed Ellipse (synced to narration ~24.5s - 33.0s)
    s_morph = min(1.0, max(0.0, (t - 24.5) / 8.5))
    if s_morph > 0:
        ell_pts = []
        for k in range(n_pts + 1):
            th = 2 * math.pi * k / n_pts
            xb, yb = math.cos(th), math.sin(th)
            tx = (1 - s_morph) * xb + s_morph * (2 * xb + yb)
            ty = (1 - s_morph) * yb + s_morph * (xb + 2 * yb)
            ell_pts.append((cx + tx * scale, cy - ty * scale))
        for k in range(n_pts):
            draw.line([ell_pts[k], ell_pts[k + 1]], fill=(0, 210, 211, 160), width=2)

    # Invariant Line 1: y = x (Cyan) & Line 2: y = -x (Gold)
    draw.line([(cx - 4.5 * scale, cy + 4.5 * scale), (cx + 4.5 * scale, cy - 4.5 * scale)], fill=(0, 210, 211, 110), width=3)
    draw.text((cx + 2.6 * scale, cy - 4.15 * scale), "Line y = x (Major Axis)", font=FONT_LABEL, fill=CYAN)

    draw.line([(cx - 4.5 * scale, cy - 4.5 * scale), (cx + 4.5 * scale, cy + 4.5 * scale)], fill=(255, 175, 25, 110), width=3)
    draw.text((cx - 4.4 * scale, cy - 4.15 * scale), "Line y = -x (Minor Axis)", font=FONT_LABEL, fill=GOLD)

    draw_vector(draw, (cx, cy), (cx + 1 * scale, cy), (120, 128, 145), width=2, label="u=[1,0]ᵀ", label_color=MUTED_GRAY, label_offset=(8, 8))

    if t < 25.0:
        progress = min(1.0, (t - 11.0) / 10.0) if t >= 11.0 else 0.0
        ux = 1.0 + 1.0 * progress
        uy = 0.0 + 1.0 * progress
        draw_vector(draw, (cx, cy), (cx + ux * scale, cy - uy * scale), CORAL, width=5, label=f"A u = [{ux:.1f}, {uy:.1f}]ᵀ", label_color=CORAL, label_offset=(12, -20))

    elif t < 57.5:
        draw_vector(draw, (cx, cy), (cx + 2 * scale, cy - 1 * scale), (190, 60, 70), width=2, label="A u (tilts 26.6°)", label_color=MUTED_GRAY, label_offset=(12, -4))

        progress = min(1.0, (t - 32.0) / 15.0) if t >= 32.0 else 0.0
        v1_len = 1.0 + 2.0 * progress
        draw_vector(draw, (cx, cy), (cx + 1 * scale, cy - 1 * scale), CYAN_DIM, width=3, label="v₁=[1,1]ᵀ", label_color=LIGHT_GRAY, label_offset=(-95, -28))
        draw_vector(draw, (cx, cy), (cx + v1_len * scale, cy - v1_len * scale), CYAN, width=5, label=f"A v₁ = {v1_len:.1f} v₁ (λ₁=3)", label_color=CYAN, label_offset=(12, -24))

    else:
        draw_vector(draw, (cx, cy), (cx + 3 * scale, cy - 3 * scale), CYAN, width=5, label="A v₁ = 3 v₁  (λ₁ = 3)", label_color=CYAN, label_offset=(12, -22))
        draw_vector(draw, (cx, cy), (cx + 1 * scale, cy - 1 * scale), CYAN_DIM, width=2)
        draw_vector(draw, (cx, cy), (cx - 1 * scale, cy - 1 * scale), GOLD, width=5, label="A v₂ = 1 v₂  (λ₂ = 1)", label_color=GOLD, label_offset=(-210, -24))

    # Right Information Panel
    draw.rounded_rectangle([1050, 105, 1850, 965], radius=20, fill=PANEL_BG, outline=BORDER_COLOR, width=1)
    draw.text((1090, 132), "GEOMETRIC DISCOVERY", font=FONT_BADGE, fill=CYAN)
    draw.text((1090, 160), "Invariant Axes & Ellipse Deformation", font=FONT_TITLE, fill=WHITE)

    # 3Blue1Brown Insight Banner
    draw.rounded_rectangle([1090, 218, 1810, 312], radius=12, fill=(0, 210, 211, 24), outline=CYAN, width=1)
    draw.text((1114, 228), "•  3BLUE1BROWN GEOMETRIC INSIGHT", font=FONT_BADGE, fill=CYAN)
    draw_math_text(draw, (1114, 254), "The Unit Circle deforms into an Ellipse! Principal axes align", FONT_MATH_SM, WHITE)
    draw_math_text(draw, (1114, 280), "EXACTLY with eigenvectors, scaled by λ₁ = 3 and λ₂ = 1.", FONT_MATH_SM, CYAN)

    # Matrix Card
    draw.rounded_rectangle([1090, 330, 1810, 438], radius=14, fill=INNER_BG, outline=BORDER_COLOR, width=1)
    draw.text((1120, 344), "Transformation Matrix A:", font=FONT_LABEL, fill=MUTED_GRAY)
    draw.text((1120, 376), "A  =  [ [ 2 , 1 ] , [ 1 , 2 ] ]", font=FONT_MATH_LG, fill=WHITE)

    # Experiment 1 Card
    col_u = CORAL if t < 25.0 else BORDER_COLOR
    draw.rounded_rectangle([1090, 456, 1810, 578], radius=14, fill=INNER_BG, outline=col_u, width=1)
    draw.text((1120, 470), "1. GENERIC VECTOR (Coral):", font=FONT_BADGE, fill=CORAL)
    draw_math_text(draw, (1120, 500), "• Vector u = [1, 0]ᵀ  →  A u = [2, 1]ᵀ", FONT_MATH_MD, WHITE)
    draw.text((1120, 542), "• Tilts by 26.6° off course! (NOT an eigenvector)", font=FONT_BODY_SM, fill=MUTED_GRAY)

    # Experiment 2 Card
    col_v1 = CYAN if t >= 25.0 else BORDER_COLOR
    draw.rounded_rectangle([1090, 596, 1810, 718], radius=14, fill=INNER_BG, outline=col_v1, width=1)
    draw.text((1120, 610), "2. MAJOR AXIS / LINE y = x (Cyan):", font=FONT_BADGE, fill=CYAN)
    draw_math_text(draw, (1120, 640), "• Vector v₁ = [1, 1]ᵀ  →  A v₁ = [3, 3]ᵀ = 3 v₁", FONT_MATH_MD, WHITE)
    draw_math_text(draw, (1120, 682), "• Pure 3× stretch along y = x. Eigenvalue λ₁ = 3!", FONT_MATH_SM, CYAN)

    # Experiment 3 Card
    col_v2 = GOLD if t >= 57.5 else BORDER_COLOR
    draw.rounded_rectangle([1090, 736, 1810, 858], radius=14, fill=INNER_BG, outline=col_v2, width=1)
    draw.text((1120, 750), "3. MINOR AXIS / LINE y = -x (Gold):", font=FONT_BADGE, fill=GOLD)
    draw_math_text(draw, (1120, 780), "• Vector v₂ = [-1, 1]ᵀ  →  A v₂ = [-1, 1]ᵀ = 1 v₂", FONT_MATH_MD, WHITE)
    draw_math_text(draw, (1120, 822), "• Zero length or angle change! Eigenvalue λ₂ = 1.", FONT_MATH_SM, GOLD)

    draw_pill(
        draw, [1090, 878, 1810, 944],
        fill_rgba=(162, 155, 254, 24), outline_rgb=PURPLE,
        text="◆ Orthogonal Eigenbasis: v₁ ⊥ v₂ (dot product = 0). Space decouples!",
        font=FONT_MATH_SM, text_fill=PURPLE, radius=12
    )

    return img


def render_scene4_frame(t, total_t):
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img, "RGBA")
    draw_header_footer(draw, 4, 6, "Algebraic Derivation: Characteristic Polynomial", t, total_t)

    draw.rounded_rectangle([80, 106, 1140, 962], radius=20, fill=PANEL_BG, outline=BORDER_COLOR, width=1)
    draw.text((120, 134), "STEP-BY-STEP MATHEMATICAL PROOF", font=FONT_BADGE, fill=CYAN)
    draw.text((120, 164), "Solving (A − λ I) v = 0", font=FONT_TITLE, fill=WHITE)

    p1_active = t < 26.5
    draw.rounded_rectangle([120, 228, 1100, 380], radius=14, fill=INNER_BG, outline=(CYAN if p1_active else BORDER_COLOR), width=1)
    draw.text((144, 242), "STEP 1: THE NULLSPACE CONDITION", font=FONT_BADGE, fill=CYAN)
    draw_math_text(draw, (144, 274), "A v = λ v   ⟹   (A − λ I) v = 0", FONT_MATH_MD, WHITE)
    draw_math_text(draw, (144, 322), "For non-trivial solution (v ≠ 0), (A − λ I) must collapse space ⟹ det(A − λ I) = 0", FONT_MATH_SM, LIGHT_GRAY)

    p2_active = 26.5 <= t < 63.5
    draw.rounded_rectangle([120, 400, 1100, 582], radius=14, fill=INNER_BG, outline=(CYAN if p2_active else BORDER_COLOR), width=1)
    draw.text((144, 414), "STEP 2: THE CHARACTERISTIC POLYNOMIAL", font=FONT_BADGE, fill=CYAN)
    draw_math_text(draw, (144, 444), "det [ [ 2 − λ , 1 ] , [ 1 , 2 − λ ] ]  =  (2 − λ)² − 1  =  0", FONT_MATH_MD, WHITE)
    draw_math_text(draw, (144, 490), "λ² − 4λ + 4 − 1 = 0   ⟹   λ² − 4λ + 3 = 0", FONT_MATH_MD, LIGHT_GRAY)
    draw_math_text(draw, (144, 536), "Factoring: (λ − 3)(λ − 1) = 0   ⟹   λ₁ = 3 ,   λ₂ = 1", FONT_MATH_MD, GOLD)

    p3_active = 63.5 <= t < 69.0
    draw.rounded_rectangle([120, 602, 1100, 762], radius=14, fill=INNER_BG, outline=(CYAN if p3_active else BORDER_COLOR), width=1)
    draw.text((144, 616), "STEP 3: EIGENSPACE FOR λ₁ = 3", font=FONT_MATH_BADGE, fill=CYAN)
    draw_math_text(draw, (144, 646), "(A − 3 I) v = [ [ −1 , 1 ] , [ 1 , −1 ] ] [ x , y ]ᵀ = [ 0 , 0 ]ᵀ", FONT_MATH_SM, WHITE)
    draw_math_text(draw, (144, 684), "−x + y = 0   ⟹   y = x   ⟹   v₁ = [ 1 , 1 ]ᵀ", FONT_MATH_MD, CYAN)
    draw_math_text(draw, (144, 726), "Eigenspace E₃ = span{ [1, 1]ᵀ }  (45° diagonal line)", FONT_MATH_SM, MUTED_GRAY)

    p4_active = t >= 69.0
    draw.rounded_rectangle([120, 782, 1100, 942], radius=14, fill=INNER_BG, outline=(GOLD if p4_active else BORDER_COLOR), width=1)
    draw.text((144, 796), "STEP 4: EIGENSPACE FOR λ₂ = 1", font=FONT_MATH_BADGE, fill=GOLD)
    draw_math_text(draw, (144, 826), "(A − 1 I) v = [ [ 1 , 1 ] , [ 1 , 1 ] ] [ x , y ]ᵀ = [ 0 , 0 ]ᵀ", FONT_MATH_SM, WHITE)
    draw_math_text(draw, (144, 864), "x + y = 0   ⟹   y = −x   ⟹   v₂ = [ −1 , 1 ]ᵀ", FONT_MATH_MD, GOLD)
    draw_math_text(draw, (144, 906), "Eigenspace E₁ = span{ [−1, 1]ᵀ }  (135° anti-diagonal line)", FONT_MATH_SM, MUTED_GRAY)

    draw.rounded_rectangle([1180, 106, 1840, 962], radius=20, fill=PANEL_BG, outline=BORDER_COLOR, width=1)
    draw.text((1220, 134), "GEOMETRIC CONFIRMATION", font=FONT_BADGE, fill=GOLD)
    draw.text((1220, 164), "Calculated Eigenspaces", font=FONT_TITLE, fill=WHITE)

    rcx, rcy = 1510, 540
    rscale = 75
    for k in range(-4, 5):
        x = rcx + k * rscale
        draw.line([(x, rcy - 4 * rscale), (x, rcy + 4 * rscale)], fill=GRID_LINE, width=1)
        y = rcy + k * rscale
        draw.line([(rcx - 4 * rscale, y), (rcx + 4 * rscale, y)], fill=GRID_LINE, width=1)
    draw.line([(rcx - 4 * rscale, rcy), (rcx + 4 * rscale, rcy)], fill=AXIS_COLOR, width=2)
    draw.line([(rcx, rcy - 4 * rscale), (rcx, rcy + 4 * rscale)], fill=AXIS_COLOR, width=2)

    draw.line([(rcx - 3.5 * rscale, rcy + 3.5 * rscale), (rcx + 3.5 * rscale, rcy - 3.5 * rscale)], fill=(0, 210, 211, 110), width=3)
    draw.line([(rcx - 3.5 * rscale, rcy - 3.5 * rscale), (rcx + 3.5 * rscale, rcy + 3.5 * rscale)], fill=(255, 175, 25, 110), width=3)

    draw_vector(draw, (rcx, rcy), (rcx + 2 * rscale, rcy - 2 * rscale), CYAN, width=5, label="v₁ = [1, 1]ᵀ", label_color=CYAN, label_offset=(12, -22))
    draw_vector(draw, (rcx, rcy), (rcx - 2 * rscale, rcy - 2 * rscale), GOLD, width=5, label="v₂ = [−1, 1]ᵀ", label_color=GOLD, label_offset=(14, -22))

    draw_pill(
        draw, [1220, 868, 1800, 938],
        fill_rgba=(0, 210, 211, 25), outline_rgb=CYAN,
        text="✓ Algebra rigorously proves geometric intuition!",
        font=FONT_MATH_SM, text_fill=CYAN, radius=12
    )

    return img


def render_scene5_frame(t, total_t):
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img, "RGBA")
    draw_header_footer(draw, 5, 6, "Interpretation: Diagonalization & Matrix Powers", t, total_t)

    draw.rounded_rectangle([120, 106, 1800, 358], radius=20, fill=PANEL_BG, outline=PURPLE, width=2)
    draw_pill(
        draw, [790, 130, 1130, 170],
        fill_rgba=(162, 155, 254, 28), outline_rgb=PURPLE,
        text="THE POWER OF DIAGONALIZATION", font=FONT_BADGE, text_fill=PURPLE, radius=8
    )

    draw_centered_text(draw, 960, 198, "A  =  P  D  P⁻¹", FONT_MATH_HERO, WHITE)
    draw_centered_text(
        draw, 960, 302,
        "In the coordinate frame of the eigenvectors, matrix A becomes purely diagonal!",
        FONT_SUBTITLE, LIGHT_GRAY
    )

    mats = [
        ("Modal Matrix P", "P = [ v₁   v₂ ] = [ [ 1 , −1 ] , [ 1 , 1 ] ]", "Columns are eigenvectors", CYAN),
        ("Diagonal Matrix D", "D = [ [ λ₁ , 0 ] , [ 0 , λ₂ ] ] = [ [ 3 , 0 ] , [ 0 , 1 ] ]", "Diagonal entries are eigenvalues", GOLD)
    ]
    for i, (head, eq, sub, col) in enumerate(mats):
        x0 = 120 + i * 860
        x1 = x0 + 820
        draw.rounded_rectangle([x0, 386, x1, 528], radius=16, fill=INNER_BG, outline=col, width=1)
        draw.text((x0 + 26, 404), head, font=FONT_BADGE, fill=col)
        draw_math_text(draw, (x0 + 26, 440), eq, FONT_MATH_MD, WHITE)
        draw.text((x0 + 26, 488), sub, font=FONT_BODY_SM, fill=MUTED_GRAY)

    draw.rounded_rectangle([120, 558, 1800, 962], radius=18, fill=PANEL_BG, outline=BORDER_COLOR, width=1)
    draw.text((160, 586), "APPLICATION TO REPEATED TRANSFORMATIONS & DYNAMICAL SYSTEMS", font=FONT_BADGE, fill=CYAN)
    draw.text((160, 616), "Computing ", font=FONT_TITLE, fill=WHITE)
    cx_a = 160 + draw.textlength("Computing ", font=FONT_TITLE)
    draw.text((cx_a, 616), "A¹⁰⁰", font=FONT_MATH_TITLE, fill=CYAN)
    cx_inst = cx_a + draw.textlength("A¹⁰⁰", font=FONT_MATH_TITLE)
    draw.text((cx_inst, 616), " Instantly", font=FONT_TITLE, fill=WHITE)

    draw.rounded_rectangle([160, 678, 930, 932], radius=14, fill=INNER_BG, outline=CORAL, width=1)
    draw_status_heading(draw, 190, 704, False, "Standard Basis (Coupled)", FONT_SUBTITLE, CORAL)
    draw_math_text(draw, (190, 756), "A¹⁰⁰ = A × A × A × ... (100 times)", FONT_MATH_MD, WHITE)
    draw.text((190, 812), "• Requires 100 consecutive matrix multiplications.", font=FONT_BODY_SM, fill=LIGHT_GRAY)
    draw_math_text(draw, (190, 846), "• Massive computation, high algorithmic complexity O(100 n³).", FONT_MATH_SM, MUTED_GRAY)
    draw.text((190, 882), "• Cumulative numerical floating-point error.", font=FONT_BODY_SM, fill=MUTED_GRAY)

    draw.rounded_rectangle([990, 678, 1760, 932], radius=14, fill=INNER_BG, outline=CYAN, width=1)
    draw_status_heading(draw, 1020, 704, True, "Eigenbasis (Decoupled)", FONT_SUBTITLE, CYAN)
    draw_math_text(draw, (1020, 756), "A¹⁰⁰ = P D¹⁰⁰ P⁻¹ = P [ [ 3¹⁰⁰ , 0 ] , [ 0 , 1¹⁰⁰ ] ] P⁻¹", FONT_MATH_SM, WHITE)
    draw_math_text(draw, (1020, 810), "• 3¹⁰⁰ = 5.15 × 10⁴⁷ along v₁, and 1¹⁰⁰ = 1 along v₂.", FONT_MATH_SM, CYAN)
    draw.text((1020, 846), "• Instant evaluation with exact analytical precision!", font=FONT_BODY_SM, fill=LIGHT_GRAY)
    draw_math_text(draw, (1020, 882), "• Powers differential equations (ẋ = Ax) & Markov chains.", FONT_MATH_SM, MUTED_GRAY)

    return img


def render_scene6_frame(t, total_t):
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img, "RGBA")
    draw_header_footer(draw, 6, 6, "Summary & Closing Credits", t, total_t)

    if t < 21.9:
        draw.rounded_rectangle([160, 106, 1760, 962], radius=20, fill=PANEL_BG, outline=CYAN, width=1)
        draw.text((200, 136), "PROJECT SYNTHESIS", font=FONT_BADGE, fill=CYAN)
        draw.text((200, 166), "Three Core Pillars of Eigen-Theory", font=FONT_TITLE, fill=WHITE)

        takeaways = [
            ("1. GEOMETRIC INVARIANCE", "Eigenvectors are the invariant axes of a linear transformation that do not rotate.\nUnder matrix multiplication, they undergo pure scalar scaling: A v = λ v.", CYAN),
            ("2. ALGEBRAIC SINGULARITY", "Eigenvalues are found by setting det(A − λ I) = 0.\nThis represents the exact condition where the transformation collapses space into\na lower dimension, unlocking non-trivial eigenspaces.", GOLD),
            ("3. DECOUPLING COMPLEX DYNAMICS", "Diagonalization (A = P D P⁻¹) aligns the problem with the eigenbasis.\nThis converts intractable matrix powers, Markov chains, and systems of differential\nequations into independent, easily solvable scalar problems.", PURPLE)
        ]

        for i, (title, text, col) in enumerate(takeaways):
            y0 = 256 + i * 222
            y1 = y0 + 194
            draw.rounded_rectangle([200, y0, 1720, y1], radius=16, fill=INNER_BG, outline=col, width=1)
            draw.text((234, y0 + 24), title, font=FONT_SUBTITLE, fill=col)
            draw_math_text(draw, (234, y0 + 72), text, FONT_MATH_SM, LIGHT_GRAY)

    else:
        draw.rounded_rectangle([200, 108, 1720, 962], radius=26, fill=PANEL_BG, outline=GOLD, width=2)
        draw_pill(
            draw, [730, 146, 1190, 188],
            fill_rgba=(255, 175, 25, 28), outline_rgb=GOLD,
            text="SUMMARY  •  CLOSING CREDITS", font=FONT_BADGE, text_fill=GOLD, radius=10
        )

        draw_centered_text(draw, 960, 214, "EIGENVALUES & EIGENVECTORS", FONT_HERO, WHITE)
        draw_centered_text(draw, 960, 296, "Thank You for Watching  •  Linear Algebra & Calculus (M3)", FONT_SUBTITLE, LIGHT_GRAY)

        # Author & Topic Clean Bar (No weightage box)
        draw.rounded_rectangle([270, 368, 1650, 502], radius=16, fill=INNER_BG, outline=BORDER_COLOR, width=1)
        draw.text((320, 396), "CREATED & NARRATED BY:", font=FONT_BADGE, fill=MUTED_GRAY)
        draw.text((320, 428), "Ritesh Kumar", font=FONT_TITLE, fill=GOLD)

        draw.line([(920, 390), (920, 480)], fill=BORDER_COLOR, width=1)
        draw.text((970, 396), "CORE CONCEPT:", font=FONT_BADGE, fill=MUTED_GRAY)
        draw_math_text(draw, (970, 428), "Av = λv  |  Eigenbasis & Diagonalization", FONT_MATH_MD, CYAN)

        # Credits & Disclosure (subtle URN inside credits for rubric compliance)
        draw.rounded_rectangle([270, 532, 1650, 915], radius=16, fill=INNER_BG, outline=BORDER_COLOR, width=1)
        draw.text((320, 560), "CREDITS, SOURCES & DISCLOSURE", font=FONT_BADGE, fill=CYAN)

        credits = [
            ("Student Author & Narration", "Ritesh Kumar  (URN: e25b070681) — Original Hinglish Voice Recording"),
            ("Animation & Code Engine", "Custom Python 3 Engine (NumPy, SciPy, Pillow, STIX Math, FFmpeg)"),
            ("Background Music", "Original Ambient Harmonic Pad (Synthesized at 432 Hz, A-minor / D-minor)"),
            ("Interactive Web Simulator", "Live HTML5 Canvas Simulator included in index.html (GitHub Pages Ready)"),
            ("AI Assistance Disclosure", "Script structure, timing alignment & rendering workflow assisted by Google Antigravity")
        ]
        for i, (k, v) in enumerate(credits):
            y = 608 + i * 54
            draw.text((320, y), f"•  {k}:", font=FONT_BODY_SM, fill=MUTED_GRAY)
            draw.text((625, y), v, font=FONT_BODY_SM, fill=LIGHT_GRAY)

    return img


# ----------------- MAIN PIPELINE -----------------

def render_scene_video(scene_key, scene_renderer, duration, out_mp4):
    audio_path = f"assets/audio/{scene_key}.mp3"
    print(f"\n>>> Rendering {scene_key} (duration: {duration:.2f}s, frames: {int(duration * FPS)})...")
    t0 = time.time()

    audio_input = ["-i", audio_path] if os.path.exists(audio_path) else ["-f", "lavfi", "-i", "anullsrc=r=48000:cl=mono"]
    cmd = [
        "ffmpeg", "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{WIDTH}x{HEIGHT}",
        "-pix_fmt", "rgb24",
        "-r", str(FPS),
        "-i", "-",
        *audio_input,
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-crf", "19",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        out_mp4
    ]

    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    total_frames = int(duration * FPS)

    for frame_idx in range(total_frames):
        t_curr = frame_idx / FPS
        frame_img = scene_renderer(t_curr, duration)
        proc.stdin.write(frame_img.tobytes())

        if frame_idx % 240 == 0 or frame_idx == total_frames - 1:
            print(f"  Frame {frame_idx}/{total_frames} ({frame_idx / total_frames * 100:.1f}%)")

    proc.stdin.close()
    proc.wait()
    print(f"Finished {scene_key} in {time.time() - t0:.1f}s -> {out_mp4}")


def export_snapshots(scene_defs):
    os.makedirs("assets/snapshots", exist_ok=True)
    print("\n>>> Exporting visual snapshot thumbnails for Storyboard PDF...")
    for idx, (scene_key, renderer, dur) in enumerate(scene_defs, start=1):
        # For scene 1, capture the premium opening frame at 3.5s so storyboard shows the new title card,
        # OR capture mid_t for action scenes. Let's capture opening frame at 3.2s for scene1 preview + mid action!
        snap_t = 3.2 if idx == 1 else (dur * 0.55)
        frame_img = renderer(snap_t, dur)
        thumb = frame_img.resize((640, 360), Image.Resampling.LANCZOS)
        out_thumb = f"assets/snapshots/scene{idx}.png"
        thumb.save(out_thumb)
        print(f"  Saved snapshot: {out_thumb}")


def main():
    durations = read_durations()
    os.makedirs("assets/rendered_scenes", exist_ok=True)

    scene_defs = [
        ("scene1_hook", render_scene1_frame, durations["scene1_hook"]),
        ("scene2_intro", render_scene2_frame, durations["scene2_intro"]),
        ("scene3_visual", render_scene3_frame, durations["scene3_visual"]),
        ("scene4_math", render_scene4_frame, durations["scene4_math"]),
        ("scene5_eigenbasis", render_scene5_frame, durations["scene5_eigenbasis"]),
        ("scene6_summary", render_scene6_frame, durations["scene6_summary"])
    ]

    # 1. Export Snapshots
    export_snapshots(scene_defs)

    # 2. Render Scenes
    rendered_scene_files = []
    for scene_key, renderer, dur in scene_defs:
        scene_mp4 = f"assets/rendered_scenes/{scene_key}.mp4"
        render_scene_video(scene_key, renderer, dur, scene_mp4)
        rendered_scene_files.append(scene_mp4)

    # 3. Concatenate all 6 scenes
    print("\n>>> Concatenating all 6 scenes...")
    concat_list_path = "assets/rendered_scenes/concat_list.txt"
    with open(concat_list_path, "w") as f:
        for fpath in rendered_scene_files:
            abs_path = os.path.abspath(fpath)
            f.write(f"file '{abs_path}'\n")

    raw_merged_mp4 = "assets/rendered_scenes/merged_raw.mp4"
    subprocess.run([
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", concat_list_path,
        "-c", "copy",
        raw_merged_mp4
    ], check=True)

    # 4. Mix background music (if present) & embed subtitles
    print("\n>>> Finalizing MP4 & embedding subtitles...")
    bg_music_path = "assets/audio/background_music.mp3"
    final_output = "_Video.mp4"
    has_bgm = os.path.exists(bg_music_path)
    has_srt = os.path.exists("subtitles.srt")

    cmd_final = ["ffmpeg", "-y", "-i", raw_merged_mp4]
    if has_bgm:
        cmd_final += ["-i", bg_music_path]
    if has_srt:
        cmd_final += ["-i", "subtitles.srt"]

    if has_bgm:
        filter_complex = (
            "[0:a]volume=1.0[voice];"
            "[1:a]volume=0.10[bgm];"
            "[voice][bgm]amix=inputs=2:duration=first:dropout_transition=3[outa]"
        )
        cmd_final += ["-filter_complex", filter_complex, "-map", "0:v", "-map", "[outa]"]
        srt_idx = "2:s"
    else:
        cmd_final += ["-map", "0:v", "-map", "0:a"]
        srt_idx = "1:s"

    if has_srt:
        cmd_final += [
            "-map", srt_idx,
            "-c:v", "copy",
            "-c:a", "aac",
            "-b:a", "192k",
            "-c:s", "mov_text",
            "-metadata:s:s:0", "language=eng",
            "-metadata:s:s:0", "title=Synced Subtitles",
            final_output
        ]
    else:
        cmd_final += [
            "-c:v", "copy",
            "-c:a", "aac",
            "-b:a", "192k",
            final_output
        ]

    subprocess.run(cmd_final, check=True)

    res = subprocess.run(
        ["ffprobe", "-i", final_output, "-show_entries", "format=duration,size", "-v", "quiet", "-of", "csv=p=0"],
        capture_output=True, text=True, check=True
    )
    lines = res.stdout.strip().split("\n")
    print(f"\n==========================================")
    print(f"🎉 FINAL 1080p VIDEO WITH SUBTITLES & RITESH'S ORIGINAL VOICE COMPLETED!")
    print(f"Path: {os.path.abspath(final_output)}")
    print(f"Details: {lines}")
    print(f"==========================================")


if __name__ == "__main__":
    main()
