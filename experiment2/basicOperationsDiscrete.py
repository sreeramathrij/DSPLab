import numpy as np;
import matplotlib.pyplot as plt;

n = np.arange(-4, 4, 0.25);

u = lambda x: np.where(x >= 0, 1, 0);

basic_op = {
  "u(-n)": u(-n),
  "u(n-2)": u(n-2),
  "u(2n)": u(2*n),
  "u(2n - 2)": u(2*n - 2),
}

basic_op_list = list(basic_op.items())

fig, a = plt.subplots(2,2)

i=0;
for row in range(2):
  for col in range(2):
    a[row][col].stem(n, basic_op_list[i][1])
    a[row][col].set_title(basic_op_list[i][0])
    a[row][col].set_xlabel("Time")
    a[row][col].set_ylabel("Amplinude")
    a[row][col].grid(True)
    i+=1

fig.tight_layout();
plt.show();