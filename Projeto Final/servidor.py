import socket
import subprocess

credentials = ["root:123456", "root:toor", "admin:123456"]

#Cria o socket
#AF_INET = Endereços IPV4
#STREAM = TCP ou DGRAN = UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Tupla endereço e porta do servidor
server_address = ('127.0.0.1', 1500)

#Level, optname, value
#Reusar imediatamente o socket após antender uma requisição
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(server_address)

sock.listen(5)  #Máximo de conexões = 5

while True:
    connection , client_address = sock.accept()
    print("[*] Nova conexao de {0}:{1}".format(*client_address))
    try:
        connection.send(b"Username: ")  #b = bytes
        username = connection.recv(32).strip().decode('utf-8')
        connection.send(b"Password: ")
        password = connection.recv(32).strip().decode('utf-8')

        if "{0}:{1}".format(username, password) in credentials:
            connection.send(b"Welcome to the Socket Server.\n$")

            while True:
                data = connection.recv(1024).strip().decode('utf-8')
                if data == "exit":
                    break
                if data == "shell":
                    connection.send(b"SHELL: ")
                    while True:
                        datapoint = connection.recv(2048).strip().decode('utf-8')
                        print(datapoint)
                        proc = subprocess.Popen(datapoint, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                        stdout_value = b'\n' + proc.stdout.read() + proc.stderr.read() + b'\n'
                        connection.send(stdout_value)
                if data == "server info":
                    cmdserver = "systeminfo"
                    proc = subprocess.Popen(cmdserver, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    stdout_value = b'\n' + proc.stdout.read() + proc.stderr.read() + b'\n'
                    connection.send(stdout_value)
                else:
                    connection.send(b'\n' + "Command not found: " + data + b'\n')
            connection.send(b"$ ")
        else:
            connection.send(b"Access denied.")
    except socket.error:
        print("An error occured with client ip = {0}, port = {1}".format(*client_address))
    finally:
        connection.close()    