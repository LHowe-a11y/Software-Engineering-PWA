import csv
i = -1
with open("myPWA/.database/FormattedDates.txt", 'w') as w:
    with open("myPWA/.database/australian_public_holidays_2025.csv", newline='') as f:
        for row in csv.reader(f):
            i += 1
            if i == 0:
                continue
            w.write('(')
            for x in row:
                w.write('"'+x+'",')
            w.write(str(i))
            w.write('),'+'\n')