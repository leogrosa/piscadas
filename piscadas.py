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

N_tentativas = 10
ntotal = 1

loop_max = 15

tentativas = np.zeros((ntotal,N_tentativas))

freq_piscada = 24 #[piscadas/minuto]
T_medio_piscada = 0.3 #[segundos]

Prob = freq_piscada/(60*fps)
print(Prob)

############################

for q in range(ntotal):

    blink= np.zeros((loop_max,N_f,N_tentativas))
    blink_cum = np.zeros((loop_max,N_f,N_tentativas))

    for m in range(0,N_tentativas-1):

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
            print(a)

            if a == 0 and j>0:
                tentativas[q,m] = j
                break 
  
