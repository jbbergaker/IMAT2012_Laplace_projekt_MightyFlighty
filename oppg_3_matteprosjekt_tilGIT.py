
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

# oppgave 3 c
numerator = [0, 2000**2]
dominator = [1, 2*0.5*2000, 2000**2]
system = sig.TransferFunction(numerator, dominator) 
x, y = sig.step(system)

plt.plot(x, y, label='v_inn')
plt.xlabel('tid')
plt.ylabel('respons')
plt.title('stepfunksjon')
plt.grid()
plt.show()