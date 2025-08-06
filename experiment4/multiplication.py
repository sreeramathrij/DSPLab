import numpy as np
import matplotlib.pyplot as plt

def circular_convolve(a, b):
    N = len(a)
    result = np.zeros(N, dtype=complex)
    for k in range(N):
        for m in range(N):
            result[k] += a[m] * b[(k - m) % N]
    return result

x1 = np.array(eval(input("Enter x1: ")));
x2 = np.array(eval(input("Enter x2: ")));

N = x1.size 

X1 = np.fft.fft(x1)
X2 = np.fft.fft(x2)

X_circconv = circular_convolve(X1, X2)

X_mult = np.fft.fft(x1 * x2)

fig, ax = plt.subplots(2, 1);
ax[0].stem(np.abs(X_circconv / N));
ax[0].set_title("Circular Convolution of DFT[x1] and DFT[x2]");
ax[0].grid(True);

ax[1].stem(np.abs(X_mult));
ax[1].set_title("Magnitude of DFT[x1 * x2]");
ax[1].grid(True);

fig.tight_layout();
plt.show();