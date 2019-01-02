#!/home/xuser/anaconda3/bin/python3

import xmlrpc.client

def main():
    print("This is a client!")

    client = xmlrpc.client.ServerProxy("http://localhost:8080")
    print(client.add(10, 20))

    file_name = "screw.png"
    data = client.send_file(file_name)
    with open('./received_files/' + file_name, 'wb') as handle:
        handle.write(data.data)

if __name__ == "__main__":
    main()
