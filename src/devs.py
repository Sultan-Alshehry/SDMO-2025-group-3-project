import csv
import pandas as pd
import unicodedata
import string
from itertools import combinations
import os


def import_repository(repository_name):
    from pydriller import Repository
    DEVS = set()
    for commit in Repository(repository_name).traverse_commits():
        DEVS.add((commit.author.name, commit.author.email))
        DEVS.add((commit.committer.name, commit.committer.email))

    DEVS = sorted(DEVS)

    with open(os.path.join("devs", "devs.csv"), 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        writer.writerow(["name", "email"])
        writer.writerows(DEVS)


# This block of code reads an existing csv of developers

def read_developers(developers="1k_devs_similarity_t=7.csv"):
    DEVS = []
    # Read csv file with name,dev columns
    with open(os.path.join("devs", developers), 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            DEVS.append([cell.strip() for cell in row[:2]])
            DEVS.append([cell.strip() for cell in row[2:4]])
    # First element is header, skip
    DEVS = DEVS[1:]
    DEVS = sorted(list(set(tuple(dev) for dev in DEVS)))
    DEVS = [list(dev) for dev in DEVS]
    return DEVS


# Function for pre-processing each name,email
def process(dev):
    name: str = dev[0]

    # Remove punctuation
    trans = name.maketrans("", "", string.punctuation)
    name = name.translate(trans)
    # Remove accents, diacritics
    name = unicodedata.normalize('NFKD', name)
    name = ''.join([c for c in name if not unicodedata.combining(c)])
    # Lowercase
    name = name.casefold()
    # Strip whitespace
    name = " ".join(name.split())

    # Attempt to split name into firstname, lastname by space
    parts = name.split(" ")
    # Expected case
    if len(parts) == 2:
        first, last = parts
    # If there is no space, firstname is full name, lastname empty
    elif len(parts) == 1:
        first, last = name, ""
    # If there is more than 1 space, firstname is until first space,
    # rest is lastname
    else:
        first, last = parts[0], " ".join(parts[1:])

    # Take initials of firstname and lastname if they are long enough
    i_first = first[0] if len(first) > 1 else ""
    i_last = last[0] if len(last) > 1 else ""

    # Determine email prefix
    email: str = dev[1]
    prefix = email.split("@")[0]

    return name, first, last, i_first, i_last, email, prefix

# sultan's testing part ends here


# Compute similarity between all possible pairs


def compute_similarity(DEVS):
    SIMILARITY = []

    for dev_a, dev_b in combinations(DEVS, 2):
        # Pre-process both developers
        name_a, first_a, last_a, i_first_a, i_last_a, \
            email_a, prefix_a = process(dev_a)
        name_b, first_b, last_b, i_first_b, i_last_b, \
            email_b, prefix_b = process(dev_b)

        c1 = c2 = False

        # Conditions of Bird heuristic
        c1 = email_a == email_b

        if len(name_a) > 4 and len(name_b) > 4:
            c2 = name_a == name_b

        # Save similarity data for each conditions. Original names are saved
        SIMILARITY.append([dev_a[0], email_a, dev_b[0], email_b,
                          c1, c2])

    # Save data on all pairs (might be too big -> comment out to avoid)
    cols = ["name_1", "email_1", "name_2", "email_2", "c1", "c2"]
    df = pd.DataFrame(SIMILARITY, columns=cols)
    df = df.drop_duplicates()
    return df
    # df.to_csv(os.path.join("devs", "devs_similarity.csv"),
    #         index=False, header=True)


def save_csv(df):
    # Set similarity threshold, check c1-c3 against the threshold
    # Keep only rows where at least one condition is True
    df = df[df[["c1", "c2"]].any(axis=1)]

    # Omit "check" columns, save to csv
    df = df[["name_1", "email_1", "name_2", "email_2", "c1", "c2"]]
    df.to_csv(os.path.join("devs", "devs_similarity.csv"),
              index=False, header=True)


if __name__ == '__main__':
    repository_name = input("Repository URL: ")
    import_repository(repository_name)
    save_csv(compute_similarity(read_developers()))
