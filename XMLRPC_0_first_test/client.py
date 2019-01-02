#!/home/xuser/anaconda3/bin/python3

import xmlrpc.client

def main():
    print("This is a client!")

    client = xmlrpc.client.ServerProxy("http://localhost:8080")
    print(client.add(10, 20))
    
    client.get_image()

if __name__ == "__main__":
    main()
