import os
import time
from colorama import Fore, init

init(autoreset=True)

def clear():
    os.system('clear')

def logo():
    print(f"{Fore.GREEN}======================================")
    print(f"{Fore.WHITE}      HOLLOW BASIC TOOLBOX v1.5")
    print(f"{Fore.GREEN}======================================")
    print(f"{Fore.YELLOW} Tier: Basic | Tools: 15 | Dev: Hollow\n")

# 15 Original Tools with Real Repos
tools = {
    "01": ("Nmap", "nmap/nmap"),
    "02": ("SQLmap", "sqlmapproject/sqlmap"),
    "03": ("Zphisher", "htr-tech/zphisher"),
    "04": ("Sherlock", "sherlock-project/sherlock"),
    "05": ("IP-Tracer", "rajkumardusad/IP-Tracer"),
    "06": ("RedHawk", "Tuhinshubhra/RED_HAWK"),
    "07": ("Wifite2", "kimhoang/wifite2"),
    "08": ("Hydra", "vanhauser-thc/thc-hydra"),
    "09": ("Metasploit", "rapid7/metasploit-framework"),
    "10": ("Ngrok", "inconshreveable/ngrok"),
    "11": ("Seeker", "thewhiteh4t/seeker"),
    "12": ("SayCheese", "thewhiteh4t/saycheese"),
    "13": ("Nikto", "sullo/nikto"),
    "14": ("Slowloris", "gkbrk/slowloris"),
    "15": ("InstaHack", "noob-hackers/instahack")
}

def main():
    clear()
    logo()
    for k, v in sorted(tools.items()):
        print(f"{Fore.CYAN}[{k}] {Fore.WHITE}{v[0]}")
    
    print(f"\n{Fore.RED}[00] Exit")
    
    choice = input(f"\n{Fore.YELLOW}Select Tool (01-15): {Fore.WHITE}")
    
    if choice in tools:
        name, repo = tools[choice]
        clear()
        logo()
        print(f"{Fore.GREEN}[*] Installing {name}...")
        print(f"{Fore.WHITE}Command: git clone https://github.com/{repo}.git")
        time.sleep(1)
        os.system(f"git clone https://github.com/{repo}.git")
        print(f"\n{Fore.GREEN}[Done] Tool cloned. Check your directory.")
        input(f"\n{Fore.YELLOW}Press Enter to return...")
        main()
    elif choice == "00" or choice == "0":
        print(f"{Fore.GREEN}Bye!")
        exit()
    else:
        print(f"{Fore.RED}Invalid selection!")
        time.sleep(1)
        main()

if __name__ == "__main__":
    main()
    
