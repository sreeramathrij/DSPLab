import numpy as np
import matplotlib.pyplot as plt

time_range = int(input("Enter the time range for the bipolar wave (e.g., 5(for -5 to 5)): "));
amplitude = int(float(input("Enter the amplitude of the bipolar wave: ")));
value = float(input("Enter the time_range the bipolar wave is active, eg: 1(for 0 to 1 and -1 to 0): "));

t = np.linspace(-time_range, time_range, 1000);
n = np.linspace(-time_range, time_range, 60);

bipolar_wave_t = np.where((t >= -value) & (t < 0), -amplitude, np.where((t >= 0) & (t < value), amplitude, 0));
bipolar_wave_n = np.where((n >= -value) & (n < 0), -amplitude, np.where((n >= 0) & (n < value), amplitude, 0));

fig, a = plt.subplots(2, 1);

a[0].plot(t, bipolar_wave_t, label="Bipolar Waveform", color="blue")
a[0].set_title("Bipolar Waveform");
a[0].set_xlabel("Time");
a[0].set_ylabel("Amplitude");
a[0].grid(True);

a[1].stem(n, bipolar_wave_n, label="Bipolar Waveform")
a[1].set_title("Bipolar Waveform (Discrete)");
a[1].set_xlabel("Time");
a[1].set_ylabel("Amplitude");
a[1].grid(True);

plt.tight_layout();
plt.show();
