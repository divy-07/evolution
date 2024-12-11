import socket

from proto import api_pb2, endpoints_pb2, world_pb2


def main():
    host = "127.0.0.1"
    port = 42069

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)

    print(f"Server is listening on {host}:{port}")

    conn, addr = s.accept()
    print(f"Connection from {addr}")

    while conn:
        request = api_pb2.Request()
        request.ParseFromString(conn.recv(1024))
        if not request:
            break
        print(f"Request: {request}")

        response = process_request(request)
        conn.send(response.SerializeToString())
        print(f"Response: {response}")


def process_request(request):
    match request.type:
        case endpoints_pb2.RequestType.PING:
            return ping_response(request)
        case endpoints_pb2.RequestType.CREATE_WORLD:
            return create_world_response(request)
        case endpoints_pb2.RequestType.GET_WORLD:
            return get_world_response(request)
        case endpoints_pb2.RequestType.MAKE_STEP:
            return make_step_response(request)


def ping_response(request):
    response = api_pb2.Response()
    response.id = request.id
    response.type = request.type
    response.success = True
    response.body.ping_response.CopyFrom(endpoints_pb2.PingResponse())
    return response


def create_world_response(request):
    response = api_pb2.Response()
    response.id = request.id
    response.type = request.type
    response.success = True
    response.body.create_world_response.CopyFrom(
        endpoints_pb2.CreateWorldResponse()
    )
    return response


def get_world_response(request):
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

    response = api_pb2.Response()
    response.id = request.id
    response.type = request.type
    response.success = True
    response.body.get_world_response.world.CopyFrom(create_world())
    return response


def make_step_response(request):
    response = api_pb2.Response()
    response.id = request.id
    response.type = request.type
    response.success = True
    response.body.make_step_response.CopyFrom(endpoints_pb2.MakeStepResponse())
    return response


if __name__ == "__main__":
    main()
