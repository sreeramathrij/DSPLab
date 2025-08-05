import numpy as np
import matplotlib.pyplot as plt

def dftMatrix(x):
  x = np.array(x, dtype='complex');
  N = len(x);
  n = np.arange(N);
  k = n.reshape((N, 1));
  W = np.exp(-2j * np.pi * k * n / N)

  return W @ x;  

x = [1, 2, 3, 4]

X = dftMatrix(x);

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