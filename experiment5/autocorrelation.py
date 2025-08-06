import numpy as np
import matplotlib.pyplot as plt

def auto_correlate(x):
  x = np.array(x)
  N = x.size

  output_len = 2*N - 1
  autocorrelation = np.zeros(output_len)
  lag = np.arange(-(N-1), N)
  for i in range(output_len):
    
    m = lag[i]
    s = 0
    
    for n in range(N):
      if 0 <= n - m < N:
        s += x[n] * x[n-m]
    autocorrelation[i] = s;
  
  return autocorrelation;
x = np.array(eval(input("Enter x1: ")));

Rxx = auto_correlate(x);

fig, ax = plt.subplots(2, 1);
ax[0].stem(x)
ax[0].set_title("x(n)");
ax[0].grid(True);

ax[1].stem(Rxx);
ax[1].set_title("Rxx");
ax[1].grid(True);

fig.tight_layout();
plt.show();