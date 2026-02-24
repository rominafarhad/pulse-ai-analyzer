import numpy as np
import matplotlib.pyplot as plt

def generate_complex_pulse(frequency=5, duration=1, sampling_rate=2000, noise_level=0.2, jitter_amount=0.01):
    """
    Simulates a digital pulse with real-world imperfections like Noise and Jitter.
    Useful for Digital Signal Processing (DSP) and Pulse Circuit analysis.
    """
    # Time vector
    t = np.linspace(0, duration, sampling_rate)
    
    # 1. Add Timing Jitter (Simulating clock instability in microprocessors)
    jitter = np.random.normal(0, jitter_amount, size=t.shape)
    t_jittered = t + jitter
    
    # 2. Generate Ideal Square Wave (Theoretically perfect 0s and 1s)
    clean_pulse = (np.sin(2 * np.pi * frequency * t_jittered) > 0).astype(float)
    
    # 3. Add Gaussian Noise (Simulating electromagnetic interference/EMI)
    noise = np.random.normal(0, noise_level, size=t.shape)
    noisy_pulse = clean_pulse + noise
    
    return t, clean_pulse, noisy_pulse

if __name__ == "__main__":
    # Generate the signals
    t, clean, noisy = generate_complex_pulse()
    
    # Visualization (Simulating a Digital Oscilloscope)
    plt.figure(figsize=(12, 6))
    
    # Plotting the noisy signal (Red)
    plt.plot(t, noisy, color='red', alpha=0.5, label='Real-world Noisy Signal (EMI)')
    
    # Plotting the ideal signal (Blue)
    plt.plot(t, clean, color='blue', linewidth=2, label='Ideal Digital Logic (Theory)')
    
    plt.title("Advanced Digital Pulse Analysis - Signal & Systems Project")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude [V]")
    plt.legend(loc='upper right')
    plt.grid(True, linestyle='--')
    
    # Display the plot
    plt.show()