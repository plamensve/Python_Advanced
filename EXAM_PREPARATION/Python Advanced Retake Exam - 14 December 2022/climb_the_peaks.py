from collections import deque

food = deque([int(x) for x in input().split(', ')])
stamina = deque([int(y) for y in input().split(', ')])

all_peaks = deque([
    ("Vihren", 80),
    ("Kutelo", 90),
    ("Banski Suhodol", 100),
    ("Polezhan", 60),
    ("Kamenitza", 70)
])

days = 1
peaks_conquered = []
while True:
    if len(peaks_conquered) == 5:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        break
    if days > 7 or not food or not stamina:
        print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
        break

    curr_food = food.pop()
    curr_stamina = stamina.popleft()
    result = curr_food + curr_stamina

    next_peak = all_peaks.popleft()
    if result >= next_peak[1]:
        days += 1
        peaks_conquered.append(next_peak[0])
    else:
        days += 1
        all_peaks.appendleft(next_peak)

if peaks_conquered:
    print("Conquered peaks:")
    for peak in peaks_conquered:
        print(peak)