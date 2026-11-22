"""
Test script to render 1 sample frame for each of the 6 scenes
and verify visual quality, layout, typography, and mathematical precision.
"""
import os
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Canvas Setup
WIDTH, HEIGHT = 1920, 1080
BG_COLOR = (11, 15, 25)        # Deep obsidian slate
PANEL_BG = (21, 27, 43)        # Sleek dark navy card
BORDER_COLOR = (38, 48, 71)    # Subtle card border
CYAN = (0, 210, 211)           # Electric Cyan (v1, lambda=3)
GOLD = (255, 165, 2)           # Radiant Gold (v2, lambda=1)
CORAL = (255, 71, 87)          # Vivid Coral (generic vector)
PURPLE = (162, 155, 254)       # Soft Purple (matrix space)
WHITE = (255, 255, 255)
LIGHT_GRAY = (226, 232, 240)
MUTED_GRAY = (148, 163, 184)
GRID_LINE = (30, 38, 56)
AXIS_COLOR = (74, 85, 104)

# Load Fonts
FONT_TITLE = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 44)
FONT_SUBTITLE = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 28)
FONT_BODY = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 22)
FONT_MATH = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 32)
FONT_MATH_LG = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 46)
FONT_BADGE = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 16)
FONT_LABEL = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 18)

def draw_header_footer(draw, scene_idx, total_scenes, scene_title, progress=0.5):
    # Top Bar Background
    draw.rectangle([0, 0, WIDTH, 64], fill=(15, 21, 35))
    draw.line([(0, 64), (WIDTH, 64)], fill=BORDER_COLOR, width=1)
    
    # Left Badge
    draw.rounded_rectangle([24, 14, 340, 50], radius=8, fill=(0, 210, 211, 40), outline=CYAN, width=1)
    draw.text((36, 22), "M3 • LINEAR ALGEBRA & CALCULUS", font=FONT_BADGE, fill=CYAN)
    
    # Center Title
    draw.text((640, 18), "EIGENVALUES & EIGENVECTORS", font=FONT_SUBTITLE, fill=WHITE)
    
    # Right Student Badge
    draw.rounded_rectangle([WIDTH - 360, 14, WIDTH - 24, 50], radius=8, fill=(255, 165, 2, 40), outline=GOLD, width=1)
    draw.text((WIDTH - 344, 22), "Ritesh Kumar  |  e25b070681", font=FONT_BADGE, fill=GOLD)
    
    # Bottom Bar
    draw.rectangle([0, HEIGHT - 54, WIDTH, HEIGHT], fill=(15, 21, 35))
    draw.line([(0, HEIGHT - 54), (WIDTH, HEIGHT - 54)], fill=BORDER_COLOR, width=1)
    
    # Progress Bar
    draw.rectangle([0, HEIGHT - 6, WIDTH, HEIGHT], fill=(25, 33, 50))
    prog_w = int(WIDTH * progress)
    if prog_w > 0:
        draw.rectangle([0, HEIGHT - 6, prog_w, HEIGHT], fill=CYAN)
        
    # Scene Label
    draw.text((30, HEIGHT - 40), f"Scene {scene_idx} of {total_scenes}: {scene_title}", font=FONT_LABEL, fill=LIGHT_GRAY)
    draw.text((WIDTH - 240, HEIGHT - 40), "M3 Internal Assessment (10%)", font=FONT_LABEL, fill=MUTED_GRAY)

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
        draw.text((lx, ly), label, font=FONT_MATH, fill=label_color)

