import numpy as np
import matplotlib.pyplot as plt

def invDFT(X):
  X = np.array(X, dtype="complex");
  N = len(X);
  x = np.zeros(N, dtype="complex");

  for k in range(N):
    s = 0;
    for n in range(N):
      angle = 2j * np.pi * k * n / N;
      s += X[n] * np.exp(angle);
    x[k] = s / N
  
  return x;

X = [10 + 0j, -2 + 2j, -2 + 0j, -2 - 2j]

x = invDFT(X);

n = np.arange(len(x));

fig, a = plt.subplots(1,1);

a.stem(n, x);
a.set_title("x(n)");
a.set_xlabel("Time");
a.set_ylabel("Amplitude");
a.grid(True)

fig.tight_layout();
plt.show();