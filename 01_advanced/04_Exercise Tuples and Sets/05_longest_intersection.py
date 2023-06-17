longest_inter = set()

for _ in range(int(input())):
    first_range, second_range = input().split("-")
    first_range_start, first_range_end = map(int, first_range.split(","))
    second_range_start, second_range_end = map(int, second_range.split(","))

    current_inter = set(range(first_range_start,first_range_end + 1)).intersection(range(second_range_start,second_range_end + 1))
    if len(current_inter) > len(longest_inter):
        longest_inter = current_inter

print(f"Longest intersection is {list(longest_inter)} with length {len(longest_inter)}")

