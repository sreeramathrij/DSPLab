import numpy as np;
import matplotlib.pyplot as plt;

x = np.linspace(-10, 10, 60);
np.arange(0, 10)

quart = len(x) // 4;

sine = np.sin(x);
cosine = np.cos(x);
ramp = x;

impulse = np.zeros(len(x));
impulse[(2*quart)] = 1;

rect = np.where(np.abs(x) <= 5, 1, 0);

bipolar = np.concatenate((np.zeros(quart), np.ones(quart), -np.ones(quart), np.zeros(quart)));

triangular = np.concatenate((-10 - x[0:quart], x[quart:3*quart], 10 - x[3*quart:]))

# fig, axs = plt.subplots(2, 4);
# axs[0, 0].plot(x, sine);
# axs[0, 1].plot(x, cosine);
# axs[0, 2].plot(x, ramp);
# axs[0, 3].plot(x, impulse);
# axs[1, 0].plot(x, rect);
# axs[1, 1].plot(x, bipolar);
# axs[1, 2].plot(x, triangular);

fig, axs = plt.subplots(2, 4);
axs[0, 0].stem(x, sine);
axs[0, 1].stem(x, cosine);
axs[0, 2].stem(x, ramp);
axs[0, 3].stem(x, impulse);
axs[1, 0].stem(x, rect);
axs[1, 1].stem(x, bipolar);
axs[1, 2].stem(x, triangular);


plt.show();