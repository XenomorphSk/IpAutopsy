import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--ip', help='Endereço IP')
parser.add_argument('--bys', type=int, help='Máscara de sub-rede')
args = parser.parse_args()
Ip = args.ip
bys = args.bys



def calcular_mascara_rede(comprimento_mascara):
    mascara_rede = 0
    for i in range(comprimento_mascara):
        mascara_rede |= 1 << (31 - i)
    return mascara_rede

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


FirstOctate = int(Ip.split(sep=".", maxsplit=1)[0])
SecondOctate = int(Ip.split(sep=".", maxsplit=2)[1])
TyrdOctate = int(Ip.split(sep=".", maxsplit=3)[2])
ForOctate = int(Ip.split(sep=".", maxsplit=4)[3])

bynaryIp = (FirstOctate << 24) + (SecondOctate << 16) + (TyrdOctate << 8) + ForOctate

FirstOctate_binario = decimal_binario(FirstOctate)
SecondOctate_binario = decimal_binario(SecondOctate)
TyrdOctate_binario = decimal_binario(TyrdOctate)
ForOctate_binario = decimal_binario(ForOctate)

mascara_rede = calcular_mascara_rede(bys)
mascara_binario = decimal_binario(mascara_rede)

subrede_binario = bynaryIp & mascara_rede
sub_rede = binario_decimal(subrede_binario)


print('=============================================== \n')
print("Primeiro octeto em binário:", FirstOctate_binario)
print("Segundo octeto em binário:", SecondOctate_binario)
print("Terceiro octeto em binário:", TyrdOctate_binario)
print("Quarto octeto em binário:", ForOctate_binario)

print('\nIp em binário:', decimal_binario(bynaryIp))
print('\nMáscara de rede:', mascara_binario)
print('\nEndereco de rede:', binario_decimal(subrede_binario))

print('=============================================== \n')

result3 = subprocess.run(['python3', 'think3.py', '--ip', sub_rede, '--bys', str(bys)], capture_output=True, text=True)


output3 = result3.stdout.strip()



print('\n', output3)

