import string


with open("/Users/jslawitsky/Downloads/p022_names.txt", "r") as fp:
    names = []
    for line in fp.readlines():
        names += line.replace("\"", "").split(",")

    ALPHABET = {char: idx for idx, char in enumerate(string.ascii_uppercase, start=1)}
    names.sort()
    seen = {}
    summation = 0
    for idx, name in enumerate(names, start=1):
        if name in seen:
            val = seen[name]
        else:
            val = sum([ALPHABET[char] for char in name])
            seen[name] = val
        summation += val * idx

    print summation
