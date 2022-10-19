from constants import TEAMS

# intro to print to console for interaction
def print_intro(teams, avgs):
  print(''' 
    BASKETBALL TEAM STATS TOOL

    ---------- MENU ----------

    Here are your choices: 
    1) Display Team Stats
    2) Quit
  ''')
  while True:
    try:
      choice_one_string = input('>>> Enter an option >  ')
      choice_one = int(choice_one_string)
      # to quit
      if choice_one == 2:
        print('\nThanks for stopping by!\n')
        quit()
      # to print teams
      elif choice_one == 1:
        print_team_options(teams, avgs)
        break
      # if invalid number
      elif choice_one <= 0 or choice_one > 2:
        raise Exception('\n** Please enter a 1 or 2 **\n')
    # if not a number
    except ValueError:
      print('\n** Please enter a number **\n')
      continue
    except Exception as e:
      print(e)
      continue


# team select options menu
def print_team_options(teams, avgs):
  print('\nTeam options:\n-------------\n')
  index = 1
  for key, value in teams.items():
    print(f'{index}) {key}')
    index += 1
  while True:
    try:
      choice_two_string = input('\n>>> Enter an option >  ')
      choice_two = int(choice_two_string)
      # if valid input
      if choice_two in range(1, index):
        team_name = TEAMS[choice_two -1]
        print_team_details(teams[team_name], team_name, avgs[choice_two - 1])
        break
      else:
        # if invalid number
        raise Exception(f'\n** Please enter a number between 1 and {index - 1} **\n')
    except ValueError:
      # if not a number
      print('\n** Please enter a number **\n')
      continue
    except Exception as e:
      print(e)
      continue


# display team details
def print_team_details(team, team_name, avg):
  exp = 0
  no_exp = 0
  for player in team:
    if player['experience'] == True:
      exp += 1
    else:
      no_exp += 1
  
  print(f'\nTeam: {team_name} Stats\n---------------------\n')
  print(f'Total players: {len(team)}')
  print(f'Total experienced: {exp}\nTotal inexperienced: {no_exp}\nAverage height: {avg}')

  player_names_list = []
  guardian_list = []
  for player in team:
    player_names_list.append(player['name'])
    guardian_list.append(player['guardians'])
  player_names = ', '.join(player_names_list)

  print(f'''\nPlayers on Team:
    {player_names}\n''')
  print(guardian_list)
  