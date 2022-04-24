#---- Imports ----#
import math 
import random
import numpy as np
import matplotlib.pyplot as plt

random.seed()

#---- Predefinições para os cálculos ----#

T_med_filme = 132*60 #seg
fps = 24
N_f = T_med_filme*fps
filme = range(N_f)

N_tentativas = 100
loop_max = 12

tentativas = np.zeros((N_tentativas))

freq_piscada = 24 #[piscadas/minuto]
T_medio_piscada = 0.3 #[segundos]

Prob = freq_piscada/(60*fps)
print("A probabilidade de piscar em um frame vale {:.3%}".format(Prob))

#---- Loop para assistir o filme ----#

for m in range(N_tentativas):

    blink = np.zeros((loop_max,N_f))
    blink_cum = np.zeros((loop_max,N_f))

    for j in range(loop_max):

        for i in range(N_f):
            if i>0:
                if ((random.random() <= Prob) and (blink[j,i-1] == 0)):
                    
                    T_piscada = T_medio_piscada + random.random()*0.1
                    NFpiscada = math.ceil(fps*T_piscada)
                    
                    if (i >= ((N_f) - (NFpiscada-1))):
                        blink[j,i:N_f] = 1
                    else:
                        blink[j,i:i+(NFpiscada)] = 1

                if (j == 0):
                    blink_cum[j,i] = blink[j,i]
    
                if (j > 0):
                    blink_cum[j,i] = blink_cum[j-1,i]*blink[j,i]
                    
    
        a = sum(blink_cum[j,:])
        print(a)

        if a == 0:
            tentativas[m] = j + 1 #o número de tentativas é o loop que parou + 1, pois, no loop 0 -> 1a tentativa.
            break 
        

#---- Contabilização das tentativas ----#      
mediaTentativas = np.mean(tentativas)
print(mediaTentativas)

contagem_pdf = np.zeros(10+1)
contagem_cdf = np.zeros(10+1)

for k in range(10+1):
    contagem_pdf[k] = np.sum(tentativas == k)

for k in range(10+1):
    contagem_cdf[k] = np.sum(tentativas <= k)

contagem_pdf = contagem_pdf/(np.size(tentativas))
contagem_cdf = contagem_cdf/(np.size(tentativas))

#---- Plotagem ----#

def autolabel(grupos,ax):
    for i in grupos:
        h = i.get_height()
        ax.annotate('{:.1%}'.format(h),
                    xy = (i.get_x() + i.get_width()/2,h),
                    xytext = (0,3),
                    textcoords = 'offset points',
                    ha = 'center')

nmin = 5
nmax = 10

fig = plt.figure(figsize = [8,6])

pdfplot = plt.subplot(121)
pdf = pdfplot.bar(np.arange(len(contagem_pdf))[nmin:nmax+1],contagem_pdf[nmin:nmax+1])
pdfplot.set_title("Proporção do número de tentativas\n em relação ao total",fontsize = 10)
pdfplot.set_xlabel("Número de tentativas")
pdfplot.set_ylabel("Proporção")

autolabel(pdf,pdfplot)

cdfplot = plt.subplot(122)
cdf = cdfplot.bar(np.arange(len(contagem_cdf))[nmin:nmax+1],contagem_cdf[nmin:nmax+1])
cdfplot.set_title("Probabilidade de ter assistido",fontsize = 10)
cdfplot.set_xlabel("Número de tentativas")
cdfplot.set_ylabel("Probabilidade")

autolabel(cdf,cdfplot)

plt.suptitle('Estudo das piscadas')
plt.show()

