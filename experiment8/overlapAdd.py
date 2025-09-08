import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 2, 4, 0, 1]);
h = np.array([1, 1, 1]);

L = 4;
M = h.size;
N = L + M - 1;

blocks = [x[i: i+L] for i in range(0, len(x), L)];
num_blocks = len(blocks);

h_padded = np.pad(h, (0, N-M));

y = np.zeros(x.size + M - 1);
cursor = 0;

for b, block in enumerate(blocks):
  block_padded = np.pad(block, (0, N-len(block)))
  Y_blk = np.fft.ifft(np.fft.fft(block_padded)* np.fft.fft(h_padded)).real

  if b==0:
    y[:N] += Y_blk
    cursor = L
  else:
    start_overlap = cursor
    end_overlap = cursor + (M-1)
    y[start_overlap: end_overlap] += Y_blk[:M-1]

    start_new = cursor + (M-1)
    end_new = start_new + L
    if end_new <= len(y):
      y[start_new: end_new] += Y_blk[M-1: L+M-1]
    else:
      y[start_new:] += Y_blk[M-1: M-1+(len(y)-start_new)]
    
    cursor += L

y_regular = np.convolve(x, h)
fig, a = plt.subplots(2,1);

n = np.arange(len(y));
n_reg = np.arange(len(y_regular))

a[0].stem(n, y);
a[0].set_title("Block Convolution");
a[0].set_xlabel("n");
a[0].set_ylabel("Amplitude");
a[0].grid(True)

a[1].stem(n_reg, y_regular)
a[1].set_title("Regular Convolution")
a[1].set_xlabel("n")
a[1].set_ylabel("Amplitude")
a[1].grid(True)

fig.tight_layout();
plt.show();