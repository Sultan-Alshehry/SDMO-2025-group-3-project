import os

filePath = ""
while os.path.exists(filePath) is False:
    filePath = input("Path to .csv file: ")
    fileName = os.path.basename(filePath)
    fileName = os.path.splitext(filePath)[0]
while True:
    lineCount = input("how many lines do you want to read? \
        press enter to read every line: ")

    if lineCount == "":
        break

    try:
        lineCount = int(lineCount)
        break

    except ValueError:
        print("invalid value, try again")

trueoutput = f"inspect-output/{fileName}-truepositive.csv"
falseoutput = f"inspect-output/{fileName}-falsepositive.csv"

tp = 0
fp = 0

os.makedirs(os.path.dirname(trueoutput), exist_ok=True)
os.makedirs(os.path.dirname(falseoutput), exist_ok=True)

with open(filePath, 'r') as file:
    fileLines = sum(1 for _ in file)

with open(filePath, "r") as file, \
        open(trueoutput, "w") as truefile, \
        open(falseoutput, "w") as falsefile:

    format = file.readline()
    count = 0

    for line in file:
        if lineCount != "" and count >= lineCount:
            break

        status = ""
        values = line.strip().split(',')
        if len(values[0]) > len(values[2]):
            nameWidth = len(values[0])
        else:
            nameWidth = len(values[2])
        if len(values[1]) > len(values[3]):
            emailWidth = len(values[1])
        else:
            emailWidth = len(values[3])
        while status != "t" and status != "f":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{fileLines} / {count}")
            print(f"{values[0]:<{nameWidth}}, {values[1]:<{emailWidth}}")
            print(f"{values[2]:<{nameWidth}}, {values[3]:<{emailWidth}}")
            status = input("t or f?")

        if status == "t":
            truefile.write(line)
            tp += 1

        else:
            falsefile.write(line)
            fp += 1

        count += 1

os.system('cls' if os.name == 'nt' else 'clear')

print(f"TPs: {tp}\nFPs: {fp}")
