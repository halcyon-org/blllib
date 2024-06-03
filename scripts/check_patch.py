import sys

args = sys.argv


def check_patch(ver1, ver2):
    [major1, minor1, patch1] = ver1.split(".")
    [major2, minor2, patch2] = ver2.split(".")
    return major1 == major2 and minor1 == minor2


if __name__ == "__main__":
    check = check_patch(args[1], args[2])
    print("true" if check else "false")
