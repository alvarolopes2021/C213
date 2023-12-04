import numpy as np
import control as cnt
import matplotlib.pyplot as plt
from scipy.io import loadmat
#considerando uma função de transferencia em malha aberta FT=k/(tau*s+1)
k = float(input("Enter the value for k: "))
tau = float(input("Enter the value for tau: "))
Theta = float(input("Enter the value for Theta: "))
setpoint = float(input("Enter the setpoint: "))
#parâmetros do controlador kp+kp/(Ti*s)+kp*Td*s


#kp = 0.6*14.865 / 3.489 * 3.045 = 0,8395
kp_chr= (0.6*tau) / (k*Theta) #ori = 0.8395 #25% 0.2098 #15% = 0.1259
Ti_chr= tau # == tau
Td_chr= 0.5*Theta # 0.5 * theta

#escrevendo a função de transferência da planta
num = np. array ([k])
den = np. array ([tau , 1])
H = cnt.tf(num , den)
n_pade = 20
( num_pade , den_pade ) = cnt.pade ( Theta , n_pade )
H_pade = cnt.tf( num_pade , den_pade )
Hs = cnt.series (H , H_pade)

plt.xlabel ( ' t [ s ] ')
plt.ylabel('Amplitude')
plt.title('Controle PID - CHR e COHEN COON SEM AJUSTE')


# Controlador proporcional -> CHR 1
numkp = np. array ([kp_chr])
denkp = np. array ([1])
#integral
numki = np. array ([kp_chr])
denki = np. array ([Ti_chr,0])
#derivativo
numkd = np. array ([kp_chr*Td_chr,0])
denkd = np. array ([1])
#Construindo o controlador PID
Hkp = cnt.tf(numkp , denkp)
Hki=cnt.tf(numki , denki)
Hkd=cnt.tf(numkd , denkd)
Hctrl1 = cnt.parallel (Hkp , Hki)
Hctrl = cnt.parallel (Hctrl1 , Hkd)
Hdel = cnt.series (Hs , Hctrl)
#Fazendo a realimentação
Hcl = cnt.feedback(Hdel, 1)

t = np . linspace (0 , 100 , 100)
(t , y ) = cnt.step_response (setpoint* Hcl, t )
plt.plot (t , y, label='Saida chr 1', color="yellow")


# realimentando a função de transferencia incial
Hmf = cnt.feedback(Hs, 1)

t = np . linspace (0 , 100 , 100)
# step_response(sys, t)
(t , y ) = cnt.step_response ( setpoint * Hs, t )
(t , y1 ) = cnt.step_response ( setpoint * Hmf, t )
plt.plot (t , y, label='Saida calculada', color="blue")
plt.plot (t , y1, label='Saida com realimentacao', color='brown')

plt.step(t,[setpoint],label='degrau de entrada')

plt.legend(loc="upper left")

plt.grid ()
plt.show()