import socket
import uuid

from proto import api_pb2, endpoints_pb2


def main():
    host = "127.0.0.1"
    port = 42069

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    print(f"Connected to {host}:{port}")

    # ping
    request = ping_request()
    s.send(request.SerializeToString())
    print(f"Sent request: {request}")
    response = api_pb2.Response()
    response.ParseFromString(s.recv(1024))
    print(f"Received response: {response}")
    input("Press Enter to continue...")

    # create_world
    request = create_world_request()
    s.send(request.SerializeToString())
    print(f"Sent request: {request}")
    response = api_pb2.Response()
    response.ParseFromString(s.recv(1024))
    print(f"Received response: {response}")
    input("Press Enter to continue...")

    # get_world
    request = get_world_request()
    s.send(request.SerializeToString())
    print(f"Sent request: {request}")
    response = api_pb2.Response()
    response.ParseFromString(s.recv(1024))
    print(f"Received response: {response}")
    input("Press Enter to continue...")

    # make_step
    request = make_step_request()
    s.send(request.SerializeToString())
    print(f"Sent request: {request}")
    response = api_pb2.Response()
    response.ParseFromString(s.recv(1024))
    print(f"Received response: {response}")
    input("Press Enter to continue...")

    # get_world
    request = get_world_request()
    s.send(request.SerializeToString())
    print(f"Sent request: {request}")
    response = api_pb2.Response()
    response.ParseFromString(s.recv(1024))
    print(f"Received response: {response}")
    input("Press Enter to continue...")


def ping_request():
    request = api_pb2.Request()
    request.id = str(uuid.uuid4())
    request.type = endpoints_pb2.RequestType.PING
    request.body.ping_request.CopyFrom(endpoints_pb2.PingRequest())
    return request


def create_world_request():
    request = api_pb2.Request()
    request.id = str(uuid.uuid4())
    request.type = endpoints_pb2.RequestType.CREATE_WORLD
    body = endpoints_pb2.CreateWorldRequest()
    body.grid_size = 3
    request.body.create_world_request.CopyFrom(body)
    return request


def get_world_request():
    request = api_pb2.Request()
    request.id = str(uuid.uuid4())
    request.type = endpoints_pb2.RequestType.GET_WORLD
    request.body.get_world_request.CopyFrom(endpoints_pb2.GetWorldRequest())
    return request


def make_step_request():
    request = api_pb2.Request()
    request.id = str(uuid.uuid4())
    request.type = endpoints_pb2.RequestType.MAKE_STEP
    request.body.make_step_request.num_steps = 1
    return request


if __name__ == "__main__":
    main()
