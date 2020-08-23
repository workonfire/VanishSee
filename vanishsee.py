from gc2client import GC2Client
from time import sleep, time
from colorama import init, deinit, Fore
from os import system
import platform
import yaml

__VERSION__ = '1.0.0'
__AUTHOR__ = ['Buty935', 'workonfire']


def main():
    def color_print(color, text, no_newline=False):
        init(autoreset=True)
        print(color + text, end='') if no_newline else print(color + text)
        deinit()

    if platform.system() == 'Windows':
        system('title VanishSee')

    color_print(Fore.LIGHTRED_EX, "\n ██▒   █▓ ▄▄▄       ███▄    █  ██▓  ██████  ██░ ██   ██████ ▓█████ ▓█████ ")
    color_print(Fore.LIGHTRED_EX, "▓██░   █▒▒████▄     ██ ▀█   █ ▓██▒▒██    ▒ ▓██░ ██▒▒██    ▒ ▓█   ▀ ▓█   ▀")
    color_print(Fore.LIGHTRED_EX, " ▓██  █▒░▒██  ▀█▄  ▓██  ▀█ ██▒▒██▒░ ▓██▄   ▒██▀▀██░░ ▓██▄   ▒███   ▒███")
    color_print(Fore.LIGHTRED_EX, "  ▒██ █░░░██▄▄▄▄██ ▓██▒  ▐▌██▒░██░  ▒   ██▒░▓█ ░██   ▒   ██▒▒▓█  ▄ ▒▓█  ▄")
    color_print(Fore.LIGHTRED_EX, "   ▒▀█░   ▓█   ▓██▒▒██░   ▓██░░██░▒██████▒▒░▓█▒░██▓▒██████▒▒░▒████▒░▒████▒")
    color_print(Fore.RED, "   ░ ▐░   ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░▓  ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒▒ ▒▓▒ ▒ ░░░ ▒░ ░░░ ▒░ ░")
    color_print(Fore.RED, "   ░ ░░    ▒   ▒▒ ░░ ░░   ░ ▒░ ▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░░ ░▒  ░ ░ ░ ░  ░ ░ ░  ░")
    color_print(Fore.RED, "     ░░    ░   ▒      ░   ░ ░  ▒ ░░  ░  ░   ░  ░░ ░░  ░  ░     ░      ░")
    color_print(Fore.RED, "      ░        ░  ░         ░  ░        ░   ░  ░  ░      ░     ░  ░   ░  ░")
    color_print(Fore.RED, "     ░                                                                    ")
    print(f"\nVanishSee v{__VERSION__}")
    color_print(Fore.LIGHTYELLOW_EX, f"by {__AUTHOR__[0]} aka {__AUTHOR__[1]}\n")

    with open('config.yml') as config_file:
        config = yaml.safe_load(config_file)

    nickname = input("Nick: ")
    password = input("Hasło (jeśli masz włączony autologin, zostaw puste): ")
    if password != '':
        color_print(Fore.RED, "UWAGA: PIN'y nie są jeszcze obsługiwane. Usuń PIN przed podaniem hasła.")
    game_mode = input("Tryb (np. SkyBlock 1): ")
    if game_mode == 'wzium':
        color_print(Fore.LIGHTRED_EX, "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        color_print(Fore.LIGHTYELLOW_EX, "██ ███ █▄▄ ██▄██ ██ █ ▄▀▄ ██")
        color_print(Fore.LIGHTGREEN_EX, "██ █ █ █▀▄███ ▄█ ██ █ █▄█ ██")
        color_print(Fore.LIGHTBLUE_EX, "██▄▀▄▀▄█▄▄▄█▄▄▄██▄▄▄█▄███▄██")
        color_print(Fore.LIGHTMAGENTA_EX, "▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
        print("Nie no, tak serio.. to SkyBlock 1.")
        game_mode = 'SkyBlock 1'

    def extract_userlist(client_output: str) -> list:
        client_output = client_output.split("\n")
        for line in client_output:
            if "[MCC] PlayerList:" in line:
                return line.strip("[MCC] PlayerList: ").split(", ")

    def perform_exploit(nick: str, account_password: str, gamemode: str) -> str:
        color_print(Fore.GREEN, "\nDołączanie na serwer...")
        client = GC2Client(nick)

        start_time = time()
        color_print(Fore.GREEN, "Logowanie...", no_newline=True)
        sleep(config['wait_before_authenticating'])
        if account_password != '':
            client.authenticate(account_password)
        print(' [' + str(round(time() - start_time, 2)) + ' s]')

        start_time = time()
        color_print(Fore.GREEN, "Wchodzenie na tryb...", no_newline=True)
        sleep(config['wait_before_joining'])
        client.join(gamemode.upper())
        print(' [' + str(round(time() - start_time, 2)) + ' s]')

        start_time = time()
        color_print(Fore.GREEN, "Sprawdzanie listy użytkowników...", no_newline=True)
        sleep(config['wait_before_checking_player_list'])
        client.send_input('/list')
        print(' [' + str(round(time() - start_time, 2)) + ' s]')

        start_time = time()
        color_print(Fore.GREEN, "Kończenie...", no_newline=True)
        sleep(config['wait_before_sending_output'])
        print(' [' + str(round(time() - start_time, 2)) + ' s]')
        return client.get_full_output()

    iterator = 0
    while True:
        if iterator == 3:
            print("Do trzech razy sztuka...")
        output = perform_exploit(nickname, password, game_mode)
        userlist = extract_userlist(output)
        if userlist is not None:
            print("\nLista wszystkich zalogowanych administratorów:")
            for user in userlist:
                if user in config['staff']:
                    color_print(Fore.LIGHTYELLOW_EX, ">> ", no_newline=True)
                    color_print(Fore.CYAN, user)
            print("\nJeśli nie udało się pobrać listy administracji na vanishu, ", end='')
            color_print(Fore.LIGHTRED_EX, "spróbuj ponownie", no_newline=True)
            print(".")
            print("Upewnij się też, że w ogóle ktoś siedzi ukryty.")
            if platform.system() == 'Windows':
                system('title VanishSee')
                print("\nBy zakończyć pracę programu, naciśnij dowolny klawisz.")
                system('pause >nul')
            break
        else:
            color_print(Fore.RED, "\nNie udało się sprawdzić listy użytkowników. Ponawianie...")
            sleep(2)
            iterator += 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
