import ipaddress
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--ip', help='Endereço IP')
parser.add_argument('--bys', type=int, help='Máscara de sub-rede')
args = parser.parse_args()
Ip = args.ip
bys = args.bys

ip = ipaddress.IPv4Address(Ip)
mascara = ipaddress.IPv4Network(Ip + '/' + str(bys), strict=False)

primeiro_host = mascara.network_address + 1
ultimo_host = mascara.broadcast_address - 1

print('=============================================== \n')
print('\n  O primeiro endereco de host valido é: ', primeiro_host)
print('\n  O último endereco de host valido é: ', ultimo_host)
print('=============================================== \n')
