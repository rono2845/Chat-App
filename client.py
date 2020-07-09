import socket
from tkinter import *


## USING TKINTER TO GIVE IT A LOOK
def send(listbox, entry):
    message = entry.get()
    listbox.insert('end',"Client: "+message)
    entry.delete(0,END)
    s.send(bytes(message, "utf-8"))
    recieve(listbox)

def recieve(listbox):
    message = s.recv(50)
    listbox.insert('end',"Server: "+ message.decode('utf-8'))

root = Tk()
root.title('Client')

entry = Entry()
entry.pack(side=BOTTOM)

listbox = Listbox(root)
listbox.pack()

sendButton = Button(root, text="Send", command = lambda : send(listbox, entry))
sendButton.pack(side=BOTTOM)

recieveButton = Button(root, text="Recieve", command = lambda : recieve(listbox))
recieveButton.pack(side=BOTTOM)

## ACTUAL SOCKET CODES TO MAKE THE APPLICATION RUN
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_NAME = socket.gethostname()
PORT = 12345

s.connect((HOST_NAME, PORT))

root.mainloop()