from tkinter import * 
from tkinter.ttk import *
import time
# a python program to send an initial packet, then listen for packets from the ESP32
import socket
UDP_IP = "192.168.137.151" # The IP that is printed in the serial monitor from the ESP32
SHARED_UDP_PORT = 4210
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet  # UDP
sock.connect((UDP_IP, SHARED_UDP_PORT))

root = Tk() 
f = Frame(root)
f.pack(side="top", expand=True, fill="both")
root.title("Motion_Detection")
label = Label(f, text ="Hello").pack() 
def loop():
    global f, root
    while True:
        data = sock.recv(2048)
        print(str(data))
        for widget in f.winfo_children():
            widget.destroy()
        if(data == b'1'):
            label = Label(f, text ="There's someone outside").pack() 
        else :
            label = Label(f, text = "Safe").pack() 
        
        root.update()
if __name__ == "__main__":
    sock.send('Hello ESP32'.encode())
    loop()