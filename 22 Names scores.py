""" Problem 22
Start: Sep/14/2021 9:00pm
Finished: Sep/14/2021 9:20pm
"""

txt = open("C:\\Users\\Ivan\\Documents\\.Programming\\Project Euler\\.resources\\22 names.txt", "r")
names = [name.strip("\"") for name in txt.read().split(",")]
txt.close()
names.sort()

# zip position of sort names and numerical score of names
name_ranks = zip(range(1,len(names)+1),[sum(map(lambda x: ord(x)-64,name)) for name in names])
name_scores = []
# multiply position and score
for rank, score in name_ranks:
    name_scores.append(rank*score)

print(f"Total Score of All Names Is: {sum(name_scores)}")