text = input()
try:
    times_to_repeat = int(input())
    print(text * times_to_repeat)
except ValueError:
    print(f"Variable times must be an integer")

