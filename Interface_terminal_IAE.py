import numpy as np
import control as cnt
import matplotlib.pyplot as plt
from scipy.io import loadmat

# Obter entrada do usuário para os parâmetros do controlador
kp = float(input("Digite o valor de kp para PID - Por Integral do Erro: "))
Ti = float(input("Digite o valor de Ti para PID - Por Integral do Erro: "))
Td = float(input("Digite o valor de Td para PID - Por Integral do Erro: "))
kp_chr = float(input("Digite o valor de kp para PID - CHR: "))
Ti_chr = float(input("Digite o valor de Ti para PID - CHR: "))
Td_chr = float(input("Digite o valor de Td para PID - CHR: "))

# Considerando a função de transferência em malha aberta: FT=k/(tau*s+1)
k = 3.489
tau = 14.865
Theta = 3.045  # atraso de propagação

# Escrevendo a função de transferência da planta
num = np.array([k])
den = np.array([tau, 1])
H = cnt.tf(num, den)
n_pade = 20
(num_pade, den_pade) = cnt.pade(Theta, n_pade)
H_pade = cnt.tf(num_pade, den_pade)
Hs = cnt.series(H, H_pade)

plt.xlabel('t [s]')
plt.ylabel('Amplitude')
plt.title('Controle PID - INTEGRAL DO ERRO')

# Controlador PID - Por Integral do Erro
numkp = np.array([kp])
denkp = np.array([1])
numki = np.array([kp / Ti])
denki = np.array([1, 0])
numkd = np.array([kp * Td, 0])
denkd = np.array([1])
Hkp = cnt.tf(numkp, denkp)
Hki = cnt.tf(numki, denki)
Hkd = cnt.tf(numkd, denkd)
Hctrl1 = cnt.parallel(Hkp, Hki)
Hctrl = cnt.parallel(Hctrl1, Hkd)
Hdel = cnt.series(Hs, Hctrl)
Hcl = cnt.feedback(Hdel, 1)

t = np.linspace(0, 100, 100)
(t, y) = cnt.step_response(16 * Hcl, t)
plt.plot(t, y, color="yellow")

# Controlador PID - CHR
numkp = np.array([kp_chr])
denkp = np.array([1])
numki = np.array([kp_chr / Ti_chr])
denki = np.array([1, 0])
numkd = np.array([kp_chr * Td_chr, 0])
denkd = np.array([1])
Hkp = cnt.tf(numkp, denkp)
Hki = cnt.tf(numki, denki)
Hkd = cnt.tf(numkd, denkd)
Hctrl1 = cnt.parallel(Hkp, Hki)
Hctrl = cnt.parallel(Hctrl1, Hkd)
Hdel = cnt.series(Hs, Hctrl)
Hcl = cnt.feedback(Hdel, 1)

t = np.linspace(0, 100, 100)
(t, y) = cnt.step_response(16 * Hcl, t)
plt.plot(t, y)

# Considerando novamente a função de transferência da planta
num = np.array([k])
den = np.array([tau, 1])
H = cnt.tf(num, den)
n_pade = 20
(num_pade, den_pade) = cnt.pade(Theta, n_pade)
H_pade = cnt.tf(num_pade, den_pade)
Hs = cnt.series(H, H_pade)

# Realimentando
Hmf = cnt.feedback(Hs, 1)

t = np.linspace(0, 100, 100)
(t, y) = cnt.step_response(16 * Hs, t)
(t, y1) = cnt.step_response(16 * Hmf, t)
plt.plot(t, y, color="blue")
plt.plot(t, y1, color='brown')

mat = loadmat('TransferFunction16.mat')

# Variáveis
degrau = mat.get('degrau')
saida = mat.get('saida')
t1 = mat.get('t')

plt.plot(t1.T, saida, label='Saída', color='green')
plt.plot(t1.T, degrau, label='Degrau de entrada', color='orange')

plt.grid()
plt.show()
