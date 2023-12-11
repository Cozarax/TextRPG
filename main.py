from saveManager import SaveManager
import ui
import os

class Game:
    def __init__(self):
        self.save_manager = SaveManager()
        self.player_pokemon = None
        self.partner_pokemon = None
    
    def start_game(self):
        menu_principal = "Menu principal"
        choices = ["Nouvelle partie", *self.save_manager.list_save_game(),"Quitter" ]

        choice = ui.menu(choices, menu_principal)
        if choice == "Nouvelle partie":
            self.new_game()
        elif choice == "Quitter":
            exit()
        else:
            save_id = choice.replace('savegame', '').replace('.txt', '')
            self.save_manager.load_game(self, save_id)
            print(f"Reprise de la partie sauvegardée. Bonjour {self.player_pokemon} et {self.partner_pokemon}.")

        # Autres initialisations...
    def new_game(self):
      save_id = self.save_manager.get_next_save_id()
      self.save_manager.create_empty_save_file(save_id)
      self.determine_player_pokemon()
      self.choose_partner_pokemon(save_id)
      self.save_manager.save_game(self, save_id)
      print(f"Commencement d'une nouvelle partie avec {self.player_pokemon} et {self.partner_pokemon}.")
    
    def determine_player_pokemon(self):
        question = "Préfères-tu le jour ou la nuit ? (jour/nuit) "
        while True:
            answer = input(question).lower()
            if answer in ["jour", "nuit"]:
                break
            print("Réponse invalide. Veuillez répondre par 'jour' ou 'nuit'.")
        
        self.player_pokemon = "Pikachu" if answer == "jour" else "Roucool"
        print(f"Tu es un(e) {self.player_pokemon} !")

    def choose_partner_pokemon(self, save_id):  # Ajout de save_id comme paramètre
      question = "Choisis un partenaire :"
      choices = ["Bulbizarre", "Salamèche", "Carapuce"]
      self.partner_pokemon = ui.menu(choices, question)
      print(f"Ton partenaire est {self.partner_pokemon} !")
      self.save_manager.save_game(self, save_id)  # Passer save_id à save_game

# Démarrer le jeu
game = Game()
game.start_game()
