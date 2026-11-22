"""
Audio Generation Script using edge-tts
Voice: en-US-GuyNeural (Tony Stark / Robert Downey Jr. style: charismatic, confident, energetic)
Generates high-definition voiceover narration for all 6 scenes.
"""
import asyncio
import os
import subprocess
import certifi
import edge_tts

# Ensure SSL cert is configured
os.environ["SSL_CERT_FILE"] = certifi.where()

VOICE = "en-US-GuyNeural"
RATE = "-2%"  # Energetic, charismatic Tony Stark delivery

SCENES = {
    "scene1_hook": (
        "Welcome. In linear algebra, when a matrix acts on space, it usually distorts, rotates, "
        "and scrambles everything in its path. Vectors tumble in all directions. "
        "But hidden inside almost every linear transformation lies a profound secret: "
        "a special set of axes that stubbornly refuse to rotate. "
        "These invariant directions are the eigenvectors, and their scaling factors are the eigenvalues. "
        "From preventing bridges from tearing themselves apart during resonant wind storms, "
        "to powering Google's PageRank algorithm and compressing complex big data, "
        "finding these hidden invariant directions is one of the most powerful ideas in all of mathematics."
    ),
    "scene2_intro": (
        "Let us define the core concept precisely. "
        "Normally, when an n by n matrix A multiplies a vector x, the resulting vector A x points in a completely new direction. "
        "Both its length and its angle change. "
        "However, if a vector v satisfies the golden equation, A v equals lambda v, something extraordinary happens. "
        "Matrix multiplication, which normally involves multi-dimensional stretching and rotating, "
        "collapses into simple scalar multiplication by a single number, lambda. "
        "The non-zero vector v is called an eigenvector, and the scalar lambda is its corresponding eigenvalue. "
        "Along this special line in space, the matrix acts not like a complicated matrix, but like a simple number."
    ),
    "scene3_visual": (
        "To truly grasp this concept, let us watch geometry in action. "
        "Consider the symmetric transformation matrix A with rows: two, one, and one, two. "
        "Notice what happens to a generic vector, like one-zero on the horizontal x-axis. "
        "As the matrix warps the coordinate grid, this vector visibly tilts upwards to two-one, rotating off its original span. "
        "It was knocked off course by more than twenty-six degrees. "
        "Now, watch the unit circle stretch into an ellipse under the transformation. "
        "Observe the diagonal line y equals x. "
        "If we place the vector v-one equals one-one on this line, watch what happens during the transformation: "
        "it does not rotate by even a fraction of a degree! "
        "It simply stretches by a factor of three along the major axis of the ellipse, landing precisely at three-three. "
        "Here, lambda-one is three. "
        "Next, look at the perpendicular diagonal line y equals negative x. "
        "When we place v-two equals negative-one, one on this line, the transformation leaves it completely unchanged in both length and direction. "
        "Its scaling factor is exactly lambda-two equals one, matching the minor axis of the ellipse. "
        "These two perpendicular invariant lines form the natural geometric skeleton of the entire transformation."
    ),
    "scene4_math": (
        "How do we find these special values without guessing? "
        "Let us walk step by step through the rigorous algebraic derivation. "
        "We begin with the golden equation: A v equals lambda v. "
        "Subtracting lambda v from both sides, and using the identity matrix I, we rewrite this as: the quantity A minus lambda I, times v, equals zero. "
        "For a non-zero eigenvector v to exist, this homogeneous linear system must have non-trivial solutions. "
        "Geometrically, this means the matrix A minus lambda I must collapse space into a lower dimension, "
        "which is possible if and only if its determinant is strictly zero. "
        "This gives us the characteristic equation: determinant of A minus lambda I equals zero. "
        "For our matrix, this gives the determinant of two minus lambda, one, one, two minus lambda. "
        "Expanding the determinant yields the characteristic polynomial: two minus lambda squared minus one equals zero. "
        "Simplifying gives lambda squared minus four lambda plus three equals zero. "
        "Factoring this quadratic equation gives lambda minus three times lambda minus one equals zero, "
        "revealing our two eigenvalues: lambda-one equals three, and lambda-two equals one. "
        "Now we find the eigenspaces by substituting each eigenvalue back into A minus lambda I times v equals zero. "
        "For lambda equals three, the system simplifies to negative x plus y equals zero, giving the eigenvector v-one equals one, one. "
        "For lambda equals one, the system simplifies to x plus y equals zero, giving the eigenvector v-two equals negative-one, one. "
        "The algebra confirms our geometric observation with flawless precision."
    ),
    "scene5_eigenbasis": (
        "Now comes the ultimate payoff: Diagonalization and change of basis. "
        "In our standard x-y coordinate system, the matrix A couples x and y together, making repeated calculations messy. "
        "However, if we change our perspective to the eigenbasis formed by v-one and v-two, the transformation matrix becomes completely diagonal: "
        "capital Lambda equals three, zero, zero, one. "
        "Why does this matter in real-world science and engineering? "
        "Imagine calculating A raised to the power of one hundred, such as modeling a population model, a Markov chain, or dynamic vibrations over time. "
        "Multiplying matrix A one hundred times directly requires massive computation. "
        "In the eigenbasis, however, A to the one hundredth power is simply three to the one hundredth along the first eigenvector, "
        "and one to the one hundredth along the second. "
        "Eigenvalues decouple complex coupled systems into independent, easily solvable dimensions."
    ),
    "scene6_summary": (
        "To summarize, let us recap three core takeaways: "
        "First: Eigenvectors are the invariant directions of space that undergo pure scaling without rotation. "
        "Second: We find eigenvalues algebraically by finding when the transformation collapses space, setting determinant of A minus lambda I to zero. "
        "And third: Aligning our coordinates along the eigenbasis decouples complex systems, turning heavy matrix powers into simple scalar scaling. "
        "Thank you for watching. "
        "This video project was developed and coded by Ritesh Kumar for the M3 Linear Algebra and Calculus internal assessment."
    )
}

async def generate_audio():
    os.makedirs("assets/audio", exist_ok=True)
    durations = {}
    
    for scene_id, text in SCENES.items():
        out_path = f"assets/audio/{scene_id}.mp3"
        print(f"Generating audio for {scene_id} using {VOICE}...")
        communicate = edge_tts.Communicate(text, VOICE, rate=RATE)
        await communicate.save(out_path)
        
        # Probe exact duration using ffprobe
        res = subprocess.run(
            ["ffprobe", "-i", out_path, "-show_entries", "format=duration", "-v", "quiet", "-of", "csv=p=0"],
            capture_output=True, text=True, check=True
        )
        duration = float(res.stdout.strip())
        durations[scene_id] = duration
        print(f"-> {scene_id}: {duration:.2f} seconds ({len(text.split())} words)")
        
    total_duration = sum(durations.values())
    print(f"\nTotal Narration Duration: {total_duration:.2f} seconds ({total_duration/60:.2f} minutes)")
    
    with open("assets/audio/durations.txt", "w") as f:
        for k, v in durations.items():
            f.write(f"{k}:{v:.3f}\n")
        f.write(f"total:{total_duration:.3f}\n")

if __name__ == "__main__":
    asyncio.run(generate_audio())
