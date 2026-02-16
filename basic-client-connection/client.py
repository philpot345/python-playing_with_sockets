import socket

host_url = "www.google.com"
port = 80

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
    print("Unable to create socket:", e)
    exit(1)

try:
    ip = socket.gethostbyname(host_url)
except socket.gaierror as e:
    print("Unable to resolve hostname:", e)
    exit(1)

s.connect((ip, port))
print(f"Successfully connected to {host_url} at {ip}:{port}")