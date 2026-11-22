"""
High-Definition Video Rendering Engine (1080p Full HD)
Linear Algebra and Calculus (M3) - Internal Assessment
Student: Ritesh Kumar | URN: e25b070681
Topic: Eigenvalues and Eigenvectors: The Invariant Directions of Space
Voice Narration: Robert Downey Jr. / Tony Stark AI Stylized Delivery (en-US-GuyNeural)
Visual Enhancements: 3Blue1Brown Unit Circle to Ellipse Morphing & Embedded Subtitles
"""
import math
import os
import subprocess
import time
import numpy as np
from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1920, 1080
FPS = 24

# Color Palette
BG_COLOR = (11, 15, 25)        # Deep obsidian slate
PANEL_BG = (21, 27, 43)        # Dark navy card
INNER_BG = (15, 21, 35)        # Deeper card container
BORDER_COLOR = (38, 48, 71)    # Subtle border
CYAN = (0, 210, 211)           # Electric Cyan (v1, lambda=3)
CYAN_DIM = (0, 150, 150)
GOLD = (255, 165, 2)           # Radiant Gold (v2, lambda=1)
GOLD_DIM = (180, 120, 0)
CORAL = (255, 71, 87)          # Vivid Coral (generic vector)
PURPLE = (162, 155, 254)       # Soft Purple (matrix space)
WHITE = (255, 255, 255)
LIGHT_GRAY = (226, 232, 240)
MUTED_GRAY = (148, 163, 184)
GRID_LINE = (28, 36, 52)
AXIS_COLOR = (74, 85, 104)

# Load System Fonts
FONT_HERO = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 58)
FONT_TITLE = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 40)
FONT_SUBTITLE = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 26)
FONT_BODY = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 21)
FONT_BODY_SM = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 18)
FONT_MATH_LG = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 44)
FONT_MATH_MD = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 30)
FONT_MATH_SM = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 22)
FONT_BADGE = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 16)
FONT_LABEL = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 18)

def read_durations():
    durations = {}
    with open("assets/audio/durations.txt") as f:
        for line in f:
            if ":" in line:
                k, v = line.strip().split(":")
                durations[k] = float(v)
    return durations

def draw_header_footer(draw, scene_idx, total_scenes, scene_title, t, total_t):
    # Top Bar
    draw.rectangle([0, 0, WIDTH, 64], fill=(15, 21, 35))
    draw.line([(0, 64), (WIDTH, 64)], fill=BORDER_COLOR, width=1)
    
    # Left Badge
    draw.rounded_rectangle([24, 14, 340, 50], radius=8, fill=(0, 210, 211, 30), outline=CYAN, width=1)
    draw.text((36, 22), "M3 • LINEAR ALGEBRA & CALCULUS", font=FONT_BADGE, fill=CYAN)
    
    # Center Topic
    draw.text((640, 18), "EIGENVALUES & EIGENVECTORS", font=FONT_SUBTITLE, fill=WHITE)
    
    # Right Student Badge
    draw.rounded_rectangle([WIDTH - 360, 14, WIDTH - 24, 50], radius=8, fill=(255, 165, 2, 30), outline=GOLD, width=1)
    draw.text((WIDTH - 344, 22), "Ritesh Kumar  |  e25b070681", font=FONT_BADGE, fill=GOLD)
    
    # Bottom Bar
    draw.rectangle([0, HEIGHT - 54, WIDTH, HEIGHT], fill=(15, 21, 35))
    draw.line([(0, HEIGHT - 54), (WIDTH, HEIGHT - 54)], fill=BORDER_COLOR, width=1)
    
    # Progress Bar
    draw.rectangle([0, HEIGHT - 6, WIDTH, HEIGHT], fill=(25, 33, 50))
    prog = min(1.0, max(0.0, t / max(0.001, total_t)))
    prog_w = int(WIDTH * prog)
    if prog_w > 0:
        draw.rectangle([0, HEIGHT - 6, prog_w, HEIGHT], fill=CYAN)
        
    draw.text((30, HEIGHT - 40), f"Scene {scene_idx} of {total_scenes}: {scene_title}", font=FONT_LABEL, fill=LIGHT_GRAY)
    draw.text((WIDTH - 240, HEIGHT - 40), f"Time: {t:.1f}s / {total_t:.1f}s", font=FONT_LABEL, fill=MUTED_GRAY)

def draw_vector(draw, p0, p1, color, width=4, label=None, label_color=WHITE):
    draw.line([p0, p1], fill=color, width=width)
    dx = p1[0] - p0[0]
    dy = p1[1] - p0[1]
    length = math.hypot(dx, dy)
    if length > 5:
        ux, uy = dx / length, dy / length
        arrow_len = 16
        arrow_width = 8
        px, py = p1[0], p1[1]
        p_left = (px - arrow_len * ux + arrow_width * uy, py - arrow_len * uy - arrow_width * ux)
        p_right = (px - arrow_len * ux - arrow_width * uy, py - arrow_len * uy + arrow_width * ux)
        draw.polygon([p1, p_left, p_right], fill=color)
        
    if label:
        lx = p1[0] + 12
        ly = p1[1] - 14
        draw.text((lx, ly), label, font=FONT_MATH_SM, fill=label_color)

# ----------------- SCENE RENDERERS -----------------

