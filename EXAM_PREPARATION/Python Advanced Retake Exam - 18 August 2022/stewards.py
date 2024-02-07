from collections import deque

seats = deque([str(s) for s in input().split(', ')])
match_a = deque([int(a) for a in input().split(', ')])
match_b = deque([int(b) for b in input().split(', ')])
taken_seats = []
rotations = 0
while True:
    if len(taken_seats) == 3:
        break
    if rotations == 10:
        break

    a_num = match_a.popleft()
    b_num = match_b.pop()
    sum_of_a_and_b = chr(a_num + b_num)
    first_seat = str(f'{a_num}{sum_of_a_and_b}')
    second_seat = str(f'{b_num}{sum_of_a_and_b}')

    if first_seat in seats:
        if first_seat not in taken_seats:
            taken_seats.append(first_seat)

    if second_seat in seats:
        if second_seat not in taken_seats:
            taken_seats.append(second_seat)

    if not first_seat in seats and not second_seat in seats:
        match_a.append(a_num)
        match_b.appendleft(b_num)
    rotations += 1

print(f"Seat matches: {(', '.join(map(str, taken_seats)))}")
print(f"Rotations count: {rotations}")