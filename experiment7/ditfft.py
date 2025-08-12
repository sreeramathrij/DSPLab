import numpy as np;
import matplotlib.pyplot as plt;

def bit_reverse_indices(N):
  bits = int(np.log2(N))
  reversal = np.zeros(N, dtype=int);

  for i in range(N):
    b = bin(i)[2:].zfill(bits)
    reversal[i] = int(b[::-1], 2);

  return reversal;

def ditfft(x):
  x = np.array(x, dtype=complex)
  N = x.size

  indices = bit_reverse_indices(N)
  X = x[indices].copy()

  stages = int(np.log2(N))
  for s in range(1, stages+1):
    m = 2**s
    m_by_2 = m // 2
    W_m = np.exp(-2j * np.pi * np.arange(m_by_2) / m)
    for k in range(0, N, m):
      for j in range(m_by_2):
        t = W_m[j] * X[k + j + m_by_2]
        u = X[k+j]
        X[k+j] = u + t
        X[k + j + m_by_2] = u - t 

  return X

x = [1,2,3,4,5,6,7,8]

fig, ax = plt.subplots(2, 1);

ax[0].stem(np.abs(ditfft(x)));
ax[1].stem(np.abs(np.fft.fft(x)));

fig.tight_layout()
plt.show();