import numpy as np;
import matplotlib.pyplot as plt;

n = np.arange(-10, 11);

u = lambda x: np.where(x >= 0, 1, 0);

fig, a = plt.subplots(1,1)

a.stem(n, -2.0**n * u(-n-1))
a.set_title('-2^n * u(-n-1)')
a.set_xlabel("Time")
a.set_ylabel("Amplitude")
a.grid(True)

fig.tight_layout();
plt.show();