def test_scene1():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header_footer(draw, 1, 6, "Opening & The Hidden Stability of Space", 0.1)
    
    # Opening Glassmorphic Card
    draw.rounded_rectangle([240, 140, 1680, 920], radius=24, fill=PANEL_BG, outline=CYAN, width=2)
    
    # Badge
    draw.rounded_rectangle([700, 180, 1220, 226], radius=12, fill=(0, 210, 211, 40), outline=CYAN, width=1)
    draw.text((720, 192), "INTERNAL ASSESSMENT • PROJECT OPTION 1", font=FONT_BADGE, fill=CYAN)
    
    # Titles
    draw.text((450, 260), "EIGENVALUES AND EIGENVECTORS", font=FONT_TITLE, fill=WHITE)
    draw.text((480, 330), "The Invariant Directions and Hidden Architecture of Linear Space", font=FONT_SUBTITLE, fill=LIGHT_GRAY)
    
    # Student Info Container
    draw.rounded_rectangle([320, 420, 1600, 580], radius=16, fill=(15, 21, 35), outline=BORDER_COLOR, width=1)
    draw.text((360, 450), "STUDENT NAME:", font=FONT_BADGE, fill=MUTED_GRAY)
    draw.text((360, 480), "Ritesh Kumar", font=FONT_MATH_LG, fill=GOLD)
    
    draw.text((820, 450), "UNIVERSITY ROLL / URN:", font=FONT_BADGE, fill=MUTED_GRAY)
    draw.text((820, 480), "e25b070681", font=FONT_MATH_LG, fill=CYAN)
    
    draw.text((1280, 450), "COURSE & WEIGHTAGE:", font=FONT_BADGE, fill=MUTED_GRAY)
    draw.text((1280, 480), "M3 (10% Internal)", font=FONT_MATH_LG, fill=WHITE)
    
    # 3 Real-World Application Cards
    cards = [
        ("Resonance & Vibrations", "Natural structural frequencies \u03c9\u00b2 are eigenvalues.", CYAN),
        ("Google PageRank", "Dominant eigenvector of the web connectivity graph.", GOLD),
        ("Principal Components", "Finds axes of maximum variance for big data.", PURPLE)
    ]
    for i, (title, desc, col) in enumerate(cards):
        x0 = 320 + i * 440
        x1 = x0 + 400
        draw.rounded_rectangle([x0, 620, x1, 840], radius=16, fill=(15, 21, 35), outline=col, width=1)
        draw.text((x0 + 20, 650), title, font=FONT_SUBTITLE, fill=col)
        draw.text((x0 + 20, 710), desc, font=FONT_BODY, fill=LIGHT_GRAY)
        
    os.makedirs("assets/test_frames", exist_ok=True)
    img.save("assets/test_frames/scene1.png")
    print("Saved scene1 test frame.")