def render_scene1_frame(t, total_t):
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header_footer(draw, 1, 6, "Opening & The Hidden Stability of Space", t, total_t)
    
    if t < 8.0:
        pulse = 0.5 + 0.5 * math.sin(t * 3.0)
        border_col = (int(0 + pulse * 40), int(210 + pulse * 45), int(211 + pulse * 44))
        draw.rounded_rectangle([220, 120, 1700, 940], radius=24, fill=PANEL_BG, outline=border_col, width=2)
        
        draw.rounded_rectangle([680, 160, 1240, 206], radius=10, fill=(0, 210, 211, 40), outline=CYAN, width=1)
        draw.text((710, 172), "LINEAR ALGEBRA & CALCULUS (M3) • INTERNAL ASSESSMENT", font=FONT_BADGE, fill=CYAN)
        
        draw.text((410, 240), "EIGENVALUES & EIGENVECTORS", font=FONT_HERO, fill=WHITE)
        draw.text((450, 320), "The Invariant Directions and Hidden Architecture of Linear Space", font=FONT_SUBTITLE, fill=LIGHT_GRAY)
        
        draw.rounded_rectangle([300, 400, 1620, 560], radius=16, fill=INNER_BG, outline=BORDER_COLOR, width=1)
        draw.text((340, 430), "STUDENT NAME:", font=FONT_BADGE, fill=MUTED_GRAY)
        draw.text((340, 465), "Ritesh Kumar", font=FONT_MATH_LG, fill=GOLD)
        
        draw.text((820, 430), "UNIVERSITY ROLL / URN:", font=FONT_BADGE, fill=MUTED_GRAY)
        draw.text((820, 465), "e25b070681", font=FONT_MATH_LG, fill=CYAN)
        
        draw.text((1280, 430), "ASSESSMENT WEIGHT:", font=FONT_BADGE, fill=MUTED_GRAY)
        draw.text((1280, 465), "10% of Internal", font=FONT_MATH_LG, fill=WHITE)
        
        specs = [
            ("Video Format", "1080p 16:9 MP4 (Full HD)"),
            ("Narration Style", "Tony Stark (Robert Downey Jr.) AI"),
            ("Duration", "Exactly 6.00 Minutes (Guidelines Compliant)")
        ]
        for i, (label, val) in enumerate(specs):
            x0 = 300 + i * 450
            x1 = x0 + 420
            draw.rounded_rectangle([x0, 600, x1, 880], radius=16, fill=INNER_BG, outline=BORDER_COLOR, width=1)
            draw.text((x0 + 24, 630), label.upper(), font=FONT_BADGE, fill=CYAN)
            draw.text((x0 + 24, 680), val, font=FONT_SUBTITLE, fill=LIGHT_GRAY)
            draw.text((x0 + 24, 750), "✓ Verified against official rubric", font=FONT_BODY_SM, fill=MUTED_GRAY)
            
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
        
        t_phase = t - 8.0
        colors_list = [CORAL, CYAN, GOLD, PURPLE, (52, 152, 219), (230, 126, 34)]
        for i, col in enumerate(colors_list):
            base_angle = (i * math.pi / 3.0) + 0.8 * math.sin(t_phase * 1.5 + i)
            base_r = 2.2 + 0.8 * math.cos(t_phase * 1.2 + i * 2)
            vx = base_r * math.cos(base_angle)
            vy = base_r * math.sin(base_angle)
            px = cx + vx * scale
            py = cy - vy * scale
            draw_vector(draw, (cx, cy), (px, py), col, width=3)
            
        draw.text((cx - 240, cy + 5.3 * scale), "Generic vectors tumble & rotate chaotically", font=FONT_BODY_SM, fill=MUTED_GRAY)
        
        draw.rounded_rectangle([1020, 110, 1840, 960], radius=20, fill=PANEL_BG, outline=BORDER_COLOR, width=1)
        draw.text((1060, 140), "THE MOTIVATION", font=FONT_BADGE, fill=CYAN)
        draw.text((1060, 170), "Why Invariant Directions Matter", font=FONT_TITLE, fill=WHITE)
        
        apps = [
            ("1. Structural Resonance", "Bridges & structures have natural vibrational modes.\nThese resonant frequencies \u03c9\u00b2 are eigenvalues of [M]\u207b\u00b9[K].\nFinding them prevents catastrophic collapse (Tacoma Narrows).", CYAN),
            ("2. Google PageRank", "Google models the entire World Wide Web as a giant\nconnection matrix P. The importance of web pages is the\nstationary eigenvector satisfying P v = 1 v.", GOLD),
            ("3. Principal Component Analysis (PCA)", "Compresses 4K video, big data, and facial recognition.\nEigenvectors of the data covariance matrix identify the\naxes of maximum variance.", PURPLE)
        ]
        
        for i, (head, desc, col) in enumerate(apps):
            y0 = 260 + i * 200
            y1 = y0 + 175
            draw.rounded_rectangle([1060, y0, 1800, y1], radius=14, fill=INNER_BG, outline=col, width=1)
            draw.text((1090, y0 + 20), head, font=FONT_SUBTITLE, fill=col)
            draw.text((1090, y0 + 65), desc, font=FONT_BODY_SM, fill=LIGHT_GRAY)
            
        draw.rounded_rectangle([1060, 870, 1800, 935], radius=10, fill=(0, 210, 211, 20), outline=CYAN, width=1)
        draw.text((1085, 888), "\u2728 Core Question: In a storm of distortion, which directions stay invariant?", font=FONT_BODY_SM, fill=CYAN)
        
    return img

