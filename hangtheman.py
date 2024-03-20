import json
import os
import random

try:
    from termcolor import colored
except ImportError:
    def cprint(*args, **kwargs):
        print(*args)


words = ["telefon", "kalemlik", "fare", "televizyon", "kestane", "ülke"]


def game_prepare():
    global choosen_word, visible_word, life
    choosen_word = random.choice(words)
    visible_word = ["-"] * len(choosen_word)
    life = 5


def take_letter():
    while True:
        letter = input("Bir harf Giriniz: ")
        if letter.lower() == "quit":
            cprint("Yavaş Yavaş eriyor...", color="red", on_color="on_blue")  
            exit()
        elif len(letter) == 1 and letter.isalpha() and letter not in visible_word:
            return letter.lower()
        else:
            cprint("Hatalı Giriş", color="red", on_color="on_grey")


def game_loop():
    global visible_word, life
    while life > 0 and choosen_word != "".join(visible_word):
        cprint("kelime: " + "".join(visible_word), color="cyan", attrs=["bold"])
        cprint("can   :  <" + "❤" * life + " " * (5 - life) + ">", color="cyan", attrs=["bold"])
        entered_letter = take_letter()
        position = letter_control(entered_letter)
        if position:
            for p in position:
                visible_word[p] = entered_letter
        else:
            life -= 1


def letter_control(entered_letter):
    pose = []
    for index, h in enumerate(choosen_word):
        if h == entered_letter:
            pose.append(index)
    return pose


def show_score_board():
    data = settings_read()
    cprint("|Skor\t\tKullanıcı|", color="white", on_color="on_grey")
    cprint("|-------------------|", color="white", on_color="on_grey")
    for score, user in data["skorlar"]:
        cprint("|" + str(score) + "\t\t" + user + " " * (9 - len(user)) + "|", color="white", on_color="on_grey")
    cprint("|-------------------|", color="white", on_color="on_grey")


def update_score_board():
    data = settings_read()
    data["skorlar"].append((life, data["last_uses"]))
    data["skorlar"].sort(key=lambda score_tuplei: score_tuplei[0], reverse=True)
    data["skorlar"] = data["skorlar"][:5]
    settings_write(data)


def game_result():
    if life > 0:
        cprint("Kazandınız", color="yellow", on_color="on_red")
        update_score_board()
    else:
        cprint("Kaybettiniz", color="red", on_color="on_yellow")
    show_score_board()


def check_folder_if_there_is_no_file_create_it():
    if not os.path.exists("settings.json"):
        settings_write({"skorlar": [], "last_uses": ""})


def settings_read():
    if os.path.exists("settings.json"):
        with open("settings.json") as f:
            return json.load(f)
    else:
        return {"skorlar": [], "last_uses": ""}


def settings_write(data):
    with open("settings.json", "w") as f:
        json.dump(data, f)


def update_user_name():
    data = settings_read()
    data["last_uses"] = input("Kullanıcı Adınız: ")
    while not data["last_uses"] or len(data["last_uses"]) > 9:
        data["last_uses"] = input("9 karakter uzunluğunda yazın: ")
    settings_write(data)


def users_control():
    data = settings_read()
    print("Son Giriş yapan: " + data["last_uses"])
    if not data["last_uses"]:
        update_user_name()
    elif input("Bu siz misiniz ?(e/h)").lower() == "h":
        update_user_name()


def main():
    is_that_repeating = True
    check_folder_if_there_is_no_file_create_it()
    cprint("Merhaba, Adam Asmacaya hoşgeldiniz", color="cyan", on_color="on_magenta", attrs=["bold"])
    cprint("Yardım: Oyun sırasında quit diyerek çıkabilirsiniz", color="cyan", on_color="on_magenta", attrs=["bold"])
    cprint("-" * 30, color="cyan", on_color="on_magenta", attrs=["bold"])
    show_score_board()
    users_control()
    while is_that_repeating:
        game_prepare()
        game_loop()
        game_result()
        if input("Devam?(e/h): ").lower() == "h":
            is_that_repeating = False
    cprint("Yavaş Yavaş gidiyor...", color="red", on_color="on_blue")


main()
