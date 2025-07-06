import numpy as np
import matplotlib.pyplot as plt

time_range = float(input("Enter the time range for the exponential wave (e.g., 5(for -5 to 5)): "));
amplitude = float(input("Enter the amplitude of the exponential wave: "));

t = np.linspace(-time_range, time_range, 1000);
n = np.linspace(-time_range, time_range, 50);
exp_t = np.exp(t) * amplitude;
exp_n = np.exp(n) * amplitude;

fig, a = plt.subplots(2, 1);

a[0].plot(t, exp_t, label="Bipolar Waveform", color="blue")
a[0].set_title("Bipolar Waveform");
a[0].set_xlabel("Time");
a[0].set_ylabel("Amplitude");
a[0].grid(True);

a[1].stem(n, exp_n, label="Bipolar Waveform")
a[1].set_title("Bipolar Waveform (Discrete)");
a[1].set_xlabel("Time");
a[1].set_ylabel("Amplitude");
a[1].grid(True);

plt.show();
