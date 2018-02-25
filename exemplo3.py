# Exemplo3

''' fi_x = a1 * g1(x) + a2 * g2(x) + a3 * g13(x) + ... + an * gn(x) '''
# Separar cada função g1(x),g2(x),g3(x)...
# OBS: CRIAR UM VETOR DE FUNCOES [g1(x),g2(x),g3(x)...]

pontos = [ [ -2.0, -1.0,  0.0,  1.0,  2.0,  3.0, 4.0 ],
           [  2.9, -1.9, -4.7, -6.2, -5.1, -2.1, 3.2 ]]

def g1(x):
    return x**2

def g2(x):
    return x

def g3(x):
    return 1

G = [g1, g2, g3]
