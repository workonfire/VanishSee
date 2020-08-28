from gc2client import GC2Client
from time import sleep, time
from colorama import init, deinit, Fore
from os import system
import platform
import yaml
import pypresence

__VERSION__ = '1.0.2'
__AUTHOR__ = ['Buty935', 'workonfire']
__CLIENT_ID__ = 747446174679564308


def color_print(color, text, no_newline=False):
    init(autoreset=True)
    print(color + text, end='') if no_newline else print(color + text)
    deinit()


def main():
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

    rpc = pypresence.Presence(__CLIENT_ID__)
    if config['discord_rich_presence']:
        try:
            rpc.connect()
            rpc.update(large_image='ghost',
                       large_text="VanishSee by workonfire#8262",
                       small_image='gc2',
                       small_text="GC2",
                       details="Sprawdza osoby na /v"
                       )
        except pypresence.ServerError and pypresence.DiscordError and pypresence.PyPresenceException:
            config['discord_rich_presence'] = False

    if config['debug']:
        color_print(Fore.RED, "UWAGA: Tryb debugowania jest włączony.")
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

    if config['discord_rich_presence']:
        rpc.update(large_image='ghost',
                   small_image='gc2',
                   small_text="GC2",
                   details="Sprawdza osoby na /v",
                   state="Tryb: " + game_mode)

    while True:
        output = perform_exploit(nickname, password, game_mode)
        userlist = extract_userlist(output)
        vanished_players = []
        if config['debug']:
            print(output)
        if userlist is not None:
            print("\nLista wszystkich zalogowanych administratorów:")
            for user in userlist:
                if user in config['staff']:
                    vanished_players.append(user)
            if vanished_players:
                for player in vanished_players:
                    color_print(Fore.LIGHTYELLOW_EX, ">> ", no_newline=True)
                    color_print(Fore.CYAN, player)
            else:
                color_print(Fore.CYAN, "Brak :(")
            print("\nJeśli nie udało się pobrać listy administracji na vanishu, ", end='')
            color_print(Fore.LIGHTRED_EX, "spróbuj ponownie", no_newline=True)
            print(".")
            print("Upewnij się też, że w ogóle ktoś siedzi ukryty.")
            if platform.system() == 'Windows':
                system('title VanishSee')
            print("\nBy spróbować ponownie, naciśnij Enter.")
            input()
        elif "Failed to login to this server." in output:
            color_print(Fore.RED, f"\nNie udało się zalogować na konto {nickname}. Jeśli jesteś obecnie na"
                                  " GC2 - wyjdź.")
            print("Naciśnij Enter, by kontynuować.")
            input()
        else:
            color_print(Fore.RED, "\nNie udało się sprawdzić listy użytkowników. Ponawianie...")
            sleep(2)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        if platform.system() == 'Windows':
            color_print(Fore.RED, "Działanie programu zostało zakończone.")
            system('pause >nul')
