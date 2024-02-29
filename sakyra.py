import os
import sys
os.system('color')
print("""                                 
▄██    ▀█         ██                                 
▀███▄    ▄█▀██▄   ██  ▄██▀▀██▀   ▀██▀███▄███ ▄█▀██▄  
  ▀█████▄█   ██   ██ ▄█     ██   ▄█   ██▀ ▀▀██   ██  
▄     ▀██▄█████   ██▄██      ██ ▄█    ██     ▄█████  
██     ███   ██   ██ ▀██▄     ███     ██    ██   ██  
█▀█████▀▀████▀██▄████▄ ██▄▄   ▄█    ▄████▄  ▀████▀██▄
                            ▄█                       
                          ██▀                        """)  

print("\033[0;35m")  # Reset text color

print("\033[0;35m")  # Set text color to bright blue
print(f"""▀ ▀
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                     [1] UrlFlooder             [10] View wifi pass
                                     [2] Webhook Spammer        [11] Password Generator
                                     [3] Nuker                  [12] Fake Info Gen
                                     [4] IP Address Lookup      [13] URL Shorten
                                     [5] IP Pinger              [14] QR Code Gen
                                     [6] IP Loggers             [15] Open Sakyra ♥
                                     [7] Screenshot Grabber     [16] DoxTracker
                                     [8] WebHook Remover        [17] setup☑
                                     [9] Linkvertise bypasser   [18] User search☭
                                     
●/
/▌
/ \. . . . . . . . . . . . . . . . . .                                                                                                                                                             
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
print("\033[0m")  # Reset text color



while True:
    print("\033[0;35m")
    q = input("> ")
    if q == "1":
        
        from data import UrlFlooder
        UrlFlooder.start()

    elif q == "2":
     from data import WebhookSpam
    elif q=="3":
        from data import nuke
    elif q == "4":
        from data import ipicker
    elif q == "5":
        from data import pinger
    elif q == "6":
        from data import Loggers
    elif q =="7":
        from data import screen
    elif q =="8":
        from data import webhookremover
    elif q =='9':
        from data import linkvertex
    elif q=='10':
        from data import wifi
    elif q=='11':
        from data import passgen
    elif q=='12':
        from data import persongen
    elif q=='13':
        from data import gentiny2
    elif q=='14':
        from data import qr
    elif q=='15':
        from data import sakura
    elif q=='16':
        from data import DoxTracker
    elif q=='17':
        from data import setup
    elif q=='18':
        from data import seeryra
    elif q=='19':
        from data import vfye


    else:
        print("invalid character")
    

        

        
