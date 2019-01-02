#!/home/xuser/anaconda3/bin/python3

from xmlrpc.server import SimpleXMLRPCServer

def add(a,b):
    return a+b

def main():
    print("This is a server!")

    server = SimpleXMLRPCServer(("0.0.0.0", 8080))
    server.register_function(add)
    print("Press CTRL+C to end...")
    server.serve_forever()

if __name__ == "__main__":
    main()
