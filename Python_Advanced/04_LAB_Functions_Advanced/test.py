def some_func(**kwargs):
    for k, v in kwargs.items():
        print(f"This is {v} from {v} and he is {v} years old")


some_func(name="Plamen", town='Byala', age=34)