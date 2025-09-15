import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000)

f1 = 50
f2 = 200

x = np.sin(2*np.pi*f1*t) + np.sin(2*np.pi*f2*t)

M = 21
h = np.ones(M) / M

y = np.convolve(x, h, mode='same')

w = np.linspace(-np.pi, np.pi, 1024)
H = np.fft.fftshift(np.fft.fft(h, 1024))

fig, ax = plt.subplots(3,1)

ax[0].plot(t, x)
ax[0].plot(t, y, label="", linewidth=2)
ax[0].set_title('Time-Domain Signals')
ax[0].grid(True)

ax[1].stem(np.arange(M), h)
ax[1].set_title('FIR Filter Impulse Response (h[n])')
ax[1].grid(True)

ax[2].plot(w/np.pi, 20*np.log10(np.abs(H)/np.max(np.abs(H))))
ax[2].set_title('Frequency Response of FIR Filter')
ax[2].grid(True)

plt.show()