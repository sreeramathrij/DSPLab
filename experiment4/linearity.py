import numpy as np
import matplotlib.pyplot as plt

x1 = np.array(eval(input("Enter x1: ")));
x2 = np.array(eval(input("Enter x2: ")));
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))

X1 = np.fft.fft(x1);
X2 = np.fft.fft(x2);

x = a*x1 + b*x2;
X = np.fft.fft(x);

fig, ax = plt.subplots(2, 1);
ax[0].stem(np.abs(X));
ax[0].set_title("Magnitude of DFT[ax1 + bx2]");
ax[0].grid(True);

ax[1].stem(np.abs(a*X1 + b*X2));
ax[1].set_title("Magnitude of aDFT[x1] + bDFT[x2]");
ax[1].grid(True);

fig.tight_layout();
plt.show();