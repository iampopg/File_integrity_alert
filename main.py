import hashlib
import time
import os
from colorama import init, Fore
from playsound import playsound
from pyfiglet import figlet_format

# Initialize colorama
init(autoreset=True)
green = Fore.GREEN
yellow = Fore.YELLOW
red = Fore.RED
white = Fore.WHITE

def calculate_sha256(file_path):
    """Calculate the SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def monitor_file_integrity(file_path, interval=10):
    """Monitor file integrity and print alert if changes are detected."""
    current_hash = calculate_sha256(file_path)
    while True:
        time.sleep(interval)
        new_hash = calculate_sha256(file_path)
        if current_hash != new_hash:
            print(green + f"File integrity alert: {red}{file_path} {white}has changed!")
            current_hash = new_hash
            # to play alert sound in the same directory
            playsound('alert.mp3')  
            pass
            

def run():
    try:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        
        
        if not os.path.exists('.integrity_file_path'):
            os.makedirs('.integrity_file_path')
        print(yellow+ figlet_format('FILE INTERGRITY', font='standard', width = 100))
        print(f'''
            {green}Coded by Pop(G)
                        {red}https://t.me/iampopg
        ''')

        print('''
            [1] Start Checking
            [2] Add File for Integrity Monitoring
            [3] Exit
        ''')
        ent = input(': ')

        if ent == "1":
            with open('.integrity_file_path/files', 'r') as read:
                path_to_files = read.readlines()
                if len(path_to_files) > 0:
                    file_path = path_to_files[-1].strip()
                    monitor_file_integrity(file_path)
                else:
                    print(yellow + "No files to monitor. Please add files first.")
        elif ent == '2':
            file_to_add = input(yellow+ "Enter Path to file: ")
            if os.path.exists(file_to_add):
                try:
                    with open('.integrity_file_path/files', 'a') as append:
                        append.write(file_to_add + '\n')
                        run()
                except FileNotFoundError:
                    print(red +'You have not added any path to your intergrity file path, please run again with option 2')
                    time.sleep(1)
                    run()
            else:
                print(yellow + "File does not exist.")
                time.sleep(1)
                run()
        elif ent == '3':
            exit()
        else:
            print(yellow + "Invalid option. Please choose 1, 2, or 3.")
            time.sleep(2)
            run()
    except KeyboardInterrupt:
        print()
        print('Thanks for your time'.center(50))
        time.sleep(1)
    except Exception as e:
        print(e)

run()
