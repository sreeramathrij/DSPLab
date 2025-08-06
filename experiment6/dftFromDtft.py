import numpy as np
import matplotlib.pyplot as plt

x = np.array(eval(input("Enter x: ")))
N = x.size

freq_resolution = 1000
omega = np.linspace(0, 2 * np.pi, freq_resolution)

X_dtft = np.array([np.sum(x * np.exp(-1j * w * np.arange(N))) for w in omega])


X_dft = np.fft.fft(x);

omega_k = ( 2 * np.pi * np.arange(N) / N )
indices = [np.argmin(np.abs(omega - w_k)) for w_k in omega_k]

X_dft_from_dtft = X_dtft[indices]

fig, ax = plt.subplots(2, 2);
ax[0][0].stem(np.abs(X_dft));
ax[0][0].set_title("|DFT[x]|");
ax[0][0].grid(True);

ax[0][1].stem(np.angle(X_dft));
ax[0][1].set_title("/_DTFT[x]");
ax[0][1].grid(True);

ax[1][0].stem(np.abs(X_dft_from_dtft));
ax[1][0].set_title("|DFT[x]| from DTFT");
ax[1][0].grid(True);

ax[1][1].stem(np.angle(X_dft_from_dtft));
ax[1][1].set_title("/_DFT[x] from DTFT");
ax[1][1].grid(True);

fig.tight_layout();
plt.show();