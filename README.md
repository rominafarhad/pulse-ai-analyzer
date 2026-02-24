# Pulse-AI-Analyzer 🚀
### Digital Signal Processing (DSP) & AI-Based Anomaly Detection

This repository contains a professional Python-based engineering tool designed to simulate, process, and analyze digital pulse signals. It demonstrates the integration of traditional **Signal Processing** with **Modern Machine Learning** for predictive maintenance.



## 🛠 Features
* **Pulse Generation:** Simulates realistic digital pulses incorporating **Timing Jitter** and **Gaussian Noise (EMI)**.
* **DSP Filtering:** Implements a **4th-order Butterworth Low-pass Filter** to recover clean signals from noisy data.
* **AI Diagnostics:** Utilizes the **Isolation Forest** algorithm to detect signal anomalies and potential system failures.

## 📁 Project Structure
* `signal_generator.py`: Generates the raw, noisy digital signals.
* `signal_processor.py`: Applies frequency-domain filtering to clean the signal.
* `pulse_ai.py`: Uses Scikit-Learn to identify points of failure (Anomalies).

## 📊 Technical Details
* **Sampling Rate ($f_s$):** 2000 Hz
* **Filter Type:** Butterworth Low-pass
* **AI Model:** Unsupervised Isolation Forest (Contamination: 5%)

## 🚀 How to Run
1.  **Clone the Repo:**
    ```bash
    git clone [https://github.com/rominafarhad/pulse-ai-analyzer.git](https://github.com/rominafarhad/pulse-ai-analyzer.git)
    ```
2.  **Activate Virtual Environment:**
    ```bash
    source .venv/Scripts/activate
    ```
3.  **Install Dependencies:**
    ```bash
    pip install numpy matplotlib scipy scikit-learn
    ```
4.  **Execute the AI Module:**
    ```bash
    python pulse_ai.py
    ```

## 🎓 Academic Significance
This project serves as a portfolio piece for:
* Digital Signal Processing (DSP)
* Machine Learning for Engineering Applications
* Predictive Maintenance in Digital Systemsss