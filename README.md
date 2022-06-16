# reverse-shell
python reverses-shell backdoor with more functionality,
you can take screeenshot of current client window, take control of clients mouse and keyboard,
once the script is running you can activate reverse shell, and run basic shell command
the program runs best in linux but can also be used with windows, it hasnt been tested yet on mac'
please contribute if you have ideas on making this program better


commands;
    "size :getclient screen size",
     "mouse:  get cursor position",
     "move:  move cursor to point (x,y)",
     "doubleclick:  double click current cursor position",
     "click:  click current cursor position",
     "rightclick:  right click current cursor position",
     "write:  write string on screen",
     "press:  press keyboard key",
     "hotkey:  compination of keyboard keys",
     "minimize:  resize current client's window (-)",
     "maximize:  resize current client's window (+)",
     "close:  close current client's window",
     "alert:  display warning box with custom message",
     "scroll:  scroll screen in distance(+,for upward scroll and -,for downward scroll)",
     "locate:  locate object on image on screen, returns none if not found",
     "takeshot:  take screenshot of current client's screen and displays it",
     "shell:  start reverse shell"
