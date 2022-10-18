# create a new teams object which will have a key for each team
# and a list of players for each
def clean_teams(teams):
  cleaned_teams = {}
  for team in teams:
    new_team = {team: []}
    cleaned_teams.update(new_team)
  return cleaned_teams


# split players into 2 lists by experience and
# evenly distribute players to each team
def balance_teams(teams, players):
  experienced_players = []
  not_experienced_players = []

  new_teams = clean_teams(teams)

  for player in players:
    if player['experience'] == True:
      experienced_players.append(player)
    else:
      not_experienced_players.append(player)

  while experienced_players:
    for key, value in new_teams.items():
      player = experienced_players.pop(0)
      value.append(player)

  while not_experienced_players:
    for key, value in new_teams.items():
      player = not_experienced_players.pop(0)
      value.append(player)
  
  return new_teams

def get_avg_heights(teams):
  avg_heights = []

  for key, value in teams.items():
    height_sum = 0
    for player in value:
      height_sum += player['height']
    team_avg = height_sum / len(value)
    avg_heights.append(round(team_avg))
    height_sum = 0
  
  return avg_heights