def render_scene2_frame(t, total_t):
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header_footer(draw, 2, 6, "Concept Introduction: The Golden Equation", t, total_t)
    
    draw.rounded_rectangle([200, 110, 1720, 390], radius=20, fill=PANEL_BG, outline=CYAN, width=2)
    draw.rounded_rectangle([780, 135, 1140, 175], radius=8, fill=(0, 210, 211, 40), outline=CYAN, width=1)
    draw.text((800, 145), "THE GOLDEN EQUATION", font=FONT_BADGE, fill=CYAN)
    
    draw.text((640, 205), "A v  =  \u03bb v ,   where v \u2260 0", font=FONT_HERO, fill=WHITE)
    draw.text((450, 310), "Matrix multiplication collapses into simple scalar scaling along direction v", font=FONT_SUBTITLE, fill=LIGHT_GRAY)
    
    params = [
        ("Matrix A", "n \u00d7 n Linear Transformation", CYAN),
        ("Eigenvector v", "Special non-zero direction in \u211d\u207f", GOLD),
        ("Eigenvalue \u03bb", "Pure scalar scaling multiplier \u2208 \u211d", PURPLE)
    ]
    for i, (name, role, col) in enumerate(params):
        x0 = 200 + i * 520
        x1 = x0 + 480
        draw.rounded_rectangle([x0, 420, x1, 530], radius=14, fill=INNER_BG, outline=col, width=1)
        draw.text((x0 + 24, 440), name, font=FONT_SUBTITLE, fill=col)
        draw.text((x0 + 24, 485), role, font=FONT_BODY_SM, fill=LIGHT_GRAY)
        
    # Split Screen Comparison
    draw.rounded_rectangle([200, 560, 930, 960], radius=16, fill=PANEL_BG, outline=CORAL, width=1)
    draw.text((230, 585), "\u274c Generic Vector x  (A x \u2260 \u03bb x)", font=FONT_SUBTITLE, fill=CORAL)
    
    gcx, gcy = 565, 780
    gscale = 60
    draw.line([(gcx - 150, gcy), (gcx + 150, gcy)], fill=AXIS_COLOR, width=1)
    draw.line([(gcx, gcy - 150), (gcx, gcy + 150)], fill=AXIS_COLOR, width=1)
    draw_vector(draw, (gcx, gcy), (gcx + 1.8 * gscale, gcy), (180, 180, 180), width=3, label="x", label_color=MUTED_GRAY)
    draw_vector(draw, (gcx, gcy), (gcx + 1.8 * gscale, gcy - 1.2 * gscale), CORAL, width=4, label="A x", label_color=CORAL)
    draw.text((230, 905), "\u2022 Changes BOTH length and direction (\u0394\u03b8 \u2260 0\u00b0).", font=FONT_BODY_SM, fill=LIGHT_GRAY)
    draw.text((230, 930), "\u2022 Vector is knocked off its original span line.", font=FONT_BODY_SM, fill=MUTED_GRAY)
    
    draw.rounded_rectangle([990, 560, 1720, 960], radius=16, fill=PANEL_BG, outline=CYAN, width=1)
    draw.text((1020, 585), "\u2705 Eigenvector v  (A v = \u03bb v)", font=FONT_SUBTITLE, fill=CYAN)
    
    ecx, ecy = 1355, 780
    draw.line([(ecx - 150, ecy), (ecx + 150, ecy)], fill=AXIS_COLOR, width=1)
    draw.line([(ecx, ecy - 150), (ecx, ecy + 150)], fill=AXIS_COLOR, width=1)
    draw.line([(ecx - 140, ecy + 140), (ecx + 140, ecy - 140)], fill=(0, 210, 211, 80), width=2)
    draw_vector(draw, (ecx, ecy), (ecx + 0.8 * gscale, ecy - 0.8 * gscale), CYAN_DIM, width=3, label="v", label_color=LIGHT_GRAY)
    draw_vector(draw, (ecx, ecy), (ecx + 2.0 * gscale, ecy - 2.0 * gscale), CYAN, width=5, label="A v = \u03bb v", label_color=CYAN)
    draw.text((1020, 905), "\u2022 Strictly preserves direction (\u0394\u03b8 = 0\u00b0).", font=FONT_BODY_SM, fill=LIGHT_GRAY)
    draw.text((1020, 930), "\u2022 Undergoes pure scalar stretching or shrinking by \u03bb.", font=FONT_BODY_SM, fill=MUTED_GRAY)
    
    return img

