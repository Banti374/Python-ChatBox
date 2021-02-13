import socket

x = socket.socket()
print("Socket Created")

x.bind(('',9999))

x.listen(3)
print("Waiting For Connections.......")


while True:
    connection, client_address = x.accept()
    name = connection.recv(1024).decode()
    passwrd = connection.recv(1024).decode()

    print("Connection with ", client_address,name)
    connection.send(bytes('Welcome to server', 'utf-8'))
    s = 3

    for de in range(10):
        ab = connection.recv(1024).decode('utf-8')
        #print(ab)
        text = ab


        def encrypt(text, s):
            result = ""

            # traverse text
            for i in range(len(text)):
                char = text[i]

                #Encrypt uppercase characters
                if (char.isupper()):
                    result += chr((ord(char) + s - 65) % 26 + 65)

                    #Encrypt lowercase characters
                else:
                    result += chr((ord(char) - s - 97) % 26 + 97)

            return result


        # check the above function

        a4 = (encrypt(text,s))
        print(a4)

        ax = input("SERVER :--> ")
        text = ax

        def encrypt(text, s):
            result = ""

            # traverse text
            for i in range(len(text)):
                char = text[i]

                # Encrypt uppercase characters
                if (char.isupper()):
                    result += chr((ord(char) + s - 65) % 26 + 65)

                    # Encrypt lowercase characters
                else:
                    result += chr((ord(char) + s - 97) % 26 + 97)

            return result


        a4 = (encrypt(text, s))
        #print(a4)
        connection.send(a4.encode('utf-8'))
   # c.close()