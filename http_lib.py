import socket
from urllib.parse import urlparse

#Test
#Get no extras
#python httpc.py get 'http://httpbin.org/get?course=networking&assignment=1'

#Get with HEADER
#python httpc.py get -h Content-Type:text/html 'http://httpbin.org/get?course=networking&assignment=1'

#Get with VERBOSE
#python httpc.py get -v 'http://httpbin.org/get?course=networking&assignment=1'

def get_request(url_get,verbose,header,overwrite_file):

    url=urlparse(url_get)
    #Test
    #print(url)

    #Open Connection
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #File to overwrite
    file = None

    try:
        conn.connect((url.netloc, 80))

        #Check For Header
        if  not header == None:
            url="GET " + url.path + "?" + url.query.replace("%26", "&") + " HTTP/1.1\r\nHost: " \
                                      + url.netloc + "\r\n" + header + "\r\n\r\n"
        else:
            url="GET " + url.path + "?" + url.query.replace("%26", "&") + " HTTP/1.1\r\nHost: " \
                                      + url.netloc + "\r\n" + "\r\n\r\n"


        request = url.encode()
        conn.send(request)


        if not overwrite_file == None:
            if verbose:
                file = open(o, 'w')
                file.write(conn.recv(4096).decode("utf-8"))
            else:
                file = open(o, 'w')
                response = conn.recv(4096).decode("utf-8")
                try:
                    index = response.index('{')
                    file.write(response[index:])
                except ValueError:
                    file.write(response)

        else:
             if verbose:
                print(conn.recv(4096).decode("utf-8"))
             else:
                response = conn.recv(4096).decode("utf-8")
                try:
                    index = response.index('{')
                    print(response[index:])
                except ValueError:
                    print(response)

    finally:
        #Close Connection
        if file:
            file.close()
        conn.close()


def post_request(url_post,verbose,header,file_name,data,overwrite_file):
    print(url,verbose,header,file_name,data,overwrite_file)
