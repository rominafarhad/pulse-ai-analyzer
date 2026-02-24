import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from signal_generator import generate_complex_pulse

def detect_anomalies(signal):
    """
    Uses AI (Isolation Forest) to detect corrupted parts of the signal.
    This is key for Predictive Maintenance in Engineering.
    """
    # Reshape signal for Scikit-Learn (Needs 2D array)
    data = signal.reshape(-1, 1)
    
    # Initialize the AI model
    # contamination=0.05 means we expect 5% of data to be anomalous (noisy)
    model = IsolationForest(contamination=0.05, random_state=42)
    
    # Fit the model and predict (-1 for anomaly, 1 for normal)
    predictions = model.fit_predict(data)
    return predictions

if __name__ == "__main__":
    # 1. Generate noisy signal
    t, clean, noisy = generate_complex_pulse()
    
    # 2. Run AI Anomaly Detection
    results = detect_anomalies(noisy)
    
    # 3. Visualization
    plt.figure(figsize=(12, 6))
    plt.plot(t, noisy, color='gray', alpha=0.5, label='Original Noisy Signal')
    
    # Highlight anomalies in red
    anomalies = noisy[results == -1]
    t_anomalies = t[results == -1]
    plt.scatter(t_anomalies, anomalies, color='red', s=10, label='AI Detected Anomalies')
    
    plt.title("AI-Powered Signal Anomaly Detection")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude [V]")
    plt.legend()
    plt.grid(True)
    plt.show()