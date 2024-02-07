def forecast(*info):
    weather = {}
    for city, forecast_for_city in info:
        mapper = {
            'Sunny': 1,
            'Cloudy': 2,
            'Rainy': 3,
        }
        weather[city] = forecast_for_city, mapper[forecast_for_city]
    sorted_weather = sorted(weather.items(), key=lambda x: (x[1][1], x[0]))
    weather_list = []
    for k, v in sorted_weather:
        weather_list.append(f'{k} - {v[0]}')

    return '\n'.join(map(str, weather_list))


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))


