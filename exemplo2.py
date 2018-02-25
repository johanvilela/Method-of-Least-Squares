# Exemplo2 - Conjunto nº2 (primeiro exemplo da aula)

''' fi_x = a1 * g1(x) + a2 * g2(x) + a3 * g13(x) + ... + an * gn(x) '''
# Separar cada função g1(x),g2(x),g3(x)...
# OBS: CRIAR UM VETOR DE FUNCOES [g1(x),g2(x),g3(x)...]

pontos = [ [ 1.0, 3.0, 5.0 ],
           [ 1.0, 2.0, 6.0 ]]

def g1(x):
    return x

def g2(x):
    return 1

G = [g1, g2]
