# sine_wave.py
import numpy as np
import matplotlib.pyplot as plt

def plot_sine_wave():
    x = np.linspace(0, 2 * np.pi, 1000)
    y = np.sin(2 * x)  # Change the frequency by multiplying x by 2

    plt.plot(x, y)
    plt.title('Modified Sine Wave')  # Update the title if needed
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.show()

if __name__ == "__main__":
    plot_sine_wave()