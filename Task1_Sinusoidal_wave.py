import math
import matplotlib.pyplot as plt

def generate_sinusoidal_wave(amplitude, frequency, duration, sampling_rate):

    num_points = int(duration * sampling_rate)  
    time_samples = [i / sampling_rate for i in range(num_points)] 
    y_values = [amplitude * math.sin(2 * math.pi * frequency * t) for t in time_samples] 
    return time_samples, y_values

def plot_wave(time_samples, y_values, title="Sinusoidal Wave", xlabel="Time [s]", ylabel="Amplitude"):

    plt.plot(time_samples, y_values)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()


amplitude = 1.0     
frequency = 1.0     
duration = 2.0      
sampling_rate = 1000 
# Generate and plot the wave
time_samples, y_values = generate_sinusoidal_wave(amplitude, frequency, duration, sampling_rate)
plot_wave(time_samples, y_values)
