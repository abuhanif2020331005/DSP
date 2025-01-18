import numpy as np
import matplotlib.pyplot as plt

# Original signal
x = np.array([1, 3, 1, 2, 3, 4, 1, 1])
t = np.array([-3, -2, -1, 0, 1, 2, 3, 4])

# Identity system
identity_x = x

# Unit delay: x[n-1]
unit_delay_x = np.concatenate(([0], x[:-1]))  # Pad with zero at the beginning

# Unit advance: x[n+1]
unit_advance_x = np.concatenate((x[1:], [0]))  # Pad with zero at the end

# Moving average: (x[n-1] + x[n] + x[n+1]) / 3
x_prev = np.concatenate(([0], x[:-1]))  # x[n-1] with zero padding
x_next = np.concatenate((x[1:], [0]))  # x[n+1] with zero padding
moving_average_x = (x_prev + x + x_next) / 3

# Moving median: median([x[n-1], x[n], x[n+1]])
moving_median_x = []
for i in range(len(x)):
    prev_x = x[i-1] if i > 0 else 0
    next_x = x[i+1] if i < len(x)-1 else 0
    moving_median_x.append(np.median([prev_x, x[i], next_x]))
moving_median_x = np.array(moving_median_x)

# Accumulator system: cumulative sum
accumulator_x = np.cumsum(x)

# Plotting the systems and their responses
plt.figure(figsize=(12, 10))

# Identity system
plt.subplot(3, 2, 1)
plt.stem(t, identity_x, basefmt=" ")
plt.title('Identity System (x[n])')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

# Unit delay system
plt.subplot(3, 2, 3)
plt.stem(t, unit_delay_x, basefmt=" ")
plt.title('Unit Delay System (x[n-1])')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

# Unit advance system
plt.subplot(3, 2, 5)
plt.stem(t, unit_advance_x, basefmt=" ")
plt.title('Unit Advance System (x[n+1])')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

# Moving average system
plt.subplot(3, 2, 2)
plt.stem(t, moving_average_x, basefmt=" ")
plt.title('Moving Average System')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

# Moving median system
plt.subplot(3, 2, 4)
plt.stem(t, moving_median_x, basefmt=" ")
plt.title('Moving Median System')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

# Accumulator system
plt.subplot(3, 2, 6)
plt.stem(t, accumulator_x, basefmt=" ")
plt.title('Accumulator System (Cumulative Sum)')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()
