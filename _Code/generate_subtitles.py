"""
Subtitle Generator (SRT) for M3 Animation Video
Synchronized directly with Ritesh Kumar's original Hinglish narration timestamps.
Total Duration: Read dynamically from assets/audio/durations.txt or fallback (~5m 34s).
"""

def format_time(seconds):
    hrs = int(seconds // 3600)
    mins = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int(round((seconds - int(seconds)) * 1000))
    if millis == 1000:
        secs += 1
        millis = 0
    return f"{hrs:02d}:{mins:02d}:{secs:02d},{millis:03d}"

import os

DEFAULT_DURATIONS = {
    "scene1_hook": 39.082,
    "scene2_intro": 49.550,
    "scene3_visual": 80.079,
    "scene4_math": 74.411,
    "scene5_eigenbasis": 62.461,
    "scene6_summary": 28.186,
}


def load_durations(path="assets/audio/durations.txt"):
    durs = dict(DEFAULT_DURATIONS)
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                if ":" in line:
                    k, v = line.strip().split(":")
                    durs[k] = float(v)
    return durs

ORIG_DURATIONS = {
    "scene1_hook": 41.680,
    "scene2_intro": 49.550,
    "scene3_visual": 83.820,
    "scene4_math": 78.600,
    "scene5_eigenbasis": 64.570,
    "scene6_summary": 30.200,
}


def scale_cues(scene_key, durs, cues):
    orig = ORIG_DURATIONS[scene_key]
    actual = durs[scene_key]
    ratio = actual / orig
    scaled = []
    for s, e, txt in cues:
        ns = min(round(s * ratio, 3), actual - 0.2)
        ne = min(round(e * ratio, 3), actual - 0.05)
        if ne > ns:
            scaled.append((ns, ne, txt))
    return scaled


def build_scene_cues(durs):
    s1_off = 0.0
    s2_off = s1_off + durs["scene1_hook"]
    s3_off = s2_off + durs["scene2_intro"]
    s4_off = s3_off + durs["scene3_visual"]
    s5_off = s4_off + durs["scene4_math"]
    s6_off = s5_off + durs["scene5_eigenbasis"]

    return [
        ("scene1", s1_off, scale_cues("scene1_hook", durs, [
            (0.2, 6.8, "Hello, my name is Ritesh. Aaj hum baat karenge Linear Algebra ke ek bahut interesting topic:"),
            (7.1, 12.6, "Eigenvalues and Eigenvectors ke bare mein. Jab bhi koi matrix space par apply hota hai,"),
            (13.2, 17.9, "toh wo sab kuch rotate aur stretch kar deta hai. Saare vectors apni direction kho dete hain."),
            (18.0, 24.3, "Lekin beech mein kuch special axes hote hain jo bilkul nahi ghumte; direction same rehti hai."),
            (24.7, 30.3, "Inhi invariant directions ko Eigenvectors kehte hain, aur scaling factor ko Eigenvalue."),
            (31.0, 36.6, "Bridges ko resonance se bachana ho, Google PageRank ho, ya data compression —"),
            (36.7, 41.4, "har jagah Eigenvectors aur Eigenvalues ka concept apply hota hai.")
        ])),
        ("scene2", s2_off, scale_cues("scene2_intro", durs, [
            (0.2, 4.5, "Ab hum log iski exact definition ko dekhte hain."),
            (4.6, 11.5, "Normally ek n x n matrix A kisi vector x se multiply hota hai, toh naya vector Ax banta hai."),
            (12.2, 16.5, "Uske angle aur length dono change ho jaate hain, jaisa left box mein dikh raha hai."),
            (16.6, 23.5, "Lekin agar koi non-zero vector v golden equation Av = lambda v satisfy kare, toh magic hota hai:"),
            (23.6, 28.6, "Matrix multiplication simplify ho kar ek simple scalar scaling ban jaati hai."),
            (29.0, 34.0, "Yahan non-zero vector v hamara Eigenvector hai, aur number lambda ek Eigenvalue."),
            (34.5, 41.5, "Matlab is special line par matrix sirf ek multiplier ki tarah kaam karta hai."),
            (42.0, 49.1, "Lambda > 1 ho toh stretch, 0 aur 1 ke beech shrink, aur negative ho toh direction reverse!")
        ])),
        ("scene3", s3_off, scale_cues("scene3_visual", durs, [
            (0.2, 4.0, "Ab iski geometry aur animation ke through samajhte hain."),
            (4.2, 11.2, "Maan lete hain hamare paas 2 x 2 matrix A hai: first row [2, 1] aur second row [1, 2]."),
            (11.5, 16.0, "Pehle left graph mein red vector u = [1, 0] ko dekhte hain."),
            (16.2, 24.8, "Matrix apply hote hi ye [2, 1] par aa jaata hai (~26 degrees tilt). Matlab ye eigenvector nahi hai."),
            (25.2, 29.3, "Ab dhyan se dekho jaise unit circle stretch ho kar ek ellipse ban raha hai!"),
            (29.6, 35.5, "Ab diagonal line y = x par agar hum vector v1 = [1, 1] lete hain,"),
            (35.8, 47.2, "toh ye bina rotate hue bilkul isi line ke along 3 times stretch ho kar [3, 3] par pahunch jaata hai."),
            (48.5, 56.9, "Ye ellipse ki major axis hai, aur pehli eigenvalue lambda1 = 3."),
            (57.8, 65.3, "Ab yellow colour ki perpendicular line y = -x par vector v2 = [-1, 1] bilkul change nahi hua."),
            (65.7, 75.1, "Na length badli na angle (1x minor axis), toh doosri eigenvalue lambda2 = 1 hai."),
            (75.7, 83.5, "Notice karo ye dono eigenvectors 90 degrees par hain, aur yahi space ka natural skeleton banate hain.")
        ])),
        ("scene4", s4_off, scale_cues("scene4_math", durs, [
            (0.2, 8.1, "Par exam ya coding mein bina graph banaye math se values kaise nikalenge? Step-by-step dekhte hain."),
            (8.7, 14.5, "First step: Av = lambda v se start karenge. Rearrange karne par (A - lambda I)v = 0 milta hai."),
            (15.3, 26.5, "Kyunki v zero nahi ho sakta, determinant det(A - lambda I) = 0 hona chahiye (Characteristic Equation)."),
            (27.3, 35.0, "Ab determinant solve karke characteristic equation se lambda ki values nikalte hain."),
            (35.4, 44.0, "Jaisa aap dekh sakte ho, expand karne par (2 - lambda)^2 - 1 = 0 milta hai,"),
            (44.6, 53.4, "jo quadratic equation lambda^2 - 4*lambda + 3 = 0 ban jaati hai."),
            (53.8, 63.6, "Iske factors (lambda - 3)(lambda - 1) = 0 se lambda1 = 3 aur lambda2 = 1 milta hai."),
            (64.5, 75.1, "Ab eigenvectors ke liye in values ko wapas (A - lambda I)v = 0 equation mein fill karte hain,"),
            (75.8, 78.4, "aur hume dono orthogonal eigenvectors v1 = [1, 1] aur v2 = [-1, 1] mil jaate hain.")
        ])),
        ("scene5", s5_off, scale_cues("scene5_eigenbasis", durs, [
            (0.2, 4.6, "Ab aate hain last mein Diagonalization: A = P D P^-1 par."),
            (5.0, 10.6, "Normal x, y axes mein matrix A variables ko aapas mein mix kar deta hai, jisse calculation mushkil hoti hai."),
            (11.1, 20.4, "Lekin coordinate system v1, v2 par shift karne se A ek simple diagonal matrix D = diag(3, 1) ban jaata hai."),
            (21.0, 30.9, "Practical use: Maan lo kisi bridge vibration ya Markov chain ke liye A^100 nikalna hai."),
            (31.4, 45.0, "Left box dekho: normal tarike se A ko 100 baar multiply karne mein bahut time, memory aur rounding errors aate hain."),
            (45.4, 53.4, "Lekin right box: eigenbasis mein A^100 nikalna sirf 1 second ka kaam hai!"),
            (54.3, 64.3, "Bas 3^100 along v1 aur 1^100 along v2 — complex problem bilkul simple scalar calculation ban jaati hai!")
        ])),
        ("scene6", s6_off, scale_cues("scene6_summary", durs, [
            (0.2, 10.8, "End mein bas 3 points yaad rakhna: Pehla, Eigenvectors jo transformation ke baad rotate nahi hote, sirf scale hote hain."),
            (11.4, 16.5, "Doosra, Eigenvalues jo hum det(A - lambda I) = 0 solve karke nikalte hain."),
            (16.8, 22.1, "Teesra, Diagonalization jo complex matrix systems ko bilkul aasaan bana deta hai."),
            (22.6, 30.0, "Thank you so much! Ye animation video aur poora Python code maine (Ritesh Kumar) banaya.")
        ]))
    ]

def generate_srt(out_file="subtitles.srt"):
    durs = load_durations()
    scene_cues = build_scene_cues(durs)
    index = 1
    prev_end = 0.0
    with open(out_file, "w") as f:
        for scene_name, base_offset, cues in scene_cues:
            for s_start, s_end, text in cues:
                abs_start = base_offset + s_start
                abs_end = base_offset + s_end
                assert abs_start >= prev_end - 1e-6, f"Subtitle overlap in {scene_name}: {abs_start:.3f} < {prev_end:.3f}"
                assert abs_end > abs_start, f"Invalid subtitle range in {scene_name}"
                prev_end = abs_end
                f.write(f"{index}\n")
                f.write(f"{format_time(abs_start)} --> {format_time(abs_end)}\n")
                f.write(f"{text}\n\n")
                index += 1
    print(f"Generated {index - 1} synced subtitle cues (0 overlaps) -> {out_file}")

if __name__ == "__main__":
    generate_srt()
