# API Design

As mentioned in [communication HLD](./communication_high_level_design.md), the sim and UI will run as separate processes. The UI will communicate with the sim using a socket connection, using google protobufs as the serializer. The sim will run as a server and the UI will run as a client.

The UI will send requests to the sim and the sim will send back responses. The format of the requests and responses is defined in the protobuf file [`api.proto`](../proto/api.proto).

### Request

```protobuf
message Request {
    string id = 1;
    string version = 2;
    RequestType type = 3;
    RequestBody body = 4;
}
```

Each request will have a `type` field that will specify the type of request. The allowed types are defined in the `RequestType` enum in the [`endpoints.proto`](../proto/endpoints.proto) file. The request will also have a `body` field that will contain the actual data of the request. This field would depend on the `type` of the request. Additionally, there will be `id` and `version` fields, that can be used to identify the request and the version of the request respectively (the `version` field is not used in the current implementation, buc it could be used in the future to handle backward compatibility).

Example of a request:
```protobuf
id: "1"
type: CREATE_WOR:D
body {
  create_world_request {
    grid_size: 10
  }
}
```

### Response

```protobuf
message Response {
    string id = 1;
    RequestType type = 2;
    ResponseBody body = 3;
    bool success = 4;
    optional string error = 5;
}
```

Each response will have `id` and `type` fields, similar to request. There will be a `body` field that will contain the actual data of the response. Similar to request, the `body` field would depend on the `type` of the response. Additionally, there will be a `success` field that will be a boolean indicating whether the request was successful or not. If the request was not successful, there will be an `error` field that will contain the error message.

Example of a response:
```protobuf
id: "1"
type: CREATE_WORLD
success: true
body {
  create_world_response {
    // empty
  }
}
```
