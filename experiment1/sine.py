import numpy as np
import matplotlib.pyplot as plt

time_range = float(input("Enter the time range for the sine wave (e.g., 5(for -5 to 5)): "));
amplitude = float(input("Enter the amplitude of the sine wave: "));
frequency = float(input("Enter the frequency of the sine wave (in Hz): "));

t = np.linspace(-time_range, time_range, 1000);
n = np.linspace(-time_range, time_range, 200);

sine_t = np.sin(2* frequency * np.pi * t ) * amplitude;
sine_n = np.sin(2 * frequency * np.pi * n ) * amplitude;

fig, a = plt.subplots(2, 1);

a[0].plot(t, sine_t, label="Sine Waveform", color="blue")
a[0].set_title("Sine Waveform");
a[0].set_xlabel("Time");
a[0].set_ylabel("Amplitude");
a[0].grid(True);

a[1].stem(n, sine_n, label="Sine Waveform")
a[1].set_title("Sine Waveform (Discrete)");
a[1].set_xlabel("Time");
a[1].set_ylabel("Amplitude");
a[1].grid(True);

plt.tight_layout();
plt.show();
