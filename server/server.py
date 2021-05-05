import socket
import threading
import sys

class HttpWebServer(object):
    # 也可以设置为类属性
    def __init__(self,port):
        tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        tcp_server.bind(('', port))
        tcp_server.listen(128)
        self.tcp_server = tcp_server

    @staticmethod
    def handle_client_request(new_socket,ip_port):
        recv_bin=new_socket.recv(4096)
        if len(recv_bin)==0:
            new_socket.close()
            return
        recv=recv_bin.decode('utf-8')
        temp_list=recv.split(' ',2)
        client_request=temp_list[1]
        print('客户端的请求:',client_request)
        if client_request=='/':
            client_request='/index.html'
        try:
            with open('static'+client_request,'rb') as file:
                file_data=file.read()
        except:
            with open('static/error.html','rb') as file:
                file_data=file.read()
            response_line='HTTP/1.1 404 Not Found\r\n'
            response_header='Server: 大米\r\n'
            response_body=file_data
            response=(response_line+response_header+'\r\n').encode('utf=8')+response_body
            new_socket.send(response)
        else:
            response_line = 'HTTP/1.1 200 OK\r\n'
            response_header = 'Server: 大米\r\n'
            response_body = file_data
            response = (response_line + response_header + '\r\n').encode('utf=8') + response_body
            new_socket.send(response)
        finally:
            new_socket.close()

    def start_porcess(self):
        while True:
            new_socket, ip_port = self.tcp_server.accept()
            sub_thread = threading.Thread(target=self.handle_client_request, args=(new_socket,ip_port))
            sub_thread.setDaemon(True)
            sub_thread.start()

def main():
    # 终端输入的端口号执行，argv返回的一个列表
    parameters = sys.argv
    print(parameters)
    if len(parameters) != 2:
        print('终端输入的格式必须为python3 xxx.py 端口号')
        return
    if not parameters[1].isdigit():
        print('端口号必须为数字')
        return
    # 指定端口
    port=int(parameters[1])
    # 传入参数, __init__方法添加新的参数port
    web = HttpWebServer(port)
    web.start_porcess()



if __name__ == '__main__':
    main()
