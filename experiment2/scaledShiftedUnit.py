import numpy as np;
import matplotlib.pyplot as plt;

t = np.linspace(-10, 10, 1000);

u = lambda x: np.where(x >= 0, 1, 0);

fig, a = plt.subplots(1,1)

a.plot(t, u(-3*t+5))
a.set_title("Impulse Signal from Unit Step Signal")
a.set_xlabel("Time")
a.set_ylabel("Amplitude")
a.grid(True)

fig.tight_layout();
plt.show();