import player_methods as players 
import team_methods as teams
import print_it
from constants import PLAYERS, TEAMS
import copy


# create a new list to not affect original
def create_new_list(list):
  new_list = copy.deepcopy(list)
  return new_list


def main():
  # create new lists
  new_players = create_new_list(PLAYERS)
  new_teams = create_new_list(TEAMS)
  # clean data / divide players into teams / get average heights
  cleaned_players = players.clean_data(new_players)
  balanced_teams = teams.balance_teams(new_teams, cleaned_players)
  avg_heights = teams.get_avg_heights(balanced_teams)
  # call print function
  print_it.print_intro(balanced_teams, avg_heights)


# Dunder Main statement
if __name__ == "__main__":
  main()
