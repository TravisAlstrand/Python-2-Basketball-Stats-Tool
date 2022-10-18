# things to print to console for interaction
def print_intro():
  print(''' 
    BASKETBALL TEAM STATS TOOL

    ---------- MENU ----------

    Here are your choices: 
    1) Display Team Stats
    2) Quit
    
  ''')

def print_team_options(teams, avgs):

  choice_one = input('>>> Enter an option >  ')
  if choice_one == '2':
    print('Thanks for stopping by!')
    quit()
  elif choice_one == '1':
    print(''' 
      Team options:
      -------------

    ''')
    index = 1
    for key, value in teams.items():
      print(f'{index}) {key}')
      index += 1
    print('')