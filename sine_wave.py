# sine_wave.py
import numpy as np
import matplotlib.pyplot as plt

def plot_sine_wave():
    x = np.linspace(0, 2 * np.pi, 1000)  # Generate x values from 0 to 2*pi
    y = np.sin(x)  # Calculate corresponding y values using the sine function

    plt.plot(x, y)  # Plot the sine wave
    plt.title('Sine Wave')  # Set the plot title
    plt.xlabel('Time')  # Set the x-axis label
    plt.ylabel('Amplitude')  # Set the y-axis label
    plt.show()  # Display the plot

if __name__ == "__main__":
    plot_sine_wave()