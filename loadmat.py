from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
mat=loadmat('TransferFunction16.mat')
#print(mat)
#Variáveis
degrau = mat.get('degrau')
saida=mat.get('saida')
t1 = mat.get('t')


plot1=plt.plot(t1.T,saida, label='Saída')
plot2=plt.plot(t1.T,degrau,label='degrau de entrada')
plt.xlabel ( ' t [ s ] ')
plt.ylabel('Amplitude')
plt.legend(loc="upper left")

plt.grid ()
plt.show()