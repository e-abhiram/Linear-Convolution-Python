import numpy as np
import matplotlib.pyplot as plt
x = np.array(list(map(int, input("Enter x[n] values separated by space: ").split())))
h = np.array(list(map(int, input("Enter h[n] values separated by space: ").split())))
N = len(x)
M = len(h)
y_manual = np.zeros(N + M - 1)
for n in range(N + M - 1):
for k in range(N):
if 0 <= n - k < M:
y_manual[n] += x[k] * h[n - k]
y_numpy = np.convolve(x, h)
print("Manual:", y_manual)
print("NumPy:", y_numpy)
plt.figure(figsize=(10, 8))
plt.subplot(3, 1, 1)
plt.stem(x)
plt.title("Input Signal x[n]")
plt.grid(True)
plt.subplot(3, 1, 2)
plt.stem(h)
plt.title("Impulse Response h[n]")
plt.grid(True)
plt.subplot(3, 1, 3)
plt.stem(y_manual)
plt.title("Output Signal y[n]")
plt.grid(True)
plt.tight_layout()
plt.show()
