import numpy as np
import matplotlib.pyplot as plt

def convolve(x1, x2):
  len_y = len(x1) + len(x2) - 1
  toplitz_matrix = np.zeros((len_y, len(x1)))
  for i in range(len_y):
    for j in range(len(x1)):
      if 0 <= i-j < len(x2):
        toplitz_matrix[i, j] = x2[i-j];

  return toplitz_matrix @ x1;
x = [1, 2, 3, 4]
h = [1, 2]

n = np.arange(-10, 11)

x_padded = np.zeros_like(n)
h_padded = np.zeros_like(n)
x_padded[10:10+len(x)] = x
h_padded[10:10+len(h)] = h

y = convolve(x, h)

y_padded = np.zeros(len(n))
start = 10
end = start + len(y)
if end > len(y_padded):
    y_padded = np.pad(y_padded, (0, end - len(y_padded)))
y_padded[start:end] = y

fig, a = plt.subplots(1, 1)

a.stem(n, y_padded)
a.set_title("Linear Convolution y(n)")
a.set_xlabel("f")
a.set_ylabel("Amplitude")
a.grid(True)

fig.tight_layout()
plt.show()