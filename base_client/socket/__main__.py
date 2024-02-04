import sys
import getopt
from common_library import socket


def args():
    address = ''
    port = 0
    timeout = 0
    opts, args = getopt.getopt(sys.argv[1:], "ha:p:t",
                               ["address=", "port=", "timeout="])
    for opt, arg in opts:
        if opt == '-h':
            print('__main__.py --addres <address> --port <port>')
            sys.exit()
        elif opt in ("-a", "--address"):
            address = arg
        elif opt in ("-p", "--port"):
            port = arg
        elif opt in ("-t", "--timeout"):
            timeout = arg

    return address, int(port), int(timeout)


def main():
    address, port, timeout = args()

    client = socket.Client()
    client.conenct(address=address, port=port, timeout=timeout)

    data = client.recv()
    print("recv data : ", data)

    send_len = client.send("data\r\n")
    print("send_len : ", send_len)

    data = client.recv()
    print("recv data : ", data)

    client.close()


if __name__ == '__main__':
    main()
