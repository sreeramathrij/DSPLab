import numpy as np;
import matplotlib.pyplot as plt;

def fft(x):
  x = np.array(x, dtype=complex)
  N = x.size

  if N == 1:
    return x
  if np.log2(N) % 1 != 0:
    print("size of x must be a power of 2")
    return
  
  X_even = fft(x[::2])
  X_odd = fft(x[1::2])

  factor = np.exp(-2j * np.pi * np.arange(N) / N)

  return np.concatenate([X_even + factor[:N // 2] * X_odd, X_even - factor[:N//2] * X_odd])


x = [1,2,3,4,5,6,7,8]

fig, ax = plt.subplots(2, 1);


ax[0].stem(np.abs(fft(x)));
ax[1].stem(np.abs(np.fft.fft(x)));

fig.tight_layout()
plt.show();
 