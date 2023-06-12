import ipaddress
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--ip', help='Endereço IP')
parser.add_argument('--bys', type=int, help='Máscara de sub-rede')
args = parser.parse_args()
Ip = args.ip
bys = args.bys

ip = ipaddress.IPv4Address(Ip)
rede = ipaddress.IPv4Network(Ip + '/' + str(bys), strict=False)
broadcast_address = rede.broadcast_address

print('=============================================== \n')
print('\n Endereço de broadcast:', broadcast_address)
print('=============================================== \n')
