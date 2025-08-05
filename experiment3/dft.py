import numpy as np
import matplotlib.pyplot as plt

def dft(x):
  x = np.array(x, dtype='complex');
  N = len(x);
  X = np.zeros(N, dtype="complex");
  for k in range(N):
    s = 0;
    for n in range(N):
      angle = -2j * np.pi * k * n / N;
      s += x[n] * np.exp(angle)  
    X[k] = s;
  
  return X;

x = [1, 2, 3, 4]

X = dft(x);

n = np.arange(len(X));

fig, a = plt.subplots(2,1);

a[0].stem(n, np.abs(X));
a[0].set_title("|X|");
a[0].set_xlabel("Magnitude");
a[0].set_ylabel("Amplitude");
a[0].grid(True)

a[1].stem(n, np.angle(X));
a[1].set_title("/_X");
a[1].set_xlabel("Phase");
a[1].set_ylabel("Amplitude");
a[1].grid(True)

fig.tight_layout();
plt.show();