"""Simple socket communication for variable-length messages."""

import socket


class SocketTalk:
    """A simple layer of socket communication, implementing
    send/receive messaging protocol where each (variable length)
    message is prefixed with a (fixed length) header containing
    the length of the remaining message data string.

    Ideas for protocol and byte-handling are borrowed from:
       http://docs.python.org/howto/sockets.html.
    """

    # Define the header of every message string handed to the socket.
    HEADER_LENGTH = 16
    HEADER_FORMAT = '{{:{0}d}}'.format(HEADER_LENGTH)

    @staticmethod
    def pair():
        """Return a pair of connected SocketTalk peers."""
        s1, s2 = socket.socketpair()
        return SocketTalk(s1), SocketTalk(s2)

    @staticmethod
    def server(addr):
        """Return a SocketTalk server."""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(addr)
        sock.listen(1)
        conn, addr = sock.accept()
        talk = SocketTalk(conn)
        return talk

    @staticmethod
    def client(addr):
        """Return a SocketTalk client."""
        success = False
        while not success:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                sock.connect(addr)
                success = True
            except socket.error as err:
                sock.close()
        talk = SocketTalk(sock)
        return talk

    def __init__(self, sock, encode=True):
        """Initialize the object with a socket."""
        self._sock = sock
        self._encode = encode

    def put(self, message):
        """Send the given *message*.
        Return True if successful, False if not."""

        # First assemble the complete message string by prefixing the header.
        header = self.HEADER_FORMAT.format(len(message))
        full_message = header + message

        # Then send all bytes of the message.
        sent_count = 0
        while sent_count < len(full_message):
            try:
                msg = full_message[sent_count:]
                msg = msg.encode() if self._encode else msg
                count = self._sock.send(msg)
            except socket.error as err:
                print('error')
                return False
            if count == 0:
                return False
            sent_count += count
        return True

    def get(self):
        """Receive a message.
        Return the message upon successful reception, or None upon failure."""

        # First retrieve all header bytes in order to extract
        # length of the message remainder.
        header = ''
        while len(header) < self.HEADER_LENGTH:
            chunk = self._sock.recv(self.HEADER_LENGTH - len(header))
            chunk = chunk.decode() if self._encode else chunk
            if chunk == '':
                return None
            header += chunk
        length = int(header)

        # Then retrieve the remainder of the message.
        message = ''
        while len(message) < length:
            chunk = self._sock.recv(length - len(message))
            chunk = chunk.decode() if self._encode else chunk
            if chunk == '':
                return None
            message += chunk
        return message

    def close(self):
        self._sock.close()
