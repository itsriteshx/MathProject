# Linear Algebra & Calculus (M3) • Internal Assessment
## Project Option 1: Mathematical Animation Video (10% Weightage)

![Resolution](https://img.shields.io/badge/Resolution-1080p_16%3A9-blue.svg)
![Duration](https://img.shields.io/badge/Duration-5m_34s-green.svg)
![Topic](https://img.shields.io/badge/Topic-Eigenvalues_%26_Eigenvectors-purple.svg)
![Voice](https://img.shields.io/badge/Voice-Original_Hinglish_Narration-red.svg)
![Subtitles](https://img.shields.io/badge/Subtitles-Embedded_CC-orange.svg)
![Interactive](https://img.shields.io/badge/Simulator-HTML5_Canvas-brightgreen.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

---

### 👨‍🎓 Student & Submission Details
* **Student Name:** Ritesh Kumar
* **University Roll / URN:** `e25b070681`
* **Course:** Linear Algebra and Calculus (M3)
* **Topic:** **Eigenvalues and Eigenvectors: The Invariant Directions of Linear Space**
* **Repository:** [`itsriteshx/MathProject`](https://github.com/itsriteshx/MathProject)
* **Final Rendered Video:** `_Video.mp4` (Duration: 5m 34s, 1080p Full HD, Embedded Subtitles, Original Hinglish Voiceover by Ritesh Kumar) *(Verified locally & committed)*
* **Official Visual Storyboard:** [`Storyboard.pdf`](./Storyboard.pdf) (With High-Res Scene Snapshots)
* **Interactive Simulator:** [`index.html`](./index.html) (Live Web Simulator, GitHub Pages Ready)
* **Closed Captions File:** [`subtitles.srt`](./subtitles.srt)

---

## 🎯 Learning Objective
> *"By the end of this video, the viewer will be able to geometrically understand why eigenvectors represent invariant transformation axes (and principal axes of ellipse deformation), calculate eigenvalues and eigenvectors step-by-step for a $2 \times 2$ matrix system, and explain how diagonalization ($A = P D P^{-1}$) simplifies complex coupled linear dynamics into independent scalar scaling."*

---

## 🌐 Interactive Web Simulator (`index.html`)
To provide full original interactive value, this repository includes a standalone **HTML5 Canvas Simulator** [`index.html`](./index.html):
* **Live 2D Cartesian Transformation Plane:** Real-time matrix deformation with smooth interpolation slider $t \in [0, 1]$.
* **Interactive Draggable Vector (Mouse & Touch):** Drag any test vector $\vec{x}$ across the plane; a live HUD computes $\Delta \theta$, supports negative-eigenvalue flips ($\Delta\theta = 180^\circ$) and zero-vector guards, and triggers **"✨ EIGENVECTOR ALIGNED"** when aligned.
* **3Blue1Brown Circle-to-Ellipse Visualizer:** Toggle unit circle morphing into an ellipse with principal axes aligned along eigenvectors.
* **Dynamic Eigenpair Solver & Snap Buttons:** Computes and plots true real/defective/complex eigenpairs for any $2 \times 2$ matrix with dynamic snap buttons for $\vec{v}_1$ and $\vec{v}_2$.
* **Eigen-Analysis HUD:** Real-time characteristic equation, eigenvalues, and eigenpair cards.

---

## 🎬 6-Scene Storyboard Breakdown

| Scene | Duration | Purpose | Key Visual & Mathematical Content |
| :--- | :--- | :--- | :--- |
| **1. Hook / Context** | `00:39` | Motivate the concept through real-world systems | • **Premium Minimalist Title Card** showcasing $A\vec{v} = \lambda\vec{v}$, live geometric eigen-field preview, and attribution (`Presented by Ritesh Kumar`).<br/>• Dynamic animation showing chaotic vector transformation.<br/>• 3 Application Cards: **Structural Resonance** (Tacoma Narrows bridge collapse prevention), **Google PageRank**, and **Principal Component Analysis (PCA)**. |
| **2. Concept Intro** | `00:50` | Define the formal equation and notation | • The Golden Equation: $A\vec{v} = \lambda \vec{v}, \quad (\vec{v} \neq \vec{0})$.<br/>• Split comparison: Generic vector $\vec{x}$ (tilts off span) vs. Eigenvector $\vec{v}$ (preserves direction, pure scalar scaling). |
| **3. Visual Intuition & Ellipse** | `01:20` | Demonstrate geometric invariant lines & 3Blue1Brown ellipse | • Transformation Matrix: $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$.<br/>• **3Blue1Brown Unit Circle to Ellipse Morphing:** Unit circle deforms into an ellipse whose semi-major axis is $\vec{v}_1$ (length $\lambda_1 = 3$) and semi-minor axis is $\vec{v}_2$ (length $\lambda_2 = 1$).<br/>• **Generic vector** $\vec{u} = [1, 0]^T \to [2, 1]^T$ rotates by $26.6^\circ$.<br/>• **Eigenvector 1:** Line $y = x$ ($\vec{v}_1 = [1, 1]^T$) stretches $3\times$ with $0^\circ$ rotation ($\lambda_1 = 3$).<br/>• **Eigenvector 2:** Line $y = -x$ ($\vec{v}_2 = [-1, 1]^T$) is completely invariant ($\lambda_2 = 1$). |
| **4. Worked Example** | `01:14` | Step-by-step algebraic derivation | • Nullspace condition: $(A - \lambda I)\vec{v} = \vec{0}$.<br/>• Why $\det(A - \lambda I) = 0$ is necessary for non-trivial solutions.<br/>• Characteristic polynomial: $\lambda^2 - 4\lambda + 3 = 0 \implies \lambda_1 = 3, \lambda_2 = 1$.<br/>• Solving eigenspaces: $E_{\lambda=3} = \text{span}\{[1, 1]^T\}$, $E_{\lambda=1} = \text{span}\{[-1, 1]^T\}$. |
| **5. Interpretation** | `01:02` | Diagonalization & computational power | • Change of basis to the eigenbasis: $A = P D P^{-1}$.<br/>• Computing matrix powers: $A^{100} = P D^{100} P^{-1} = P \begin{pmatrix} 3^{100} & 0 \\ 0 & 1^{100} \end{pmatrix} P^{-1}$.<br/>• Decoupling complex differential equations and Markov chains. |
| **6. Summary & Credits**| `00:28` | Synthesize key ideas & official closing frame | • 3 Core Takeaways: Geometric Invariance, Algebraic Singularity, and Decoupling Power.<br/>• **Closing Credits Frame** with author details (Ritesh Kumar, `e25b070681`), tools, AI disclosure, and citations. |

---

## 🧮 Mathematical Derivations

### 1. The Fundamental Equation
For a square matrix $A \in \mathbb{R}^{n \times n}$, a non-zero vector $\vec{v} \in \mathbb{R}^n$ is an **eigenvector** with corresponding **eigenvalue** $\lambda \in \mathbb{R}$ if:
$$A\vec{v} = \lambda \vec{v}$$

Rearranging gives the homogeneous system:
$$(A - \lambda I)\vec{v} = \vec{0}$$

### 2. The Singularity Condition
For a non-zero solution $\vec{v} \neq \vec{0}$ to exist, the matrix $(A - \lambda I)$ must have a non-trivial null space. In geometric terms, the transformation must compress space into a lower dimension. This occurs if and only if:
$$\det(A - \lambda I) = 0$$

### 3. Worked Example: $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$
$$\det \begin{pmatrix} 2-\lambda & 1 \\ 1 & 2-\lambda \end{pmatrix} = (2-\lambda)^2 - (1)(1) = 0$$
$$\lambda^2 - 4\lambda + 4 - 1 = 0 \implies \lambda^2 - 4\lambda + 3 = 0$$
Factoring:
$$(\lambda - 3)(\lambda - 1) = 0 \implies \lambda_1 = 3, \quad \lambda_2 = 1$$

#### Finding Eigenspace for $\lambda_1 = 3$:
$$(A - 3I)\vec{v} = \begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \implies -x + y = 0 \implies y = x$$
$$\vec{v}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$$

#### Finding Eigenspace for $\lambda_2 = 1$:
$$(A - I)\vec{v} = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \implies x + y = 0 \implies y = -x$$
$$\vec{v}_2 = \begin{pmatrix} -1 \\ 1 \end{pmatrix}$$

Notice that because $A$ is symmetric ($A = A^T$), its eigenvectors are orthogonal:
$$\vec{v}_1 \cdot \vec{v}_2 = (1)(-1) + (1)(1) = 0$$

---

## 💻 Animation Code Architecture & Reproduction

The entire video is programmatically generated using Python 3 and FFmpeg:

```bash
# 1. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 2. Install required packages
pip install -r _Code/requirements.txt

# 3. (Optional) Generate ambient background music or place narration clips in assets/audio/
# python3 _Code/generate_music.py

# 4. Generate synchronized subtitles (SRT)
python3 _Code/generate_subtitles.py

# 5. Render 1080p video scenes and assemble final video with subtitles
python3 _Code/render_video.py

# 6. Generate official visual storyboard PDF with snapshots
python3 _Code/generate_storyboard.py

# 7. Run independent mathematical verification suite
python3 _Code/verify_math.py
```

---

## 📜 Originality & AI Tools Disclosure
* **Animation Engine:** Custom Python 3 script utilizing `Pillow`, `NumPy`, `SciPy`, and `FFmpeg` for direct 1080p raw-frame piping.
* **Voice-Over Narration:** Original Hinglish student voice recording by Ritesh Kumar (noise-filtered, loudness-normalized, and frame-synced across all 6 scenes).
* **Closed Captions:** Synchronized `.srt` Hinglish subtitles embedded directly into `_Video.mp4` as a switchable subtitle track.
* **Background Music:** Programmatically synthesized 432 Hz ambient harmonic pad in A-minor / D-minor with soft low-pass filtering.
* **Interactive Tool:** Custom HTML5 Canvas web simulator (`index.html`) allowing interactive real-time vector dragging and eigen-detection.
* **AI Disclosure:** Script writing assistance, visual timing calibration, and code structure assisted by Google Antigravity. Mathematical proofs, verification, and code execution conducted independently.
