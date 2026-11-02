import csv

try:
    with open("hubs.csv", "r") as f:
        rows = list(csv.DictReader(f))
except FileNotFoundError:
    print("hubs.csv not found")
    rows = []

total = 0
passed = 0

for row in rows:
    score = int(row["score"])
    total += score

    if score >= 50:
        passed += 1

failed = len(rows) - passed

if rows:
    average = round(total / len(rows), 1)
else:
    average = 0

with open("report.txt", "w") as f:
    f.write("LEARNER REPORT\n")
    f.write("Total learners: " + str(len(rows)) + "\n")
    f.write("Passed: " + str(passed) + "\n")
    f.write("Failed: " + str(failed) + "\n")
    f.write("Average score: " + str(average) + "\n")

print("Report written to report.txt")