import numpy as np
import control as cnt
import matplotlib.pyplot as plt
from scipy.io import loadmat
#considerando uma função de transferencia em malha aberta FT=k/(tau*s+1)
k = 3.489
tau = 14.865
Theta = 3.045 # atraso de propagação
#parâmetros do controlador kp+kp/(Ti*s)+kp*Td*s

#kp = 0.6*14.865 / 3.489 * 3.045 = 0,8395
kp_chr=0.8395 
Ti_chr=14.865 # == tau
Td_chr= 1.5225 # 0.5 * theta

# por integral do erro
kp = 0.7079
Ti = 13.4850
Td = 0.1651

print(kp)
print(Ti)
print(Td)
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
plt.title('Controle PID - INTEGRAL DO ERRO')



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
(t , y ) = cnt.step_response (16* Hcl, t )
plt.plot (t , y, color="yellow")



# Controlador proporcional -> INTEGRAL DO ERRO
numkp = np. array ([kp])
denkp = np. array ([1])
#integral
numki = np. array ([kp])
denki = np. array ([Ti,0])
#derivativo
numkd = np. array ([kp*Td,0])
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
(t , y ) = cnt.step_response (16* Hcl, t )
plt.plot (t , y )


###
num = np. array ([k])
den = np. array ([tau , 1])
H = cnt.tf(num , den)
n_pade = 20
( num_pade , den_pade ) = cnt.pade ( Theta , n_pade )
H_pade = cnt.tf( num_pade , den_pade )
Hs = cnt.series (H , H_pade)

# realimentando
Hmf = cnt.feedback(Hs, 1)

t = np . linspace (0 , 100 , 100)
(t , y ) = cnt.step_response ( 16 * Hs, t )
(t , y1 ) = cnt.step_response ( 16 * Hmf, t )
plt.plot (t , y, color="blue")
plt.plot (t , y1, color='brown')



mat=loadmat('TransferFunction16.mat')
#print(mat)
#Variáveis
degrau = mat.get('degrau')
saida=mat.get('saida')
t1 = mat.get('t')

plt.plot(t1.T,saida, label='Saída', color='green')
plt.plot(t1.T,degrau,label='degrau de entrada', color='orange')

plt.grid ()
plt.show()