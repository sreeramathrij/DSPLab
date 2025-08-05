import numpy as np
import matplotlib.pyplot as plt

def convolve(x1, x2):
  n = np.arange(-10, 11)
  y = np.zeros_like(n, dtype=float);

  for k, nk in enumerate(n):
    summation = 0;
    for m in n:
      if (nk - m) in n:
        ix_m = np.where(n==m)[0][0];
        ix_h = np.where(n == nk - m)[0][0];
        summation += x1(n)[ix_m] * x2(n)[ix_h];
        
    y[k] = summation;
  return y;

delta = lambda x: np.where(x == 0, 1, 0);

x = lambda n: delta(n) + 2 * delta(n - 1) + 3 * delta(n - 2) + 4 * delta(n - 3);
h = lambda n: delta(n) + 2 * delta(n - 1)

n = np.arange(-10, 11)

fig, a = plt.subplots(3,1);

a[0].stem(n, x(n));
a[0].set_title("x(n) = {1, 2, 3, 4}");
a[0].set_xlabel("Time");
a[0].set_ylabel("Amplitude");

a[1].stem(n, h(n));
a[1].set_title("x(n) = {1, 2}");
a[1].set_xlabel("Time");
a[1].set_ylabel("Amplitude");

a[2].stem(n, convolve(x, h));
a[2].set_title("Linear Convolution");
a[2].set_xlabel("Frequency");
a[2].set_ylabel("Amplitude");
a[2].grid(True)

fig.tight_layout();
plt.show();