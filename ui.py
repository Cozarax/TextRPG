import curses

def draw_menu(win, choices, current_row, question=None):
    win.clear()
    h, w = win.getmaxyx()

    # Affiche la question si elle existe
    start_y = 0  # Commence à afficher à partir du haut
    if question:
        win.addstr(start_y, 0, question)  # Affiche la question alignée à gauche
        start_y += 2  # Espace supplémentaire après la question

    # Affiche les choix alignés à gauche
    for idx, choice in enumerate(choices):
        y = start_y + idx
        if idx == current_row:
            win.addstr(y, 0, choice, curses.A_REVERSE)  # Option sélectionnée
        else:
            win.addstr(y, 0, choice)  # Options non sélectionnées

    win.refresh()

def show_menu(stdscr, choices, question=None):
    curses.curs_set(0)
    current_row = 0
    height, width = 30, 30
    start_y, start_x = 0, 0

    menu_win = curses.newwin(height, width, start_y, start_x)
    menu_win.keypad(True)

    while True:
        draw_menu(menu_win, choices, current_row, question)
        key = menu_win.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(choices) - 1:
            current_row += 1
        elif key in [curses.KEY_ENTER, 10, 13]:
            return choices[current_row]

def menu(choices, question=None):
    return curses.wrapper(show_menu, choices, question)

# Exemple d'utilisation
# choices = ["Option 1", "Option 2", "Option 3"]
# selected_choice = menu(choices, "Choisis une option:")
# print(f"Tu as sélectionné : {selected_choice}")
