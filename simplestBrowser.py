import socket

# make a phone
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# dial the phone: arg1 (domain name), arg2 (a port within the domain)
mysock.connect(('data.pr4e.org', 80))

# create request (blank line indicates no headers)
# .encode() --> convert unicode (py) into UTF-8
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()

# send request
mysock.send(cmd)

while True:
    # receive data until sockets close -- recv waits till it gets 512 characters
    data = mysock.recv(512)
    if len(data) < 1:
        break

    # convert UTF-8 back to unicode in order to print
    print(data.decode(),end='')

mysock.close()

#---------- result:----------
# <h1>The First Page</h1>
# <p>
# If you like, you can switch to the 
# <a href="http://data.pr4e.org/page2.htm">
# Second Page</a>.
# </p>