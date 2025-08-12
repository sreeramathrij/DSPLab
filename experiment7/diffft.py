import numpy as np;
import matplotlib.pyplot as plt;

def bit_reverse_indices(N):
  bits = int(np.log2(N))
  reversal = np.zeros(N, dtype=int);

  for i in range(N):
    b = bin(i)[2:].zfill(bits)
    reversal[i] = int(b[::-1], 2);

  return reversal;

def diffft(x):
  x = np.array(x, dtype=complex)
  N = x.size

  length = N
  while length > 1:
    m_by_2 = length // 2
    W_m = np.exp(-2j * np.pi * np.arange(m_by_2) / length)
    for i in range(0, N, length):
      for j in range(m_by_2):
        u = x[i + j]
        v = x[i + j + m_by_2]
        x[i + j] = u + v
        x[i + j + m_by_2] = (u - v) * W_m[j]

    length = m_by_2

  indices = bit_reverse_indices(N)

  return x[indices]


x = [1,2,3,4,5,6,7,8]

fig, ax = plt.subplots(2, 1);

ax[0].stem(np.abs(diffft(x)));
ax[1].stem(np.abs(np.fft.fft(x)));

fig.tight_layout()
plt.show();
 
        
