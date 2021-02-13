import socket

c = socket.socket()
#ADD YOUR HOST IP ADD
c.connect(('127.0.0.1', 9999))  #LOCALHOST

name = input("Enter your name : ")
passwrd = input("Enter Passward : ")

c.send(bytes(name, 'utf-8'))
c.send(bytes(passwrd, 'utf-8'))
print(c.recv(1024))

s = 3

for en in range(10):
    az = input("CLIENT : --| ")
    text = az


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


    a1 = (encrypt(text, s))
    #print(a1)
    c.send(a1.encode('utf-8'))

    az = c.recv(1024).decode('utf-8')
    #print(az)
    text = az
    def encrypt(text, s):
        result = ""
        for i in range(len(text)):
            char = text[i]

            # Encrypt uppercase characters
            if (char.isupper()):
                result += chr((ord(char) + s - 65) % 26 + 65)

                # Encrypt lowercase characters
            else:
                result += chr((ord(char) - s - 97) % 26 + 97)

        return result


    # check the above function

    a3 = (encrypt(text,s).encode('utf-8'))

    print(a3)