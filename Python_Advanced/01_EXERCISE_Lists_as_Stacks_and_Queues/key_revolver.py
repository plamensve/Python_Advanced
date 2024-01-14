from collections import deque

bullet_price = int(input())
size_of_gun_barrel = int(input())
bullets = deque([int(bullet) for bullet in input().split()])
locks = deque([int(locks) for locks in input().split()])
value_of_the_intelligence = int(input())

shot_counter = 0
bullets_waste = 0
bullets_cost = 0
while True:

    if not bullets or not locks:
        break

    current_bullets = bullets.pop()
    current_locks = locks.popleft()

    if current_locks >= current_bullets:
        print('Bang!')
        bullets_waste += current_bullets
        shot_counter += 1
        bullets_cost += bullet_price
    else:
        print('Ping!')
        bullets_waste += current_bullets
        shot_counter += 1
        bullets_cost += bullet_price
        locks.appendleft(current_locks)

    if shot_counter == size_of_gun_barrel:
        if bullets:
            print('Reloading!')
            shot_counter = 0
        else:
            break

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${value_of_the_intelligence - bullets_cost}")
