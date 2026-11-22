"""
Subtitle Generator (SRT) for M3 Animation Video
Synchronized with Tony Stark (en-US-GuyNeural) scene durations.
Total Duration: 360.24 seconds (6.00 minutes).
"""

def format_time(seconds):
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int(round((seconds - int(seconds)) * 1000))
    return f"{hrs:02d}:{mins:02d}:{secs:02d},{millis:03d}"

SCENE_CUES = [
    # Scene 1: Hook / Context (Total: 39.98s)
    ("scene1", 0.0, [
        (0.5, 7.0, "Welcome. In linear algebra, when a matrix acts on space, it usually distorts, rotates,"),
        (7.5, 13.0, "and scrambles everything in its path. Vectors tumble in all directions."),
        (13.5, 18.0, "But hidden inside almost every linear transformation lies a profound secret:"),
        (18.5, 24.0, "a special set of axes that stubbornly refuse to rotate."),
        (24.5, 30.5, "These invariant directions are the eigenvectors, and their scaling factors are the eigenvalues."),
        (31.0, 36.0, "From preventing bridges from tearing themselves apart during resonant wind storms,"),
        (36.5, 39.5, "to powering Google's PageRank and big data: finding these directions is peak mathematics.")
    ]),
    
    # Scene 2: Concept Intro (Total: 44.52s)
    ("scene2", 39.98, [
        (0.5, 4.5, "Let us define the core concept precisely."),
        (5.0, 10.5, "Normally, an n by n matrix A multiplies a vector x into a completely new direction."),
        (11.0, 14.5, "Both its length and its angle change."),
        (15.0, 20.5, "However, if a vector v satisfies the golden equation, A v equals lambda v, magic happens."),
        (21.0, 26.5, "Matrix multiplication collapses into simple scalar multiplication by a single number, lambda."),
        (27.0, 32.5, "The non-zero vector v is an eigenvector, and scalar lambda is its eigenvalue."),
        (33.0, 39.5, "Along this line in space, the matrix acts not like a matrix, but like a simple number."),
        (40.0, 44.0, "Pure stretching, shrinking, or reversal along a single invariant line.")
    ]),

    # Scene 3: Visual Intuition (Total: 80.40s)
    ("scene3", 39.98 + 44.52, [
        (0.5, 5.0, "To truly grasp this concept, let us watch geometry in action."),
        (5.5, 11.5, "Consider the symmetric transformation matrix A with rows: two, one, and one, two."),
        (12.0, 17.5, "Notice what happens to a generic vector, like one-zero on the horizontal x-axis."),
        (18.0, 24.0, "As the matrix warps the grid, this vector visibly tilts upwards to two-one, rotating off span."),
        (24.5, 30.5, "It was knocked off course by more than twenty-six degrees."),
        (31.0, 36.5, "Now, watch the unit circle stretch into an ellipse under the transformation."),
        (37.0, 43.0, "Observe the diagonal line y equals x. If we place vector v1 = [1, 1] on this line,"),
        (43.5, 49.5, "it does not rotate by even a fraction of a degree!"),
        (50.0, 56.5, "It simply stretches by a factor of 3 along the major axis of the ellipse to [3, 3]. Lambda 1 is 3."),
        (57.0, 63.5, "Next, look at the perpendicular diagonal line y equals negative x."),
        (64.0, 71.0, "Vector v2 = [-1, 1] remains completely unchanged in both length and direction!"),
        (71.5, 76.5, "Its scaling factor is exactly lambda 2 equals 1, matching the minor axis of the ellipse."),
        (77.0, 80.0, "These two perpendicular invariant lines form the natural geometric skeleton of space.")
    ]),

    # Scene 4: Worked Example (Total: 100.70s)
    ("scene4", 39.98 + 44.52 + 80.40, [
        (0.5, 5.0, "How do we find these special values without guessing?"),
        (5.5, 11.0, "Let us walk step by step through the rigorous algebraic derivation."),
        (11.5, 17.5, "We begin with A v equals lambda v. Subtracting yields: (A - lambda I) v = 0."),
        (18.0, 24.5, "For a non-zero eigenvector v to exist, this system must have non-trivial solutions."),
        (25.0, 31.5, "Geometrically, (A - lambda I) must collapse space into a line or point,"),
        (32.0, 37.5, "which is possible if and only if its determinant is strictly zero."),
        (38.0, 45.0, "Setting determinant of [2 - lambda, 1; 1, 2 - lambda] to zero gives the characteristic equation:"),
        (45.5, 52.0, "(2 - lambda) squared minus 1 equals zero, simplifying to lambda squared minus 4 lambda plus 3 equals 0."),
        (52.5, 59.0, "Factoring gives (lambda - 3)(lambda - 1) = 0, revealing lambda 1 = 3, and lambda 2 = 1."),
        (59.5, 67.0, "Now we find eigenspaces by substituting back into (A - lambda I) v = 0."),
        (67.5, 75.0, "For lambda = 3: the system simplifies to -x + y = 0, giving eigenvector v1 = [1, 1]."),
        (75.5, 83.5, "For lambda = 1: the system simplifies to x + y = 0, giving eigenvector v2 = [-1, 1]."),
        (84.0, 92.5, "Because matrix A is symmetric, v1 and v2 are guaranteed to be mutually orthogonal!"),
        (93.0, 100.0, "The algebra confirms our geometric observation with flawless precision.")
    ]),

    # Scene 5: Interpretation (Total: 58.15s)
    ("scene5", 39.98 + 44.52 + 80.40 + 100.70, [
        (0.5, 5.5, "Now comes the ultimate payoff: Diagonalization and change of basis."),
        (6.0, 12.5, "In our standard x-y system, matrix A couples x and y, making repeated calculations messy."),
        (13.0, 20.0, "However, in the eigenbasis of v1 and v2, matrix A becomes completely diagonal: D = diag(3, 1)."),
        (20.5, 26.5, "Why does this matter in real-world science and engineering?"),
        (27.0, 34.0, "Imagine calculating A raised to the 100th power, such as modeling dynamic vibrations over time."),
        (34.5, 41.5, "Multiplying matrix A 100 times directly requires massive computation and accumulates error."),
        (42.0, 49.5, "In the eigenbasis, A^100 is simply 3^100 along v1, and 1^100 along v2!"),
        (50.0, 57.5, "Eigenvalues decouple complex coupled systems into independent, easily solvable dimensions.")
    ]),

    # Scene 6: Summary & Credits (Total: 36.48s)
    ("scene6", 39.98 + 44.52 + 80.40 + 100.70 + 58.15, [
        (0.5, 4.0, "To summarize, let us recap three core takeaways:"),
        (4.5, 10.5, "First: Eigenvectors are invariant directions that undergo pure scaling without rotation."),
        (11.0, 17.5, "Second: We find eigenvalues algebraically by setting determinant of (A - lambda I) to zero."),
        (18.0, 24.5, "And third: Aligning with the eigenbasis decouples complex systems into simple scalar scaling."),
        (25.0, 30.0, "Thank you for watching this presentation."),
        (30.5, 36.0, "Developed and coded by Ritesh Kumar for the M3 Linear Algebra and Calculus internal assessment.")
    ])
]

def generate_srt(out_file="subtitles.srt"):
    index = 1
    with open(out_file, "w") as f:
        for scene_name, base_offset, cues in SCENE_CUES:
            for s_start, s_end, text in cues:
                abs_start = base_offset + s_start
                abs_end = base_offset + s_end
                f.write(f"{index}\n")
                f.write(f"{format_time(abs_start)} --> {format_time(abs_end)}\n")
                f.write(f"{text}\n\n")
                index += 1
    print(f"Generated {index - 1} subtitle cues -> {out_file}")

if __name__ == "__main__":
    generate_srt()
