import argparse

# Configurar o parser de argumentos
parser = argparse.ArgumentParser()
parser.add_argument('--ip', help='Endereço IP')
parser.add_argument('--bys', type=int, help='Máscara de sub-rede')
args = parser.parse_args()

Ip = args.ip
bys = args.bys

# Separar o primeiro octeto do endereço IP
FirstOctate = int(Ip.split(sep=".", maxsplit=1)[0])

# Determinar a classe do endereço IP com base no primeiro octeto
if bys <= 8:
    result = 'O IP é classe A'
elif bys <= 16:
    result = 'O IP é classe B'
elif bys <= 24:
    result = 'O IP é classe C'
else:
    result = 'O IP não pertence às classes A, B ou C'

print(result)
