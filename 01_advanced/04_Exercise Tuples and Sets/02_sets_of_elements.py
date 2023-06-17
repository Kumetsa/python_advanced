n, m = input().split()

n_set = set()
m_set = set()

for _ in range(int(n)):
    n_set.add(input())

for _ in range(int(m)):
    m_set.add(input())

unique_elements = n_set.intersection(m_set)

print(*unique_elements, sep="\n")
