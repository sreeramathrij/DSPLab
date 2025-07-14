import numpy as np
import matplotlib.pyplot as plt

time_range = float(input("Enter the time range for the sinc wave (e.g., 5(for -5 to 5)): "));
amplitude = float(input("Enter the amplitude of the sinc wave: "));
frequency = float(input("Enter the frequency of the sinc wave (in Hz): "));

t = np.linspace(-time_range, time_range, 1000);
n = np.linspace(-time_range, time_range, 200);

sinc_t = amplitude * np.sinc(2 * np.pi * frequency * t) 
sinc_n = amplitude * np.sinc(2 * np.pi * frequency * n) 

fig, a = plt.subplots(1, 1);

a.plot(t, sinc_t, label="Sinc Waveform", color="blue")
a.set_title("Sinc Waveform");
a.set_xlabel("Time");
a.set_ylabel("Amplitude");
a.grid(True);

plt.tight_layout();
plt.show();

