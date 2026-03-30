import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title("📡 Smart Signal Analyzer")

st.write("Analyze signals in Time and Frequency Domain using FFT")

# Sidebar inputs
st.sidebar.header("Input Parameters")

wave_type = st.sidebar.selectbox("Wave Type", ["Sine", "Cosine"])
freq = st.sidebar.slider("Frequency (Hz)", 1, 50, 5)
amp = st.sidebar.slider("Amplitude", 1, 10, 2)
noise_level = st.sidebar.slider("Noise Level", 0.0, 1.0, 0.1)

# Time axis
fs = 500
t = np.linspace(0, 1, fs)

# Generate signal
if wave_type == "Sine":
    signal = amp * np.sin(2 * np.pi * freq * t)
else:
    signal = amp * np.cos(2 * np.pi * freq * t)

# Add noise
noise = noise_level * np.random.randn(len(t))
noisy_signal = signal + noise

# FFT computation
fft_vals = np.abs(np.fft.fft(noisy_signal))
freq_axis = np.fft.fftfreq(len(noisy_signal), 1/fs)

# Time domain plot
st.subheader("📊 Time Domain Signal")
fig1, ax1 = plt.subplots()
ax1.plot(t, noisy_signal, label="Noisy Signal")
ax1.plot(t, signal, linestyle='dashed', label="Original Signal")
ax1.set_xlabel("Time")
ax1.set_ylabel("Amplitude")
ax1.legend()
st.pyplot(fig1)

# Frequency domain plot
st.subheader("📈 Frequency Domain (FFT)")
fig2, ax2 = plt.subplots()
ax2.plot(freq_axis[:fs//2], fft_vals[:fs//2])
ax2.set_xlabel("Frequency (Hz)")
ax2.set_ylabel("Magnitude")
st.pyplot(fig2)

# Info
st.subheader("📌 Signal Info")
st.write(f"Wave Type: {wave_type}")
st.write(f"Frequency: {freq} Hz")
st.write(f"Amplitude: {amp}")
st.write(f"Noise Level: {noise_level}")

# Insight
st.success("FFT peak shows the dominant frequency component.")
