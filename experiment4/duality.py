import numpy as np
import matplotlib.pyplot as plt

x = np.array(eval(input("Enter x1: ")));

N = x.size 

X = np.fft.fft(x)
x_back = np.fft.fft(X)

fig, ax = plt.subplots(2, 1);
ax[0].stem(x);
ax[0].set_title("x");
ax[0].grid(True);

ax[1].stem(np.abs(x_back / N));
ax[1].set_title("DFT[DFT[x]] / N");
ax[1].grid(True);

fig.tight_layout();
plt.show();