import copy
from constants import PLAYERS
from constants import TEAMS


# create a new list to not affect original
def create_new_list(list):
  new_list = copy.deepcopy(list)
  return new_list


# convert PLAYER experience to a BOOL
def convert_bool(string):
  bool = None
  if string == 'YES':
    bool = True
  else:
    bool = False
  return bool


# convert PLAYER height to an INT
def convert_int(string):
  substring = ' inches'
  new_string = string.replace(substring, '')
  new_int = int(new_string)
  return new_int


def balance_teams(teams, players):
  experienced_players = []
  not_experienced_players = []
  div_length = (len(players) / 2) / len(teams)
  balanced_team = {}

  for team in teams:
    balanced_team.update({
      team : []
    })

  for player in players:
    if player['experience'] == True:
      experienced_players.append(player)
    else:
      not_experienced_players.append(player)

  split_exp = [] 
  for i in range(0, len(experienced_players), int(div_length)):
    split_exp.append(experienced_players[i])

  split_no_exp = []
  for i in range(0, len(not_experienced_players), int(div_length)):
    split_no_exp.append(not_experienced_players[i])
  
  print(split_exp)
  print(split_no_exp)

    
  # print(balanced_team)


# convert PLAYER guardians to a LIST
def convert_to_list(string):
  substring = ' and '
  if substring in string:
    new_list = string.split(substring)
  else:
    new_list = [string]
  return new_list


# replace PLAYER experience / height / guardians with new values
def clean_data(list):
  for dict in list:
    dict['experience'] = convert_bool(dict['experience'])
    dict['height'] = convert_int(dict['height'])
    dict['guardians'] = convert_to_list(dict['guardians'])


# Dunder Main statement
if __name__ == "__main__":
  new_players = create_new_list(PLAYERS)
  new_teams = create_new_list(TEAMS)
  clean_data(new_players)
  balance_teams(new_teams, new_players)
