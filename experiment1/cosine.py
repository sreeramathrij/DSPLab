import numpy as np
import matplotlib.pyplot as plt

time_range = float(input("Enter the time range for the cosine wave (e.g., 5(for -5 to 5)): "));
amplitude = float(input("Enter the amplitude of the cosine wave: "));
frequency = float(input("Enter the frequency of the cosine wave (in Hz): "));

t = np.linspace(-time_range, time_range, 1000);
n = np.linspace(-time_range, time_range, 200);

sine_t = np.cos(2 * frequency * np.pi * t ) * amplitude;
sine_n = np.cos(2 * frequency * np.pi * n ) * amplitude;

fig, a = plt.subplots(2, 1);

a[0].plot(t, sine_t, label="Cosine Waveform", color="blue")
a[0].set_title("Cosine Waveform");
a[0].set_xlabel("Time");
a[0].set_ylabel("Amplitude");
a[0].grid(True);

a[1].stem(n, sine_n, label="Cosine Waveform")
a[1].set_title("Cosine Waveform (Discrete)");
a[1].set_xlabel("Time");
a[1].set_ylabel("Amplitude");
a[1].grid(True);

plt.tight_layout();
plt.show();
