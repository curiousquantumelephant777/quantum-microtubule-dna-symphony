import numpy as np
import matplotlib.pyplot as plt

# 1. Spatial matrix from Mitochondria (left) to Nuclear LINC complex (right)
x = np.linspace(-5, 5, 1000)
wave_number = 9.0 # High-frequency terahertz component

# 2. Simulate the wave moving and focusing over 3 structural steps
plt.figure(figsize=(12, 8))

colors = ["#ffb6c1", "#8844aa", "#00aa55"]
labels = [
"Step 1: UPE Generation (Focused through DNA)",
"Step 2: LINC complex Propagation (ER Gaussian Waveguide)",
"Step 3: Energy Focusing and UPE/Electron Coupling (Mitochondrial Cristae)"
]

# We recursively change the decay factor (alpha) to simulate "focusing"
alpha_values = [0.2, 0.8, 2.5]

for i in range(3):
  alpha = alpha_values[i]

  # Calculate Gaussian Envelope and Sinusoidal component
  envelope = np.exp(-alpha * (x - (i - 1))**2) # Shift center forward each step
  wave = np.cos(wave_number * (x - (i - 1)))
  wave_packet = envelope * wave

  # Plot each phase in a subplot to show progression
  plt.subplot(3, 1, i + 1)
  plt.plot(x, wave_packet, color=colors[i], lw=2, label=labels[i])
  plt.plot(x, envelope, '--', color='plum', alpha=0.5)
  plt.plot(x, -envelope, '--', color='plum', alpha=0.5)

  plt.xlim(-5, 5)
  plt.ylim(-1.2, 1.2)
  plt.legend(loc="upper left")
  if i == 0:
    plt.title("Recursive Spatial Focusing: DNA to Microtubules to Mitochondria", fontsize=14, fontweight='bold', color='purple')

plt.tight_layout()
plt.show()
