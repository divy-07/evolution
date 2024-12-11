import socket

from proto import world_pb2


def main():
    host = "127.0.0.1"
    port = 42069

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    print(f"Connected to {host}:{port}")

    data = "Get World"
    s.send(data.encode())
    print(f"Sent data: {data}")

    world = world_pb2.World()
    world.ParseFromString(s.recv(1024))
    print(f"Received data: {world}")


if __name__ == "__main__":
    main()
