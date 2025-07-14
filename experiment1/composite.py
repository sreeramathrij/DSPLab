import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-0.005, 0.005, 1000);
n = np.linspace(-0.005, 0.005, 200);

composite_t = 10 * np.sin(6280 * t) + 5 * np.cos(3140 * t)
composite_n = 10 * np.sin(6280 * n) + 5 * np.cos(3140 * n)

fig, a = plt.subplots(1, 1);

a.plot(t, composite_t, label="Sine Waveform", color="blue")
a.set_title("Sine Waveform");
a.set_xlabel("Time");
a.set_ylabel("Amplitude");
a.grid(True);

plt.tight_layout();
plt.show();

