import numpy as np
import matplotlib.pyplot as plt

time_range = float(input("Enter the time range for the ramp wave (e.g., 5(for -5 to 5)): "));
scalar = float(input("Enter the scalar of the ramp wave: "));

t = np.linspace(-time_range, time_range, 1000);
n = np.linspace(-time_range, time_range, 60);

ramp_t = np.where(t >= 0, t * scalar, 0)
ramp_n = np.where(n >= 0, n * scalar, 0);

fig, a = plt.subplots(2, 1);

a[0].plot(t, ramp_t, label="Ramp Waveform", color="blue")
a[0].set_title("Ramp Waveform");
a[0].set_xlabel("Time");
a[0].set_ylabel("Amplitude");
a[0].grid(True);

a[1].stem(n, ramp_n, label="Ramp Waveform")
a[1].set_title("Ramp Waveform (Discrete)");
a[1].set_xlabel("Time");
a[1].set_ylabel("Amplitude");
a[1].grid(True);

plt.tight_layout();
plt.show();
