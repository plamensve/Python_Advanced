def team_lineup(*information):
    team = {}
    for name, country in information:
        if country not in team:
            team[country] = []
        team[country].append(name)

    sorted_by_number_of_players = sorted(team.items(), key=lambda s: (-len(s[1]), s[0]))
    result = ''
    for country, names in dict(sorted_by_number_of_players).items():
        result += f"{country}:\n"
        for player in names:
            result += f"  -{player}\n"

    return result.strip()


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))