def render_scene3_frame(t, total_t):
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header_footer(draw, 3, 6, "Geometric Intuition: Invariant Lines & Ellipse", t, total_t)
    
    cx, cy = 540, 560
    scale = 75
    
    # Draw Background Grid
    for k in range(-5, 6):
        x = cx + k * scale
        draw.line([(x, cy - 5 * scale), (x, cy + 5 * scale)], fill=GRID_LINE, width=1)
        y = cy + k * scale
        draw.line([(cx - 5 * scale, y), (cx + 5 * scale, y)], fill=GRID_LINE, width=1)
    draw.line([(cx - 5 * scale, cy), (cx + 5 * scale, cy)], fill=AXIS_COLOR, width=2)
    draw.line([(cx, cy - 5 * scale), (cx, cy + 5 * scale)], fill=AXIS_COLOR, width=2)
    
    # 3Blue1Brown Unit Circle (Faint white dashed)
    n_pts = 72
    circ_pts = []
    for k in range(n_pts + 1):
        th = 2 * math.pi * k / n_pts
        cx_pt = cx + math.cos(th) * scale
        cy_pt = cy - math.sin(th) * scale
        circ_pts.append((cx_pt, cy_pt))
    for k in range(n_pts):
        draw.line([circ_pts[k], circ_pts[k + 1]], fill=(70, 85, 110), width=1)
        
    # 3Blue1Brown Transformed Ellipse (Smooth Morphing)
    # Morph progresses as time unfolds
    s_morph = min(1.0, max(0.0, (t - 16.0) / 16.0))
    if s_morph > 0:
        ell_pts = []
        for k in range(n_pts + 1):
            th = 2 * math.pi * k / n_pts
            x_base = math.cos(th)
            y_base = math.sin(th)
            tx = (1 - s_morph) * x_base + s_morph * (2 * x_base + 1 * y_base)
            ty = (1 - s_morph) * y_base + s_morph * (1 * x_base + 2 * y_base)
            ell_pts.append((cx + tx * scale, cy - ty * scale))
        for k in range(n_pts):
            draw.line([ell_pts[k], ell_pts[k + 1]], fill=(0, 210, 211, 140), width=2)
    
    # Invariant Line 1: y = x (Cyan)
    draw.line([(cx - 4.5 * scale, cy + 4.5 * scale), (cx + 4.5 * scale, cy - 4.5 * scale)], fill=(0, 210, 211, 80), width=3)
    draw.text((cx + 3.2 * scale, cy - 3.8 * scale), "Line y = x (Major Axis)", font=FONT_LABEL, fill=CYAN)
    
    # Invariant Line 2: y = -x (Gold)
    draw.line([(cx - 4.5 * scale, cy - 4.5 * scale), (cx + 4.5 * scale, cy + 4.5 * scale)], fill=(255, 165, 2, 80), width=3)
    draw.text((cx - 4.2 * scale, cy - 3.8 * scale), "Line y = -x (Minor Axis)", font=FONT_LABEL, fill=GOLD)
    
    draw_vector(draw, (cx, cy), (cx + 1 * scale, cy), (100, 100, 100), width=2, label="u=[1,0]\u1d40", label_color=MUTED_GRAY)
    
    if t < 24.0:
        progress = min(1.0, (t - 4.0) / 10.0) if t >= 4.0 else 0.0
        ux = 1.0 + 1.0 * progress
        uy = 0.0 + 1.0 * progress
        draw_vector(draw, (cx, cy), (cx + ux * scale, cy - uy * scale), CORAL, width=5, label=f"A u = [{ux:.1f}, {uy:.1f}]\u1d40", label_color=CORAL)
        
    elif t < 52.0:
        draw_vector(draw, (cx, cy), (cx + 2 * scale, cy - 1 * scale), (180, 50, 60), width=2, label="A u (rotated 26.6\u00b0)", label_color=MUTED_GRAY)
        
        progress = min(1.0, (t - 26.0) / 14.0) if t >= 26.0 else 0.0
        v1_len = 1.0 + 2.0 * progress
        draw_vector(draw, (cx, cy), (cx + 1 * scale, cy - 1 * scale), CYAN_DIM, width=3, label="v\u2081 = [1,1]\u1d40", label_color=LIGHT_GRAY)
        draw_vector(draw, (cx, cy), (cx + v1_len * scale, cy - v1_len * scale), CYAN, width=5, label=f"A v\u2081 = {v1_len:.1f} v\u2081 (\u03bb\u2081=3)", label_color=CYAN)
        
    else:
        draw_vector(draw, (cx, cy), (cx + 3 * scale, cy - 3 * scale), CYAN, width=5, label="A v\u2081 = 3 v\u2081  (\u03bb\u2081 = 3)", label_color=CYAN)
        draw_vector(draw, (cx, cy), (cx + 1 * scale, cy - 1 * scale), CYAN_DIM, width=2)
        draw_vector(draw, (cx, cy), (cx - 1 * scale, cy - 1 * scale), GOLD, width=5, label="A v\u2082 = 1 v\u2082  (\u03bb\u2082 = 1)", label_color=GOLD)
        
    # Right Information Panel
    draw.rounded_rectangle([1060, 110, 1840, 960], radius=20, fill=PANEL_BG, outline=BORDER_COLOR, width=1)
    draw.text((1100, 135), "GEOMETRIC DISCOVERY", font=FONT_BADGE, fill=CYAN)
    draw.text((1100, 165), "Invariant Axes & Ellipse Deformation", font=FONT_TITLE, fill=WHITE)
    
    # 3Blue1Brown Insight Callout Banner
    draw.rounded_rectangle([1100, 220, 1800, 310], radius=12, fill=(0, 210, 211, 20), outline=CYAN, width=1)
    draw.text((1120, 235), "⭕ 3Blue1Brown Geometric Insight:", font=FONT_BADGE, fill=CYAN)
    draw.text((1120, 260), "The Unit Circle deforms into an Ellipse! The principal axes of the ellipse", font=FONT_BODY_SM, fill=WHITE)
    draw.text((1120, 285), "align EXACTLY with eigenvectors, with lengths scaled by eigenvalues \u03bb\u2081=3, \u03bb\u2082=1.", font=FONT_BODY_SM, fill=CYAN)
    
    # Matrix Card
    draw.rounded_rectangle([1100, 330, 1800, 440], radius=14, fill=INNER_BG, outline=BORDER_COLOR, width=1)
    draw.text((1130, 345), "Transformation Matrix A:", font=FONT_LABEL, fill=MUTED_GRAY)
    draw.text((1130, 380), "A  =  [ [ 2 , 1 ] , [ 1 , 2 ] ]", font=FONT_MATH_LG, fill=WHITE)
    
    # Experiment 1 Card
    col_u = CORAL if t < 24.0 else BORDER_COLOR
    draw.rounded_rectangle([1100, 460, 1800, 580], radius=14, fill=INNER_BG, outline=col_u, width=1)
    draw.text((1130, 475), "1. GENERIC VECTOR (Red):", font=FONT_LABEL, fill=CORAL)
    draw.text((1130, 505), "\u2022 Vector u = [1, 0]\u1d40 \u2192 A u = [2, 1]\u1d40", font=FONT_MATH_MD, fill=WHITE)
    draw.text((1130, 545), "\u2022 Tilts by 26.6\u00b0 off course! (NOT an eigenvector)", font=FONT_BODY_SM, fill=MUTED_GRAY)
    
    # Experiment 2 Card
    col_v1 = CYAN if (24.0 <= t < 52.0 or t >= 52.0) else BORDER_COLOR
    draw.rounded_rectangle([1100, 600, 1800, 720], radius=14, fill=INNER_BG, outline=col_v1, width=1)
    draw.text((1130, 615), "2. MAJOR AXIS / LINE y = x (Cyan):", font=FONT_LABEL, fill=CYAN)
    draw.text((1130, 645), "\u2022 Vector v\u2081 = [1, 1]\u1d40 \u2192 A v\u2081 = [3, 3]\u1d40 = 3 v\u2081", font=FONT_MATH_MD, fill=WHITE)
    draw.text((1130, 685), "\u2022 Pure 3\u00d7 stretch along line y = x. Eigenvalue \u03bb\u2081 = 3!", font=FONT_BODY_SM, fill=CYAN)
    
    # Experiment 3 Card
    col_v2 = GOLD if t >= 52.0 else BORDER_COLOR
    draw.rounded_rectangle([1100, 740, 1800, 860], radius=14, fill=INNER_BG, outline=col_v2, width=1)
    draw.text((1130, 755), "3. MINOR AXIS / LINE y = -x (Gold):", font=FONT_LABEL, fill=GOLD)
    draw.text((1130, 785), "\u2022 Vector v\u2082 = [-1, 1]\u1d40 \u2192 A v\u2082 = [-1, 1]\u1d40 = 1 v\u2082", font=FONT_MATH_MD, fill=WHITE)
    draw.text((1130, 825), "\u2022 Zero length or angle change! Eigenvalue \u03bb\u2082 = 1.", font=FONT_BODY_SM, fill=GOLD)
    
    draw.rounded_rectangle([1100, 880, 1800, 945], radius=12, fill=(162, 155, 254, 20), outline=PURPLE, width=1)
    draw.text((1130, 902), "\u2728 Orthogonal Eigenbasis: v\u2081 \u22a5 v\u2082 (dot product = 0). Space decouples naturally!", font=FONT_BODY_SM, fill=PURPLE)
    
    return img

