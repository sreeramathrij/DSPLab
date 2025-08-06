import numpy as np
import matplotlib.pyplot as plt

def cross_correlate(x, y):
  x = np.array(x)
  y = np.array(y)
  N = x.size
  M = y.size

  output_len = N + M - 1
  crosscorrelation = np.zeros(output_len)
  lag = np.arange(-(N-1), N)
  
  for i in range(output_len):
    m = lag[i]
    s = 0
    
    for n in range(N):
      if 0 <= n - m < N:
        s += x[n] * y[n-m]
    crosscorrelation[i] = s;
  
  return crosscorrelation;
x = np.array(eval(input("Enter x: ")));
y = np.array(eval(input("Enter y: ")))
Rxy = cross_correlate(x, y);

fig, ax = plt.subplots(3, 1);
ax[0].stem(x)
ax[0].set_title("x(n)");
ax[0].grid(True);

ax[1].stem(y);
ax[1].set_title("y(n)");
ax[1].grid(True);

ax[2].stem(Rxy);
ax[2].set_title("Rxy");
ax[2].grid(True);

fig.tight_layout();
plt.show();