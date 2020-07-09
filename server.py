import socket
from tkinter import *

## USING TKINTER TO GIVE IT A LOOK
def send(listbox, entry):
    message = entry.get()
    listbox.insert('end', "Server: "+message)
    entry.delete(0,END)
    client.send(bytes(message, "utf-8"))
    receive(listbox)

def receive(listbox):
    message_from_client = client.recv(50)
    listbox.insert('end', "Client: "+message_from_client.decode('utf-8'))

root = Tk()
root.title('Server')

entry = Entry()
entry.pack(side=BOTTOM)

listbox = Listbox(root)
listbox.pack()

sendButton = Button(root, text="Send", command = lambda : send(listbox, entry))
sendButton.pack(side=BOTTOM)

receiveButton = Button(root, text="receive", command = lambda : receive(listbox))
receiveButton.pack(side=BOTTOM)

## ACTUAL SOCKET CODES TO MAKE THE APPLICATION RUN
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_NAME = socket.gethostname()
PORT = 12345

s.bind((HOST_NAME, PORT))
s.listen(4)
client, address = s.accept()

root.mainloop()