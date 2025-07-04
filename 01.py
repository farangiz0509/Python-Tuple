people : list[tuple[str, int]] = [("Ali", 24), ("Laylo", 30), ("Jasur", 19)]

oldest_one = people[0]
for person in people:
    if person[1] > oldest_one[1]:
        oldest_one = person

print(oldest_one)