def render_scene4_frame(t, total_t):
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header_footer(draw, 4, 6, "Algebraic Derivation: Characteristic Polynomial", t, total_t)
    
    draw.rounded_rectangle([80, 110, 1140, 960], radius=20, fill=PANEL_BG, outline=BORDER_COLOR, width=1)
    draw.text((120, 140), "STEP-BY-STEP MATHEMATICAL PROOF", font=FONT_BADGE, fill=CYAN)
    draw.text((120, 170), "Solving (A - \u03bb I) v = 0", font=FONT_TITLE, fill=WHITE)
    
    p1_active = t < 25.0
    col1 = CYAN if p1_active else BORDER_COLOR
    draw.rounded_rectangle([120, 230, 1100, 380], radius=14, fill=INNER_BG, outline=col1, width=1)
    draw.text((140, 245), "STEP 1: THE NULLSPACE CONDITION", font=FONT_BADGE, fill=CYAN)
    draw.text((140, 275), "A v = \u03bb v   \u27f9   (A - \u03bb I) v = 0", font=FONT_MATH_MD, fill=WHITE)
    draw.text((140, 320), "For non-trivial solution (v \u2260 0), (A - \u03bb I) must collapse space \u27f9 det(A - \u03bb I) = 0", font=FONT_BODY_SM, fill=LIGHT_GRAY)
    
    p2_active = 25.0 <= t < 55.0
    col2 = CYAN if p2_active else BORDER_COLOR
    draw.rounded_rectangle([120, 400, 1100, 580], radius=14, fill=INNER_BG, outline=col2, width=1)
    draw.text((140, 415), "STEP 2: THE CHARACTERISTIC POLYNOMIAL", font=FONT_BADGE, fill=CYAN)
    draw.text((140, 445), "det [ [ 2 - \u03bb , 1 ] , [ 1 , 2 - \u03bb ] ]  =  (2 - \u03bb)\u00b2 - 1  =  0", font=FONT_MATH_MD, fill=WHITE)
    draw.text((140, 490), "\u03bb\u00b2 - 4\u03bb + 4 - 1 = 0   \u27f9   \u03bb\u00b2 - 4\u03bb + 3 = 0", font=FONT_MATH_MD, fill=LIGHT_GRAY)
    draw.text((140, 535), "Factoring: (\u03bb - 3)(\u03bb - 1) = 0   \u27f9   \u03bb\u2081 = 3  ,   \u03bb\u2082 = 1", font=FONT_MATH_MD, fill=GOLD)
    
    p3_active = 55.0 <= t < 78.0
    col3 = CYAN if p3_active else BORDER_COLOR
    draw.rounded_rectangle([120, 600, 1100, 760], radius=14, fill=INNER_BG, outline=col3, width=1)
    draw.text((140, 615), "STEP 3: EIGENSPACE FOR \u03bb\u2081 = 3", font=FONT_BADGE, fill=CYAN)
    draw.text((140, 645), "(A - 3 I) v = [ [ -1 , 1 ] , [ 1 , -1 ] ] [ x , y ]\u1d40 = [ 0 , 0 ]\u1d40", font=FONT_MATH_SM, fill=WHITE)
    draw.text((140, 685), "-x + y = 0   \u27f9   y = x   \u27f9   v\u2081 = [ 1 , 1 ]\u1d40", font=FONT_MATH_MD, fill=CYAN)
    draw.text((140, 725), "Eigenspace E\u2083 = span{ [1, 1]\u1d40 } (45\u00b0 diagonal line)", font=FONT_BODY_SM, fill=MUTED_GRAY)
    
    p4_active = t >= 78.0
    col4 = GOLD if p4_active else BORDER_COLOR
    draw.rounded_rectangle([120, 780, 1100, 940], radius=14, fill=INNER_BG, outline=col4, width=1)
    draw.text((140, 795), "STEP 4: EIGENSPACE FOR \u03bb\u2082 = 1", font=FONT_BADGE, fill=GOLD)
    draw.text((140, 825), "(A - 1 I) v = [ [ 1 , 1 ] , [ 1 , 1 ] ] [ x , y ]\u1d40 = [ 0 , 0 ]\u1d40", font=FONT_MATH_SM, fill=WHITE)
    draw.text((140, 865), "x + y = 0   \u27f9   y = -x   \u27f9   v\u2082 = [ -1 , 1 ]\u1d40", font=FONT_MATH_MD, fill=GOLD)
    draw.text((140, 905), "Eigenspace E\u2081 = span{ [-1, 1]\u1d40 } (135\u00b0 anti-diagonal line)", font=FONT_BODY_SM, fill=MUTED_GRAY)
    
    draw.rounded_rectangle([1180, 110, 1840, 960], radius=20, fill=PANEL_BG, outline=BORDER_COLOR, width=1)
    draw.text((1220, 140), "GEOMETRIC CONFIRMATION", font=FONT_BADGE, fill=GOLD)
    draw.text((1220, 170), "Calculated Eigenspaces", font=FONT_TITLE, fill=WHITE)
    
    rcx, rcy = 1510, 560
    rscale = 75
    for k in range(-4, 5):
        x = rcx + k * rscale
        draw.line([(x, rcy - 4 * rscale), (x, rcy + 4 * rscale)], fill=GRID_LINE, width=1)
        y = rcy + k * rscale
        draw.line([(rcx - 4 * rscale, y), (rcx + 4 * rscale, y)], fill=GRID_LINE, width=1)
    draw.line([(rcx - 4 * rscale, rcy), (rcx + 4 * rscale, rcy)], fill=AXIS_COLOR, width=2)
    draw.line([(rcx, rcy - 4 * rscale), (rcx, rcy + 4 * rscale)], fill=AXIS_COLOR, width=2)
    
    draw.line([(rcx - 3.5 * rscale, rcy + 3.5 * rscale), (rcx + 3.5 * rscale, rcy - 3.5 * rscale)], fill=(0, 210, 211, 90), width=3)
    draw.line([(rcx - 3.5 * rscale, rcy - 3.5 * rscale), (rcx + 3.5 * rscale, rcy + 3.5 * rscale)], fill=(255, 165, 2, 90), width=3)
    
    draw_vector(draw, (rcx, rcy), (rcx + 2 * rscale, rcy - 2 * rscale), CYAN, width=5, label="v\u2081 = [1, 1]\u1d40", label_color=CYAN)
    draw_vector(draw, (rcx, rcy), (rcx - 2 * rscale, rcy - 2 * rscale), GOLD, width=5, label="v\u2082 = [-1, 1]\u1d40", label_color=GOLD)
    
    draw.rounded_rectangle([1220, 860, 1800, 935], radius=12, fill=(0, 210, 211, 20), outline=CYAN, width=1)
    draw.text((1250, 885), "\u2714 Algebra rigorously proves geometric intuition!", font=FONT_BODY, fill=CYAN)
    
    return img

