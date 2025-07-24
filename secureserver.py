import http.server
import ssl

# Define the server address and port
server_address = ('localhost', 8443)  # Use a port like 8443 or 4443

# Create an SSLContext
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')

# Create an HTTPServer instance
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

# Wrap the server socket with SSL
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print(f"Serving HTTPS on {server_address[0]}:{server_address[1]}")
httpd.serve_forever()