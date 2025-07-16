import numpy as np;
import matplotlib.pyplot as plt;

t = np.linspace(-5, 5, 1000);

rect = lambda x: np.where(np.abs(x) <= 0.5, 1, 0);

fig, a = plt.subplots(2,1)

a[0].plot(t, rect(t/8))
a[0].set_title("rect(t/8)")
a[0].set_xlabel("Time")
a[0].set_ylabel("Amplinude")
a[0].grid(True)

a[1].plot(t, rect(8*t))
a[1].set_title("rect(t/8)")
a[1].set_xlabel("Time")
a[1].set_ylabel("Amplinude")
a[1].grid(True)

fig.tight_layout();
plt.show();