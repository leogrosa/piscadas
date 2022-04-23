import math 
import random
import numpy as np
import matplotlib.pyplot as plt

random.seed()

###########################

T_med_filme = 132*60 #seg
fps = 24
N_f = T_med_filme*fps
filme = range(N_f)

N_tentativas = 100
loop_max = 15

tentativas = np.zeros(N_tentativas)

freq_piscada = 24 #[piscadas/minuto]
T_medio_piscada = 0.3 #[segundos]

Prob = freq_piscada/(60*fps)
print(Prob)

############################



blink= np.zeros((loop_max,N_f,N_tentativas))
blink_cum = np.zeros((loop_max,N_f,N_tentativas))

for m in range(0,N_tentativas):

    for j in range(0,loop_max-1):

        for i in range(0,N_f-1):

            if i>0:

                if ((random.random() <= Prob) and (blink[j,i-1,m] == 0)):
                    
                    T_piscada = T_medio_piscada + random.random()*0.1
                    NFpiscada = math.ceil(fps*T_piscada)
                    
                    if (i >= ((N_f-1) - (NFpiscada))):
                        blink[j,range(i,(N_f-1)),m] = 1
                    else:
                        blink[j,range(i,i+(NFpiscada-1)),m] = 1
    
        
        if (j == 1):
            blink_cum[j,:,m] = blink[j,:,m]
    
        if (j > 1):
            blink_cum[j,:,m] = blink_cum[j-1,:,m]*blink[j,:,m]
    
        a = sum(blink_cum[j,:,m])

        if a == 0 and j>0:
            tentativas[m] = j
            break 
            

contagem_pdf = np.zeros(10)
contagem_cdf = np.zeros(10)

for k in range(0,10):
    contagem_pdf[k] = sum(tentativas == k)

for k in range(0,10):
    contagem_cdf[k] = sum(tentativas <= k)

contagem_pdf = contagem_pdf/(np.size(tentativas))
contagem_cdf = contagem_cdf/(np.size(tentativas))

fig = plt.figure(figsize = [8,6])

pdfplot = plt.subplot(121)
plt.bar(np.arange(len(contagem_pdf))[5:10],contagem_pdf[5:10])
pdfplot.set_title("Proporção do número de tentativas\n em relação ao total",fontsize = 10)
pdfplot.set_xlabel("Número de tentativas")
pdfplot.set_ylabel("Proporção")

cdfplot = plt.subplot(122)
plt.bar(np.arange(len(contagem_cdf))[5:10],contagem_cdf[5:10])
cdfplot.set_title("Probabilidade de ter assistido",fontsize = 10)
cdfplot.set_xlabel("Número de tentativas")
cdfplot.set_ylabel("Probabilidade")

plt.suptitle('Estudo das piscadas')
plt.show()

