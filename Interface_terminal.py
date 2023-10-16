import numpy as np
import control as cnt
import matplotlib.pyplot as plt
from scipy.io import loadmat

# Get k, tau, Theta from terminal
k = float(input("Enter the value for k: "))
tau = float(input("Enter the value for tau: "))
Theta = float(input("Enter the value for Theta: "))

num = np.array([k])
den = np.array([tau, 1])
H = cnt.tf(num, den)

n_pade = 20
(num_pade, den_pade) = cnt.pade(Theta, n_pade)
H_pade = cnt.tf(num_pade, den_pade)
Hs = cnt.series(H, H_pade)

Hmf = cnt.feedback(Hs, 1)

t = np.linspace(0, 100, 100)
(t, y) = cnt.step_response(16 * Hs, t)
(t, y1) = cnt.step_response(16 * Hmf, t)

plt.plot(t, y1, color='brown')
plt.xlabel('t [s]')
plt.ylabel('Amplitude')
plt.title('Planta malha fechada')

mat=loadmat('TransferFunction16.mat')

degrau = mat.get('degrau')
saida=mat.get('saida')
t1 = mat.get('t')

plot1=plt.plot(t1.T,saida, label='Saída', color='green')
plot2=plt.plot(t1.T,degrau,label='degrau de entrada', color='orange')

plt.grid()
plt.show()
