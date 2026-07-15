import pytest
import os
import sys

# Ensure backend folder is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "backend")))

from analyzer import count_filler_words, analyze_audio_features

def test_count_filler_words():
    text = "Um, so basically, like, I think machine learning is, you know, very useful."
    count = count_filler_words(text)
    assert count == 5  # um, so, basically, like, you know

def test_analyze_audio_features_empty():
    # Test fallback behavior when file doesn't exist
    features = analyze_audio_features("non_existent_file.wav")
    assert features["average_pitch"] == 0.0
    assert features["average_energy"] == 0.0
    assert features["pause_rate"] == 0.0
