def team_lineup(*players_information):
    football_team = {}
    for info in players_information:
        player_name = info[0]
        player_country = info[1]

        if player_country not in football_team:
            football_team[player_country] = [player_name]
        else:
            football_team[player_country].append(player_name)

    sorted_countries = dict(sorted(football_team.items(), key=lambda x: (-len(x[1]), (x[0]))))

    result = ''
    for country, player_names in sorted_countries.items():
        result += f'{country}:\n'

        for player in player_names:
            result += f"  -{player}\n"

    return result.strip()


print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))



