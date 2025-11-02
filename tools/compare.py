import os
import csv

if input("Use default path for old TP and FP files? y/n: ") == "y":
    oldFalse = os.path.join("..", "src", "devs", "old",
                            "old_1k_devs_similarity_t=7.csv-falsepositive.csv")
    oldTrue = os.path.join("..", "src", "devs", "old",
                           "old_1k_devs_similarity_t=7.csv-truepositive.csv")
else:
    oldFalse = ""
    while not os.path.exists(oldFalse):
        oldFalse = os.path.normpath(input("Path to old false positive file: "))
    oldTrue = ""
    while not os.path.exists(oldTrue):
        oldTrue = os.path.normpath(input("Path to old true positive file: "))

if input("Use default path for new TP and FP files? y/n: ") == "y":
    newFalse = os.path.join("inspect-output",
                            "devs_similarity-falsepositive.csv")
    newTrue = os.path.join("inspect-output",
                           "devs_similarity-truepositive.csv")
else:
    newFalse = ""
    while not os.path.exists(newFalse):
        newFalse = os.path.normpath(input("Path to new false positive file: "))
    newTrue = ""
    while not os.path.exists(newTrue):
        newTrue = os.path.normpath(input("Path to new true positive file: "))

os.makedirs("compare-results", exist_ok=True)

afName = os.path.join(
    "compare-results", f"{os.path.splitext(os.path.basename(newFalse))[0]}-addedFPs.csv")
rfName = os.path.join(
    "compare-results", f"{os.path.splitext(os.path.basename(newFalse))[0]}-removedFPs.csv")
atName = os.path.join(
    "compare-results", f"{os.path.splitext(os.path.basename(newTrue))[0]}-addedTPs.csv")
rtName = os.path.join(
    "compare-results", f"{os.path.splitext(os.path.basename(newTrue))[0]}-removedTPs.csv")


def get_pairs(positive_list, positive_file):
    with open(positive_file, 'r', encoding='utf-8') as raw_file:
        file = csv.reader(raw_file)
        for row in file:
            found = False
            for x in positive_list:
                for y in x:
                    if any(row[:2] == y[i:i+2] or row[2:4] == y[i:i+2] for i in range(len(y)-1)):
                        x.append(row[:4])
                        found = True
                        break
                if found:
                    break
            if not found:
                positive_list.append([row[:4]])
    for i in range(len(positive_list)):
        for j in range(i + 1, len(positive_list)):
            list1 = positive_list[i]
            list2 = positive_list[j]
            common_pairs = [pair for pair in list1 if pair in list2]
            if common_pairs:
                positive_list[i] = list1 + list2
                positive_list[j] = []
    positive_list = [lst for lst in positive_list if lst]


new_tp = []
new_fp = []
old_tp = []
old_fp = []

get_pairs(new_tp, newTrue)
get_pairs(new_fp, newFalse)
get_pairs(old_tp, oldTrue)
get_pairs(old_fp, oldFalse)


def compare_lists(list1, list2):
    diff = []
    for pair_list in list1:
        found = False
        for pair in pair_list:
            for pair_list2 in list2:
                for pair2 in pair_list2:
                    if any(pair[:2] == pair2[i:i+2] or pair[2:4] == pair2[i:i+2] for i in range(len(pair2)-1)):
                        found = True
                        break
                if found:
                    break
            if found:
                break
            diff += [pair]
    return diff


added_tp = []
added_fp = []
removed_tp = []
removed_fp = []

added_tp = compare_lists(new_tp, old_tp)
added_fp = compare_lists(new_fp, old_fp)
removed_tp = compare_lists(old_tp, new_tp)
removed_fp = compare_lists(old_fp, new_fp)


def write_file(positive, name):
    with open(name, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in positive:
            writer.writerow(row)


write_file(added_tp, atName)
write_file(added_fp, afName)
write_file(removed_tp, rtName)
write_file(removed_fp, rfName)

print(f"Added True Positives: {len(added_tp)}")
print(f"Added False Positives: {len(added_fp)}")
print(f"Removed True Positives: {len(removed_tp)}")
print(f"Removed False Positives: {len(removed_fp)}")
