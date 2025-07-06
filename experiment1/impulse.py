import numpy as np
import matplotlib.pyplot as plt

time_range = float(input("Enter the time range for the impluse wave (e.g., 5(for -5 to 5)): "));
amplitude = float(input("Enter the amplitude of the impulse wave: "));

t = np.linspace(-time_range, time_range, 1000);
n = np.linspace(-time_range, time_range, 50);

impulse_t = np.zeros_like(t);
impulse_t[len(t) // 2] = amplitude;
impulse_n = np.zeros_like(n);
impulse_n[len(n) // 2] = amplitude;

fig, a = plt.subplots(2, 1);

a[0].plot(t, impulse_t, label="Impulse Waveform", color="blue")
a[0].set_title("Impulse Waveform");
a[0].set_xlabel("Time");
a[0].set_ylabel("Amplitude");
a[0].grid(True);

a[1].stem(n, impulse_n, label="Impulse Waveform")
a[1].set_title("Impulse Waveform (Discrete)");
a[1].set_xlabel("Time");
a[1].set_ylabel("Amplitude");
a[1].grid(True);

plt.tight_layout();
plt.show();
