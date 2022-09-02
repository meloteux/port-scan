import socket

ports = [21,22,80,443,445,3306,25,3000]

for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.5)
        code = client.connect_ex(("site.com", port))
        if code == 0:
                print("PORTA", port, "ABERTA")
