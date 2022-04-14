import matplotlib.pyplot as plt
import plot_style
import numpy as np
import pandas as pd
import time

A = 1.0
fs = 44100
f0 = 5
t = np.arange(0.0,5.0,1/fs)

sinwav = A * np.sin(np.pi*f0*t)
sindf = pd.DataFrame(data={'x':t,'y':sinwav})
sindf.to_csv('sin_wav.csv')

time.sleep(1)

read_sin = pd.read_csv('sin_wav.csv')

# plt.plot(read_sin['x'],read_sin['y'])
# plt.show()

coswav = A * np.cos(np.pi*f0*t)

# plt.plot(read_sin['x'],read_sin['y'])
# plt.plot(read_sin['x'],coswav)
# plt.savefig('sin_cos_fig.jpg')

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax1.plot(read_sin['x'],read_sin['y'])
ax1.set_xlabel('time')
ax1.set_ylabel('sin')
ax2 = fig.add_subplot(2,1,2)
ax2.plot(read_sin['x'],coswav)
ax2.set_xlabel('time')
ax2.set_ylabel('cos')
plt.subplots_adjust(wspace=0.4, hspace=0.6)
plt.show()