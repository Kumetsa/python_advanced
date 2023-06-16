from collections import deque

seats = input().split(", ")

sequence_one = deque(map(int, input().split(", ")))
sequence_two = deque(map(int, input().split(", ")))

available_seats = {}

matched_seats = []

rotations = 0

for seat in seats:
    current_letter = seat[-1]
    current_number = seat[:-1]
    if current_letter not in available_seats:
        available_seats[current_letter] = []
    available_seats[current_letter].append(int(current_number))


while sequence_one and sequence_two and rotations < 10 and len(matched_seats) < 3:
    first_num = sequence_one.popleft()
    second_num = sequence_two.pop()

    rotations += 1

    ascii_char = chr(first_num+second_num)
    if ascii_char in available_seats:
        for num in available_seats[ascii_char]:
            if first_num == num:
                matched_seats.append(''.join(str(first_num)+ascii_char))
                available_seats[ascii_char].remove(num)

            elif second_num == num:
                matched_seats.append(''.join(str(second_num)+ascii_char))
                available_seats[ascii_char].remove(num)

    else:
        sequence_one.append(first_num)
        sequence_two.appendleft(second_num)


print(f"Seat matches: {', '.join(matched_seats  )}")
print(f"Rotations count: {rotations}")
