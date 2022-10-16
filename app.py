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

def convert_to_list(string):
  substring = ' and '
  if substring in string:
    new_list = string.split(substring)
  else:
    new_list = [string]
  return new_list

# replace PLAYER experience / height with new values
def clean_data(list):
  for dict in list:
    new_exp = convert_bool(dict['experience'])
    dict['experience'] = new_exp
    new_height = convert_int(dict['height'])
    dict['height'] = new_height
    new_guardians = convert_to_list(dict['guardians'])
    dict['guardians'] = new_guardians


if __name__ == "__main__":
  new_players = create_new_list(PLAYERS)
  new_teams = create_new_list(TEAMS)
  clean_data(new_players)

print(new_players)
  # print(len(PLAYERS) / len(TEAMS))

