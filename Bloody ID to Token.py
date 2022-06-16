import os
import base64
import ctypes
import pystyle
from console.utils import set_title
from time import sleep
from pystyle import *

banner = """
██████╗ ██╗      ██████╗  ██████╗ ██████╗ ██╗   ██╗                              
██╔══██╗██║     ██╔═══██╗██╔═══██╗██╔══██╗╚██╗ ██╔╝                              
██████╔╝██║     ██║   ██║██║   ██║██║  ██║ ╚████╔╝                               
██╔══██╗██║     ██║   ██║██║   ██║██║  ██║  ╚██╔╝                                
██████╔╝███████╗╚██████╔╝╚██████╔╝██████╔╝   ██║                                 
╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝    ╚═╝                                 
                                                                                 
██╗██████╗     ████████╗ ██████╗     ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗
██║██╔══██╗    ╚══██╔══╝██╔═══██╗    ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║
██║██║  ██║       ██║   ██║   ██║       ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║
██║██║  ██║       ██║   ██║   ██║       ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║
██║██████╔╝       ██║   ╚██████╔╝       ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║
╚═╝╚═════╝        ╚═╝    ╚═════╝        ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝"""
set_title("Bloody ID to Token | Loading | by Bloody")
Anime.Fade(Center.Center(banner), Colors.purple_to_blue, Colorate.Vertical, interval=0.025, time=3)
print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(banner)))

set_title("Bloody ID to Token | Enter User ID | Bloody")
userid = Write.Input("User ID:\n", Colors.purple_to_blue, interval=0.008)
encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
os.system('cls')

set_title("Bloody ID to Token | Success | by Bloody")
Write.Print(f'Token First Part:\n{encodedStr}\n', Colors.purple_to_blue, interval=0.008)
sleep(3)
Write.Print(f'Press any key to exit\n', Colors.purple_to_blue, interval=0.008)
os.system('pause >nul')