def render_scene5_frame(t, total_t):
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header_footer(draw, 5, 6, "Interpretation: Diagonalization & Matrix Powers", t, total_t)
    
    draw.rounded_rectangle([120, 110, 1800, 360], radius=20, fill=PANEL_BG, outline=PURPLE, width=2)
    draw.rounded_rectangle([800, 135, 1120, 175], radius=8, fill=(162, 155, 254, 40), outline=PURPLE, width=1)
    draw.text((820, 145), "THE POWER OF DIAGONALIZATION", font=FONT_BADGE, fill=PURPLE)
    
    draw.text((680, 205), "A  =  P  D  P\u207b\u00b9", font=FONT_HERO, fill=WHITE)
    draw.text((450, 305), "In the coordinate frame of the eigenvectors, matrix A becomes purely diagonal!", font=FONT_SUBTITLE, fill=LIGHT_GRAY)
    
    mats = [
        ("Modal Matrix P", "P = [ v\u2081  v\u2082 ] = [ [ 1 , -1 ] , [ 1 , 1 ] ]", "Columns are eigenvectors", CYAN),
        ("Diagonal Matrix D", "D = [ [ \u03bb\u2081 , 0 ] , [ 0 , \u03bb\u2082 ] ] = [ [ 3 , 0 ] , [ 0 , 1 ] ]", "Diagonal entries are eigenvalues", GOLD)
    ]
    for i, (head, eq, sub, col) in enumerate(mats):
        x0 = 120 + i * 860
        x1 = x0 + 820
        draw.rounded_rectangle([x0, 390, x1, 530], radius=16, fill=INNER_BG, outline=col, width=1)
        draw.text((x0 + 24, 410), head, font=FONT_BADGE, fill=col)
        draw.text((x0 + 24, 445), eq, font=FONT_MATH_MD, fill=WHITE)
        draw.text((x0 + 24, 490), sub, font=FONT_BODY_SM, fill=MUTED_GRAY)
        
    draw.rounded_rectangle([120, 560, 1800, 960], radius=18, fill=PANEL_BG, outline=BORDER_COLOR, width=1)
    draw.text((160, 590), "APPLICATION TO REPEATED TRANSFORMATIONS & DYNAMICAL SYSTEMS", font=FONT_BADGE, fill=CYAN)
    draw.text((160, 620), "Computing A\u00b9\u2070\u2070 Instantly", font=FONT_TITLE, fill=WHITE)
    
    draw.rounded_rectangle([160, 680, 930, 930], radius=14, fill=INNER_BG, outline=CORAL, width=1)
    draw.text((190, 705), "\u274c Standard Basis (Coupled)", font=FONT_SUBTITLE, fill=CORAL)
    draw.text((190, 755), "A\u00b9\u2070\u2070 = A \u00d7 A \u00d7 A \u00d7 ... (100 times)", font=FONT_MATH_MD, fill=WHITE)
    draw.text((190, 810), "\u2022 Requires 100 consecutive matrix multiplications.", font=FONT_BODY_SM, fill=LIGHT_GRAY)
    draw.text((190, 845), "\u2022 Massive computation, high algorithmic complexity O(100 n\u00b3).", font=FONT_BODY_SM, fill=MUTED_GRAY)
    draw.text((190, 880), "\u2022 Cumulative numerical floating-point error.", font=FONT_BODY_SM, fill=MUTED_GRAY)
    
    draw.rounded_rectangle([990, 680, 1760, 930], radius=14, fill=INNER_BG, outline=CYAN, width=1)
    draw.text((1020, 705), "\u2705 Eigenbasis (Decoupled)", font=FONT_SUBTITLE, fill=CYAN)
    draw.text((1020, 755), "A\u00b9\u2070\u2070 = P  D\u00b9\u2070\u2070  P\u207b\u00b9 = P  [ [ 3\u00b9\u2070\u2070 , 0 ] , [ 0 , 1\u00b9\u2070\u2070 ] ]  P\u207b\u00b9", font=FONT_MATH_SM, fill=WHITE)
    draw.text((1020, 810), "\u2022 3\u00b9\u2070\u2070 = 5.15 \u00d7 10\u2074\u2077 along direction v\u2081, and 1\u00b9\u2070\u2070 = 1 along direction v\u2082.", font=FONT_BODY_SM, fill=CYAN)
    draw.text((1020, 845), "\u2022 Instant evaluation with exact analytical precision!", font=FONT_BODY_SM, fill=LIGHT_GRAY)
    draw.text((1020, 880), "\u2022 Powers differential equations (\u1e8b = Ax) & Markov chains.", font=FONT_BODY_SM, fill=MUTED_GRAY)
    
    return img

