import numpy as np
import matplotlib.pyplot as plt

x = np.array(eval(input("Enter x1: ")));

N = x.size

X = np.fft.fft(x)

k = 1;

x_shift = np.zeros(N)

for i in range(N):
  for j in range(k):
    if(i == N-1):
      x_shift[0] = x[i]
      continue
    x_shift[i+1] = x[i]

X_shift = np.fft.fft(x_shift)
W = np.exp(-2j * np.pi * k * np.arange(N) / N)

fig, ax = plt.subplots(2, 1);
ax[0].stem(np.abs(X_shift));
ax[0].set_title("Magnitude of DFT[x(n-1)]");
ax[0].grid(True);

ax[1].stem(np.abs(X * W));
ax[1].set_title("Magnitude of aDFT[x1] + bDFT[x2]");
ax[1].grid(True);

fig.tight_layout();
plt.show();