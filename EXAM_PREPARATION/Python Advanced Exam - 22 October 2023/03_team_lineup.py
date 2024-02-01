def team_lineup(*args):
    # Count the number of players per country
    country_count = {}

    # Iterate through the input.txt arguments and count players per country
    for player, country in args:
        if country not in country_count:
            country_count[country] = []

        country_count[country].append(player)

    # Sort the countries by the number of players (descending) and then by country name length
    sorted_countries = dict(sorted(country_count.items(), key=lambda x: (-len(x[1]), (x[0]))))

    # Generate the output.txt
    result = ''
    for country, player_names in sorted_countries.items():
        result += f'{country}:\n'

        for player in player_names:
            result += f"  -{player}\n"

    return result.strip()


# print(team_lineup(
#     ("Harry Kane", "England"),
#     ("Manuel Neuer", "Germany"),
#     ("Raheem Sterling", "England"),
#     ("Toni Kroos", "Germany"),
#     ("Cristiano Ronaldo", "Portugal"),
#     ("Thomas Muller", "Germany")))


# print(team_lineup(
#    ("Lionel Messi", "Argentina"),
#    ("Neymar", "Brazil"),
#    ("Cristiano Ronaldo", "Portugal"),
#    ("Harry Kane", "England"),
#    ("Kylian Mbappe", "France"),
#    ("Raheem Sterling", "England")))


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

