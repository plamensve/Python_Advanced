from collections import deque

textiles = deque([int(t) for t in input().split()])
medicament = deque([int(m) for m in input().split()])

items_build = {
    'Patch': [30, 0],
    'Bandage': [40, 0],
    'MedKit': [100, 0]
}

created_item = False
while True:
    if not textiles:
        break
    if not medicament:
        break
    current_textiles = textiles.popleft()
    current_medicament = medicament.pop()

    result = current_textiles + current_medicament
    for item, resource in items_build.items():
        if result == resource[0]:
            resource[1] += 1
            created_item = True

    if not created_item and result > 100:
        diff = result - items_build['MedKit'][0]
        items_build['MedKit'][1] += 1
        medicament[-1] += diff

    elif not created_item and result < 100:
        current_medicament += 10
        medicament.append(current_medicament)
    created_item = False

if not textiles and not medicament:
    print(f"Textiles and medicaments are both empty.")
else:
    if not textiles:
        print(f"Textiles are empty.")
    if not medicament:
        print(f"Medicaments are empty.")

new_dict = {}
for k, v in items_build.items():
    new_dict[k] = v[1]

sorted_new_dict = sorted(new_dict.items(), key=lambda x: (-x[1], x[0]))
for k, v in sorted_new_dict:
    if v > 0:
        print(f"{k} - {v}")

if textiles:
    print(f"Textiles left: {', '.join(str(y) for y in textiles)}")
if medicament:
    medicament.reverse()
    print(f"Medicaments left: {', '.join(str(y) for y in medicament)}")

# SOLUTION 2

# from collections import deque
#
# textiles = deque([int(t) for t in input().split()])
# medicament = deque([int(m) for m in input().split()])
#
#
# items_build = {
#     'Patch': 0,
#     'Bandage': 0,
#     'MedKit': 0,
# }
#
# created_item = False
# while True:
#     if not textiles:
#         break
#     if not medicament:
#         break
#     current_textiles = textiles.popleft()
#     current_medicament = medicament.pop()
#     result = current_textiles + current_medicament
#     if result == 30:
#         items_build['Patch'] += 1
#     elif result == 40:
#         items_build['Bandage'] += 1
#     elif result == 100:
#         items_build['MedKit'] += 1
#     else:
#         if result > 100:
#             items_build['MedKit'] += 1
#             diff = result - 100
#             medicament[-1] += diff
#         elif result < 100:
#             medicament.append(current_medicament + 10)
#
# if not textiles and not medicament:
#     print(f"Textiles and medicaments are both empty.")
# else:
#     if not textiles:
#         print(f"Textiles are empty.")
#     if not medicament:
#         print(f"Medicaments are empty.")
#
#
# sorted_new_dict = sorted(items_build.items(), key=lambda x: (-x[1], x[0]))
# for k, v in sorted_new_dict:
#     if v > 0:
#         print(f"{k} - {v}")
#
#
# if textiles:
#     print(f"Textiles left: {', '.join(str(y) for y in textiles)}")
# if medicament:
#     medicament.reverse()
#     print(f"Medicaments left: {', '.join(str(y) for y in medicament)}")