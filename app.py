
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# TITLE
st.title("📡 Smart Signal Analyzer")

# AIM
st.header("🎯 Aim")
st.write("""
To design and develop a Smart Signal Analyzer using Streamlit 
to generate signals and analyze them using FFT.
""")

# THEORY
st.header("📚 Theory")
st.write("""
A signal is a function that conveys information.

**Time Domain:**
Represents signal variation with respect to time.

**Frequency Domain:**
Represents signal in terms of frequencies present.

**FFT (Fast Fourier Transform):**
FFT converts a signal from time domain to frequency domain 
and helps identify dominant frequency components.

**Applications:**
- Communication systems
- Audio processing
- Biomedical signals (ECG, EEG)
""")

# INPUT SECTION
st.header("⚙️ Input Parameters")

wave_type = st.selectbox("Wave Type", ["Sine", "Cosine"])
freq = st.slider("Frequency (Hz)", 1, 50, 5)
amp = st.slider("Amplitude", 1, 10, 2)
noise_level = st.slider("Noise Level", 0.0, 1.0, 0.1)

# TIME AXIS
fs = 500
t = np.linspace(0, 1, fs)

# SIGNAL GENERATION
if wave_type == "Sine":
    signal = amp * np.sin(2 * np.pi * freq * t)
else:
    signal = amp * np.cos(2 * np.pi * freq * t)

# ADD NOISE
noise = noise_level * np.random.randn(len(t))
noisy_signal = signal + noise

# FFT
fft_vals = np.abs(np.fft.fft(noisy_signal))
freq_axis = np.fft.fftfreq(len(noisy_signal), 1/fs)

# TIME DOMAIN
st.header("📊 Time Domain Signal")
fig1, ax1 = plt.subplots()
ax1.plot(t, noisy_signal, label="Noisy Signal")
ax1.plot(t, signal, linestyle='dashed', label="Original Signal")
ax1.set_xlabel("Time")
ax1.set_ylabel("Amplitude")
ax1.legend()
st.pyplot(fig1)

# FREQUENCY DOMAIN
st.header("📈 Frequency Domain (FFT)")
fig2, ax2 = plt.subplots()
ax2.plot(freq_axis[:fs//2], fft_vals[:fs//2])
ax2.set_xlabel("Frequency (Hz)")
ax2.set_ylabel("Magnitude")
st.pyplot(fig2)

# RESULT
st.header("📌 Result")
st.write(f"Wave Type: {wave_type}")
st.write(f"Frequency: {freq} Hz")
st.write(f"Amplitude: {amp}")
st.write(f"Noise Level: {noise_level}")
st.success("FFT peak indicates dominant frequency component.")

# QUIZ
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
    "2. What is the unit of frequency?",
    ["Volt", "Hz", "Seconds"]
)
if q2 == "Hz":
    st.success("Correct ✅")
elif q2:
    st.error("Wrong ❌")

q3 = st.radio(
    "3. Which domain shows amplitude vs time?",
    ["Frequency Domain", "Time Domain", "Phase Domain"]
)
if q3 == "Time Domain":
    st.success("Correct ✅")
elif q3:
    st.error("Wrong ❌")

# CONCLUSION
st.header("📌 Conclusion")
st.write("""
The Smart Signal Analyzer was successfully developed using Streamlit.

The application allows users to generate and analyze signals in both 
time and frequency domains. FFT helps identify dominant frequencies.

This project demonstrates real-world applications of signal processing 
in an interactive way.
""")
