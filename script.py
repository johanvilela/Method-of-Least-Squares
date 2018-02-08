import numpy as np
import matplotlib.pyplot as plt

####  ETAPA I  ####

# Entrada do conjunto de pontos

# Conjunto nº0
# pontos = np.array([ [0.0,0.0],
#                     [0.0,0.0]])
# Conjunto nº1
pontos = np.array([ [ -2.0, -1.0,  0.0,  1.0,  2.0,  3.0, 4.0 ],
                    [  2.9, -1.9, -4.7, -6.2, -5.1, -2.1, 3.2 ]])

print(pontos)

# Plotando os pontos
plt.plot(pontos[1],'ro')
plt.show()
