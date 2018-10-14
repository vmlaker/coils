"""
A simple client/server framework with socket communication.
A server serves associative container of key/value pairs.
A client can insert/query/delete container elements.
"""

# Import system modules.
import logging
import socket
import pickle

# Import application modules.
# Keep Python 2 and 3 happy during nosetests.
try:
    import SocketTalk
except ImportError:
    from .SocketTalk import SocketTalk


class MapSockRequest(object):
    """
    Request object sent from client to server.
    """
    def __init__(self, action, key=None, value=None):
        self.action = action
        self.key = key
        self.value = value


class MapSockClient:
    """
    Client to the map server.
    """

    def __init__(self, host, port, encode=True):
        """
        Initialize the object.

        *host*  -  socket host

        *port*  -  socket port
        """
        self._logger = logging.getLogger(__name__)
        self._host = host
        self._port = port
        self._encode = encode

    def send(self, request):
        """
        Send request to server and return server response.
        """
        self._logger.debug('Opening connection')
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.connect((self._host, self._port))
        talk = SocketTalk(sock, encode=self._encode)

        self._logger.debug('Sending action %s' % request.action)
        if not talk.put(request.action):
            self._logger.error('Failed to send action %s' % request.action)
            return None

        if request.key is not None:
            self._logger.debug('Sending key %s' % request.key)
            if not talk.put(request.key):
                self._logger.error('Failed to send key %s' % request.key)
                return None

        if request.value is not None:
            self._logger.debug('Sending value')
            if not talk.put(request.value):
                self._logger.error('Failed to send value')
                return None

        self._logger.debug('Receiving status')
        response = talk.get()
        if not response:
            self._logger.error('Failed to receive status')
            return None
        self._logger.debug('Status response = %s' % response)

        if request.action in ('get', 'size', 'keys') and response == 'ok':
            self._logger.debug('Receiving value')
            response = talk.get()
            if not response:
                self._logger.error('Failed to receive value')
                return None

        if request.action in ('keys',):
            response = pickle.loads(response)

        self._logger.debug('Closing connection')
        try:
            sock.shutdown(socket.SHUT_RDWR)
        except:
            self._logger.error('Failed to shutdown')
        sock.close()

        return response


class MapSockServer:
    def __init__(self, host, port, on_action=None, encode=True):
        """
        Initialize the server object.

        *host*       -  socket host

        *port*       -  socket port

        *on_action*  -  callback upon action reception,
                        is called with action string
        """
        self._logger = logging.getLogger(__name__)
        self._data = dict()
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._sock.bind((host, port))
        self._sock.listen(1)
        self._talk = None
        self._on_action = on_action
        self._encode = encode

    def _send(self, message):
        """
        Return response message to client.
        """
        result = self._talk.put(message)
        if not result:
            self._logger.error('Failed to send "%s"' % message)
        return result

    def _receive(self):
        """
        Receive a chunk of request from client.
        """
        result = self._talk.get()
        if not result:
            self._logger.error('Failed to receive')
        return result

    def run(self):
        """
        Continuously retrieve client requests until given "stop" request.
        """
        while True:
            self._logger.debug('Accepting connection')
            conn, addr = self._sock.accept()
            self._talk = SocketTalk(conn, encode=self._encode)

            self._logger.debug('Receiving action')
            action = self._receive()

            if self._on_action:
                self._on_action(action)

            key = None
            if action in ('set', 'get', 'del',):
                self._logger.debug('Receiving key')
                key = self._receive()

            value = None
            if action in ('set',):
                self._logger.debug('Receiving value')
                value = self._receive()

            # Process the request.
            if action == 'stop':
                self._send('ok')

            elif action == 'set':
                self._data[key] = value
                self._send('ok')

            elif action == 'get':
                try:
                    value = self._data[key]
                except:
                    self._logger.debug('Sending "key not found"')
                    self._send('key not found')
                else:
                    self._logger.debug('Sending "ok"')
                    self._send('ok')
                    self._logger.debug('Sending value')
                    self._send(value)

            elif action == 'del':
                try:
                    del self._data[key]
                except:
                    self._logger.debug('Sending "key not found"')
                    self._send('key not found')
                else:
                    self._logger.debug('Sending "ok"')
                    self._send('ok')

            elif action == 'size':
                self._send('ok')
                self._send(str(len(self._data)))

            elif action == 'keys':
                pickled = pickle.dumps(self._data.keys())
                self._send('ok')
                self._send(pickled)

            else:
                self._send('unknown action %s' % action)

            self._logger.debug('Closing')
            try:
                conn.shutdown(socket.SHUT_RDWR)
            except:
                self._logger.error('Failed to shutdown')
            conn.close()

            if action == 'stop':
                break

        self._logger.debug('Stopped')
