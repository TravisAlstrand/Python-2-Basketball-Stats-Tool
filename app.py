import player_methods as players 
import team_methods as teams
from constants import PLAYERS
from constants import TEAMS
import copy


# create a new list to not affect original
def create_new_list(list):
  new_list = copy.deepcopy(list)
  return new_list


def main():
  new_players = create_new_list(PLAYERS)
  new_teams = create_new_list(TEAMS)

  cleaned_players = players.clean_data(new_players)
  balanced_teams = teams.balance_teams(new_teams, new_players)


# Dunder Main statement
if __name__ == "__main__":
  main()
