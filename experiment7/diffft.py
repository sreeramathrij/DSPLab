import numpy as np;
import matplotlib.pyplot as plt;

def bit_reverse_indices(N):
    bits = int(np.log2(N))
    reversal = np.zeros(N, dtype=int)

    for i in range(N):
      b = bin(i)[2:].zfill(bits)
      reversal[i] = int(b[::-1], 2)
    
    return reversal

def diffft(x):
  x = np.array(x, dtype=complex)
  N = x.shape[0]
  if N == 1:
        return x
  if N % 2 != 0:
    print("size of x must be a power of 2")
    return
  even = x[:N//2] + x[N//2:]
  odd  = (x[:N//2] - x[N//2:]) * np.exp(-2j * np.pi * np.arange(N//2) / N)


  X_even = diffft(even)
  X_odd  = diffft(odd)

  X = np.concatenate([X_even, X_odd])

  return X


x = [1,2,3,4,5,6,7,8]
X = diffft(x)

N = X.size

bit_rev = bit_reverse_indices(N)

X_ordered = np.zeros(N, dtype=complex)
for i in range(N):
  X_ordered[bit_rev[i]] = X[i]

fig, ax = plt.subplots(2,1)

ax[0].stem(np.abs(X_ordered))
ax[1].stem(np.abs(np.fft.fft(x)))

fig.tight_layout()
plt.show()