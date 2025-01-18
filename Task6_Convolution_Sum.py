import numpy as np
import matplotlib.pyplot as plt

# Given signals
x = [1, 2, 3,4]  
h = [1, -1, 2,3]  

# Step 1: Folding
h_folded = [0] * len(h) 

for i in range(len(h)):
    h_folded[i] = h[len(h) - 1 - i]


y = [0] * (len(x) + len(h) - 1)


for n in range(len(y)):
    total_sum = 0
    for k in range(len(x)):
        if 0 <= n-k < len(h):
            shift = h_folded[n-k]  # Shifting
            mul = x[k] * shift  # Multiplication
            total_sum += mul  # Summation
    y[n] = total_sum


# Print the signals
print("Input signal x[n]:", x)
print("Impulse response h[n]:", h)
print("Flipped impulse response h[n] (folded):", h_folded)
print("Convolution Sum y[n]:", y)

# Plot the signals and their convolution result
plt.figure(figsize=(10, 6))

# Plot input signal x[n]
plt.subplot(3, 1, 1)
plt.stem(range(len(x)), x, basefmt="r")
plt.title("Input Signal x[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)

# Plot impulse response h[n]
plt.subplot(3, 1, 2)
plt.stem(range(len(h)), h, basefmt="g")
plt.title("Impulse Response h[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)

# Plot the convolution sum signal y[n]
plt.subplot(3, 1, 3)
plt.stem(range(len(y)), y, basefmt="b")
plt.title("Convolution Sum y[n]")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()