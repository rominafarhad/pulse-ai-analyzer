import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter
from signal_generator import generate_complex_pulse

def butter_lowpass_filter(data, cutoff, fs, order=5):
    """
    Standard Butterworth Lowpass Filter to remove high-frequency noise.
    """
    nyq = 0.5 * fs  # Nyquist Frequency
    normal_cutoff = cutoff / nyq
    # Get the filter coefficients
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = lfilter(b, a, data)
    return y

if __name__ == "__main__":
    # 1. Generate the same noisy signal
    fs = 2000  # Sampling rate
    t, clean, noisy = generate_complex_pulse(sampling_rate=fs)
    
    # 2. Apply the Filter (Cutoff frequency = 15Hz)
    filtered_signal = butter_lowpass_filter(noisy, cutoff=15, fs=fs, order=4)
    
    # 3. Visual Comparison
    plt.figure(figsize=(12, 7))
    
    plt.subplot(2, 1, 1)
    plt.plot(t, noisy, color='red', alpha=0.4, label='Noisy Input')
    plt.title("Before Processing: Raw Sensor Data with EMI")
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(t, filtered_signal, color='green', linewidth=2, label='Filtered Output')
    plt.plot(t, clean, 'b--', alpha=0.5, label='Original Ideal Reference')
    plt.title("After DSP: Cleaned Signal using Butterworth Lowpass Filter")
    plt.xlabel("Time [s]")
    plt.grid(True)
    plt.legend()
    
    plt.tight_layout()
    plt.show()