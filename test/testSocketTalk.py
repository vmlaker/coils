def test1():
    """Test the SocketTalk peers."""
    from SocketTalk import SocketTalk
    talk1, talk2 = SocketTalk.pair()
    talk1.put('one')
    assert talk2.get() == 'one'
    talk2.put('two')
    assert talk1.get() == 'two'
    talk2.close()
    assert talk1.get() is None
    talk1.close()
test1()

def test2():
    """Test the SocketTalk client/server."""
    from threading import Thread
    from SocketTalk import SocketTalk

    addr = 'localhost', 50002
    def client():
        talk = SocketTalk.client(addr)
        talk.put('one')
        assert talk.get() == 'two'
        talk.close()

    def server():
        talk = SocketTalk.server(addr)
        assert talk.get() == 'one'
        talk.put('two')
        talk.close()

    Thread(target=client).start()
    Thread(target=server).start()
test2()

