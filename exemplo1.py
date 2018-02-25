# Exemplo1

''' fi_x = a1 * g1(x) + a2 * g2(x) + a3 * g13(x) + ... + an * gn(x) '''
# Separar cada função g1(x),g2(x),g3(x)...
# OBS: CRIAR UM VETOR DE FUNCOES [g1(x),g2(x),g3(x)...]

pontos = [ [ -1.0, -0.75,  -0.6,  -0.5,  -0.3,  0.0, 0.2, 0.4, 0.5, 0.7, 1.0],
                    [  2.05, 1.153, 0.45, 0.4, 0.5, 0.0, 0.2, 0.6, 0.512, 1.2, 2.05 ]]

def g1(x):
    return x**2

G = [g1]
