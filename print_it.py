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

        # this is where I'll call the print_team_details function
        # my goal is to send the correct dictionary as an argument without hardcoding in a team name like - teams('Panthers')
        # but can't seem to access dictionary key/values by index like a list.
        # is there a way OR better way to achieve something like this?

        # my goal (if it were a list) for comparison below
        print_team_details(teams[choice_two - 1], avgs)
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
def print_team_details(team, avg):
  print("ahhh... I've been expecting you...")