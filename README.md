# DSPLab

This repository contains code for digital signal processing (DSP) lab experiments. It is designed to generate and visualize basic discrete-time signals commonly used in DSP. Currently, the repository includes **Experiment 1: Basic Signals**, with each signal implemented in a separate Python script under the `experiment1/` directory. Each script generates one signal and plots its waveform.

## 🔧 Setup and Installation

To run the experiments, you need Python 3 with NumPy and Matplotlib. Follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sreeramathrij/DSPLab.git
   cd DSPLab
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Linux/macOS:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install required packages**:
   ```bash
   pip install numpy matplotlib
   ```

5. **Run the experiment scripts**:
   ```bash
   python experiment1/sine.py
   ```

# Experiment 1: Elementary Signals

## AIM:
To plot sine, cosine, ramp, exponential, impulse, rectangular, bipolar pulse and triangular signals in continuous and discrete forms.

| File            | Description                        |
|-----------------|------------------------------------|
| `sine.py`       | Generates a sine wave              |
| `cosine.py`     | Generates a cosine wave            |
| `triangular.py` | Generates a triangular waveform    |
| `rectangular.py`| Generates a rectangular pulse      |
| `bipolar.py`    | Generates a bipolar waveform       |
| `impulse.py`    | Generates a unit impulse           |
| `ramp.py`       | Generates a ramp function          |
| `exponential.py`| Generates an exponential signal    |

## 📐 Signal Equations
<img src="assets/experiment1eq(1).png" alt="sin" />

## 📷 Example Outputs

Each script generates and plots a waveform. Add the output images in the respective directory and name them as follows:
### SINE
<img src="assets/sine.png" alt="sin" />

---

### COSINE
<img src="assets/cosine.png" alt="cos" />

---

### EXPONENTIAL
<img src="assets/exponential.png" alt="exp" />

---

### RAMP
<img src="assets/ramp.png" alt="ramp" />

---

### RECTANGULAR
<img src="assets/rectangular.png" alt="rect" />

---

### IMPULSE
<img src="assets/impulse.png" alt="impulse" />

---

### BIPOLAR
<img src="assets/bipolar.png" alt="bipolar" />

---

### TRIANGULAR
<img src="assets/triangular.png" alt="triangle" />

---

### COMPOSITE
<img src="assets/composite.png" alt="composite" />

---

### TRUNCATED
<img src="assets/truncated.png" alt="truncated" />

---

### SINC
<img src="assets/sinc.png" alt="sinc" />

---

# Experiment 2: Basic Time Functions on Signals

## AIM:
To plot shifting, scaling, reversing and their combination of elementary signals.

| File                          | Description                                                 |
|-------------------------------|-------------------------------------------------------------|
| `basicOperationsContinuos.py` | Generates all the time functions in continuous time         |
| `basicOperationsDiscrete.py`  | Generates all the time functions in discrete time           |
| `impulseFromUnit.py`          | Generates a dirac delta function from unit step function    |
| `inverseShiftedExponential.py`| Generates the $-(2^n) u(-n-1)$ signal                       |
| `scaledRect.py`               | Generates the $rect(8t)$ and $rect(t / 8)$ signals          |
| `scaledShiftedUnit.py`        | Generates the $u(-3t + 5)$ signal                           |

## 📐 Signal Equations
<img src="assets/experiment2/experiment2.png" alt="All Experiment 2 Equations" />

## 📷 Example Outputs

### BASIC OPERATIONS (CONTINUOUS)
<img src="assets/experiment2/basicOperationsContinuous.png" alt="basicOperationsContinuous" />

---

### BASIC OPERATIONS (DISCRETE)
<img src="assets/experiment2/basicOperationsDiscrete.png" alt="basicOperationsDiscrete" />

---

### IMPULSE FROM UNIT
<img src="assets/experiment2/impulseFromUnit.png" alt="Impulse From Unit" />

---

### SCALED SHIFTED EXPONENTIAL
<img src="assets/experiment2/scaledShiftedExponential.png" alt="Scaled Shifted Exponential" />

---

### SCALED RECT
<img src="assets/experiment2/scaledRect.png" alt="Scaled Rect" />

---

### SCALED AND SHIFTED UNIT
<img src="assets/experiment2/scaledShiftedUnit.png" alt="Scaled Shifted Unit" />

---

## 👤 Author

Developed by [sreeramathrij](https://github.com/sreeramathrij)
