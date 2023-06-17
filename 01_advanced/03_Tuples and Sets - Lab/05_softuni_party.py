guest_number = int(input())

guest_list = set()

for _ in range(guest_number):
    guest_list.add(input())

guest_arriving = input()
while guest_arriving != "END":
    if guest_arriving in guest_list:
        guest_list.remove(guest_arriving)
    guest_arriving = input()

print(len(guest_list))
for guest in sorted(guest_list):
    print(guest)