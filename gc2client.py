from subprocess import Popen, PIPE, STDOUT
from time import sleep
import platform


class GC2Client:
    def __init__(self, nick: str):
        if platform.system() == 'Windows':
            process = ['MinecraftClient.exe', 'BasicIO']
        else:
            process = ['mono', 'MinecraftClient.exe', 'BasicIO']
        self.client = Popen(process, stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        self.send_input(nick)
        self.send_input('')
        self.send_input('gc2.pl')

    def __del__(self):
        self.client.kill()

    def send_input(self, message: str):
        message = message.encode('utf-8') + '\n'.encode('utf-8')
        self.client.stdin.write(message)
        self.client.stdin.flush()

    def click(self, inventory_id: int, slot: int):
        self.send_input(f'/inventory {inventory_id} click {slot}')

    def authenticate(self, password: str):
        self.send_input(f'/login {password}')

    def join(self, gamemode: str):
        gamemodes = {'SKYBLOCK 1': [11, 12],
                     'SKYBLOCK 2': [11, 13],
                     'SKYBLOCK 3': [11, 14],
                     'SKYBLOCK 4': [11, 21],
                     'SEABLOCK': [13],
                     'MINEBLOCK 1': [15, 12],
                     'MINEBLOCK 2': [15, 14],
                     'CREATIVE': [19],
                     'LAVABLOCK': [21],
                     'CLASSIC MC': [25],
                     'PVP': [31]}
        self.click(1, gamemodes.get(gamemode)[0])
        if gamemodes.get(gamemode)[1]:
            sleep(2)
            self.click(2, gamemodes.get(gamemode)[1])

    def get_full_output(self) -> str:
        self.__del__()
        output = self.client.communicate()[0].decode('utf-8')
        color_codes = list(range(10)) + ['a', 'b', 'c', 'd', 'e', 'f', 'l', 'o', 'm', 'n', 'k', 'r']
        for code in color_codes:
            output = output.replace('§' + str(code), '')
        return output
