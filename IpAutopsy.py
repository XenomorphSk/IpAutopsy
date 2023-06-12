import subprocess

print(''' 
 _____          ___          _                             
|_   _|        / _ \        | |                            
  | |   _ __  / /_\ \ _   _ | |_   ___   _ __   ___  _   _ 
  | |  | '_ \ |  _  || | | || __| / _ \ | '_ \ / __|| | | |
 _| |_ | |_) || | | || |_| || |_ | (_) || |_) |\__ \| |_| |
 \___/ | .__/ \_| |_/ \__,_| \__| \___/ | .__/ |___/ \__, |
       | |                              | |           __/ |
       |_|                              |_|          |___/ 

Mr.Xeno
''')


Ip = str(input('Insira o Ip: '))
bys = int(input('Insira a mascara de sub-rede (ex: /24): '))
redes = int(input('Insira o número de redes: '))

result = subprocess.run(['python3', 'think.py', '--ip', Ip, '--bys', str(bys)], capture_output=True, text=True)
result2 = subprocess.run(['python3', 'think2.py', '--ip', Ip, '--bys', str(bys)], capture_output=True, text=True)
result4 = subprocess.run(['python3', 'think4.py', '--ip', Ip, '--bys', str(bys)], capture_output=True, text=True)
result5 = subprocess.run(['python3', 'think5.py', '--ip', Ip, '--bys', str(bys)], capture_output=True, text=True)
result6 = subprocess.run(['python3', 'think6.py', '--ip', Ip, '--bys', str(bys), '--re', str(redes)], capture_output=True, text=True)

output = result.stdout.strip()
output2 = result2.stdout.strip()
output4 = result4.stdout.strip()
output5 = result5.stdout.strip()
output6 = result6.stdout.strip()

print('\n', output)
print('\n', output2)
print('\n', output4)
print('\n', output5)
print('\n', output6)
