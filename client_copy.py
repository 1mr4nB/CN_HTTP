import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print(local_ip)

SERVER = local_ip  # Dynamic IP grab (not hardcoded)
PORT = 5055  # High port number
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
HEADER = 100  # Amount of bytes received by client

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)        # TODO: Telnet-like address input


def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)


while True:
    send(input("Enter a message to send to server: "))
    if bool(client.recv(HEADER).decode(FORMAT)) == False:
        break
print("Client terminating. Server terminated connection to this client.")
