import numpy as np
import matplotlib.pyplot as plt

time_range = float(input("Enter the time range for the truncated wave (e.g., 5(for -5 to 5)): "));
frequency = float(input("Enter the frequency of the truncated wave (in Hz): "));

t = np.linspace(0, time_range, 1000);
n = np.linspace(0, time_range, 200);

truncated_t = np.cos(2 * np.pi * frequency * t) * np.where((t >= 0) & (t < 1), 1, 0)

fig, a = plt.subplots(1, 1);

a.plot(t, truncated_t, label="Truncated Waveform", color="blue")
a.set_title("Truncated Waveform");
a.set_xlabel("Time");
a.set_ylabel("Amplitude");
a.grid(True);

plt.tight_layout();
plt.show();