def test_scene3():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    draw_header_footer(draw, 3, 6, "Geometric Intuition: Invariant Lines", 0.6)
    
    # 2D Grid Left
    cx, cy = 540, 560
    scale = 75
    # Grid lines
    for k in range(-5, 6):
        # Vertical
        x = cx + k * scale
        draw.line([(x, cy - 5 * scale), (x, cy + 5 * scale)], fill=GRID_LINE, width=1)
        # Horizontal
        y = cy + k * scale
        draw.line([(cx - 5 * scale, y), (cx + 5 * scale, y)], fill=GRID_LINE, width=1)
        
    # Axes
    draw.line([(cx - 5 * scale, cy), (cx + 5 * scale, cy)], fill=AXIS_COLOR, width=2)
    draw.line([(cx, cy - 5 * scale), (cx, cy + 5 * scale)], fill=AXIS_COLOR, width=2)
    
    # Invariant Line 1: y = x (Cyan)
    draw.line([(cx - 4.5 * scale, cy + 4.5 * scale), (cx + 4.5 * scale, cy - 4.5 * scale)], fill=(0, 210, 211, 100), width=3)
    draw.text((cx + 3.2 * scale, cy - 3.8 * scale), "Line y = x", font=FONT_LABEL, fill=CYAN)
    
    # Invariant Line 2: y = -x (Gold)
    draw.line([(cx - 4.5 * scale, cy - 4.5 * scale), (cx + 4.5 * scale, cy + 4.5 * scale)], fill=(255, 165, 2, 100), width=3)
    draw.text((cx - 4.2 * scale, cy - 3.8 * scale), "Line y = -x", font=FONT_LABEL, fill=GOLD)
    
    # Draw Eigenvector 1 (Original & Stretched)
    # v1 = (1, 1) -> (3, 3)
    draw_vector(draw, (cx, cy), (cx + 3 * scale, cy - 3 * scale), CYAN, width=5, label="A v1 = 3 v1  (\u03bb\u2081 = 3)", label_color=CYAN)
    draw_vector(draw, (cx, cy), (cx + 1 * scale, cy - 1 * scale), (0, 180, 180), width=3, label="v1 = [1, 1]\u1d40", label_color=LIGHT_GRAY)
    
    # Draw Eigenvector 2
    # v2 = (-1, 1) -> (-1, 1)
    draw_vector(draw, (cx, cy), (cx - 1 * scale, cy - 1 * scale), GOLD, width=5, label="A v2 = 1 v2  (\u03bb\u2082 = 1)", label_color=GOLD)
    
    # Generic Vector that rotated
    draw_vector(draw, (cx, cy), (cx + 2 * scale, cy - 1 * scale), CORAL, width=4, label="A u = [2, 1]\u1d40  (\u0394\u03b8 = 26.6\u00b0)", label_color=CORAL)
    
    # Right Information Panel
    draw.rounded_rectangle([1060, 120, 1840, 960], radius=20, fill=PANEL_BG, outline=BORDER_COLOR, width=1)
    draw.text((1100, 160), "GEOMETRIC DISCOVERY", font=FONT_SUBTITLE, fill=WHITE)
    
    # Matrix Card
    draw.rounded_rectangle([1100, 220, 1800, 360], radius=14, fill=(15, 21, 35), outline=CYAN, width=1)
    draw.text((1130, 240), "Transformation Matrix A:", font=FONT_LABEL, fill=MUTED_GRAY)
    draw.text((1130, 275), "A = [ [ 2 , 1 ] , [ 1 , 2 ] ]", font=FONT_MATH_LG, fill=WHITE)
    
    # Invariant Direction 1 Card
    draw.rounded_rectangle([1100, 390, 1800, 560], radius=14, fill=(15, 21, 35), outline=CYAN, width=1)
    draw.text((1130, 410), "EIGENPAIR 1 (Line y = x):", font=FONT_LABEL, fill=CYAN)
    draw.text((1130, 445), "\u2022 Vector v\u2081 = [ 1 , 1 ]\u1d40", font=FONT_MATH, fill=WHITE)
    draw.text((1130, 490), "\u2022 Stretches by factor \u03bb\u2081 = 3 (0\u00b0 rotation!)", font=FONT_MATH, fill=CYAN)
    
    # Invariant Direction 2 Card
    draw.rounded_rectangle([1100, 590, 1800, 760], radius=14, fill=(15, 21, 35), outline=GOLD, width=1)
    draw.text((1130, 610), "EIGENPAIR 2 (Line y = -x):", font=FONT_LABEL, fill=GOLD)
    draw.text((1130, 645), "\u2022 Vector v\u2082 = [ -1 , 1 ]\u1d40", font=FONT_MATH, fill=WHITE)
    draw.text((1130, 690), "\u2022 Completely invariant: \u03bb\u2082 = 1 (0\u00b0 rotation!)", font=FONT_MATH, fill=GOLD)
    
    # Key Takeaway Card
    draw.rounded_rectangle([1100, 790, 1800, 920], radius=14, fill=(15, 21, 35), outline=PURPLE, width=1)
    draw.text((1130, 810), "\u2728 Orthogonality Note:", font=FONT_LABEL, fill=PURPLE)
    draw.text((1130, 845), "v\u2081 \u22a5 v\u2082 (dot product = 0). They form a natural basis!", font=FONT_BODY, fill=LIGHT_GRAY)
    
    img.save("assets/test_frames/scene3.png")
    print("Saved scene3 test frame.")

if __name__ == "__main__":
    test_scene1()
    test_scene3()
