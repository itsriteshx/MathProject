"""
Visual Storyboard PDF Generator (With Embedded 1080p Snapshots)
Builds the official 6-Scene Storyboard PDF for GitHub submission
aligned with M3 Internal Assessment guidelines.
"""
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
import os

def generate_storyboard_pdf():
    pdf_path = "Storyboard.pdf"
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=32,
        rightMargin=32,
        topMargin=32,
        bottomMargin=32
    )
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=colors.HexColor('#0F172A'),
        alignment=0
    )
    
    subtitle_style = ParagraphStyle(
        'DocSub',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#475569')
    )
    
    section_heading = ParagraphStyle(
        'SecHead',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#1E293B'),
        spaceBefore=8,
        spaceAfter=6
    )
    
    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#334155')
    )
    
    table_header = ParagraphStyle(
        'TblHead',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white
    )
    
    table_cell = ParagraphStyle(
        'TblCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#1E293B')
    )
    
    elements = []
    
    # Document Header
    elements.append(Paragraph("LINEAR ALGEBRA & CALCULUS (M3) • INTERNAL ASSESSMENT", subtitle_style))
    elements.append(Spacer(1, 3))
    elements.append(Paragraph("Visual Storyboard Document: 6-Scene Production Plan", title_style))
    elements.append(Paragraph("<b>Topic:</b> Eigenvalues & Eigenvectors: The Invariant Directions of Space", subtitle_style))
    elements.append(Spacer(1, 6))
    
    # Metadata Table
    meta_data = [
        [
            Paragraph("<b>Student Name:</b> Ritesh Kumar", body_style),
            Paragraph("<b>University Roll / URN:</b> e25b070681", body_style),
            Paragraph("<b>Assessment Weightage:</b> 10% Internal", body_style)
        ],
        [
            Paragraph("<b>Duration:</b> Exactly 6.00 Minutes (Guidelines Compliant)", body_style),
            Paragraph("<b>Format:</b> 1080p 16:9 Landscape MP4 + Subtitles", body_style),
            Paragraph("<b>Narration:</b> Tony Stark AI Stylized Delivery", body_style)
        ]
    ]
    meta_table = Table(meta_data, colWidths=[180, 200, 168])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    elements.append(meta_table)
    elements.append(Spacer(1, 8))
    
    # Learning Objective Callout Box
    obj_text = (
        "<b>Core Learning Objective:</b> <i>\"By the end of this video, the viewer will be able to geometrically understand "
        "why eigenvectors represent invariant transformation axes (and principal axes of ellipse deformation), calculate eigenvalues "
        "and eigenvectors step-by-step for a 2 × 2 matrix, and explain how diagonalization (A = P D P⁻¹) converts complex linear systems "
        "into independent scalar scaling.\"</i>"
    )
    obj_table = Table([[Paragraph(obj_text, body_style)]], colWidths=[548])
    obj_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#EFF6FF')),
        ('BOX', (0,0), (-1,-1), 1.2, colors.HexColor('#2563EB')),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    elements.append(obj_table)
    elements.append(Spacer(1, 10))
    
    # 6 Scenes with Embedded Thumbnails
    elements.append(Paragraph("6-Scene Visual Storyboard & Math Plan", section_heading))
    
    scenes_info = [
        (
            1, "Scene 1: Hook / Context (~40 sec)",
            "assets/snapshots/scene1.png",
            "Spark curiosity & motivate topic with real-world applications.",
            "• Official Opening Frame displaying Student Credentials (Ritesh Kumar, e25b070681).<br/>"
            "• Dynamic visualization of matrix transformation chaos (vectors tumbling in all directions).<br/>"
            "• 3 Application Cards: Structural Resonance (Tacoma Narrows bridge collapse prevention), Google PageRank, and PCA.<br/>"
            "• Guiding Question: 'In a storm of distortion, which directions stay invariant?'"
        ),
        (
            2, "Scene 2: Concept Introduction (~45 sec)",
            "assets/snapshots/scene2.png",
            "Define the concept, formal notation, and core learning goals.",
            "• Centered Golden Equation: Av = λv (v ≠ 0).<br/>"
            "• Component breakdown: Matrix A (operator), Eigenvector v (invariant axis), Eigenvalue λ (scalar multiplier).<br/>"
            "• Split comparison: Generic vector x (rotates off span) vs. Eigenvector v (direction preserved).<br/>"
            "• Scaling regimes: λ > 1 (stretch), 0 < λ < 1 (shrink), λ < 0 (flip)."
        ),
        (
            3, "Scene 3: Visual Intuition & Ellipse (~80 sec)",
            "assets/snapshots/scene3.png",
            "Demonstrate geometric invariant lines and 3Blue1Brown circle-to-ellipse morphing.",
            "• 2D grid deformation under matrix A = [[2, 1], [1, 2]].<br/>"
            "• 3Blue1Brown Unit Circle to Ellipse morphing: circle stretches into an ellipse whose semi-major axis is v₁ (length λ₁=3) and semi-minor axis is v₂ (length λ₂=1).<br/>"
            "• Generic vector u = [1, 0]^T tilts by 26.6° to [2, 1]^T (not an eigenvector).<br/>"
            "• Invariant Line y = x (Cyan, v₁=[1, 1]^T) stretches 3× with 0° rotation.<br/>"
            "• Invariant Line y = -x (Gold, v₂=[-1, 1]^T) preserved with λ₂=1. Orthogonality highlight."
        ),
        (
            4, "Scene 4: Worked Example Step-by-Step (~101 sec)",
            "assets/snapshots/scene4.png",
            "Demonstrate rigorous algebraic derivation step-by-step.",
            "• Step 1: Nullspace condition (A - λI)v = 0. Explain why det(A - λI) = 0 is required for non-trivial solutions.<br/>"
            "• Step 2: Characteristic polynomial det[[2-λ, 1], [1, 2-λ]] = (2-λ)² - 1 = λ² - 4λ + 3 = 0.<br/>"
            "• Step 3: Factoring gives λ₁ = 3 and λ₂ = 1.<br/>"
            "• Step 4: Solving eigenspaces: E₃ = span{[1, 1]^T} and E₁ = span{[-1, 1]^T}."
        ),
        (
            5, "Scene 5: Interpretation & Eigenbasis (~58 sec)",
            "assets/snapshots/scene5.png",
            "Connect algebra to real-world power: Diagonalization & matrix powers.",
            "• Change of basis to eigenbasis: A = P D P⁻¹, where D = diag(3, 1).<br/>"
            "• Computing matrix powers: A¹⁰⁰ = P D¹⁰⁰ P⁻¹.<br/>"
            "• Visual comparison: 100 consecutive matrix multiplications vs. instant scalar powers (3¹⁰⁰ and 1¹⁰⁰).<br/>"
            "• Decoupling coupled multivariable dynamic systems and Markov chains."
        ),
        (
            6, "Scene 6: Summary & Closing Credits (~36 sec)",
            "assets/snapshots/scene6.png",
            "Reinforce 3 core takeaways, display credits, and official closing frame.",
            "• 3 Core Takeaways: Geometric Invariance, Algebraic Singularity, and Decoupling Dynamics.<br/>"
            "• Official Closing Frame with student credentials, tools, AI disclosure, and interactive simulator notice."
        )
    ]
    
    table_rows = [
        [
            Paragraph("Scene & Visual Snapshot", table_header),
            Paragraph("Purpose & Educational Plan", table_header)
        ]
    ]
    
    for idx, title, img_path, purpose, plan in scenes_info:
        img_elem = RLImage(img_path, width=170, height=95.6) if os.path.exists(img_path) else Paragraph("Snapshot", body_style)
        left_cell = [
            Paragraph(f"<b>{title}</b>", body_style),
            Spacer(1, 3),
            img_elem
        ]
        right_cell = [
            Paragraph(f"<b>Purpose:</b> {purpose}", body_style),
            Spacer(1, 4),
            Paragraph(f"<b>Visual, Narration & Math Plan:</b><br/>{plan}", table_cell)
        ]
        table_rows.append([left_cell, right_cell])
        
    story_table = Table(table_rows, colWidths=[185, 363])
    story_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E293B')),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')]),
        ('PADDING', (0,0), (-1,-1), 4),
    ]))
    
    elements.append(story_table)
    elements.append(Spacer(1, 10))
    
    # Footer Notes
    elements.append(Paragraph("<b>Rubric & Deliverables Alignment Summary:</b>", body_style))
    elements.append(Paragraph(
        "• <b>Video & Audio:</b> 1080p Full HD MP4, exactly 6.00 minutes, Tony Stark AI stylized voiceover narration, embedded English subtitles.<br/>"
        "• <b>Original Effort:</b> Custom Python rendering pipeline (NumPy, SciPy, Pillow, FFmpeg) + Interactive HTML5 Canvas Simulator (index.html).<br/>"
        "• <b>Mathematical Rigor:</b> Geometric circle-to-ellipse transformation, algebraic nullspace proof, characteristic equation, and diagonalization.",
        body_style
    ))
    
    doc.build(elements)
    print(f"Generated official Visual Storyboard PDF with Snapshots: {pdf_path}")

if __name__ == "__main__":
    generate_storyboard_pdf()
