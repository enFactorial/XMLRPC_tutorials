#!/home/xuser/anaconda3/bin/python3

from xmlrpc.server import SimpleXMLRPCServer

def add(a,b):
    return a+b

def send_file(file_name):
    with open('./acquired_data/' + file_name, 'rb') as handle:
        return handle.read()

def main():
    print("This is a server!")

    server = SimpleXMLRPCServer(("0.0.0.0", 8080))
    server.register_function(add)
    server.register_function(send_file)
    print("Press CTRL+C to end...")
    server.serve_forever()

if __name__ == "__main__":
    main()
