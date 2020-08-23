# VanishSee
Program do sprawdzania osób będących na vanishu na serwerze [GC2](https://gc2.pl).

![Screnshot](https://i.imgur.com/aMoHz6A.png)

## Działanie
Program wykorzystuje fakt, że w milisekundy po wejściu gracza na serwer, ten musi przetworzyć dla użytkownika listę wszystkich osób, by dowiedzieć się, kogo możemy zobaczyć, a kogo nie.

Jeśli sprawdzimy wspomnianą listę **przed** tą procedurą, dostaniemy na tacy listę wszystkich zalogowanych osób, bez wyjątku.

Wykorzystując ten sposób, nie musimy bawić się w żadne bugowanie `/is team` - program **nie wykonuje żadnych komend na serwerze**.

Problemem jest jednak to, że VanishSee nie zawsze zadziała. Każda akcja programu musi zostać wykonana "na wyczucie". Niektórym osobom zadziała za pierwszym razem, a niektórym za dziesiątym. Na szczęście VanishSee wszystko robi automatycznie 😉

## Konfiguracja
Wszystko jest szerzej opisane w pliku [config.yml](config.yml).

Najciekawsza jest opcja `wait_before_checking_player_list`. Najlepiej jest zostawić domyślną wartość (`0.8`), ale kiedy coś będzie nie działać, można się pobawić. Zalecane jest ustawianie wartości od `0.5` do `1`.

## Informacje
**VanishSee** wykorzystuje projekt [ORelio/Minecraft-Console-Client](https://github.com/ORelio/Minecraft-Console-Client) do swojego działania, który jest udostępniany na licencji [CDDL-1.0](https://opensource.org/licenses/CDDL-1.0).

Ślę również podziękowania dla [@k073l](https://github.com/k073l) za pomoc w napisaniu wrappera do klienta [@ORelio](https://github.com/ORelio).
