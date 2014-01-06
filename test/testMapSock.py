def test1():
    """Test the MapSock client/server."""

    from threading import Thread
    from MapSock import MapSockServer, MapSockClient, MapSockRequest

    host = 'localhost'
    port = 50002

    # Start the server.
    server = MapSockServer(host, port)
    thread = Thread(target=server.run)
    thread.start()
    
    # Send set, get, stop.    
    client = MapSockClient(host, port)
    assert client.send(MapSockRequest('size')) == '0'
    assert client.send(MapSockRequest('set', 'tool', 'wrench')) == 'ok'
    assert client.send(MapSockRequest('set', 'fruit', 'apple')) == 'ok'
    assert client.send(MapSockRequest('set', 'animal', 'rabbit')) == 'ok'
    assert client.send(MapSockRequest('size')) == '3'
    assert client.send(MapSockRequest('get', 'fruit')) == 'apple'
    assert client.send(MapSockRequest('get', 'animal')) == 'rabbit'
    assert client.send(MapSockRequest('get', 'pizza')) == 'key not found'
    assert client.send(MapSockRequest('get', 'tool')) == 'wrench'
    assert client.send(MapSockRequest('del', 'fruit')) == 'ok'
    assert client.send(MapSockRequest('del', 'animal')) == 'ok'
    assert client.send(MapSockRequest('del', 'pizza')) == 'key not found'
    assert client.send(MapSockRequest('size')) == '1'
    assert client.send(MapSockRequest('stop')) == 'ok'

    # Join the server thread.
    thread.join()
test1()
