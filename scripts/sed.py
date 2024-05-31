import sys


def replace_in_file(file_path, search_text, replace_text):
    with open(file_path, "r", encoding="utf-8") as file:
        file_data = file.read()

    new_data = file_data.replace(search_text, replace_text)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(new_data)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python replace.py <file_path> <search_text> <replace_text>")
        sys.exit(1)

    file_path = sys.argv[1]
    search_text = sys.argv[2]
    replace_text = sys.argv[3]

    replace_in_file(file_path, search_text, replace_text)
    print(f"Write in {file_path}")
