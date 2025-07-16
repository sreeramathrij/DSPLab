import numpy as np;
import matplotlib.pyplot as plt;

t = np.linspace(-4, 4, 1000);

u = lambda x: np.where(x >= 0, 1, 0);

basic_op = {
  "u(-t)": u(-t),
  "u(t-2)": u(t-2),
  "u(2t)": u(2*t),
  "u(2t - 2)": u(2*t - 2),
}

basic_op_list = list(basic_op.items())

fig, a = plt.subplots(2,2)

i=0;
for row in range(2):
  for col in range(2):
    a[row][col].plot(t, basic_op_list[i][1])
    a[row][col].set_title(basic_op_list[i][0])
    a[row][col].set_xlabel("Time")
    a[row][col].set_ylabel("Amplitude")
    a[row][col].grid(True)
    i+=1

fig.tight_layout();
plt.show();