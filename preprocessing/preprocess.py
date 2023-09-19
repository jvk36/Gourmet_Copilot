import csv

source = "RAW_recipes.csv"
output = "training.txt"

def main():
    with open(source, newline='') as csvfile:
        r = csv.reader(csvfile)
        with open("training.txt", 'w') as f:
            next(r)
            for row in r:
                f.write("[" + row[0] + "]\n")
                f.write(row[10].replace("'", "") + "\n")
                f.write("\n")
                steps = row[8].lstrip("['").rstrip("']").split("', '")
                for step in steps:
                    f.write(step + '\n')
                f.write('\n\n')

if __name__ == '__main__':
    main()
