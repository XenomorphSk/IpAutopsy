import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--ip', help='Endereço IP')
parser.add_argument('--bys', type=int, help='Máscara de sub-rede')
args = parser.parse_args()
Ip = args.ip
bys = args.bys

hosts = 2 ** (32 - bys) - 2

print('O número total de enderecos que podem ser reservados é ', hosts)
print('=============================================== \n')