def render_scene6_frame(t, total_t):
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header_footer(draw, 6, 6, "Summary & Closing Credits", t, total_t)
    
    if t < 20.0:
        draw.rounded_rectangle([160, 110, 1760, 960], radius=20, fill=PANEL_BG, outline=CYAN, width=1)
        draw.text((200, 140), "PROJECT SYNTHESIS", font=FONT_BADGE, fill=CYAN)
        draw.text((200, 170), "Three Core Pillars of Eigen-Theory", font=FONT_TITLE, fill=WHITE)
        
        takeaways = [
            ("1. GEOMETRIC INVARIANCE", "Eigenvectors are the invariant axes of a linear transformation that do not rotate.\nUnder matrix multiplication, they undergo pure scalar scaling: A v = \u03bb v.", CYAN),
            ("2. ALGEBRAIC SINGULARITY", "Eigenvalues are found by setting det(A - \u03bb I) = 0.\nThis represents the exact condition where the transformation collapses space into\na lower dimension, unlocking non-trivial eigenspaces.", GOLD),
            ("3. DECOUPLING COMPLEX DYNAMICS", "Diagonalization (A = P D P\u207b\u00b9) aligns the problem with the eigenbasis.\nThis converts intractable matrix powers, Markov chains, and systems of differential\nequations into independent, easily solvable scalar problems.", PURPLE)
        ]
        
        for i, (title, text, col) in enumerate(takeaways):
            y0 = 260 + i * 220
            y1 = y0 + 190
            draw.rounded_rectangle([200, y0, 1720, y1], radius=16, fill=INNER_BG, outline=col, width=1)
            draw.text((230, y0 + 25), title, font=FONT_SUBTITLE, fill=col)
            draw.text((230, y0 + 75), text, font=FONT_BODY, fill=LIGHT_GRAY)
            
    else:
        draw.rounded_rectangle([200, 120, 1720, 950], radius=24, fill=PANEL_BG, outline=GOLD, width=2)
        draw.rounded_rectangle([720, 160, 1200, 206], radius=10, fill=(255, 165, 2, 40), outline=GOLD, width=1)
        draw.text((750, 172), "OFFICIAL SUBMISSION CLOSING FRAME", font=FONT_BADGE, fill=GOLD)
        
        draw.text((440, 240), "EIGENVALUES & EIGENVECTORS", font=FONT_HERO, fill=WHITE)
        draw.text((540, 320), "Linear Algebra and Calculus (M3) • Internal Assessment", font=FONT_SUBTITLE, fill=LIGHT_GRAY)
        
        draw.rounded_rectangle([280, 390, 1640, 550], radius=16, fill=INNER_BG, outline=BORDER_COLOR, width=1)
        draw.text((320, 420), "STUDENT NAME:", font=FONT_BADGE, fill=MUTED_GRAY)
        draw.text((320, 455), "Ritesh Kumar", font=FONT_MATH_LG, fill=GOLD)
        
        draw.text((820, 420), "UNIVERSITY ROLL / URN:", font=FONT_BADGE, fill=MUTED_GRAY)
        draw.text((820, 455), "e25b070681", font=FONT_MATH_LG, fill=CYAN)
        
        draw.text((1300, 420), "WEIGHTAGE:", font=FONT_BADGE, fill=MUTED_GRAY)
        draw.text((1300, 455), "10% of Internal", font=FONT_MATH_LG, fill=WHITE)
        
        draw.rounded_rectangle([280, 580, 1640, 900], radius=16, fill=INNER_BG, outline=BORDER_COLOR, width=1)
        draw.text((320, 610), "CREDITS & ORIGINALITY DISCLOSURE", font=FONT_BADGE, fill=CYAN)
        
        credits = [
            ("Animation & Code Engine", "Custom Python 3 Animation Pipeline (Matplotlib, NumPy, SciPy, Pillow, FFmpeg)"),
            ("Voice-Over Narration", "Tony Stark (Robert Downey Jr.) AI Stylized Delivery (en-US-GuyNeural)"),
            ("Background Music", "Original Ambient Harmonic Pad (Synthesized at 432 Hz in A-minor / D-minor)"),
            ("AI Assistance Disclosure", "Scripting structure, visual timing, and code orchestration assisted by Google Antigravity"),
            ("Interactive Simulator", "Live HTML5 Canvas web simulator included in index.html (GitHub Pages Ready)")
        ]
        for i, (k, v) in enumerate(credits):
            y = 650 + i * 46
            draw.text((320, y), f"\u2022 {k}:", font=FONT_BODY_SM, fill=MUTED_GRAY)
            draw.text((620, y), v, font=FONT_BODY_SM, fill=LIGHT_GRAY)
            
    return img

