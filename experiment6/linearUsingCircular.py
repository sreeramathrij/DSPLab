import numpy as np;
import matplotlib.pyplot as plt

def circ_convolve(a, b):
  N = a.size
  result = np.zeros(N, dtype=complex)
  for k in range(N):
    for n in range(N):
      result[k] += a[n] * b[(k - n) % N]

  return result;

x1 = np.array(eval(input("Enter x1: ")))
x2 = np.array(eval(input("Enter x2: ")))

Nx1 = x1.size;
Nx2 = x2.size;

Ny = Nx1 + Nx2 - 1;

x1_padded = np.pad(x1, (0, (Ny - Nx1)));
x2_padded = np.pad(x2, (0, (Ny - Nx2)));

X1 = np.fft.fft(x1_padded);
X2 = np.fft.fft(x2_padded);

Y = X1 * X2;

y = np.fft.ifft(Y).real;

fig, ax = plt.subplots(2, 1);
ax[0].stem(np.convolve(x1, x2));
ax[0].set_title("Linear Convolution of x1 and x2");
ax[0].grid(True);

ax[1].stem(y);
ax[1].set_title("Linear Convolution from circular convolution of x1 and x2");
ax[1].grid(True);

fig.tight_layout();
plt.show();
