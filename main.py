from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()

authorizer.add_user("username", "password", "./files", perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer

address = ("127.0.0.1", 21)  # Listen on every IP on port 21

server = FTPServer(address, handler)

server.serve_forever()
