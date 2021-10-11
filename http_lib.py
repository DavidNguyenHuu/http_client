import socket
from urllib.parse import urlparse


def get_request(url_get,verbose,header,overwrite_file):
    #Initiating file to overwrite.
    file_o = None
    #Open Connection
    url=urlparse(url_get)
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        conn.connect((url.netloc, 80))

        #Check For Get Header
        if  not header == None:
            url="GET " + url.path + "?" + url.query.replace("%26", "&") + " HTTP/1.1\r\nHost: " \
                                      + url.netloc + "\r\n" + header + "\r\n\r\n"
        else:
            url="GET " + url.path + "?" + url.query.replace("%26", "&") + " HTTP/1.1\r\nHost: " \
                                      + url.netloc + "\r\n" + "\r\n\r\n"

        request = url.encode()
        conn.send(request)
        #Check for Overwrite & Verbose
        if not overwrite_file == None:
            if verbose:
                file_o = open(overwrite_file, 'w')
                file_o.write(conn.recv(4096).decode("utf-8"))
            else:
                file_o = open(overwrite_file, 'w')
                response = conn.recv(4096).decode("utf-8")
                try:
                    index = response.index('{')
                    file_o.write(response[index:])
                except :
                    file_o.write(response)

        #Check for Verbose or Standard
        else:
             if verbose:
                print(conn.recv(4096).decode("utf-8"))
             else:
                response = conn.recv(4096).decode("utf-8")
                try:
                    index = response.index('{')
                    print(response[index:])
                except:
                    print(response)

    finally:
        #If overwrite_file option = true
        if file_o:
            file_o.close()
        #Close Connection
        conn.close()


def post_request(url_post,verbose,header,data,file,overwrite_file):

    #Initiating file,data and file to overwrite.
    f = None
    d = None
    file_o = None

    #Open Connection
    url=urlparse(url_post)
    #For Testing
    #print(url)
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        conn.connect((url.netloc, 80))

        #Check for -data or -file & (-data and -file)
        if not data == None and not file == None:
            print("Either [-d] or [-f] can be used but not both.")

        elif not data == None:
             d = "Content-Length:" + str(len(data)) + "\r\n\r\n" + data
        elif not file == None:
            f = open(file, 'r')
            data = f.read()
            f.close()
            d = "Content-Length:" + str(len(data)) + "\r\n\r\n" + data

        #Check for -header
        if not header == None:
            if not d == None:
                url="POST " + url.path + "?" + url.query.replace("%26", "&") + \
                                          " HTTP/1.1\r\nHost: " + url.netloc + "\r\n" + header + "\r\n" + d + "\r\n"
            else:
                url="POST " + url.path + "?" + url.query.replace("%26", "&") + \
                                          " HTTP/1.1\r\nHost: " + url.netloc + "\r\n" + header + "\r\n\r\n"

        #If no -header,check for -data
        else:
            if not d == None:
                print("got here")
                url="POST " + url.path + "?" + url.query.replace("%26", "&") + " HTTP/1.1\r\nHost: " \
                                  + url.netloc + "\r\n" + d + "\r\n"
            else:
                url="POST " + url.path + "?" + url.query.replace("%26", "&") + " HTTP/1.1\r\nHost: " \
                                      + url.netloc + "\r\n" + "\r\n\r\n"

        request = url.encode()
        conn.send(request)

        #Check for overwrite_file
        if not overwrite_file == None:
            if verbose:
                file_o = open(overwrite_file, 'w')
                file_o.write(conn.recv(4096).decode("utf-8"))
            else:
                file_o = open(overwrite_file, 'w')
                response = conn.recv(4096).decode("utf-8")
                try:
                    index = response.index('{')
                    file_o.write(response[index:])
                except:
                    file_o.write(response)
        else:
            if verbose:
                print(conn.recv(4096).decode("utf-8"))
            else:
                response = conn.recv(4096).decode("utf-8")
                try:
                    index = response.index('{')
                    print(response[index:])
                except:
                    print(response)

    finally:
        #If overwrite_file option = true
        if file_o:
            file_o.close()
        #Close Connection
        conn.close()

