import argparse
import math
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--ip', help='Endereço IP')
parser.add_argument('--bys', type=int, help='Máscara de sub-rede')
parser.add_argument('--re', type=int, help='número de redes')
args = parser.parse_args()

Ip = args.ip
bys = args.bys
re = args.re

def binario_decimal(decimal):
    octeto1 = decimal >> 24 & 255
    octeto2 = decimal >> 16 & 255
    octeto3 = decimal >> 8 & 255
    octeto4 = decimal & 255
    return f"{octeto1}.{octeto2}.{octeto3}.{octeto4}"

def decimal_binario(decimal):
    binario = bin(decimal)[2:]  # Remove o prefixo "0b" do resultado binário
    binario = binario.zfill(32)  # Preenche com zeros à esquerda para ter 32 dígitos
    octetos = [binario[i:i+8] for i in range(0, 32, 8)]  # Separa em grupos de 8 bits
    binario_formatado = ".".join(octetos)  # Formata como endereço IP com os octetos separados por ponto
    return binario_formatado

bits = math.ceil(math.log2(re))
mascara = 2**(bys) - 1
mascara_decimal = binario_decimal(mascara)

result = binario_decimal(int(mascara))

print('=============================================== \n')
print('\nEssa é a máscara de rede conforme as {} redes: {}'.format(re, result))
print('Máscara de rede (decimal): {}'.format(mascara_decimal))
print('=============================================== \n')
sys.stdout.flush()
