import numpy as np
import matplotlib.pyplot as plt

time_range = float(input("Enter the time range for the triangular wave (e.g., 5(for -5 to 5)): "));
frequency = float(input("Enter the frequency of the triangular wave: "));
amplitude = float(input("Enter the amplitude of the triangular wave: "));
t = np.linspace(-time_range, time_range, 1000);
n = np.linspace(-time_range, time_range, 60);

T = 1 / frequency

triangle_test = 2 * amplitude * np.abs(-((t/T) + np.floor(t/T) + 0.5)) - amplitude;
triangular_t = 2 * amplitude * np.abs(2 * (-((t + T / 4) / T) + np.floor(((t + T / 4)/ T) + 0.5))) - amplitude;
triangular_n = 2 * amplitude * np.abs(2 * (-((n + T / 4) / T) + np.floor(((n + T / 4) / T) + 0.5))) - amplitude;
fig, a = plt.subplots(2, 1);

a[0].plot(t, triangle_test, label="Triangular Waveform", color="blue")
a[0].set_title("Triangular Waveform");
a[0].set_xlabel("Time");
a[0].set_ylabel("Amplitude");
a[0].grid(True);

a[1].stem(n, triangular_n, label="Triangular Waveform")
a[1].set_title("Triangular Waveform (Discrete)");
a[1].set_xlabel("Time");
a[1].set_ylabel("Amplitude");
a[1].grid(True);

plt.tight_layout();
plt.show();
