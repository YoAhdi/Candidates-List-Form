import csv

Candidates = [
    {"Firstname": "John", "Lastname": "Doe", "Skillset": "SAP", "Email": "Johndoe@yourmail.com"},
    {"Firstname": "James", "Lastname": "Lan", "Skillset": "Python", "Email": "James@yourmail.com"},
    {"Firstname": "Larry", "Lastname": "Blan", "Skillset": "C++", "Email": "Larry@yourmail.com"}
]

with open("candidates.csv", mode="w") as csvfile:
    fieldnames = ["Firstname", "Lastname", "Skillset", "Email"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in Candidates:
        writer.writerow(row)

