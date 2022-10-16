import copy
from constants import PLAYERS


def create_new_list(list):
  new_list = copy.deepcopy(list)
  return new_list


def convert_int(string):
  substring = ' inches'
  new_string = string.replace(substring, '')
  new_int = int(new_string)
  return new_int


def convert_bool(string):
  bool = None
  if string == 'YES':
    bool = True
  else:
    bool = False
  return bool


def clean_data(list):
  for dict in list:
    new_exp = convert_bool(dict['experience'])
    dict['experience'] = new_exp
    new_height = convert_int(dict['height'])
    dict['height'] = new_height


if __name__ == "__main__":
  new_players = create_new_list(PLAYERS)
  clean_data(new_players)

