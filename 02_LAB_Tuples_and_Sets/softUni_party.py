number_of_guests = int(input())

codes = set()

for x in range(number_of_guests):
    guests = input()
    codes.add(guests)

guest_come = input()
while guest_come != 'END':
    if guest_come in codes:
        codes.remove(guest_come)
    guest_come = input()

print(len(codes))
for g in sorted(codes):
    print(g)