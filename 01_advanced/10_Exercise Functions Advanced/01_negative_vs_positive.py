def print_numbers(pos_num, neg_num):
    print(neg_num)
    print(pos_num)
    if pos_num > abs(neg_num):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


numbers = [int(el) for el in input().split()]
positive = sum(x for x in numbers if x > 0)
negative = sum(x for x in numbers if x < 0)

print_numbers(positive, negative)
