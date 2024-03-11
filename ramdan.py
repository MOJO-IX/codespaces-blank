import csv 

with open ("ramdan.csv", "r") as file:
    reader = csv.DictReader(file)   
    counts = {}

    for row in reader :
        favorite = row["favorite"]
        if favorite in count:
            counts [favorite] += 1
        else:
            counts[favorite] = 1

for favorite in sorted(counts, key=counts.get, reverse=True):
    print(f"{favorite}: {counts[favorite]}")
