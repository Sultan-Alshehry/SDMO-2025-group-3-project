import os

oldFalse = ""
while not os.path.exists(oldFalse):
    oldFalse = input("Path to old false positive file: ")
oldTrue = ""
while not os.path.exists(oldTrue):
    oldTrue = input("Path to old true positive file: ")
newFalse = ""
while not os.path.exists(newFalse):
    newFalse = input("Path to new fale positive file: ")
newTrue = ""
while not os.path.exists(newTrue):
    newTrue = input("Path to new true positive file: ")

afName = f"compare-results/{os.path.basename(newFalse)}-addedFPs"
rfName = f"compare-results/{os.path.basename(newFalse)}-removedFPs"
atName = f"compare-results/{os.path.basename(newTrue)}-addedTPs"
rtName = f"compare-results/{os.path.basename(newTrue)}-removedTPs"

addedFP = []
addedTP = []
removedFP = []
removedTP = []

with open(oldFalse, "r") as of, open(newFalse, "r") as nf:
    nfLines = set(line.strip() for line in nf)
    ofLines = set(line.strip() for line in of)
    removedFP.append(ofLines - nfLines)
    addedFP.append(nfLines - ofLines)
with open(oldTrue, "r") as ot, open(newTrue, "r") as nt:
    ntLines = set(line.strip() for line in nt)
    otLines = set(line.strip() for line in ot)
    removedFP.append(otLines - ntLines)
    addedFP.append(ntLines - otLines)

with open(afName, "w") as af:
    for line in addedFP:
        af.write(line + "\n")
with open(rfName, "w") as rf:
    for line in removedFP:
        rf.write(line + "\n")
with open(atName, "w") as at:
    for line in addedTP:
        at.write(line + "\n")
with open(rtName, "w") as rt:
    for line in removedTP:
        rt.write(line + "\n")

print(f"Added TPs: {len(addedTP)}")
print(f"Removed TPs: {len(removedTP)}")
print(f"Added FPs: {len(addedFP)}")
print(f"Removed FPs: {len(removedFP)}")
