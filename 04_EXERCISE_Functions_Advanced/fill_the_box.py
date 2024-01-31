def fill_the_box(height, length, wight, *cubes):
    box_size = height * length * wight
    quantity_of_cubes = 0

    for cube in cubes:
        try:
            quantity_of_cubes += cube
        except TypeError:
            break

    if box_size > quantity_of_cubes:
        return f"There is free space in the box. You could put {box_size - quantity_of_cubes} more cubes."
    else:
        return f"No more free space! You have {quantity_of_cubes - box_size} more cubes."


print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
