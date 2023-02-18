from ping3 import ping, verbose_ping

servidores = ['172.16.100.1', '172.16.100.2', '172.16.100.5', '172.16.100.6', '172.16.100.19', 'uol.com.br', 'cnn.com']

print("\nIniciando teste de ping nos servidores ...\n")
for s in servidores:
    resultado = str(ping(s))
    if "None" in resultado:
        print(s + " NOT OK")
    else:
        print(s + " OK")