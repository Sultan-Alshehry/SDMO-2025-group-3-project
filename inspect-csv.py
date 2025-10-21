import os

fileName = ""
while os.path.exists(fileName) is False:
    fileName = input("Path to .csv file: ")

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

trueoutput = "output-inspection/truepositive.csv"
falseoutput = "output-inspection/falsepositive.csv"

tp = 0
fp = 0

os.makedirs(os.path.dirname(trueoutput), exist_ok=True)
os.makedirs(os.path.dirname(falseoutput), exist_ok=True)

with open(fileName, "r") as file, \
        open(trueoutput, "w") as truefile, \
        open(falseoutput, "w") as falsefile:

    format = file.readline()
    count = 0

    for line in file:
        if lineCount != "" and count >= lineCount:
            break

        status = ""

        while status != "t" and status != "f":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(line)
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
