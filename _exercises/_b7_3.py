
def decode(encoded, l):
    output = ""
    for i in range(0, len(l)):
        if l[i] == 1:
            output += encoded[i]
    return output


def sort_set(theset):
    return sorted(theset, key=lambda x: x[-1])


def reverse_dict(d):
    output = {}
    for key in d.keys():
        val = d[key]
        if val in output.keys():
            output[val] += key
        else:
            output[val] = key
    return output


if __name__ == "__main__":
    # print(decode("zzfaeliciztaricc", [0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1,1, 0, 0]))
    # print(sort_set({"ai", "picat~~~", "nu", "trecut"}))
    print(reverse_dict({1: "a", 2: "b", 3: "a"}))
