import socket

from proto import world_pb2


def main():
    host = "127.0.0.1"
    port = 42069

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)

    print(f"Server is listening on {host}:{port}")

    conn, addr = s.accept()
    print(f"Connection from {addr}")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"Received data: {data}")

        world = create_world()
        conn.send(world.SerializeToString())
        print(f"Sent data: {world}")


def create_world():
    world = world_pb2.World()
    grid = world.grid
    row = grid.row.add()
    row.cell.add(value=1)
    row.cell.add(value=2)
    row.cell.add(value=3)
    row = grid.row.add()
    row.cell.add(value=4)
    row.cell.add(value=5)
    row.cell.add(value=6)
    row = grid.row.add()
    row.cell.add(value=7)
    row.cell.add(value=8)
    row.cell.add(value=9)
    return world


if __name__ == "__main__":
    main()
