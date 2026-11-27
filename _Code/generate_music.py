"""
Background Music Generator (Vectorized - Lightning Fast)
Synthesizes a warm, cinematic, low-volume ambient harmonic pad track
perfect for educational narration.
Total duration: ~385 seconds.
"""
import numpy as np
from scipy.io import wavfile
import subprocess
import os

SAMPLE_RATE = 44100
DURATION = 385.0  # seconds

def generate_ambient_track():
    print(f"Generating {DURATION}s ambient background music...")
    chord_progression = [
        # Dm9
        [146.83, 174.61, 220.00, 261.63, 329.63],
        # Bbmaj7
        [116.54, 146.83, 174.61, 220.00, 293.66],
        # Fmaj9
        [87.31, 130.81, 174.61, 220.00, 261.63],
        # Cadd9
        [130.81, 164.81, 196.00, 246.94, 293.66]
    ]
    chord_len = 16.0  # seconds per chord
    n_chords = int(np.ceil(DURATION / chord_len))
    
    samples_per_chord = int(SAMPLE_RATE * chord_len)
    t_chord = np.linspace(0, chord_len, samples_per_chord, endpoint=False)
    
    # Smooth bell-shaped envelope for each chord with crossfade
    fade = np.sin(np.pi * t_chord / chord_len) ** 0.5
    
    chord_audio_blocks = []
    for i in range(len(chord_progression)):
        freqs = chord_progression[i]
        block = np.zeros(samples_per_chord, dtype=np.float32)
        for f in freqs:
            block += np.sin(2 * np.pi * f * t_chord) * 0.15
            block += np.sin(2 * np.pi * (f * 2.0) * t_chord) * 0.05
            block += np.sin(2 * np.pi * (f * 0.5) * t_chord) * 0.08
        block *= fade
        chord_audio_blocks.append(block)
        
    full_blocks = []
    for k in range(n_chords):
        full_blocks.append(chord_audio_blocks[k % len(chord_progression)])
        
    audio = np.concatenate(full_blocks)
    target_samples = int(SAMPLE_RATE * DURATION)
    audio = audio[:target_samples]
    
    t = np.linspace(0, DURATION, target_samples, endpoint=False)
    # Shimmer LFO
    lfo = 0.82 + 0.18 * np.sin(2 * np.pi * 0.08 * t)
    audio = audio * lfo
    
    # Fade in / fade out
    fade_len = int(5.0 * SAMPLE_RATE)
    audio[:fade_len] *= np.linspace(0, 1, fade_len)
    audio[-fade_len:] *= np.linspace(1, 0, fade_len)
    
    # Normalize and scale to subtle background level
    audio = audio / np.max(np.abs(audio)) * 0.12
    
    os.makedirs("assets/audio", exist_ok=True)
    wav_path = "assets/audio/background_pad.wav"
    wavfile.write(wav_path, SAMPLE_RATE, (audio * 32767).astype(np.int16))
    
    mp3_path = "assets/audio/background_music.mp3"
    subprocess.run([
        "ffmpeg", "-y", "-i", wav_path,
        "-codec:a", "libmp3lame", "-qscale:a", "3",
        mp3_path
    ], check=True, capture_output=True)
    
    if os.path.exists(wav_path):
        os.remove(wav_path)
    print(f"Background music created successfully: {mp3_path}")

if __name__ == "__main__":
    generate_ambient_track()
