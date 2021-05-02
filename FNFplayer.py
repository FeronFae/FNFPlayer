"""
A scirpt to automatically play ninjamuffin99's Friday Night Funkin' (currently only supports Fullscreen Windowed @ 1080p and Weeks 1 through 5) by




          _____                    _____                    _____                  _______                  _____                    _____                    _____                    _____          
         /\    \                  /\    \                  /\    \                /::\    \                /\    \                  /\    \                  /\    \                  /\    \         
        /::\    \                /::\    \                /::\    \              /::::\    \              /::\____\                /::\    \                /::\    \                /::\    \        
       /::::\    \              /::::\    \              /::::\    \            /::::::\    \            /::::|   |               /::::\    \              /::::\    \              /::::\    \       
      /::::::\    \            /::::::\    \            /::::::\    \          /::::::::\    \          /:::::|   |              /::::::\    \            /::::::\    \            /::::::\    \      
     /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \        /:::/~~\:::\    \        /::::::|   |             /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \     
    /:::/__\:::\    \        /:::/__\:::\    \        /:::/__\:::\    \      /:::/    \:::\    \      /:::/|::|   |            /:::/__\:::\    \        /:::/__\:::\    \        /:::/__\:::\    \    
   /::::\   \:::\    \      /::::\   \:::\    \      /::::\   \:::\    \    /:::/    / \:::\    \    /:::/ |::|   |           /::::\   \:::\    \      /::::\   \:::\    \      /::::\   \:::\    \   
  /::::::\   \:::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \  /:::/____/   \:::\____\  /:::/  |::|   | _____    /::::::\   \:::\    \    /::::::\   \:::\    \    /::::::\   \:::\    \  
 /:::/\:::\   \:::\    \  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\____\|:::|    |     |:::|    |/:::/   |::|   |/\    \  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\    \ 
/:::/  \:::\   \:::\____\/:::/__\:::\   \:::\____\/:::/  \:::\   \:::|    |:::|____|     |:::|    /:: /    |::|   /::\____\/:::/  \:::\   \:::\____\/:::/  \:::\   \:::\____\/:::/__\:::\   \:::\____\
\::/    \:::\   \::/    /\:::\   \:::\   \::/    /\::/   |::::\  /:::|____|\:::\    \   /:::/    /\::/    /|::|  /:::/    /\::/    \:::\   \::/    /\::/    \:::\  /:::/    /\:::\   \:::\   \::/    /
 \/____/ \:::\   \/____/  \:::\   \:::\   \/____/  \/____|:::::\/:::/    /  \:::\    \ /:::/    /  \/____/ |::| /:::/    /  \/____/ \:::\   \/____/  \/____/ \:::\/:::/    /  \:::\   \:::\   \/____/ 
          \:::\    \       \:::\   \:::\    \            |:::::::::/    /    \:::\    /:::/    /           |::|/:::/    /            \:::\    \               \::::::/    /    \:::\   \:::\    \     
           \:::\____\       \:::\   \:::\____\           |::|\::::/    /      \:::\__/:::/    /            |::::::/    /              \:::\____\               \::::/    /      \:::\   \:::\____\    
            \::/    /        \:::\   \::/    /           |::| \::/____/        \::::::::/    /             |:::::/    /                \::/    /               /:::/    /        \:::\   \::/    /    
             \/____/          \:::\   \/____/            |::|  ~|               \::::::/    /              |::::/    /                  \/____/               /:::/    /          \:::\   \/____/     
                               \:::\    \                |::|   |                \::::/    /               /:::/    /                                        /:::/    /            \:::\    \         
                                \:::\____\               \::|   |                 \::/____/               /:::/    /                                        /:::/    /              \:::\____\        
                                 \::/    /                \:|   |                  ~~                     \::/    /                                         \::/    /                \::/    /        
                                  \/____/                  \|___|                                          \/____/                                           \/____/                  \/____/         
                                                                                                                                                                                                      
"""


#Imports

import pyautogui
import keyboard as key
from multiprocessing import Process

#Main Arguments

class loop():
    
    def left():
        while 1:
            scan.left()
            key_up.left(inp_l)
            key_down.left(inp_l)
    
    def down():
        while 1:
            scan.down()
            key_up.down(inp_d)
            key_down.down(inp_d)

    def up():
        while 1:
            scan.up()
            key_up.up(inp_u)
            key_down.up(inp_u)
    
    def right():
        while 1:
            scan.right()
            key_up.right(inp_r)
            key_down.right(inp_r)
        





class scan():

    def left():
        global inp_l
        if pyautogui.pixelMatchesColor(1086, 210, (194, 75, 153)) == True:
            inp_l = 1
        else:
            inp_l = 0
            
    def down():
        global inp_d
        if pyautogui.pixelMatchesColor(1263, 210, (0, 255, 255)) == True:
            inp_d = 2
        else:
            inp_d = 0
            
    def up():
        global inp_u
        if pyautogui.pixelMatchesColor(1423, 210, (18, 250, 5)) == True:
            inp_u = 3
        else:
            inp_u = 0
            
    def right():
        global inp_r
        if pyautogui.pixelMatchesColor(1590, 210, (249, 57, 63)) == True:
            inp_r = 4
        else:
            inp_r = 0

class key_up():

    def left(inp_l):
        if inp_l == 1:
            key.release('left')
        elif inp_l == 0:
            pass

    def down(inp_d):
        if inp_d == 2:
            key.release('down')
        elif inp_d == 0:
            pass
        
    def up(inp_u):
        if inp_u == 3:
            key.release('up')
        elif inp_u == 0:
            pass

    def right(inp_r):
        if inp_r == 4:
            key.release('right')
        elif inp_r == 0:
            pass

class key_down():    

    def left(inp_l):
        if inp_l == 1:
            key.press('left')
        elif inp_l == 0:
            pass

    def down(inp_d):
        if inp_d == 2:
            key.press('down')
        elif inp_d == 0:
            pass
        
    def up(inp_u):        
        if inp_u == 3:
            key.press('up')
        elif inp_u == 0:
            pass
        
    def right(inp_r):
        if inp_r == 4:
            key.press('right')
        elif inp_r == 0:
            pass
        

if __name__ == '__main__':
    Process(target=loop.left).start()
    Process(target=loop.down).start()
    Process(target=loop.up).start()
    Process(target=loop.right).start()
