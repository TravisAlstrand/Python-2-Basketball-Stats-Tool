from constants import PLAYERS


def create_new_list(list):
  new_list = []
  for item in list:
    new_list.append(item)
  return new_list


def convert_int(string):
  new_int = int(string)
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


if __name__ == "__main__":
  new_players = create_new_list(PLAYERS)
  clean_data(new_players)
  print(PLAYERS)