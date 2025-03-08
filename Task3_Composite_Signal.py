import math
import matplotlib.pyplot as plt
import numpy as np


def generate_sine_wave(amplitude, frequency, time_values):
    return [amplitude * math.sin(2 * math.pi * frequency * t) for t in time_values]


def generate_step_function(time_values):
    return [1 if t >= 0 else 0 for t in time_values]


def generate_impulse_function(time_values, threshold=1e-5):
    return [1 if abs(t) < threshold else 0 for t in time_values]


def generate_composite_signal(sine_wave, step_function, impulse_function):
    return [sine_wave[i] + step_function[i] + impulse_function[i] for i in range(len(sine_wave))]


amplitude_sine = 1      
frequency_sine = 1      
num_points = 100         
t_start = -1            
t_end = 2               

#time_values = [t_start + i * (t_end - t_start) / (num_points - 1) for i in range(num_points)]
time_values=np.linspace(t_start,t_end,num_points)

sine_wave = generate_sine_wave(amplitude_sine, frequency_sine, time_values)
step_function = generate_step_function(time_values)
impulse_function = generate_impulse_function(time_values)


composite_signal = generate_composite_signal(sine_wave, step_function, impulse_function)

plt.figure(figsize=(12, 8))

# Plot sine wave
plt.subplot(4, 1, 1)
plt.plot(time_values, sine_wave, label='Sine Wave', color='blue')
plt.title('Sine Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

# Plot step function
plt.subplot(4, 1, 2)
plt.plot(time_values, step_function, label='Step Function', color='green')
plt.title('Step Function')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

# Plot impulse function
plt.subplot(4, 1, 3)
plt.plot(time_values, impulse_function, label='Impulse Function', color='red')
plt.title('Impulse Function')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

# Plot composite signal
plt.subplot(4, 1, 4)
plt.plot(time_values, composite_signal, label='Composite Signal', color='purple')
plt.title('Composite Signal (Sine + Step + Impulse)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
