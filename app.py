 import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# TITLE
st.title("📡 Smart Signal Analyzer")

# SIDEBAR MENU
section = st.sidebar.selectbox(
    "Select Section",
    ["Aim", "Theory", "Simulation", "Quiz", "Conclusion"]
)

# ---------------- AIM ----------------
if section == "Aim":
    st.header("🎯 Aim")
    st.write("""
    To design and develop a Smart Signal Analyzer using Streamlit 
    to generate signals and analyze them using FFT.
    """)

# ---------------- THEORY ----------------
elif section == "Theory":
    st.header("📚 Theory")
    st.write("""
    A signal is a function that conveys information.

    **Time Domain:**
    Represents signal with respect to time.

    **Frequency Domain:**
    Represents signal with respect to frequency.

    **FFT (Fast Fourier Transform):**
    Converts signal from time domain to frequency domain.

    **Applications:**
    - Communication systems
    - Audio processing
    - Biomedical signals (ECG, EEG)
    """)

# ---------------- SIMULATION ----------------
elif section == "Simulation":
    st.header("⚙️ Signal Simulation & Analysis")

    wave_type = st.selectbox("Wave Type", ["Sine", "Cosine"])
    freq = st.slider("Frequency (Hz)", 1, 50, 5)
    amp = st.slider("Amplitude", 1, 10, 2)
    noise_level = st.slider("Noise Level", 0.0, 1.0, 0.1)

    fs = 500
    t = np.linspace(0, 1, fs)

    if wave_type == "Sine":
        signal = amp * np.sin(2 * np.pi * freq * t)
    else:
        signal = amp * np.cos(2 * np.pi * freq * t)

    noise = noise_level * np.random.randn(len(t))
    noisy_signal = signal + noise

    fft_vals = np.abs(np.fft.fft(noisy_signal))
    freq_axis = np.fft.fftfreq(len(noisy_signal), 1/fs)

    # Time domain
    st.subheader("📊 Time Domain")
    fig1, ax1 = plt.subplots()
    ax1.plot(t, noisy_signal, label="Noisy")
    ax1.plot(t, signal, linestyle='dashed', label="Original")
    ax1.legend()
    st.pyplot(fig1)

    # Frequency domain
    st.subheader("📈 Frequency Domain")
    fig2, ax2 = plt.subplots()
    ax2.plot(freq_axis[:fs//2], fft_vals[:fs//2])
    st.pyplot(fig2)

# ---------------- QUIZ ----------------
elif section == "Quiz":
    st.header("📝 Quiz")

    q1 = st.radio(
        "1. What does FFT do?",
        ["Time to Frequency conversion", "Frequency to Time conversion", "Noise removal"]
    )
    if q1 == "Time to Frequency conversion":
        st.success("Correct ✅")
    elif q1:
        st.error("Wrong ❌")

    q2 = st.radio(
        "2. Unit of frequency?",
        ["Volt", "Hz", "Seconds"]
    )
    if q2 == "Hz":
        st.success("Correct ✅")
    elif q2:
        st.error("Wrong ❌")

# ---------------- CONCLUSION ----------------
elif section == "Conclusion":
    st.header("📌 Conclusion")
    st.write("""
    The Smart Signal Analyzer was successfully developed using Streamlit.

    It allows users to visualize signals in both time and frequency domains.
    FFT helps identify dominant frequencies.

    This project demonstrates real-world signal processing applications.
    """)
