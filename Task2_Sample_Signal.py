import matplotlib.pyplot as plt

def generate_unit_impulse(n):
    
    return [1 if i == 0 else 0 for i in n]

def generate_unit_step(n):
    
    return [1 if i >= 0 else 0 for i in n]

def generate_unit_ramp(n):
    
    return [i if i >= 0 else 0 for i in n]

def plot_discrete_signals(n, signals, titles):
  
   
    plt.figure(figsize=(10, 8))
    num_signals = len(signals)
    
    for i, signal in enumerate(signals, 1):
        plt.subplot(num_signals, 1, i)
        plt.stem(n, signal, basefmt=" ")
        plt.title(titles[i - 1])
        plt.xlabel('n')
        plt.ylabel('Amplitude')
        plt.grid(True)
    
    plt.tight_layout()
    plt.show()

# Customize range and scale
n = range(-10, 11)  # Time range from -10 to 10

# Generate signals
delta_n = generate_unit_impulse(n)
u_n = generate_unit_step(n)
r_n = generate_unit_ramp(n)

# Plot signals
signals = [delta_n, u_n, r_n]
titles = [
    'Unit Impulse Signal (delta[n])',
    'Unit Step Signal (u[n])',
    'Unit Ramp Signal (r[n])'
]

plot_discrete_signals(n, signals, titles)
