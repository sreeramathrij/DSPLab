import numpy as np
import matplotlib.pyplot as plt

x = np.array(eval(input("Enter x1: ")));

X = np.fft.fft(x)

energy_time = np.sum(np.abs(x) ** 2);
energy_frequency = np.sum(np.abs(X) ** 2) / x.size;

print(f"Energy in time domain: {energy_time}")
print(f"Energy in frequency domain: {energy_frequency}")

fig, ax = plt.subplots(1, 1);
ax.bar([0,1], [energy_time, energy_frequency], tick_label=["Time Domain", "Frequency Domain"]);
ax.set_title("Parseval's Theorem Energy Comparison");

fig.tight_layout();
plt.show();