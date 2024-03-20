# Lesson Teams Python

## Python Basics

### Classes in Python
- **Definition**: A blueprint for objects, comprising attributes and methods.
- ### Python vs Other Languages
- **Syntax**: Python’s syntax is different. It relies heavily on indentation and doesn’t use semicolons or parentheses for scope.
- **Access Specifiers**: Unlike languages like C++ or Java, Python does not use access specifiers such as `public` or `private`.
- **Constructors**: Python employs `__init__` for constructors, in contrast to using the class name as in C++ or Java.

### Functions in Python
- **Defining Functions**: Utilize the `def` keyword. Indentation rather than braces `{}` determines the scope.
- **Python vs Other Languages**: Python functions default to returning `None`, unlike mandatory return types in languages like C++ or Java.

## Application Structure and Explanation

### `Player` Class
```python
class Player:
    def __init__(self, name):
        self.name = name
```
- **Purpose**: Represents an individual player.
- **Constructor (`__init__`)**: Initializes a `Player` with a `name`.

### `Team` Class
```python
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
```
- **Functionality**: Manages a team's name, players, and captain.
- **Constructor**: Sets up the team name, an empty player list, and no captain initially.
- **Methods**: Include adding players and setting a team captain.

### `PlayerPool` Class
```python
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
```
- **Purpose**: Manages a pool of player objects.
- **Constructor**: Initializes an empty list of players.
- **Methods**: Allow adding new players and retrieving existing ones.

### `TeamPool` Class
```python
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
```
- **Functionality**: Holds and manages a collection of teams.
- **Constructor**: Creates an empty list for teams.
- **Methods**: Facilitate adding new teams and finding specific ones.

### Main Function and Interactive Workflow
```python
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
```

### `assign_player_to_team` Function
```python
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
```
- **Purpose**: Assigns a player to a team.
- **Process**:
  - Collects user input for player and team names.
  - Retrieves the corresponding player and team objects.
  - If either is not found, it notifies the user and exits.
  - If valid, adds the player to the team and confirms the action.

### `set_team_captain` Function
```python
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
```
- **Functionality**: Sets a team captain.
- **Operation**:
  - Takes user input for the player to be made captain and the respective team.
  - Retrieves the player and team from the pools.
  - Verifies the existence of both. If not found, exits.
  - Sets the player as captain of the team and confirms the assignment.

### `display_teams` Function
```python
def display_teams(team_pool):
    for team in team_pool.teams:
        print(f"\nTeam: {team.team_name}")
        print("Players: ", ', '.join([player.name for player in team.players]))
        if team.captain:
            print(f"Captain: {team.captain.name}")
        else:
            print("Captain: None")
```
- **Purpose**: Displays all teams and their members.
- **Mechanism**:
  - Iterates through each team in the pool.
  - Prints the team name, list of player names, and the captain's name.
  - If no captain is set, it indicates so.

### Main Execution Block
```python
if __name__ == "__main__":
    main()
```
- **Role**: Ensures that the script runs the `main` function when executed as a standalone program.
- **Explanation**: This is a standard Python practice to differentiate script execution from module import.

## Comprehensive Understanding

The application's functional aspects, like assigning players to teams, setting team captains, and displaying team details, are handled through specific functions. Each function follows a clear structure: take user input
- **Overview**: Sets up the application and handles user interactions.
- **Process**: Initializes pools, populates them, and enters a loop to offer options like assigning players, setting captains, and displaying team details.

### Functional Design
- **`assign_player_to_team`**: Assigns a player to a specific team.
- **`set_team_captain`**: Sets a player as a team's captain.
- **`display_teams`**: Shows the composition of each team.

### Application's Structure Merits
- **Modularity**: Each class and function has a distinct, isolated role.
- **Scalability**: The structure allows for easy expansion and modification.
- **Readability**: The clear organization and flow facilitate understanding by others.
