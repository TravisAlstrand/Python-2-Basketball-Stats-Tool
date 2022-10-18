# replace PLAYER experience / height / guardians with new values
def clean_data(list):
  for dict in list:
    dict['experience'] = convert_bool(dict['experience'])
    dict['height'] = convert_int(dict['height'])
    dict['guardians'] = convert_to_list(dict['guardians'])
  return list


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


# convert PLAYER guardians to a LIST
def convert_to_list(string):
  substring = ' and '
  if substring in string:
    new_list = string.split(substring)
  else:
    new_list = [string]
  return new_list