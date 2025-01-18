import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

def record_audio(duration=5, sample_rate=44100):
    print("Recording...")
    audio_signal = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
    sd.wait()  
    print("Recording finished.")
    return audio_signal.flatten() 

def quantize_to_bits(audio_signal, bit_depth=16):
    
    normalized_signal = np.clip(audio_signal, -1, 1)  
    quantized_signal = ((normalized_signal + 1) * (2**(bit_depth - 1) - 1)).astype(int)  

    
    binary_signal = np.array([f"{sample:0{bit_depth}b}" for sample in quantized_signal])

    return binary_signal

def plot_audio_signal(audio_signal, sample_rate=44100, bit_depth=8):
    # Time axis for plotting
    time_axis = np.linspace(0, len(audio_signal) / sample_rate, num=len(audio_signal))

    # Plot continuous audio signal
    plt.figure(figsize=(10, 8))

    # Digital Signal (idealized)
    plt.subplot(3, 1, 1)
    plt.plot(time_axis, audio_signal, label='Audio Signal', color='b')
    plt.title('Digital Audio Signal')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.grid(True)


    binary_signal = quantize_to_bits(audio_signal, bit_depth=bit_depth)
   
    time_axis_binary = np.arange(len(binary_signal))


    plt.subplot(3, 1, 2)
    for i in range(bit_depth): 
        plt.step(time_axis_binary, [int(binary_signal[j][i]) for j in range(len(binary_signal))],
                 label=f'Bit {i+1}', where='mid', linestyle='-', alpha=0.6)

    plt.title('Digital Bit Representation of Audio Signal')
    plt.xlabel('Sample Index')
    plt.ylabel('Bit Value [0 or 1]')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()



audio_signal = record_audio(duration=5, sample_rate=44100)


plot_audio_signal(audio_signal, sample_rate=44100, bit_depth=8)
