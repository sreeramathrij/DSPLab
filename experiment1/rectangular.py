import numpy as np
import matplotlib.pyplot as plt

time_range = float(input("Enter the time range for the rectangular wave (e.g., 5(for -5 to 5)): "));
amplitude = float(input("Enter the amplitude of the rectangular wave: "));
value = float(input("Enter the time_range the rectangular wave is active, eg: 1(for 0 to 1 and -1 to 0): "));

t = np.linspace(-time_range, time_range, 1000);
n = np.linspace(-time_range, time_range, 50);

rect_t = np.where(np.abs(t) < value, amplitude, 0);
rect_n = np.where(np.abs(n) < value, amplitude, 0);

fig, a = plt.subplots(2, 1);

a[0].plot(t, rect_t, label="Rectangular Waveform", color="blue")
a[0].set_title("Rectangular Waveform");
a[0].set_xlabel("Time");
a[0].set_ylabel("Amplitude");
a[0].grid(True);

a[1].stem(n, rect_n, label="Rectangular Waveform")
a[1].set_title("Rectangular sWaveform (Discrete)");
a[1].set_xlabel("Time");
a[1].set_ylabel("Amplitude");
a[1].grid(True);

plt.tight_layout();
plt.show();
