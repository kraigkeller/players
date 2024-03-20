class Player:
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []
        self.captain = None

    def add_player(self, player):
        self.players.append(player)

    def set_captain(self, player):
        if player in self.players:
            self.captain = player

class PlayerPool:
    def __init__(self):
        self.players = []

    def add_player(self, player_name):
        player = Player(player_name)
        self.players.append(player)
        return player

    def get_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player
        return None

class TeamPool:
    def __init__(self):
        self.teams = []

    def add_team(self, team_name):
        team = Team(team_name)
        self.teams.append(team)
        return team

    def get_team(self, team_name):
        for team in self.teams:
            if team.team_name == team_name:
                return team
        return None

import sys

def main():
    player_names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]
    team_names = ["Titans", "Warriors", "Rangers"]

    player_pool = PlayerPool()
    team_pool = TeamPool()

    # Populating players
    for name in player_names:
        player_pool.add_player(name)

    # Populating teams
    for name in team_names:
        team_pool.add_team(name)

    while True:
        print("\nOptions:")
        print("1. Assign Player to Team")
        print("2. Set Team Captain")
        print("3. Display Teams")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            assign_player_to_team(player_pool, team_pool)
        elif choice == "2":
            set_team_captain(player_pool, team_pool)
        elif choice == "3":
            display_teams(team_pool)
        elif choice == "4":
            print("Exiting program.")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

def assign_player_to_team(player_pool, team_pool):
    player_name = input("Enter player name: ")
    team_name = input("Enter team name: ")

    player = player_pool.get_player(player_name)
    team = team_pool.get_team(team_name)

    if player is None or team is None:
        print("Invalid player or team name.")
        return

    team.add_player(player)
    print(f"{player.name} assigned to {team.team_name}")

def set_team_captain(player_pool, team_pool):
    player_name = input("Enter player name for captain: ")
    team_name = input("Enter team name: ")

    player = player_pool.get_player(player_name)
    team = team_pool.get_team(team_name)

    if player is None or team is None:
        print("Invalid player or team name.")
        return

    team.set_captain(player)
    print(f"{player.name} set as captain of {team.team_name}")

def display_teams(team_pool):
    for team in team_pool.teams:
        print(f"\nTeam: {team.team_name}")
        print("Players: ", ', '.join([player.name for player in team.players]))
        if team.captain:
            print(f"Captain: {team.captain.name}")
        else:
            print("Captain: None")

if __name__ == "__main__":
    main()
