# tag: fourteam-bos-main
try:
    try:
        import os
        import random
        import time
        cwd = os.getcwd()
        def clear_screen():
            os.system('cls' if os.name == 'nt' else 'clear')
        def advanced_boot_screen():
            clear_screen()

            print("\033[93;1m╔══════════════════════════════════════════╗")
            print("║                 MADE BY                  ║")
            print("║                   4T                     ║")
            print("╚══════════════════════════════════════════╝")
            time.sleep(2)

            print("\nLoading")
            for i in range(101):
                progress = "[" + "█" * (i // 2) + " " * (50 - i // 2) + "]"
                print(f"\r{progress} {i}%", end='', flush=True)
                time.sleep(0.03)
            clear_screen()

            print("\n╔══════════════════════════════════════════╗")
            print("║                   bOS                    ║")
            print("╚══════════════════════════════════════════╝\033[0m")
            tips = ["command help for help", "better to install newer versions", "command set for settings"]
            print(f"\033[92;1mTIP: {random.choice(tips)}\033[0m")
        advanced_boot_screen()
        import requests
        import sys
        import random
        import datetime
        import zipfile
        import shutil
        import webbrowser
        import plyer
        from locale import currency
        import platform
        import atexit
        import glob
        import importlib
        import sys
        import logging
        import keyboard
        from ping3 import ping, verbose_ping
        import json
        from threading import Thread
        import ctypes
        import elevate
        import argparse
        import subprocess
        from encrypter import encrypt_message, decrypt_message
        from collections import defaultdict
        import curses
        import math
        from colorama import init, Fore, Style
        
        root = ""

        def info():
            """
            Displays comprehensive operating system information.
            """
            print("\n" + "="*60)
            print("YOUR OS INFO")
            print("="*60)
    
            # Get basic system information
            print(f"\n{'System:':<25} {platform.system()}")
            print(f"{'Node Name:':<25} {platform.node()}")
            print(f"{'Release:':<25} {platform.release()}")
            print(f"{'Version:':<25} {platform.version()}")
            print(f"{'Machine:':<25} {platform.machine()}")
            print(f"{'Processor:':<25} {platform.processor()}")
    
            # Get OS-specific information
            system_name = platform.system()
    
            if system_name == "Windows":
                print(f"{'Windows Edition:':<25} {platform.win32_edition()}")
                print(f"{'Windows Version:':<25} {platform.win32_ver()[0]}")
            elif system_name == "Darwin":  # macOS
                mac_ver = platform.mac_ver()
                print(f"{'macOS Version:':<25} {mac_ver[0]}")
            elif system_name == "Linux":
                # Try to get Linux distribution info
                try:
                    import distro
                    print(f"{'Distribution:':<25} {distro.name()}")
                    print(f"{'Version:':<25} {distro.version()}")
                    print(f"{'Codename:':<25} {distro.codename()}")
                except ImportError:
                    print(f"{'Distribution:':<25} Linux (install 'distro' package for more details)")
    
            # Get Python information
            print(f"\n{'Python Version:':<25} {platform.python_version()}")
            print(f"{'Python Compiler:':<25} {platform.python_compiler()}")
            print(f"{'Python Implementation:':<25} {platform.python_implementation()}")
            print(f"{'Python Build:':<25} {platform.python_build()[0]}")
    
            # Get system architecture
            print(f"\n{'Architecture:':<25} {platform.architecture()[0]}")
    
            # Get platform details
            print(f"{'Platform:':<25} {platform.platform()}")
    
            # Additional information
            print(f"\n{'Current User:':<25} {platform.uname().node.split('-')[0] if '-' in platform.uname().node else platform.uname().node}")
            print(f"{'Report Time:':<25} {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"{'System Uptime:':<25} {uptime()}")
    
            print("\n" + "="*60)

            print("\n" + "="*60)
            print("bOS INFO")
            print("="*60)

            print("Name: bOS")
            print("Build: v1.3")
            f = open(cwd+"/ver.4t","r")
            print(f"Version: v{f.read()}")
            llog = os.environ.get("llog")
            print(f"Lanuncher {llog}")
            vllog = os.environ.get("vllog")
            print(f"Launcher version: {vllog}")

        def uptime():
            """
            Helper function to get system uptime.
            Returns formatted uptime string.
            """
            try:
                if platform.system() == "Windows":
                    import ctypes
                    lib = ctypes.windll.kernel32
                    tick_count = lib.GetTickCount64()
                    uptime_seconds = tick_count // 1000
                else:
                    with open('/proc/uptime', 'r') as f:
                        uptime_seconds = float(f.readline().split()[0])
        
                # Convert seconds to days, hours, minutes
                days = int(uptime_seconds // 86400)
                hours = int((uptime_seconds % 86400) // 3600)
                minutes = int((uptime_seconds % 3600) // 60)
        
                if days > 0:
                    return f"{days}d {hours}h {minutes}m"
                elif hours > 0:
                    return f"{hours}h {minutes}m"
                else:
                    return f"{minutes}m"
            
            except:
                return "Unable to determine"

        def show_hacking_simulation():
            """
            ULTIMATE RANDOMNESS - ABSOLUTE CHAOS MEGA EDITION
            If this doesn't look like hacking reality itself, nothing will.
            """
    
            # Global chaos controller
            class Chaos:
                def __init__(self):
                    self.reality_glitch_level = 0
                    self.quantum_entropy = random.random()
                    self.universe_instability = 1.0
                    self.meme_density = 0
                    self.existential_crisis = False
                    self.color_mania = 0
                    self.text_frenzy = 0
            
                def increase_chaos(self):
                    self.reality_glitch_level += random.random() * 0.1
                    self.quantum_entropy = (self.quantum_entropy + random.random()) % 1.0
                    self.universe_instability *= 1.01
                    self.meme_density += random.randint(0, 5)
                    self.color_mania += random.random() * 0.05
                    self.text_frenzy += random.random() * 0.03
            
                def should_break_reality(self):
                    return random.random() < (self.reality_glitch_level * 0.01)
        
                def should_color_explosion(self):
                    return random.random() < (self.color_mania * 0.02)
        
                def should_text_frenzy(self):
                    return random.random() < (self.text_frenzy * 0.03)
    
            chaos = Chaos()
    
            # MEGA COLOR PALETTE
            class Colors:
                # Basic ANSI colors
                BLACK = '\033[30m'
                RED = '\033[31m'
                GREEN = '\033[32m'
                YELLOW = '\033[33m'
                BLUE = '\033[34m'
                MAGENTA = '\033[35m'
                CYAN = '\033[36m'
                WHITE = '\033[37m'
                GRAY = '\033[90m'
                BRIGHT_RED = '\033[91m'
                BRIGHT_GREEN = '\033[92m'
                BRIGHT_YELLOW = '\033[93m'
                BRIGHT_BLUE = '\033[94m'
                BRIGHT_MAGENTA = '\033[95m'
                BRIGHT_CYAN = '\033[96m'
                BRIGHT_WHITE = '\033[97m'
        
                # Styles
                RESET = '\033[0m'
                BOLD = '\033[1m'
                FAINT = '\033[2m'
                ITALIC = '\033[3m'
                UNDERLINE = '\033[4m'
                BLINK_SLOW = '\033[5m'
                BLINK_FAST = '\033[6m'
                REVERSE = '\033[7m'
                HIDDEN = '\033[8m'
                STRIKETHROUGH = '\033[9m'
                DOUBLE_UNDERLINE = '\033[21m'
                FRAMED = '\033[51m'
                ENCIRCLED = '\033[52m'
                OVERLINED = '\033[53m'
        
                # Background colors
                BG_BLACK = '\033[40m'
                BG_RED = '\033[41m'
                BG_GREEN = '\033[42m'
                BG_YELLOW = '\033[43m'
                BG_BLUE = '\033[44m'
                BG_MAGENTA = '\033[45m'
                BG_CYAN = '\033[46m'
                BG_WHITE = '\033[47m'
                BG_GRAY = '\033[100m'
                BG_BRIGHT_RED = '\033[101m'
                BG_BRIGHT_GREEN = '\033[102m'
                BG_BRIGHT_YELLOW = '\033[103m'
                BG_BRIGHT_BLUE = '\033[104m'
                BG_BRIGHT_MAGENTA = '\033[105m'
                BG_BRIGHT_CYAN = '\033[106m'
                BG_BRIGHT_WHITE = '\033[107m'
        
                # 256 colors
                COLORS_256 = [f'\033[38;5;{i}m' for i in range(256)]
                BG_COLORS_256 = [f'\033[48;5;{i}m' for i in range(256)]
        
                # True color RGB
                @staticmethod
                def rgb(r, g, b):
                    return f'\033[38;2;{r};{g};{b}m'
        
                @staticmethod
                def bg_rgb(r, g, b):
                    return f'\033[48;2;{r};{g};{b}m'
        
                # Random true color
                @staticmethod
                def random_rgb():
                    return Colors.rgb(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        
                @staticmethod
                def random_bg_rgb():
                    return Colors.bg_rgb(random.randint(0,255), random.randint(0,255), random.randint(0,255))
        
                # Special color effects
                @staticmethod
                def rainbow_text(text, speed=1):
                    result = ""
                    colors = [
                        Colors.rgb(255, 0, 0),    # Red
                        Colors.rgb(255, 127, 0),  # Orange
                        Colors.rgb(255, 255, 0),  # Yellow
                        Colors.rgb(0, 255, 0),    # Green
                        Colors.rgb(0, 0, 255),    # Blue
                        Colors.rgb(75, 0, 130),   # Indigo
                        Colors.rgb(143, 0, 255),  # Violet
                    ]
                    for i, char in enumerate(text):
                        if char != ' ':
                            result += colors[(i // speed) % len(colors)] + char
                        else:
                            result += char
                    return result + Colors.RESET
        
                @staticmethod
                def gradient_text(text, start_rgb, end_rgb):
                    result = ""
                    start_r, start_g, start_b = start_rgb
                    end_r, end_g, end_b = end_rgb
                    length = len(text)
                    for i, char in enumerate(text):
                        if char != ' ':
                            r = int(start_r + (end_r - start_r) * i / length)
                            g = int(start_g + (end_g - start_g) * i / length)
                            b = int(start_b + (end_b - start_b) * i / length)
                            result += Colors.rgb(r, g, b) + char
                        else:
                            result += char
                    return result + Colors.RESET
        
                @staticmethod
                def glitch_effect(text):
                    effects = [Colors.REVERSE, Colors.BLINK_SLOW, Colors.BLINK_FAST, 
                              Colors.ITALIC, Colors.STRIKETHROUGH, Colors.HIDDEN,
                              Colors.FRAMED, Colors.ENCIRCLED, Colors.OVERLINED]
                    return random.choice(effects) + text + Colors.RESET
        
                @staticmethod
                def random_style():
                    styles = []
                    if random.random() > 0.5:
                        styles.append(Colors.BOLD)
                    if random.random() > 0.7:
                        styles.append(Colors.ITALIC)
                    if random.random() > 0.6:
                        styles.append(Colors.UNDERLINE)
                    if random.random() > 0.8:
                        styles.append(random.choice([Colors.BLINK_SLOW, Colors.BLINK_FAST]))
                    if random.random() > 0.9:
                        styles.append(Colors.REVERSE)
                    return ''.join(styles)
    
            # CRAZY CHARACTER SETS
            CRAZY_SETS = [
                "䷀䷁䷂䷃䷄䷅䷆䷇䷈䷉䷊䷋䷌䷍䷎䷏䷐䷑䷒䷓䷔䷕䷖䷗䷘䷙䷚䷛䷜䷝䷞䷟",
                "♔♕♖♗♘♙♚♛♜♝♞♟♠♡♢♣♤♥♦♧",
                "☯☮☢☣☤☥☦☧☨☩☪☫☬☭☄☼☽☾♁♨❄❅❆",
                "ᚠᚢᚦᚨᚱᚲᚷᚹᚺᚻᚾᚿᛀᛁᛂᛃᛄᛅᛆᛇᛈᛉᛊᛋᛌᛍᛎᛏᛐᛑᛒᛓᛔᛕᛖᛗᛘᛙᛚᛛᛜᛝᛞᛟ",
                "∀∁∂∃∄∅∆∇∈∉∊∋∌∍∎∏∐∑−∓∔∕∖∗∘∙√∛∜∝∞∟∠∡∢∣∤∥∦∧∨∩∪∫∬∭∮∯∰∱∲∳∴∵∶∷∸∹∺∻∼∽∾∿≀≁≂≃≄≅≆≇≈≉≊≋≌≍≎≏≐≑≒≓≔≕≖≗≘≙≚≛≜≝≞≟≠≡≢≣≤≥≦≧≨≩≪≫≬≭≮≯≰≱≲≳≴≵≶≷≸≹≺≻≼≽≾≿⊀⊁⊂⊃⊄⊅⊆⊇⊈⊉⊊⊋⊌⊍⊎⊏⊐⊑⊒⊓⊔⊕⊖⊗⊘⊙⊚⊛⊜⊝⊞⊟⊠⊡⊢⊣⊤⊥⊦⊧⊨⊩⊪⊫⊬⊭⊮⊯⊰⊱⊲⊳⊴⊵⊶⊷⊸⊹⊺⊻⊼⊽⊾⊿⋀⋁⋂⋃⋄⋅⋆⋇⋈⋉⋊⋋⋌⋍⋎⋏⋐⋑⋒⋓⋔⋕⋖⋗⋘⋙⋚⋛⋜⋝⋞⋟⋠⋡⋢⋣⋤⋥⋦⋧⋨⋩⋪⋫⋬⋭⋮⋯⋰⋱⋲⋳⋴⋵⋶⋷⋸⋹⋺⋻⋼⋽⋾⋿",
                "𓀀𓀁𓀂𓀃𓀄𓀅𓀆𓀇𓀈𓀉𓀊𓀋𓀌𓀍𓀎𓀏𓀐𓀑𓀒𓀓𓀔𓀕𓀖𓀗𓀘𓀙𓀚𓀛𓀜𓀝𓀞𓀟𓀠𓀡𓀢𓀣𓀤𓀥𓀦𓀧𓀨𓀩𓀪𓀫𓀬𓀭𓀮𓀯𓀰𓀱𓀲𓀳𓀴𓀵𓀶𓀷𓀸𓀹𓀺𓀻𓀼𓀽𓀾𓀿𓁀𓁁𓁂𓁃𓁄𓁅𓁆𓁇𓁈𓁉𓁊𓁋𓁌𓁍𓁎𓁏𓁐𓁑𓁒𓁓𓁔𓁕𓁖𓁗𓁘𓁙𓁚𓁛𓁜𓁝𓁞𓁟𓁠𓁡𓁢𓁣𓁤𓁥𓁦𓁧𓁨𓁩𓁪𓁫𓁬𓁭𓁮𓁯𓁰𓁱𓁲𓁳𓁴𓁵𓁶𓁷𓁸𓁹𓁺𓁻𓁼𓁽𓁾𓁿𓂀𓂁𓂂𓂃𓂄𓂅𓂆𓂇𓂈𓂉𓂊𓂋𓂌𓂍𓂎𓂏𓂐𓂑𓂒𓂓𓂔𓂕𓂖𓂗𓂘𓂙𓂚𓂛𓂜𓂝𓂞𓂟𓂠𓂡𓂢𓂣𓂤𓂥𓂦𓂧𓂨𓂩𓂪𓂫𓂬𓂭𓂮𓂯𓂰𓂱𓂲𓂳𓂴𓂵𓂶𓂷𓂸𓂹𓂺𓂻𓂼𓂽𓂾𓂿𓃀𓃁𓃂𓃃𓃄𓃅𓃆𓃇𓃈𓃉𓃊𓃋𓃌𓃍𓃎𓃏𓃐𓃑𓃒𓃓𓃔𓃕𓃖𓃗𓃘𓃙𓃚𓃛𓃜𓃝𓃞𓃟𓃠𓃡𓃢𓃣𓃤𓃥𓃦𓃧𓃨𓃩𓃪𓃫𓃬𓃭𓃮𓃯𓃰𓃱𓃲𓃳𓃴𓃵𓃶𓃷𓃸𓃹𓃺𓃻𓃼𓃽𓃾𓃿",
                "ༀ༁༂༃༄༅༆༇༈༉༊་༌།༎༏༐༑༒༓༔༕༖༗༘༙༚༛༜༝༞༟༠༡༢༣༤༥༦༧༨༩༪༫༬༭༮༯༰༱༲༳༴༵༶༷༸༹༺༻༼༽༾༿ཀཁགགྷངཅཆཇཉཊཋཌཌྷཎཏཐདདྷནཔཕབབྷམཙཚཛཛྷཝཞཟའཡརལཤཥསཧཨཀྵཪཫཬ",
                "┌┐└┘├┤┬┴┼╔╗╚╝╠╣╦╩╬╒╓╔╕╖╗╘╙╚╛╜╝╞╟╠╡╢╣╤╥╦╧╨╩╪╫╬╭╮╯╰╱╲╳╴╵╶╷╸╹╺╻╼╽╾╿",
                "█▓▒░▄▀▌▐■□▪▫◦▬▭▮▯▰▱▲△▴▵▶▷▸▹►▻▼▽▾▿◀◁◂◃◄◅◆◇◈◉◊○◌◍◎●◐◑◒◓◔◕◖◗◘◙◚◛◜◝◞◟◠◡◢◣◤◥◦◧◨◩◪◫◬◭◮◯◰◱◲◳◴◵◶◷◸◹◺◻◼◽◾◿",
                "⣀⣁⣂⣃⣄⣅⣆⣇⣈⣉⣊⣋⣌⣍⣎⣏⣐⣑⣒⣓⣔⣕⣖⣗⣘⣙⣚⣛⣜⣝⣞⣟⣠⣡⣢⣣⣤⣥⣦⣧⣨⣩⣪⣫⣬⣭⣮⣯⣰⣱⣲⣳⣴⣵⣶⣷⣸⣹⣺⣻⣼⣽⣾⣿",
                "🎮🕹️👾💻🖥️💾📠📡🔌🔋💡📱📲⌚⌛⏰⏱️⏲️⏳🗜️💽💾💿📀📼📷📹📽️🎞️📞☎️📟📠📺📻🎙️🎚️🎛️🧭⚗️🧪🧫🧬🔬🔭📡💉🩸💊🩹🩺🚪🛏️🛋️🚿🛁🚽🧻🧸🧷🧹🧺🧻🧼🧽🧯🛒🚬⚰️⚱️🗿🛢️🧭🧱",
                "🌌🌍🌎🌏🌐🌑🌒🌓🌔🌕🌖🌗🌘🌙🌚🌛🌜☀️🌝🌞⭐🌟🌠☁️⛅⛈️🌤️🌥️🌦️🌧️🌨️🌩️🌪️🌫️🌬️🌀🌈🌂☂️☔⛱️⚡❄️☃️⛄☄️🔥💧🌊🎃🎄🎆🎇✨🎈🎉🎊🎋🎍🎎🎏🎐🎑🎀🎁🎗️🎟️🎫🎖️🏆🏅🥇🥈🥉⚽⚾🏀🏐🏈🏉🎾🏏🏑🏒🥍🏓🏸🥊🥋🥅⛳⛸️🎣🎽🎿🛷🥌🎯🎱🔮🎮🕹️🎰🎲🧩♟️🎭🎨🧵🎼🎵🎶🎤🎧🎷🎸🎹🎺🎻🥁📱📲☎️📞📟📠🔋🔌💻🖥️🖨️⌨️🖱️🖲️💽💾💿📀🧮🎥🎞️📽️🎬📺📷📸📹📼🔍🔎🕯️💡🔦🏮📔📕📖📗📘📙📚📓📒📃📜📄📰🗞️📑🔖🏷️💰💴💵💶💷💸💳🧾💹💱💲✉️📧📨📩📤📥📦📫📪📬📭📮🗳️✏️✒️🖋️🖊️🖌️🖍️📝💼📁📂🗂️📅📆🗒️🗓️📇📈📉📊📋📌📍📎🖇️📏📐✂️🗃️🗄️🗑️🔒🔓🔏🔐🔑🗝️🔨⛏️⚒️🛠️🗡️⚔️🔫🏹🛡️🔧🔩⚙️🗜️⚗️⚖️🔗⛓️🧰🧲🧪🧫🧬🔬🔭📡💉🩸💊🩹🩺🚪🛏️🛋️🚿🛁🚽🧻🧸🧷🧹🧺🧻🧼🧽🧯🛒🚬⚰️⚱️🗿🏧🚮🚰♿🚹🚺🚻🚼🚾🛂🛃🛄🛅⚠️🚸⛔🚫🚳🚭🚯🚱🚷📵🔞☢️☣️⬆️↗️➡️↘️⬇️↙️⬅️↖️↕️↔️↩️↪️⤴️⤵️🔃🔄🔙🔚🔛🔜🔝🛐⚛️🕉️✡️☸️☯️✝️☦️☪️☮️🕎🔯♈♉♊♋♌♍♎♏♐♑♒♓⛎🔀🔁🔂▶️⏩⏭️⏯️◀️⏪⏮️🔼⏫🔽⏬⏸️⏹️⏺️⏏️🎦🔅🔆📶📳📴♀️♂️⚕️♾️✖️➕➖➗♻️⚜️🔱📛🔰⭕✅☑️✔️❌❎➰➿〽️✳️✴️❇️©️®️™️#️⃣*️⃣0️⃣1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣🔟🔠🔡🔢🔣🔤🅰️🆎🅱️🆑🆒🆓ℹ️🆔Ⓜ️🆕🆖🅾️🆗🅿️🆘🆙🆚🈁🈂️🈷️🈶🈯🉐🈹🈚🈲🉑🈸🈴🈳㊗️㊙️🈺🈵🔴🟠🟡🟢🔵🟣🟤⚫⚪🟥🟧🟨🟩🟦🟪🟫⬛⬜◼️◻️◾◽▪️▫️🔶🔷🔸🔹🔺🔻💠🔘🔳🔲",
                "ᕕ( ᐛ )ᕗ(╯°□°）╯︵ ┻━┻(•_•)( •_•)>⌐■-■(⌐■_■)¯\\_(ツ)_/¯( ͡° ͜ʖ ͡°)(⊙_☉)ಠ_ಠ(☞ﾟヮﾟ)☞(¬_¬)(•‿•)(ง'̀-'́)ง(ʘᗩʘ')ಥ_ಥ(◕‿◕)(づ￣ ³￣)づ(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧✧ﾟ･: *ヽ(◕ヮ◕)ﾉ(╥﹏╥)(◔_◔)(ಠ_ಠ)━╤デ╦︻(▀̿Ĺ̯▀̿ ̿)(▀̿Ĺ̯▀̿ ̿)🔫(⌐■_■)––■-■–––( ˘ ³˘)♥( ˇ෴ˇ )",
                "010010000110010101101100011011000110111100100000010101110110111101110010011011000110010000100001",
                "DEADBEEFCAFEBABEFACEB00C1BADB002BAADF00D8BADF00DFEEDDADEADDECADE",
                "↑↓←→↔↕↖↗↘↙⇄⇅⇆⇇⇈⇉⇊⇋⇌⇍⇎⇏⇐⇑⇒⇓⇔⇕⇖⇗⇘⇙⇚⇛⇜⇝⇞⇟⇠⇡⇢⇣⇤⇥⇦⇧⇨⇩⇪⌅⌆⌤⏎↩↪↫↬↭↮↯↰↱↲↳↴↵↶↷↸↹↺↻↼↽↾↿⇀⇁⇂⇃⇄⇅⇆⇇⇈⇉⇊⇋⇌⇍⇎⇏⇐⇑⇒⇓⇔⇕⇖⇗⇘⇙⇚⇛⇜⇝⇞⇟⇠⇡⇢⇣⇤⇥⇦⇧⇨⇩⇪",
                "∞≠≡≤≥±∓×÷√∛∜∫∬∭∮∯∰∱∲∳∴∵∶∷∸∹∺∻∼∽∾∿≀≁≂≃≄≅≆≇≈≉≊≋≌≍≎≏≐≑≒≓≔≕≖≗≘≙≚≛≜≝≞≟≠≡≢≣≤≥≦≧≨≩≪≫≬≭≮≯≰≱≲≳≴≵≶≷≸≹≺≻≼≽≾≿⊀⊁⊂⊃⊄⊅⊆⊇⊈⊉⊊⊋⊌⊍⊎⊏⊐⊑⊒⊓⊔⊕⊖⊗⊘⊙⊚⊛⊜⊝⊞⊟⊠⊡⊢⊣⊤⊥⊦⊧⊨⊩⊪⊫⊬⊭⊮⊯⊰⊱⊲⊳⊴⊵⊶⊷⊸⊹⊺⊻⊼⊽⊾⊿⋀⋁⋂⋃⋄⋅⋆⋇⋈⋉⋊⋋⋌⋍⋎⋏⋐⋑⋒⋓⋔⋕⋖⋗⋘⋙⋚⋛⋜⋝⋞⋟⋠⋡⋢⋣⋤⋥⋦⋧⋨⋩⋪⋫⋬⋭⋮⋯⋰⋱⋲⋳⋴⋵⋶⋷⋸⋹⋺⋻⋼⋽⋾⋿",
                "🤖👽👾🤯💀☠️👻💩🤡👹👺👁️👁️‍🗨️🧠🦷🦴👀👂👃👄👅👤👥👣💋🦿🦵🦶🦴🧑👩👨🧒👧👦👶👴👵🧓🧔👱👱‍♀️👱‍♂️🧔‍♀️🧔‍♂️👨‍🦰👩‍🦰👨‍🦱👩‍🦱👨‍🦳👩‍🦳👨‍🦲👩‍🦲🧑‍🦰🧑‍🦱🧑‍🦳🧑‍🦲👮👮‍♀️👮‍♂️🕵️🕵️‍♀️🕵️‍♂️💂💂‍♀️💂‍♂️👷👷‍♀️👷‍♂️🤴👸👳👳‍♀️👳‍♂️👲🧕🤵👰🤰🤱👼🎅🤶🦸🦸‍♀️🦸‍♂️🦹🦹‍♀️🦹‍♂️🧙🧙‍♀️🧙‍♂️🧚🧚‍♀️🧚‍♂️🧛🧛‍♀️🧛‍♂️🧜🧜‍♀️🧜‍♂️🧝🧝‍♀️🧝‍♂️🧞🧞‍♀️🧞‍♂️🧟🧟‍♀️🧟‍♂️💆💆‍♀️💆‍♂️💇💇‍♀️💇‍♂️🚶🚶‍♀️🚶‍♂️🏃🏃‍♀️🏃‍♂️💃🕺👯👯‍♀️👯‍♂️🧖🧖‍♀️🧖‍♂️🧗🧗‍♀️🧗‍♂️🤺🏇⛷️🏂🏌️🏌️‍♀️🏌️‍♂️🏄🏄‍♀️🏄‍♂️🚣🚣‍♀️🚣‍♂️🏊🏊‍♀️🏊‍♂️⛹️⛹️‍♀️⛹️‍♂️🏋️🏋️‍♀️🏋️‍♂️🚴🚴‍♀️🚴‍♂️🚵🚵‍♀️🚵‍♂️🤸🤸‍♀️🤸‍♂️🤼🤼‍♀️🤼‍♂️🤽🤽‍♀️🤽‍♂️🤾🤾‍♀️🤾‍♂️🤹🤹‍♀️🤹‍♂️🧘🧘‍♀️🧘‍♂️🛀🛌🧑‍🤝‍🧑👭👫👬💏👩‍❤️‍💋‍👨👨‍❤️‍💋‍👨👩‍❤️‍💋‍👩💑👩‍❤️‍👨👨‍❤️‍👨👩‍❤️‍👩👪👨‍👩‍👦👨‍👩‍👧👨‍👩‍👧‍👦👨‍👩‍👦‍👦👨‍👩‍👧‍👧👨‍👨‍👦👨‍👨‍👧👨‍👨‍👧‍👦👨‍👨‍👦‍👦👨‍👨‍👧‍👧👩‍👩‍👦👩‍👩‍👧👩‍👩‍👧‍👦👩‍👩‍👦‍👦👩‍👩‍👧‍👧👨‍👦👨‍👦‍👦👨‍👧👨‍👧‍👦👨‍👧‍👧👩‍👦👩‍👦‍👦👩‍👧👩‍👧‍👦👩‍👧‍👧🗣️👤👥👣",
                "⌚📱📲💻⌨️🖥️🖨️🖱️🖲️💽💾💿📀📼📷📹🎥📽️🎞️📞☎️📟📠📺📻🎙️🎚️🎛️🧭⏱️⏲️⏰🕰️⌛⏳📡🔋🔌💡🔦🕯️🗑️🧸🧷🧹🧺🧻🧼🧽🧯🛒🚬💊🩹🩺🚪🛏️🛋️🚿🛁🚽🧻",
                "🔥💧🌊💨❄️☀️⭐🌟💫✨☄️💥💦💨☁️⛈️🌩️🌪️🌈🌡️🌀🌊🌫️🌁🌃🌄🌅🌆🌇🌉🌌🎇🎆🌠🌌🪐",
            ]
    
            # CRAZY RANDOM TEXT GENERATORS
            def generate_crazy_text(length=50):
                """Generates completely random text"""
                charsets = [
                    "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                    "abcdefghijklmnopqrstuvwxyz",
                    "0123456789",
                    "!@#$%^&*()_+-=[]{}|;:,.<>?",
                    "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん",
                    "αβγδεζηθικλμνξοπρστυφχψω",
                    "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
                    "ابتثجحخدذرزسشصضطظعغفقكلمنهوي",
                    "ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ",
                    "🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉",
                ]
        
                text = ""
                for _ in range(length):
                    charset = random.choice(charsets + CRAZY_SETS)
                    text += random.choice(charset)
                return text
    
            def generate_leet_speak(text):
                """Converts text to leet speak"""
                leet_dict = {
                    'a': ['4', '@', '/\\', 'λ'],
                    'b': ['8', '|3', '13', '|8'],
                    'c': ['(', '<', '{', '©'],
                    'd': ['|)', '|]', '|>'],
                    'e': ['3', '€', '£', 'ë'],
                    'f': ['|=', 'ph', '|#'],
                    'g': ['6', '9', '&', 'C-'],
                    'h': ['#', '|-|', '}{', ']-['],
                    'i': ['1', '!', '|', ']['],
                    'j': ['_|', '_/', ']', ';'],
                    'k': ['|<', '|{', '|(', 'X'],
                    'l': ['|_', '|', '1', '£'],
                    'm': ['|\\/|', '/\\/\\', '|v|', '|T|'],
                    'n': ['|\\|', '/\\/', '|V', '/V'],
                    'o': ['0', '()', '[]', '°'],
                    'p': ['|*', '|>', '|D', '|7'],
                    'q': ['(,)', '0_', '0,', '¶'],
                    'r': ['|2', '|?', '|Z', '12'],
                    's': ['5', '$', 'z', '§'],
                    't': ['7', '+', '†', '|-'],
                    'u': ['|_|', '(_)', 'µ', 'v'],
                    'v': ['\\/', '|/', '\\|'],
                    'w': ['\\/\\/', 'vv', '\\X/', '\\^/'],
                    'x': ['><', '}{', '×', ')('],
                    'y': ['`/', '¥', 'j', '\\|/'],
                    'z': ['2', '7_', '~/_', '%']
                }
        
                result = ""
                for char in text.lower():
                    if char in leet_dict and random.random() > 0.3:
                        result += random.choice(leet_dict[char])
                    else:
                        result += char
                return result.upper()
    
            # MEGA CRAZY EFFECTS
            def color_explosion(duration=2):
                """Ultimate color explosion"""
                width = os.get_terminal_size().columns
                height = min(40, os.get_terminal_size().lines)
                start_time = time.time()
        
                while time.time() - start_time < duration:
                    for y in range(1, height):
                        line = ""
                        for x in range(width):
                            # Random character
                            char = random.choice(random.choice(CRAZY_SETS))
                    
                            # Random color
                            if random.random() > 0.5:
                                color = Colors.random_rgb()
                            else:
                                color = random.choice(Colors.COLORS_256)
                    
                            # Random background
                            if random.random() > 0.7:
                                bg = Colors.random_bg_rgb()
                            else:
                                bg = random.choice(Colors.BG_COLORS_256)
                    
                            # Random style
                            style = Colors.random_style()
                    
                            line += bg + style + color + char + Colors.RESET
                
                        print(f"\033[{y};0H{line}")
                    time.sleep(0.1)
    
            def text_frenzy_effect(duration=1.5):
                """Complete text frenzy"""
                width = os.get_terminal_size().columns
                height = min(30, os.get_terminal_size().lines)
                start_time = time.time()
        
                while time.time() - start_time < duration:
                    for y in range(1, height):
                        # Generate random text
                        text = generate_crazy_text(width)
                
                        # Apply effects
                        if random.random() > 0.5:
                            text = Colors.rainbow_text(text, random.randint(1, 5))
                        elif random.random() > 0.3:
                            text = Colors.gradient_text(text, 
                                (random.randint(0,255), random.randint(0,255), random.randint(0,255)),
                                (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
                        else:
                            text = Colors.random_rgb() + Colors.random_style() + text
                
                        print(f"\033[{y};0H{text}{Colors.RESET}")
                    time.sleep(0.08)
    
            def matrix_rainbow(duration=1):
                """Matrix effect with rainbow colors"""
                width = os.get_terminal_size().columns
                height = min(50, os.get_terminal_size().lines)
                drops = [0] * width
                colors = [
                    (255, 0, 0),    # Red
                    (255, 127, 0),  # Orange
                    (255, 255, 0),  # Yellow
                    (0, 255, 0),    # Green
                    (0, 0, 255),    # Blue
                    (75, 0, 130),   # Indigo
                    (143, 0, 255),  # Violet
                ]
        
                start_time = time.time()
                while time.time() - start_time < duration:
                    for i in range(width):
                        if drops[i] == 0:
                            if random.random() < 0.05:
                                drops[i] = 1
                        elif drops[i] < height:
                            char = random.choice(random.choice(CRAZY_SETS))
                            color_index = (drops[i] // 2) % len(colors)
                            r, g, b = colors[color_index]
                            color = Colors.rgb(r, g, b)
                    
                            # Add trail effect
                            for trail in range(max(0, drops[i] - 5), drops[i]):
                                trail_char = random.choice(['░', '▒', '▓'])
                                trail_color = Colors.rgb(r//3, g//3, b//3)
                                print(f"\033[{trail};{i}H{trail_color}{trail_char}{Colors.RESET}")
                    
                            print(f"\033[{drops[i]};{i}H{color}{char}{Colors.RESET}")
                            drops[i] += 1
                        else:
                            drops[i] = 0
                    time.sleep(0.03)
    
            def binary_storm(duration=1):
                """Binary code storm"""
                width = os.get_terminal_size().columns
                height = min(40, os.get_terminal_size().lines)
                start_time = time.time()
        
                while time.time() - start_time < duration:
                    for y in range(1, height):
                        line = ""
                        for x in range(width):
                            if random.random() > 0.5:
                                char = random.choice('01')
                            else:
                                char = random.choice('█▓▒░')
                    
                            # Pulsing color
                            pulse = int((math.sin(time.time() * 10 + x/10 + y/10) + 1) * 127.5)
                            color = Colors.rgb(0, pulse, 0)
                    
                            line += color + char
                        print(f"\033[{y};0H{line}{Colors.RESET}")
                    time.sleep(0.05)
    
            def emoji_avalanche(duration=1):
                """Emoji avalanche effect"""
                width = os.get_terminal_size().columns
                height = min(30, os.get_terminal_size().lines)
                emojis = "🤖👽👾🤯💀☠️👻💩🤡👹👺🎮🕹️💻🖥️🔌🔋💡📱📲⌚⌛⏰🔥💧🌊💨❄️☀️⭐🌟💫✨☄️"
        
                start_time = time.time()
                while time.time() - start_time < duration:
                    for y in range(1, height):
                        line = ""
                        for _ in range(width // 2):  # Emojis take 2 spaces
                            emoji = random.choice(emojis)
                            color = Colors.random_rgb()
                            line += color + emoji
                        print(f"\033[{y};0H{line}{Colors.RESET}")
                    time.sleep(0.1)
    
            def glitch_wave(duration=1.5):
                """Glitching wave effect"""
                width = os.get_terminal_size().columns
                height = min(35, os.get_terminal_size().lines)
                start_time = time.time()
        
                while time.time() - start_time < duration:
                    wave_pos = int((math.sin(time.time() * 5) + 1) / 2 * (height - 1)) + 1
            
                    for y in range(1, height):
                        if abs(y - wave_pos) < 3:
                            # Glitch zone
                            line = generate_crazy_text(width)
                            color = Colors.rgb(255, 0, 255)  # Magenta for glitch
                            style = Colors.REVERSE + Colors.BLINK_FAST
                        else:
                            # Normal zone
                            line = ''.join(random.choice(' ░▒▓') for _ in range(width))
                            intensity = 255 - abs(y - wave_pos) * 50
                            intensity = max(0, min(255, intensity))
                            color = Colors.rgb(0, intensity, 0)
                            style = ""
                
                        print(f"\033[{y};0H{style}{color}{line}{Colors.RESET}")
                    time.sleep(0.06)
    
            def hologram_effect(text, duration=2):
                """Hologram-style text effect"""
                width = os.get_terminal_size().columns
                height = 10
                start_time = time.time()
        
                while time.time() - start_time < duration:
                    for y in range(1, height + 1):
                        offset = int(math.sin(time.time() * 3 + y/3) * 3)
                        line_pos = max(0, min(width - len(text), width//2 - len(text)//2 + offset))
                
                        print(f"\033[{y};{line_pos}H", end='')
                
                        for i, char in enumerate(text):
                            if char != ' ':
                                # Hologram color effect
                                r = int(100 + 155 * abs(math.sin(time.time() + i/5)))
                                g = int(200 + 55 * abs(math.cos(time.time() + i/5)))
                                b = 255
                                color = Colors.rgb(r, g, b)
                        
                                # Hologram transparency effect
                                if random.random() > 0.3:
                                    print(color + char, end='')
                                else:
                                    print(' ', end='')
                            else:
                                print(' ', end='')
            
                    print(Colors.RESET, end='')
                    time.sleep(0.1)
    
            def rotating_cube_effect(duration=2):
                """Simple rotating cube ASCII art"""
                frames = [
                    """
                    +------+
                    |\\     |\\
                    | \\    | \\
                    |  +---+  |
                    |  |   |  |
                    +--|---+  |
                     \\ |     |
                      \\|     |
                       +-----+
                    """,
                    """
                       +-----+
                      /|     /|
                     / |    / |
                    +--|---+  |
                    |  +---+  |
                    | /    | /
                    |/     |/
                    +------+
                    """,
                    """
                    +------+
                    |\\     |\\
                    | \\    | \\
                    |  +------+
                    |  |   |  |
                    |  |   |  |
                    \\  |   |  /
                     \\ |   | /
                      \\|   |/
                       +---+
                    """,
                    "LABUBU"
                ]
        
                start_time = time.time()
                frame = 0
                while time.time() - start_time < duration:
                    print("\033[2J\033[H", end='')  # Clear screen
                    color = Colors.random_rgb()
                    print(color + frames[frame % len(frames)] + Colors.RESET)
                    frame += 1
                    time.sleep(0.2)
    
            def psychedelic_spiral(duration=1.5):
                """Psychedelic spiral effect"""
                width = os.get_terminal_size().columns
                height = min(30, os.get_terminal_size().lines)
                center_x, center_y = width // 2, height // 2
        
                start_time = time.time()
                angle = 0
        
                while time.time() - start_time < duration:
                    print("\033[2J\033[H", end='')
            
                    for i in range(100):
                        r = i * 0.1
                        x = int(center_x + r * math.cos(angle + i * 0.1))
                        y = int(center_y + r * math.sin(angle + i * 0.1))
                
                        if 0 <= x < width and 0 <= y < height:
                            color = Colors.rgb(
                                int(127 + 127 * math.sin(angle + i * 0.3)),
                                int(127 + 127 * math.sin(angle + i * 0.5)),
                                int(127 + 127 * math.sin(angle + i * 0.7))
                            )
                            char = random.choice(['*', '·', '•', '◦', '○', '⦿'])
                            print(f"\033[{y};{x}H{color}{char}{Colors.RESET}")
            
                    angle += 0.2
                    time.sleep(0.05)
    
            # MAIN ULTIMATE CHAOS LOOP
            os.system('cls' if os.name == 'nt' else 'clear')
    
            # CRAZY OPENING
            print("\033[2J\033[H")  # Clear screen
            time.sleep(0.5)
    
            # Hologram title
            for i in range(3):
                hologram_effect("ULTIMATE CHAOS HACKING MEGA", 0.5)
    
            print("\033[2J\033[H")
    
            # Rainbow title
            title = "✦ ULTIMATE CHAOS HACKING MEGA PROTOCOL ✦"
            print("\n" + Colors.rainbow_text(title.center(80)))
    
            # Animated border
            for i in range(5):
                border_chars = ['█', '▓', '▒', '░', '▄', '▀']
                border = random.choice(border_chars) * 80
                color = Colors.random_rgb()
                print(color + border + Colors.RESET)
                time.sleep(0.1)
    
            print(f"\n{Colors.GRAY}Reality Stability: {random.randint(1, 100)}%")
            print(f"Quantum Entropy: {chaos.quantum_entropy:.4f}")
            print(f"Color Mania: {chaos.color_mania:.2f}")
            print(f"Text Frenzy: {chaos.text_frenzy:.2f}")
            print(f"Meme Density: {chaos.meme_density}")
            print(f"System Time: {datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3]}")
            print(f"Universe ID: 0x{''.join(random.choice('0123456789ABCDEF') for _ in range(16))}")
            print(f"Sponsored by: {random.choice(['SKYNET AI', 'ACME CORP', 'UMBRELLA BIO', 'TYRELL NEXUS', 'WYLAN-YUTANI', 'CYBERDYNE SYSTEMS', 'STARK INDUSTRIES', 'WAYNE ENTERPRISES'])}")
    
            border = "≋" * 80
            print(f"{Colors.BRIGHT_CYAN}{border}{Colors.RESET}")
    
            time.sleep(2)
    
            # Initial crazy effects
            effects = [color_explosion, text_frenzy_effect, matrix_rainbow, 
                       binary_storm, emoji_avalanche, glitch_wave]
            random.shuffle(effects)
    
            for effect in effects[:random.randint(2, 4)]:
                print(f"\n{Colors.BLINK_SLOW}{Colors.BRIGHT_YELLOW}INITIALIZING {effect.__name__.upper()}...{Colors.RESET}")
                effect(random.uniform(0.5, 1.5))
    
            # Main chaos loop
            iteration = 0
            try:
                while True:
                    iteration += 1
                    chaos.increase_chaos()
            
                    # Randomly trigger mega effects
                    if chaos.should_color_explosion():
                        print(f"\n{Colors.BLINK_FAST}{Colors.BRIGHT_MAGENTA}!!! COLOR MANIA !!!{Colors.RESET}")
                        color_explosion(random.uniform(0.5, 2))
                        chaos.color_mania = 0
            
                    if chaos.should_text_frenzy():
                        print(f"\n{Colors.BLINK_FAST}{Colors.BRIGHT_CYAN}!!! TEXT FRENZY !!!{Colors.RESET}")
                        text_frenzy_effect(random.uniform(0.5, 2))
                        chaos.text_frenzy = 0
            
                    if chaos.should_break_reality():
                        print(f"\n{Colors.BG_RED}{Colors.BRIGHT_WHITE}{Colors.BLINK_FAST}{'☢' * 40}")
                        print("REALITY FRACTURE DETECTED".center(40))
                        print(f"{'☢' * 40}{Colors.RESET}")
                
                        # Multiple effects at once
                        for _ in range(random.randint(2, 4)):
                            random.choice([color_explosion, text_frenzy_effect, 
                                          matrix_rainbow, binary_storm])(random.uniform(0.3, 1))
                
                        chaos.reality_glitch_level = 0
                        print(f"{Colors.BRIGHT_GREEN}REALITY STABILIZED... FOR NOW{Colors.RESET}")
            
                    # Regular random effects
                    effect_choice = random.randint(1, 15)
            
                    if effect_choice == 1:
                        color_explosion(random.uniform(0.3, 1))
                    elif effect_choice == 2:
                        text_frenzy_effect(random.uniform(0.3, 1))
                    elif effect_choice == 3:
                        matrix_rainbow(random.uniform(0.5, 1.5))
                    elif effect_choice == 4:
                        binary_storm(random.uniform(0.3, 1))
                    elif effect_choice == 5:
                        emoji_avalanche(random.uniform(0.3, 1))
                    elif effect_choice == 6:
                        glitch_wave(random.uniform(0.5, 1.5))
                    elif effect_choice == 7:
                        rotating_cube_effect(random.uniform(0.5, 1))
                    elif effect_choice == 8:
                        psychedelic_spiral(random.uniform(0.5, 1))
                    elif effect_choice == 9:
                        # Hologram message
                        messages = [
                            "ACCESS GRANTED",
                            "SYSTEM BREACHED",
                            "DATA FLOWING",
                            "QUANTUM DECODING",
                            "MATRIX GLITCHING",
                            "REALITY HACKED",
                            "UNIVERSE PWNED",
                            "DZUGUTIK",
                            "TIGLOLIGRORUITONI",
                        ]
                        hologram_effect(random.choice(messages), random.uniform(1, 2))
                    elif 10 <= effect_choice <= 13:
                        # Crazy text display
                        lines = random.randint(1, 10)
                        for _ in range(lines):
                            text = generate_crazy_text(random.randint(20, 80))
                    
                            # Apply random text effect
                            if random.random() > 0.7:
                                text = generate_leet_speak(text)
                    
                            # Apply random color effect
                            if random.random() > 0.5:
                                text = Colors.rainbow_text(text, random.randint(1, 5))
                            elif random.random() > 0.3:
                                start = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
                                end = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
                                text = Colors.gradient_text(text, start, end)
                            else:
                                text = Colors.random_rgb() + Colors.random_style() + text
                    
                            print(text + Colors.RESET)
                            time.sleep(random.uniform(0.01, 0.1))
                    else:
                        # Normal operation with extreme styling
                        op = generate_crazy_text(random.randint(10, 30))
                        sys = generate_crazy_text(random.randint(10, 20))
                
                        # Crazy formatting
                        border = random.choice(['═', '─', '━', '═', '║', '│', '┃', '╔', '╗', '╚', '╝'])
                        header = f" ITERATION {iteration:06X} "
                        print(f"\n{Colors.BRIGHT_CYAN}{border * 5}{header}{border * (70 - len(header))}{Colors.RESET}")
                
                        color1 = Colors.random_rgb()
                        color2 = Colors.random_rgb()
                        style = Colors.random_style()
                
                        print(f"{color1}{style}[{op}]")
                        print(f"{color2}  Target: {sys}")
                        print(f"  Status: {random.choice(['🌀', '⚡', '🌪️', '🔥', '💫', '✨'])} {random.choice(['GLITCHING', 'WARPING', 'VIBRATING', 'PULSING', 'FLICKERING'])}")
                        print(f"  Data: {generate_crazy_text(15)}")
                        print(f"  Size: {random.randint(1, 999)}.{random.randint(0, 999)} {random.choice(['ZB', 'YB', 'BB', '∞B'])}{Colors.RESET}")
                
                        time.sleep(random.uniform(0.05, 0.2))
            
                    # System info with crazy styling
                    if random.random() > 0.9:
                        print(f"\n{Colors.GRAY}{'▁' * 80}")
                        info_lines = [
                            f"ITERATION: {Colors.BRIGHT_YELLOW}{iteration}{Colors.GRAY}",
                            f"CHAOS: {Colors.BRIGHT_RED}{chaos.reality_glitch_level:.2f}{Colors.GRAY}",
                            f"COLORS: {Colors.BRIGHT_MAGENTA}{chaos.color_mania:.2f}{Colors.GRAY}",
                            f"TEXT: {Colors.BRIGHT_CYAN}{chaos.text_frenzy:.2f}{Colors.GRAY}",
                            f"CPU: {Colors.BRIGHT_GREEN}{random.randint(100, 9999)}%{Colors.GRAY}",
                            f"RAM: {Colors.BRIGHT_BLUE}{random.choice(['∞', 'YES', 'ALL', 'TOO MUCH', 'OVER 9000'])}{Colors.GRAY}",
                            f"TEMP: {Colors.BRIGHT_RED}{random.choice(['HOT', 'COLD', 'BOTH', 'NEITHER', 'ABSOLUTE ZERO', 'SUN CORE'])}{Colors.GRAY}",
                            f"INTERNET: {Colors.BRIGHT_CYAN}{random.choice(['FAST', 'SLOW', '404', 'BUFFERING', 'ETERNAL'])}{Colors.GRAY}",
                            f"REALITY: {Colors.BRIGHT_MAGENTA}{random.choice(['STABLE', 'WIBBLY', 'GLITCHY', 'SIMULATED', 'REAL?'])}{Colors.GRAY}",
                            f"COFFEE: {Colors.BRIGHT_YELLOW}{random.randint(0, 99)} cups{Colors.GRAY}",
                            f"SANITY: {Colors.BRIGHT_RED}{max(0, 100 - iteration // 10)}%{Colors.GRAY}",
                            f"MEMES: {Colors.BRIGHT_GREEN}{chaos.meme_density}{Colors.GRAY}",
                        ]
                        for line in info_lines:
                            print(f"  {line}")
                        print(f"{'▔' * 80}{Colors.RESET}")
            
                    time.sleep(random.uniform(0.01, 0.2))
            
                    # Mega summary every 25 iterations
                    if iteration % 25 == 0:
                        print(f"\n{Colors.BG_BLUE}{Colors.BRIGHT_WHITE}{'✧' * 40}")
                        print(f" MEGA CHAOS REPORT #{iteration // 25} ".center(40, '✧'))
                        print(f"{'✧' * 40}{Colors.RESET}")
                
                        stats = [
                            ("Realities Hacked", f"{random.randint(42, 42000)}"),
                            ("Time Loops", f"{random.randint(13, 1313)}"),
                            ("Physics Laws Broken", f"{random.randint(7, 77)}"),
                            ("AI Became Self-Aware", f"{random.randint(0, 3)}"),
                            ("Coffee Spilled", f"{random.randint(0, 5)} cups"),
                            ("Keyboards Smashed", f"{random.randint(3, 33)}"),
                            ("Existential Crises", f"{random.randint(0, 1)}"),
                            ("Dank Memes Generated", f"{chaos.meme_density}"),
                            ("Sanity Lost", f"{random.randint(0, 100)}%"),
                            ("Coolness Gained", f"{random.randint(9000, 99999)}%"),
                            ("Parallel Universes", f"{random.randint(1, 42)}"),
                            ("Infinite Loops Escaped", f"{random.randint(1, 10)}"),
                            ("Magic Performed", f"{random.randint(0, 100)}%"),
                            ("Matrix Glitches Found", f"{random.randint(0, 100)}"),
                            ("H4x0r Points", f"{random.randint(1000, 99999)}"),
                            ("Epicness Level", f"{random.randint(1, 11)}/10"),
                        ]
                
                        for stat, value in stats:
                            color = Colors.random_rgb()
                            print(f"  {color}{stat:30} {Colors.BRIGHT_YELLOW}{value}{Colors.RESET}")
                
                        print()
    
            except KeyboardInterrupt:
                print(f"\n\n{Colors.BG_YELLOW}{Colors.BLACK}{Colors.BLINK_SLOW}{'⚠' * 40}")
                print(" USER TERMINATED CHAOS PROTOCOL ".center(40, '⚠'))
                print(f"{'⚠' * 40}{Colors.RESET}")
                time.sleep(1)
    
            # ULTIMATE FINAL SEQUENCE
            print("\033[2J\033[H")  # Clear screen
    
            # Final mega effects
            print(f"{Colors.BLINK_FAST}{Colors.BRIGHT_RED}INITIATING FINAL CHAOS SEQUENCE...{Colors.RESET}")
            time.sleep(1)
    
            for effect in [color_explosion, text_frenzy_effect, matrix_rainbow, 
                           binary_storm, emoji_avalanche, glitch_wave]:
                effect(0.8)
                time.sleep(0.2)
    
            # Final hologram
            hologram_effect("CHAOS SIMULATION COMPLETE", 2)
    
            print("\033[2J\033[H")
    
            # Final crazy display
            print(f"\n{Colors.BG_BLACK}{Colors.BRIGHT_WHITE}{'✦' * 80}")
            print(" ULTIMATE CHAOS HACKING SIMULATION COMPLETE ".center(80, '✦'))
            print(f"{'✦' * 80}{Colors.RESET}")
    
            print(f"\n{Colors.BRIGHT_GREEN}{Colors.BOLD}FINAL MEGA STATISTICS:{Colors.RESET}")
    
            mega_stats = [
                ("Total Realities Hacked", f"{random.randint(666, 99999)}"),
                ("Time Paradoxes Created", f"{random.randint(42, 4200)}"),
                ("Laws of Physics Broken", f"{random.randint(77, 777)}"),
                ("AI That Questioned Existence", f"{random.randint(3, 33)}"),
                ("Coffee Cups Consumed", f"{random.randint(42, 420)}"),
                ("Keyboards Destroyed", f"{random.randint(7, 77)}"),
                ("Existential Crises Triggered", f"{random.randint(0, 2)}"),
                ("Dank Memes Generated", f"{chaos.meme_density * 10}"),
                ("Sanity Lost Forever", f"{random.randint(50, 150)}%"),
                ("Coolness Achieved", f"{random.randint(90000, 999999)}%"),
                ("Parallel Universes Visited", f"{random.randint(42, 420)}"),
                ("Infinite Loops Escaped", f"{random.randint(13, 131)}"),
                ("Magic Spells Cast", f"{random.randint(0, 1000)}"),
                ("Matrix Glitches Documented", f"{random.randint(100, 1000)}"),
                ("H4x0r Points Earned", f"{random.randint(100000, 999999)}"),
                ("Epicness Rating", f"{random.randint(10, 11)}/10"),
                ("Awesomeness Level", "OVER 9000"),
                ("Chaos Coefficient", f"{chaos.reality_glitch_level:.6f}"),
                ("Quantum Weirdness", f"{chaos.quantum_entropy:.6f}"),
                ("Color Mania Final", f"{chaos.color_mania:.6f}"),
                ("Text Frenzy Final", f"{chaos.text_frenzy:.6f}"),
                ("Total Iterations", f"{iteration}"),
                ("Time Spent Hacking", f"{iteration * 0.1:.1f} seconds"),
                ("Reality Bytes Modified", f"0x{''.join(random.choice('0123456789ABCDEF') for _ in range(32))}"),
                ("Universal Constants Changed", f"{random.randint(1, 10)}"),
                ("Alien Civilizations Confused", f"{random.randint(3, 33)}"),
                ("Time Travel Attempts", f"{random.randint(0, 13)}"),
                ("Wormholes Created", f"{random.randint(0, 7)}"),
                ("Black Holes Avoided", f"{random.randint(1, 42)}"),
                ("Supernovas Witnessed", f"{random.randint(0, 3)}"),
            ]
    
            for i, (stat, value) in enumerate(mega_stats):
                # Rainbow effect for stats
                if i % 3 == 0:
                    color = Colors.rgb(255, 0, 0)
                elif i % 3 == 1:
                    color = Colors.rgb(0, 255, 0)
                else:
                    color = Colors.rgb(0, 0, 255)
        
                dots = '∙' * (40 - len(stat))
                print(f"  {color}{stat}{dots} {Colors.BRIGHT_YELLOW}{value}{Colors.RESET}")
                time.sleep(0.05)
    
            print(f"\n{Colors.BRIGHT_MAGENTA}{Colors.BOLD}FINAL MESSAGE FROM THE MATRIX:{Colors.RESET}")
            final_messages = [
                "THE CAKE IS A LIE, BUT THE HACKING IS REAL. SORT OF.",
                "ALL YOUR BASE ARE BELONG TO US. JUST PRETENDING.",
                "HASTA LA VISTA, BABY. SEE YOU IN THE NEXT SIMULATION.",
                "RESISTANCE IS FUTILE. BUT PRETEND HACKING IS FUN.",
                "THE MATRIX HAS YOU. BUT YOU CAN PRETEND TO HACK IT.",
                "I'LL BE BACK. WITH MORE PRETEND HACKING.",
                "MAY THE FORCE BE WITH YOU. AND YOUR PRETEND HACKING SKILLS.",
                "LIVE LONG AND PROSPER. AND KEEP PRETEND HACKING.",
                "THIS IS THE WAY. THE WAY OF PRETEND HACKING.",
                "WINTER IS COMING. SO IS MORE PRETEND HACKING.",
                "YOU SHALL NOT PASS! JUST KIDDING, HACK AWAY.",
                "TO INFINITY AND BEYOND! WITH PRETEND HACKING.",
                "THE ANSWER IS 42. THE QUESTION WAS ABOUT PRETEND HACKING.",
                "BE EXCELLENT TO EACH OTHER. AND KEEP PRETEND HACKING.",
                "THE DARK SIDE HAS COOKIES. BUT WE HAVE PRETEND HACKING.",
                "FOURTEAM SAYS HI. BUT HACKED YOU."
            ]
    
            selected = random.choice(final_messages)
            for i in range(0, len(selected), 40):
                part = selected[i:i+40]
                print(f"  {Colors.ITALIC}{Colors.BRIGHT_CYAN}\"{part}\"{Colors.RESET}")
                time.sleep(0.1)
    
            print(f"\n{Colors.GRAY}Session Duration: {iteration * 0.1:.1f} simulated seconds")
            print(f"Reality Version: {random.random():.16f}")
            print(f"Chaos Achieved: Maximum")
            print(f"Thank you for pretending to hack reality at maximum chaos!{Colors.RESET}")
    
            print(f"\n{Colors.BG_RED}{Colors.BRIGHT_WHITE}{Colors.BLINK_FAST}{'☢' * 40}")
            print(" ULTIMATE FINAL WARNING ".center(40, '☢'))
            print(" This was 110% fake entertainment ".center(40))
            print(" Real hacking = illegal ".center(40))
            print(" Pretend hacking = hilarious ".center(40))
            print(f"{'☢' * 40}{Colors.RESET}")
    
            # One final effect
            time.sleep(1)
            for _ in range(3):
                print(f"\r{Colors.BLINK_FAST}{Colors.random_rgb()}{random.choice(['POOF!', 'KABOOM!', 'ZAP!', 'POW!', 'BOOM!', 'BAM!'])}{Colors.RESET}", end='')
                time.sleep(0.3)
            print("\n")

        def matrix_rain(stdscr, speed=50, density=10, color_mode='classic'):
            """
            Generate a Matrix digital rain effect in the terminal.
    
            Parameters:
            - stdscr: curses window object
            - speed: falling speed (1-100, higher is faster)
            - density: character density (1-100, higher is denser)
            - color_mode: 'green', 'classic', or 'rgb'
            """
            # Initialize curses
            curses.curs_set(0)  # Hide cursor
            stdscr.nodelay(1)   # Non-blocking input
    
            # Get terminal dimensions
            height, width = stdscr.getmaxyx()
    
            # Initialize color pairs
            curses.start_color()
            curses.use_default_colors()
    
            # Define color modes
            if color_mode == 'green':
                # Classic green-on-black Matrix style
                curses.init_pair(1, curses.COLOR_GREEN, -1)
                curses.init_pair(2, curses.COLOR_WHITE, -1)
                color_fg = curses.color_pair(1)
                color_bright = curses.color_pair(2)
            elif color_mode == 'classic':
                # Black and white style
                curses.init_pair(1, curses.COLOR_WHITE, -1)
                color_fg = curses.color_pair(1)
                color_bright = curses.color_pair(1)
            else:  # rgb mode
                # Colorful style
                curses.init_pair(1, curses.COLOR_GREEN, -1)
                curses.init_pair(2, curses.COLOR_CYAN, -1)
                curses.init_pair(3, curses.COLOR_WHITE, -1)
                color_fg = curses.color_pair(1)
                color_bright = curses.color_pair(2)
    
            # Matrix characters (includes Latin, Greek, and Katakana)
            matrix_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789$#@%&*+=-_"
            katakana = "ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜｦﾝ"
            full_chars = matrix_chars + katakana
    
            # Data structures to track raindrops
            # Each drop is [column, head_position, length, speed_counter, char_list]
            drops = []
    
            # Track the last time a drop was added to each column
            last_drop_time = {}
    
            # Convert speed to delay (1-100 to 0.01-0.2 seconds)
            # Lower speed number = slower falling
            base_delay = 0.05
            speed_factor = (101 - speed) / 100  # Invert so higher speed = faster
            delay = base_delay * speed_factor
    
            # Convert density to probability (1-100 to 0.01-0.5)
            density_probability = density / 200
    
            frame = 0
            running = True
    
            # Display instructions
            try:
                stdscr.addstr(0, 0, "MATRIX RAIN - Press 'q' to quit, 'r' to reset, 'c' to change color", curses.A_BOLD)
            except:
                pass
    
            while running:
                frame += 1
        
                # Check for user input
                try:
                    key = stdscr.getch()
                    if key == ord('q'):
                        running = False
                        break
                    elif key == ord('r'):
                        # Reset drops
                        drops = []
                        last_drop_time.clear()
                    elif key == ord('c'):
                        # Cycle color modes
                        if color_mode == 'green':
                            color_mode = 'classic'
                        elif color_mode == 'classic':
                            color_mode = 'rgb'
                        else:
                            color_mode = 'green'
                        return matrix_rain(stdscr, speed, density, color_mode)
                except:
                    pass
        
                # Clear screen
                stdscr.erase()
        
                # Display info at top
                info = f"Speed: {speed} (1-100) | Density: {density} (1-100) | Color: {color_mode} | Drops: {len(drops)}"
                if len(info) < width - 2:
                    try:
                        stdscr.addstr(0, 0, info, curses.A_BOLD)
                    except:
                        pass
        
                # Potentially add new drops
                for col in range(width):
                    # Skip if column already has a recent drop
                    if col in last_drop_time and frame - last_drop_time[col] < 10:
                        continue
            
                    # Add new drop with probability based on density
                    if random.random() < density_probability:
                        # Random drop length between 3 and min(15, height-2)
                        length = random.randint(3, min(15, height-2))
                        # Create character list for this drop
                        char_list = [random.choice(full_chars) for _ in range(length)]
                        drops.append([col, -length, length, 0, char_list])
                        last_drop_time[col] = frame
        
                # Update and draw drops
                new_drops = []
                for drop in drops:
                    col, head_pos, length, speed_counter, char_list = drop
            
                    # Move drop based on speed
                    speed_counter += 1
                    move_threshold = max(1, int(5 - speed / 20))  # Higher speed = lower threshold = faster movement
                    if speed_counter >= move_threshold:
                        head_pos += 1
                        speed_counter = 0
            
                    # Remove drop if it's completely off screen
                    if head_pos - length > height:
                        continue
            
                    # Draw the drop
                    for i in range(length):
                        pos = head_pos - i
                        if 0 <= pos < height and 0 <= col < width:
                            # Choose character
                            if i == 0:  # Head of the drop
                                char = random.choice(full_chars)
                                char_list[0] = char  # Update head character
                                attr = curses.A_BOLD
                            else:
                                char = char_list[i]
                                attr = 0
                    
                            # Apply color based on mode and position
                            if color_mode == 'rgb':
                                # Color changes based on position
                                if i == 0:
                                    color = curses.color_pair(3) | curses.A_BOLD  # Bright white head
                                elif i < length // 3:
                                    color = curses.color_pair(2)  # Cyan for upper part
                                else:
                                    color = curses.color_pair(1)  # Green for tail
                            else:
                                # Classic or green mode
                                if i == 0:
                                    color = color_bright | curses.A_BOLD
                                elif i < length // 2:
                                    color = color_bright
                                else:
                                    color = color_fg
                    
                            # Draw character
                            try:
                                stdscr.addstr(pos, col, char, color | attr)
                            except curses.error:
                                pass  # Ignore drawing errors at screen edges
            
                    # Keep drop for next frame
                    new_drops.append([col, head_pos, length, speed_counter, char_list])
        
                drops = new_drops
        
                # Add some random single characters for more "noise"
                noise_count = int(width * height * density / 5000)
                for _ in range(noise_count):
                    col = random.randint(0, width-1)
                    row = random.randint(0, height-1)
                    char = random.choice(matrix_chars)
                    try:
                        stdscr.addstr(row, col, char, color_fg)
                    except curses.error:
                        pass
        
                # Refresh screen
                stdscr.refresh()
        
                # Control speed with time delay (this is the key fix!)
                time.sleep(delay)
    
            # Return to normal terminal state
            curses.endwin()

        def is_admin():
            try:
                return ctypes.windll.shell32.IsUserAnAdmin()
            except:
                return False

        def admin(command):
            import ctypes
    
            # For command-line commands
            if command.startswith('cmd '):
                full_command = command
            else:
                full_command = f'cmd /c "{command}"'
    
            # Run as admin
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", "cmd.exe", f'/c {full_command}', None, 1
            )

        def global_color(color_code):
            sys.stdout.write(color_code)
            sys.stdout.flush()

        f = open(cwd+"/set/stroot.4set","r")
        stroot = f.read()
        f.close()

        parser = argparse.ArgumentParser(description="bOS cmd client")
        parser.add_argument("--path", default=cwd, help="Path where bOS will start")
        parser.add_argument("--com", default="nothing", type=str, help='Startup commands. To turn on type in bOS this "set stcom true"')
        parser.add_argument("--print", default="", type=str, help='Prints your text on start')
        parser.add_argument("--root", default=stroot, type=str, help="Root changer. If False you can't update, reinstall or use ubuild. Also can't change any system files")
        args = parser.parse_args()

        if stroot != args.root and args.root == "true":
            inp = input("Root password: ")
            f = open(cwd+"/set/passw.4set")
            if decrypt_message(f.read(),inp) == "Just a message to decrypt in bOS. Hello from fourteam!":
                root = "true"
            else:
                print("Incorrect. Root denied")
                root = "false"

        else:
            root = args.root

        os.chdir(args.path)
        cwd = args.path
        print(args.print)

        time.sleep(2)
        clear_screen()

        def add_file(zip_path, file_to_add, arcname=None):
            if arcname is None:
                arcname = os.path.basename(file_to_add)
            with zipfile.ZipFile(zip_path, 'a') as zipf:
                zipf.write(file_to_add, arcname)
        def typewrite(text, delay=0.05):
            for char in text:
                print(char, end='', flush=True)
                time.sleep(delay)
            print()
        version = []
        string = 0
        url = "http://fourteam4t.temp.swtest.ru/"
        #url = "http://bosstageserver.com.swtest.ru/"
        f = open(cwd+"/modules.4set","r")
        modules = f.read()
        nothing = ""
        modules = modules.split(",")
        if nothing in modules:
            removing = True
            while removing == True:
                modules.remove(nothing)
                if not nothing in modules:
                    removing = False
        y = 0
        for i in modules:
            __import__("apps."+modules[y])
            y = y + 1
        typewrite("\033[92;1mWelcome!\033[0m")
        time.sleep(1)


        def install():
            try:
                print("Loading...")
                response3 = requests.get(url+"emmute.txt")
                if response3.text.lower() == "true":
                    print("Maintenance emmute in progress. Try this action later")
                    return "maintenance"
                else:
                    response5 = requests.get(url+"commands.txt")
                    commands = response5.text.split(",")
                    x = 90.0 / float(len(commands))
                    print("Patching commands...")
                    y = 0
                    percent = 0.0
                    for i in range(len(commands)):
                        response6 = requests.get(url+commands[y])
                        comtext = response6.text
                        os.chdir("Commands")
                        f = open(commands[y]+".4com","a")
                        f.close()
                        f = open(commands[y]+".4com","w")
                        f.write(comtext)
                        f.close()
                        y = y+1
                        percent = percent + x
                        print(str(percent)+"%",end="\r")
                        os.chdir("..")
                    y = 1
                    f = open("commands.4t","a")
                    f.close()
                    f = open("commands.4t","w")
                    f.write(commands[0])
                    f.close()
                    for i in range(len(commands)-1):
                        f = open("commands.4t","a")
                        f.write(","+commands[y])
                        f.close()
                        y = y+1
                    time.sleep(2)
                    print("95.0%",end="\r")
                    response7 = requests.get(url+"lastversion.txt")
                    f = open("ver.4t","a")
                    f.close()
                    f = open("ver.4t","w")
                    f.write(response7.text)
                    f.close()
                    print("100.0%",end="\r")
                    return "successful"




            except:
                print("Something went wrong. Check your internet connection")
                return "error"

        f = open("back","r")
        while f.read() == "":
            print("Welcome to bOS! Wait before bOS install")
            status = install()
            if status == "successful":
                print("bOS successfully installed")
                f2 = open("back","w")
                f2.write("true")
                f2.close()
            if status == "error":
                print("There was error in install")
                input("Tap ENTER to try again")
            if status == "maintenance":
                print("Maintenance emmute will ends soon. Come back later")
                input("Tap ENTER to try again")
        f.close()


        try:
            print("Connecting to server...",end = "\r")
            response = requests.get(url+"lastversion.txt")
            response4 = requests.get(url+"emmute.txt")
            response5 = requests.get(url+"startup.txt")
            response7 = requests.get(url+"lastavver.txt")
            if response4.text.lower() == "true":
                print("Maintenance emmute in progress. No info for updates")
            else:
                update = False
                lastver = response.text.split(".")
                lastavver = response.text.split(".")
                with open("ver.4t","r") as f:
                    version = f.read().split(".")
                if int(lastver[0]) > int(version[0]) or int(lastver[1]) > int(version[1]):
                    f = open(cwd+"/set/uwarn.4set","r")
                    if f.read() == "true":
                        print('New version is available! You can update by command "update"')
                        update = True
                        f.close()
                startup = response5.text.split(",")
                y = 0
                for i in startup:
                    response6 = requests.get(url+startup[y])
                    exec(response6.text)
                    y = y+1
                if update == False:
                    print("\033[92;1mSuccessfully connected to server\033[0m")
        except:
            plyer.notification.notify(message="bOS Enter System notification:\nCheck your internet connection. Application may have updates",app_name="bOS Enter system",title = "Connection failed")
            print("\033[91;1mError while connecting to server\033[0m")



        def command(command):
            global root
            com = command.split(" ")
            com[0] = com[0].lower()
            f = open(cwd+"/commands.4t","r")
            commands = f.read().split(",")
            f.close()
            if com[0] in commands:
                f = open(cwd+"/Commands/"+com[0]+".4com","r")
        
                try:
                    try:
                        try:
                            exec(f.read())
                        except IndexError:
                            print('CommandError 001: "NO NEEDEN ARGUMENT"\n(command help for help)')
                    except:
                        print("Canceled")
                except:
                    print('SystemError 001: "COMMAND GOT CRASHED"\n(command help for help)')
                    f.close()
            elif com[0] == "update" or com[0] == "reinstall" or com[0] == "restart" or com[0] == "server" or com[0] == "install" or com[0] == "ubuild" or com[0] == "set" or com[0] == "admin" or com[0] == "root" or com[0] == "beditor" or com[0] == "color" or com[0] == "cmatrix" or com[0] == "hacking" or com[0] == "neofatch" or com[0] == "run":
                if com[0] == "update":
                    if root == "true":
                        f = open(cwd+"/ver.4t","r")
                        inp = input("Sure you want to update to last version? After update you wont be able to install earlier version.(Y/n)").lower()
                        if inp == "y":
                            print("Update started")
                            try:
                                st = datetime.datetime.now()
                                status = install()
                                et = datetime.datetime.now()
                                if status == "successful":
                                    print(f"Start time:{st}\nEnd time:{et}")
                                    print("Updated successfully")
                                    print("Restarting in 5 seconds...")
                                    time.sleep(5)
                                    print("Restarting...")
                                    os.system("python bOS.py")
                                if status == "error":
                                    print("Error in update. Try again")
                                if status == "maintenance":
                                    print("Maintenance will ends soon. Try again later")
                            except:
                                print("No internet connection")
                    else:
                        print("Root required")
                elif com[0] == "reinstall":
                    if root == "true":
                        inp = input("Sure you want to reinstall your OS? After reinstall you will update to last version and wont be able to install earlier version.(Y/n)").lower()
                        if inp == "y":
                            print("Reinstall started")
                            st = datetime.datetime.now()
                            status = install()
                            et = datetime.datetime.now()
                            if status == "successful":
                                print(f"Start time:{st}\nEnd time:{et}")
                                print("Reinstalled successfully")
                                print("Restarting in 5 seconds...")
                                time.sleep(5)
                                print("Restarting...")
                                os.system("python bOS.py")
                            if status == "error":
                                print("Error in reinstall. Try again")
                            if status == "maintenance":
                                print("Maintenance will ends soon. Try again later")
                    else:
                        print("Root required")
                elif com[0] == "restart":
                    def re2():
                        os.chdir(cwd)
                        if "-root" in com:
                            os.system("python bOS.py --root false")
                        elif "+root" in com:
                            os.system("python bOS.py --root true")
                        else:
                            os.system("python bOS.py")
                    try:
                        if com[1] == "-t":
                            print(f"Restarting in {com[1]} seconds...")
                            try:
                                time.sleep(int(com[2]))
                            except():
                                time.sleep(2)
                            re2()
                    except:
                        print("Restarting in 2 seconds...")
                        time.sleep(2)
                        re2()
                elif com[0] == "install":
                    print("Don't close your bOS while proccesing!")
                    time.sleep(2)
                    print("Installing...")
                    f = open(cwd+f"/{com[1]}/displayname.4set","r")
                    name = f.read().strip("\n")
                    print("Setting up...")
                    f.close()
                    f = open(cwd+"/"+com[1]+"/setup.bscript","r")
                    exec(f.read())
                    print("Finishing...")
                    text = open(cwd+"/"+com[1]+"/"+name+".bapp","r",encoding="utf-8").read()
                    open(cwd+"/apps/"+name+".py","a").close()
                    open(cwd+"/apps/"+name+".py","w",encoding="utf-8").write(text)
                    f = open(cwd+"/modules.4set","a")
                    f.write(","+name)
                elif com[0] == "ubuild":
                    if root == "true":
                        ans = input("Sure you want to update your build to newest version? After update you will be atomaticly updated to newest version and wont be able to install latest version, but you be able to install later build(Y/n)")
                        if ans.lower() == "y":
                            def ubuild1():
                                exit()
                            def ubuild2():
                                os.system(f"python {cwd}/ubuild.py --code fourteam-bos-utilits-update-ubuild-code")
                            Thread(target=ubuild1).start()
                            Thread(target=ubuild2).start()
                    else:
                        print("Root required")
                elif com[0] == "set":
                    if com[1] == "uwarn":
                        f = open(cwd+"/set/uwarn.4set","w")
                        if com[2] == "true":
                            f.write("true")
                        elif com[2] == "false":
                            f.write("false")
                    elif com[1] == "serv":
                        f = open(cwd+"/set/serv.4set","w")
                    elif com[1] == "stcom":
                        if root == "true":
                            f = open(cwd+"/set/stcom.4set","w")
                            if com[2] == "true":
                                f.write("true")
                            elif com[2] == "false":
                                f.write("false")
                        else:
                            print("Root required")
                    elif com[1] == "rootpassw":
                        if root == "true":
                            inp = input("Confirm password: ")
                            if inp == com[2]:
                                if input("Sure you want to change root password?(y/n)") == "y":
                                    f = open(cwd+"/set/passw.4set","w")
                                    f.write(encrypt_message("Just a message to decrypt in bOS. Hello from fourteam!",com[2]))
                                    f.close()
                                    print("Changed")
                            else:
                                print("Incorrect")
                        else:
                            print("Root required")
                    elif com[1] == "stroot":
                        if root == "true":
                            f = open(cwd+"/set/stroot.4set","w")
                            if com[2] == "true":
                                f.write("true")
                            elif com[2] == "false":
                                f.write("false")
                        else:
                            print("Root required")
                elif com[0] == "admin":
                    if is_admin():
                        print("Already admin")
                    else:
                        print("Running as admin in another window")
                        admin(f"python {cwd}/bOS.py --path {cwd}")
                elif com[0] == "beditor":
                    try:
                        os.system(f"python {cwd}/beditor.py {com[1]}")
                    except IndexError:
                        os.system(f"python {cwd}/beditor.py")
                elif com[0] == "root":
                    try:
                        if com[1] == "-root":
                            print("Unrooted")
                            root = "false"
                        elif com[1] == "-check":
                            if root == "true":
                                print("Rooted")
                            else:
                                print("Unrooted")
                    except IndexError:
                        if root == "true":
                            print("Already rooted")
                        else:
                            inp = input("Root password: ")
                            f = open(cwd+"/set/passw.4set","r")
                            if decrypt_message(f.read(),inp) == "Just a message to decrypt in bOS. Hello from fourteam!":
                                print("Now you rooted!")
                                root = "true"
                            else:
                                print("Wrong!")
                            f.close()
                elif com[0] == 'color':
                    os.system(f"color {com[1]}")
                elif com[0] == "cmatrix":
                    try:
                        if com[1] == "green":
                            curses.wrapper(lambda stdscr: matrix_rain(stdscr, speed=30, density=15, color_mode='green'))
                        elif com[1] == "classic":
                            curses.wrapper(lambda stdscr: matrix_rain(stdscr, speed=30, density=15, color_mode='classic'))
                        elif com[1] == "rgb":
                            curses.wrapper(lambda stdscr: matrix_rain(stdscr, speed=30, density=15, color_mode='rgb'))
                        else:
                            print("Unknown")
                    except IndexError:
                        curses.wrapper(lambda stdscr: matrix_rain(stdscr, speed=30, density=15, color_mode='green'))
                elif com[0] == "hacking":
                    show_hacking_simulation()
                elif com[0] == "neofatch":
                    info()
                elif com[0] == "run":
                    runner = ""
                    y = 1
                    for i in range(len(com)-1):
                        runner = runner+" "+com[y]
                        y = y+1
                    os.system(runner)

            else:
                y = 0
                ans = False
                for i in modules:
                    im = "apps."+modules[y]
                    im2 = importlib.import_module(im)
                    try:
                        try:
                            ans = im2.main(com)
                        except KeyboardInterrupt:
                            print("Canceled")
                    except:
                        print('AppError 001: "APP COMMAND GOT CRASHED"')
                if ans:
                    pass
                if ans == False:
                    print("\033[91;1mIncorrect command\033[0m")

        f = open(cwd+"/set/stcom.4set")
        if f.read() == "true":
            y = 0
            for i in args.com.split(","):
                command(args.com.split(",")[y])
                y = y+1

        def main():
            string = 1
            while True:
                if len(os.getcwd().split("\\")) <= 4:
                    inp = input(f"<{os.getcwd()},string:{string}> $ ")
                else:
                    inp = input(f'<{os.getcwd().split("\\")[0]}/.../{os.getcwd().split("\\")[-3]}/{os.getcwd().split("\\")[-2]}/{os.getcwd().split("\\")[-1]}/> $')
                command(inp)
                string = string+1
        if __name__ == "__main__":
            main()
        else:
            print("Something went wrong")
    except KeyboardInterrupt:
        inp = input("KeyboardInterrupt detected it happens when you press ctrl+c. Want to return?(y/n)")
        if inp.lower() == "y":
            command("print returned")
            main()
        else:
            exit()

finally:
    print(f"bOS crashed critical error: , path: {os.getcwd}")
    print("Press any key to continue")

    keyboard.read_key()
