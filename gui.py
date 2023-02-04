import time
from tkinter import *

import entry_placeholder
import funcs
import log_commands


def launcher():
    # settings of windows
    def set_window(window):
        screen_width = window.winfo_screenwidth() // 6
        screen_height = window.winfo_screenheight() // 6
        start_position = "800x600+" + str(screen_width) + "+" + str(screen_height)
        window.geometry(start_position)
        window.resizable(width=False, height=False)
        window.title("MW Bot")

    # background setter
    def set_background(window, photo, icon):
        global img
        img = PhotoImage(file=str(photo), master=window)
        img_label = Label(window, image=img)
        img_label.place(x=0, y=0)
        window.iconphoto(False, PhotoImage(file=icon))

    # login into game
    def logiin(event):
        new_window()

    def login(event):
        try:
            if username.get() and password.get():
                if funcs.login(username.get(), password.get()):
                    if remember_me.get():
                        with open("userdata", 'w') as f:
                            f.write(username.get())
                            f.write(' ')
                            f.write(password.get())
                            f.close()
                    new_window()
                else:
                    log_label["text"] = log_commands.login_fail
        except:
            log_label["text"] = log_commands.login_fail

    # Login window start
    root = Tk()

    # Main window
    set_window(root)
    set_background(root, "images/background.png", "images/icon.png")

    # variables
    username = StringVar()
    password = StringVar()
    alley_fight_count_easy = IntVar()
    alley_fight_count_normal = IntVar()
    alley_fight_count_hard = IntVar()
    metro_fight_count = IntVar()
    neft_fight_count = IntVar()
    world2_fight_count = IntVar()
    world_fight_count = IntVar()
    bombing_count = IntVar()
    petrics_count = IntVar()
    poly_dice_count = IntVar()
    always_bomb = BooleanVar()
    remember_me = BooleanVar()
    world_boss_attack = BooleanVar()

    # check is there saved data
    login_data, default_login, default_password = "", "", ""
    with open("userdata", 'r') as f:
        for i in f:
            login_data += i
        f.close()
        if " " in login_data:
            default_login, default_password = login_data.split(" ")

    login_bg_label = Label(root, background="#f7b142")
    login_bg_label.place(x=305, y=236, width=203, height=119)

    if default_login and default_password:
        username_entry = Entry(width=30, textvariable=username)
        username_entry.insert(0, default_login)
        username_entry.place(x=315, y=248)
        password_entry = Entry(width=30, textvariable=password)
        password_entry.insert(0, default_password)
        password_entry.place(x=315, y=268)
    else:
        username_entry = entry_placeholder.PlaceholderEntry(width=30, textvariable=username, placeholder='Email')
        username_entry.place(x=315, y=248)
        password_entry = entry_placeholder.PlaceholderEntry(width=30, textvariable=password, placeholder='Password')
        password_entry.place(x=315, y=268)

    login_button = Button(width=25, text="Login")
    login_button.place(x=315, y=288)
    login_button.bind("<Button-1>", login)

    login_checkbox = Checkbutton(text=log_commands.login_remember, variable=remember_me)
    login_checkbox.select()
    login_checkbox.place(x=315, y=315)

    # logs of game
    log_label = Label(root, background="#f7b142", text="")
    log_label.place(x=3, y=555, width=795, height=35)

    def new_window():

        # easy PVP fight
        def alley_fight_easy(event):
            try:
                log_label_change(log_commands.pvp_ok_easy)
                for i in range(alley_fight_count_easy.get()):
                    funcs.pvp_fight_easy()
            except:
                log_label_change(log_commands.pvp_fail_easy)

        # normal PVP fight
        def alley_fight_normal(event):
            try:
                log_label_change(log_commands.pvp_ok_normal)
                for i in range(alley_fight_count_normal.get()):
                    funcs.pvp_fight_normal()
            except:
                log_label_change(log_commands.pvp_fail_normal)

        # hard PVP fight
        def alley_fight_hard(event):
            try:
                log_label_change(log_commands.pvp_ok_hard)
                for i in range(alley_fight_count_hard.get()):
                    funcs.pvp_fight_hard()
            except:
                log_label_change(log_commands.pvp_fail_hard)

        # metro fight against rats
        def metro_fight(event):
            try:
                log_label_change(log_commands.metro_ok)
                for i in range(metro_fight_count.get()):
                    funcs.metrofight()
                funcs.refresh()
            except:
                log_label_change(log_commands.metro_fail)

        # Neftlenin fights
        def neft_fight(event):
            try:
                log_label_change(log_commands.neft_ok)
                for i in range(metro_fight_count.get()):
                    funcs.neftleninfight()
            except:
                log_label_change(log_commands.neft_fail)

        # Weekly raid fights
        def world2_fight(event):
            try:
                log_label_change(log_commands.raid_ok)
                for i in range(world2_fight_count.get()):
                    funcs.worldtour2fight()
            except:
                log_label_change(log_commands.raid_fail)

        def world_fight(event):
            try:
                log_label_change(log_commands.worldtour_ok)
                for i in range(world_fight_count.get()):
                    if world_boss_attack.get():
                        funcs.worldtourfight("auto")
                    else:
                        funcs.worldtourfight()
            except:
                log_label_change(log_commands.worldtour_fail)

        # Taxi at monday
        def bombing(event):
            try:
                log_label_change(log_commands.bombing_ok)
                if always_bomb.get():
                    while True:
                        funcs.bombing()
                else:
                    for i in range(bombing_count.get()):
                        funcs.bombing()
            except:
                log_label_change(log_commands.bombing_fail)

        def product_petrics(event):
            try:
                log_label_change(log_commands.petrics_ok)
                funcs.make_petrics(petrics_count.get())
            except:
                log_label_change(log_commands.petrics_fail)

        def play_moscowpoly(event):
            try:
                log_label_change(log_commands.moscowpoly_ok)
                funcs.moscowpoly_game(poly_dice_count.get())
            except:
                log_label_change(log_commands.moscowpoly_fail)

        def car_travel(event):
            try:
                log_label_change(log_commands.cars_ok)
                funcs.auto_travels()
            except:
                log_label_change(log_commands.cars_fail)

        def log_label_change(text):
            log_label["text"] = text

        # in-game window start
        top = root
        set_window(top)
        set_background(top, "images/background.png", "images/icon.png")

        # logs of game
        log_label = Label(top, background="#f7b142", text="Logged In")
        log_label.place(x=3, y=555, width=795, height=35)

        # Pvp fight interface
        alley_fight_label = Label(top, background="#f7b142")
        alley_fight_label.place(x=45, y=48, width=180, height=90)

        alley_fight_spinbox_easy = Spinbox(from_=1, to=10, width=4, textvariable=alley_fight_count_easy)
        alley_fight_button_easy = Button(width=15, text=log_commands.pvp_fight_easy)
        alley_fight_spinbox_easy.place(x=55, y=55)
        alley_fight_button_easy.place(x=100, y=50)
        alley_fight_button_easy.bind("<Button-1>", alley_fight_easy)

        alley_fight_spinbox_normal = Spinbox(from_=1, to=10, width=4, textvariable=alley_fight_count_normal)
        alley_fight_button_normal = Button(width=15, text=log_commands.pvp_fight_normal)
        alley_fight_spinbox_normal.place(x=55, y=85)
        alley_fight_button_normal.place(x=100, y=80)
        alley_fight_button_normal.bind("<Button-1>", alley_fight_normal)

        alley_fight_spinbox_hard = Spinbox(from_=1, to=10, width=4, textvariable=alley_fight_count_hard)
        alley_fight_button_hard = Button(width=15, text=log_commands.pvp_fight_hard)
        alley_fight_spinbox_hard.place(x=55, y=115)
        alley_fight_button_hard.place(x=100, y=110)
        alley_fight_button_hard.bind("<Button-1>", alley_fight_hard)

        # Pve fight interface
        pve_fight_label = Label(top, background="#f7b142")
        pve_fight_label.place(x=45, y=178, width=180, height=90)

        metro_fight_spinbox = Spinbox(from_=1, to=10, width=4, textvariable=metro_fight_count)
        metro_fight_button = Button(width=15, text=log_commands.metro_fight)
        metro_fight_spinbox.place(x=55, y=185)
        metro_fight_button.place(x=100, y=180)
        metro_fight_button.bind("<Button-1>", metro_fight)

        neft_fight_spinbox = Spinbox(from_=1, to=10, width=4, textvariable=neft_fight_count)
        neft_fight_button = Button(width=15, text=log_commands.neft_fight)
        neft_fight_spinbox.place(x=55, y=215)
        neft_fight_button.place(x=100, y=210)
        neft_fight_button.bind("<Button-1>", neft_fight)

        world2_fight_spinbox = Spinbox(from_=1, to=10, width=4, textvariable=world2_fight_count)
        world2_fight_button = Button(width=15, text=log_commands.raid_fight)
        world2_fight_spinbox.place(x=55, y=245)
        world2_fight_button.place(x=100, y=240)
        world2_fight_button.bind("<Button-1>", world2_fight)

        # events
        event_label = Label(top, background="#f7b142")
        event_label.place(x=45, y=297, width=180, height=113)

        bombing_spinbox = Spinbox(from_=1, to=10, width=4, textvariable=bombing_count)
        bombing_button = Button(width=15, text=log_commands.bombing_event)
        bombing_spinbox.place(x=57, y=302)
        bombing_button.place(x=100, y=300)
        bombing_button.bind("<Button-1>", bombing)
        bombing_checkbox = Checkbutton(text=log_commands.bombing_event_all_day, variable=always_bomb)
        bombing_checkbox.place(width=159, x=55, y=325)

        world_fight_spinbox = Spinbox(from_=1, to=10, width=4, textvariable=world_fight_count)
        world_fight_button = Button(width=15, text=log_commands.worldtour_fight)
        world_fight_spinbox.place(x=55, y=357)
        world_fight_button.place(x=100, y=355)
        world_fight_button.bind("<Button-1>", world_fight)
        bombing_checkbox = Checkbutton(text=log_commands.worldtour_boss_attack, variable=world_boss_attack)
        bombing_checkbox.place(width=159, x=55, y=380)

        # products
        products_label = Label(top, background="#f7b142")
        products_label.place(x=245, y=48, width=180, height=90)

        petrics_spinbox = Spinbox(from_=1, to=999, width=4, textvariable=petrics_count)
        petrics_button = Button(width=15, text=log_commands.petrics_make)
        petrics_spinbox.place(x=257, y=55)
        petrics_button.place(x=300, y=50)
        petrics_button.bind("<Button-1>", product_petrics)

        moscowpoly_spinbox = Spinbox(from_=1, to=3, width=4, textvariable=poly_dice_count)
        moscowpoly_button = Button(width=15, text=log_commands.moscowpoly_play)
        moscowpoly_spinbox.place(x=257, y=85)
        moscowpoly_button.place(x=300, y=80)
        moscowpoly_button.bind("<Button-1>", play_moscowpoly)

        cars_spinbox = Spinbox(from_=0, to=1, width=4)
        cars_button = Button(width=15, text=log_commands.cars_travel)
        cars_spinbox.place(x=257, y=115)
        cars_button.place(x=300, y=110)
        cars_button.bind("<Button-1>", car_travel)

        buff_label = Label(top, background="#f7b142")
        buff_label.place(x=445, y=48, width=150, height=220)

        heal_hp_button = Button(width=17, text=log_commands.heal_hp)
        heal_hp_button.place(x=455, y=50)

        heal_tonus_button = Button(width=17, text=log_commands.heal_tonus)
        heal_tonus_button.place(x=455, y=80)

        red_gloves_button = Button(width=17, text=log_commands.red_gloves)
        red_gloves_button.place(x=455, y=110)

        black_gloves_button = Button(width=17, text=log_commands.black_gloves)
        black_gloves_button.place(x=455, y=140)

        respirator_button = Button(width=17, text=log_commands.respirator)
        respirator_button.place(x=455, y=170)

        gasmask_button = Button(width=17, text=log_commands.gasmask)
        gasmask_button.place(x=455, y=200)

        snickers_button = Button(width=17, text=log_commands.eat_snickers)
        snickers_button.place(x=455, y=230)

        person_label = Label(top, background="#f7b142")
        person_label.place(x=614, y=48, width=178, height=220)

        # name, health, max health, touns, max tonus, gold, ruda, oil, honey
        # messages, logs, duels

        def person(event):
            person_info = funcs.get_person_info()
            # person_info = ["Name: M03M15", "Health: 800K/1,4M", "Touns: 104/160", "Money: 18M", "Ore: 2,4M",
            #                "Oil: 3,1M", "Honey: 80", "Messages: 2", "Logs: 41", "Duels: 3"]

            person_info_text = ""
            for info in person_info:
                person_info_text += str(info)+"\n"

            person_info_label = Label(top, width=20, background="aqua",
                                      text=person_info_text,
                                      justify=CENTER, font="Papyrus 10")
            person_info_label.place(x=620, y=55)

        person(0)
        person_info_refresh_button = Button(width=22, text=log_commands.person_refresh)
        person_info_refresh_button.place(x=621, y=235)
        person_info_refresh_button.bind("<Button-1>", person)
    root.mainloop()
