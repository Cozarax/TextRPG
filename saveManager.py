import os

class SaveManager: 
  def __init__(self, save_directory="saves"):
    self.save_directory = save_directory
    if not os.path.exists(self.save_directory):
      os.makedirs(self.save_directory)

  def list_save_game(self):
    return [f for f in os.listdir('saves') if f.endswith('.txt')]

  def create_empty_save_file(self, save_id):
    filename = os.path.join('saves', f'savegame{save_id}.txt')
    open(filename, 'a').close()  

  def get_next_save_id(self):
    save_files = self.list_save_game()
    max_id = 0
    for file in save_files:
        # Extrait le numéro de chaque fichier de sauvegarde
        file_id = int(file.replace('savegame', '').replace('.txt', ''))
        if file_id > max_id:
            max_id = file_id
    return max_id + 1
  
  def save_game(self, game, save_id):
    filename = os.path.join(self.save_directory, f'savegame{save_id}.txt')
    with open(filename, "w") as file:
        file.write(f"{game.player_pokemon}\n")
        file.write(f"{game.partner_pokemon}\n")

  def load_game(self, game, save_id):
    filename = os.path.join(self.save_directory, f'savegame{save_id}.txt')
    try:
        with open(filename, "r") as file:
            game.player_pokemon = file.readline().strip()
            game.partner_pokemon = file.readline().strip()
    except FileNotFoundError:
        pass