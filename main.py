import ui

# MAIN LOOP
while True:
    ui.clear()
    start_option = ui.initial_option()
    if start_option == "3":
        exit()
    elif start_option == "1":
        ui.account_creation_screen()
    elif start_option == "2":
        login_state = ui.login_screen()
        if login_state == "2":
            ui.login_error()
        elif login_state == "1":
            ui.no_account()
        else:
            while True:
                home_option = ui.home_screen(login_state)
                if home_option == "4":
                    break
