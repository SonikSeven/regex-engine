import sys


def compare_strings(regex, string, pattern):
    chars_match = regex[:1] in (string[:1], ".")
    if regex[:1] == "\\":
        regex = regex[1:]
        chars_match = regex[:1] == string[:1]
    if regex[1:2] == "?":
        if compare_strings(regex[2:], string, pattern):
            return compare_strings(regex[2:], string, pattern)
        elif chars_match:
            return compare_strings(regex[2:], string[1:], pattern)
    elif regex[1:2] == "*":
        if compare_strings(regex[2:], string, pattern):
            return compare_strings(regex[2:], string, pattern)
        elif string and chars_match:
            return compare_strings(regex, string[1:], pattern)
    elif regex[1:2] == "+":
        if not string or not chars_match:
            return False
        elif compare_strings(regex[2:], string[1:], pattern):
            return compare_strings(regex[2:], string[1:], pattern)
        else:
            return compare_strings(regex, string[1:], pattern)
    if not regex and (pattern[-1:] != "$" or not string):
        return True
    elif not string:
        return False
    elif chars_match:
        return compare_strings(regex[1:], string[1:], pattern)
    else:
        return False


def find_match(pattern, string):
    regex = "".join(pattern.rsplit("^", 1)).replace("$", "", 1)
    if compare_strings(regex, string, pattern):
        return True
    elif string[1:] and pattern[:1] != "^":
        return find_match(pattern, string[1:])
    else:
        return False


def main():
    sys.setrecursionlimit(10000)
    pattern, string = input().split("|")
    print(find_match(pattern, string))


if __name__ == "__main__":
    main()
