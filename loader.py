import os
import time

def wait(x):
    time.sleep(x)

def clear():
    os.system("cls")

def logo():
    print("""
                                           
         ,---._      ,----..               
       .-- -.' \    /   /   \   .--.--.    
       |    |   :  /   .     : /  /    '.  
       :    ;   | .   /   ;.  \  :  /`. /  
       :        |.   ;   /  ` ;  |  |--`   
       |    :   :;   |  ; \ ; |  :  ;_     
       :         |   :  | ; | '\  \    `.  
       |    ;   |.   |  ' ' ' : `----.   \ 
   ___ l         '   ;  \; /  | __ \  \  | 
 /    /\    J   : \   \  ',  / /  /`--'  / 
/  ../  `..-    ,  ;   :    / '--'.     /  
\    \         ;    \   \ .'    `--'---'   
 \    \      ,'      `---`                 
  "---....--'                              
                                           
""")

def LoadBIOS():
    clear()
    logo()
    print("Loading BIOS...")
    wait(2)
    clear()
    print("Loaded BIOS")
    print("""
    [1] = EFI Shell
    [2] = JOS
    """)
    BIOSinput = input("/:")
    if BIOSinput == "1":
        clear()
        BIOSSel = input("/:/")
        if BIOSSel == "boot":
            LoadJOS()
    if BIOSinput == "2":
        LoadJOS()

def LoadJOS():
    clear()
    print("Loading JOS.")
    wait(.5)
    clear()
    print("Loading JOS..")
    wait(.5)
    clear()
    print("Loading JOS...")
    wait(.5)
    clear()
    commline()


def commline():
    commlinein = input("J:/")

    if commlinein == "LoadBIOS":
        BIOSinput = "1"
        LoadBIOS()
    

LoadBIOS()
    