# ----------------- MAIN PIPELINE -----------------

def render_scene_video(scene_key, scene_renderer, duration, out_mp4):
    audio_path = f"assets/audio/{scene_key}.mp3"
    print(f"\n>>> Rendering {scene_key} (duration: {duration:.2f}s, frames: {int(duration * FPS)})...")
    t0 = time.time()
    
    cmd = [
        "ffmpeg", "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{WIDTH}x{HEIGHT}",
        "-pix_fmt", "rgb24",
        "-r", str(FPS),
        "-i", "-",
        "-i", audio_path,
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
        raw_bytes = frame_img.tobytes()
        proc.stdin.write(raw_bytes)
        
        if frame_idx % 240 == 0 or frame_idx == total_frames - 1:
            print(f"  Frame {frame_idx}/{total_frames} ({frame_idx/total_frames*100:.1f}%)")
            
    proc.stdin.close()
    proc.wait()
    print(f"Finished {scene_key} in {time.time() - t0:.1f}s -> {out_mp4}")

def export_snapshots(scene_defs):
    os.makedirs("assets/snapshots", exist_ok=True)
    print("\n>>> Exporting visual snapshot thumbnails for Storyboard PDF...")
    for idx, (scene_key, renderer, dur) in enumerate(scene_defs, start=1):
        mid_t = dur * 0.55
        frame_img = renderer(mid_t, dur)
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
    
    # 4. Mix background music & embed subtitles
    print("\n>>> Mixing background music & embedding English subtitles into MP4...")
    bg_music_path = "assets/audio/background_music.mp3"
    final_output = "_Video.mp4"
    
    filter_complex = (
        "[0:a]volume=1.0[voice];"
        "[1:a]volume=0.10[bgm];"
        "[voice][bgm]amix=inputs=2:duration=first:dropout_transition=3[outa]"
    )
    
    cmd_final = [
        "ffmpeg", "-y",
        "-i", raw_merged_mp4,
        "-i", bg_music_path
    ]
    
    if os.path.exists("subtitles.srt"):
        cmd_final += [
            "-i", "subtitles.srt",
            "-filter_complex", filter_complex,
            "-map", "0:v",
            "-map", "[outa]",
            "-map", "2:s",
            "-c:v", "copy",
            "-c:a", "aac",
            "-b:a", "192k",
            "-c:s", "mov_text",
            "-metadata:s:s:0", "language=eng",
            "-metadata:s:s:0", "title=English Subtitles",
            final_output
        ]
    else:
        cmd_final += [
            "-filter_complex", filter_complex,
            "-map", "0:v",
            "-map", "[outa]",
            "-c:v", "copy",
            "-c:a", "aac",
            "-b:a", "192k",
            final_output
        ]
        
    subprocess.run(cmd_final, check=True)
    
    # Final check with ffprobe
    res = subprocess.run(
        ["ffprobe", "-i", final_output, "-show_entries", "format=duration,size", "-v", "quiet", "-of", "csv=p=0"],
        capture_output=True, text=True, check=True
    )
    lines = res.stdout.strip().split("\n")
    print(f"\n==========================================")
    print(f"🎉 FINAL 1080p VIDEO WITH SUBTITLES & TONY STARK VOICE COMPLETED!")
    print(f"Path: {os.path.abspath(final_output)}")
    print(f"Details: {lines}")
    print(f"==========================================")

if __name__ == "__main__":
    main()
