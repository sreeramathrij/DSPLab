import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 2, 4, 0, 1])
h = np.array([1, 1, 1])

L = 4
M = h.size
N = L + M - 1

h_padded = np.pad(h, (0, N-M))

x_padded = np.pad(x, (M-1, 0))

blocks = [x_padded[i: i+N] for i in range(0, x_padded.size - N + 1, L)]

if x_padded.size % L != (M-1) % L:
  last_block_start = len(blocks) * L
  if last_block_start < x_padded.size:
    last_block = x_padded[last_block_start:]
    last_block = np.pad(last_block, (0, N-last_block.size))
    blocks.append(last_block)

y = np.zeros(x.size + M - 1)
cursor = 0

for b, block in enumerate(blocks):
  Y_blk = np.fft.ifft(np.fft.fft(block) * np.fft.fft(h_padded)).real

  y_valid = Y_blk[M-1:]

  end_idx = min(cursor+len(y_valid), len(y))

  y[cursor: end_idx] = y_valid[: end_idx - cursor]

  cursor += L

n = np.arange(y.size)
y_regular = np.convolve(x, h)
n_regular = np.arange(y_regular.size)

fig, a = plt.subplots(2, 1, figsize=(10, 8))

a[0].stem(n, y)
a[0].set_title("Overlap-Save Block Convolution")
a[0].set_xlabel("n")
a[0].set_ylabel("Amplitude")
a[0].grid(True)

a[1].stem(n_regular, y_regular)
a[1].set_title("Regular Convolution")
a[1].set_xlabel("n")
a[1].set_ylabel("Amplitude")
a[1].grid(True)

fig.tight_layout()
plt.show()