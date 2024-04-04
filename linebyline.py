def read(file_name):
    """Read a file line by line into a list."""
    lines = []
    with open(file_name, "r") as file:
        for line in file:
            lines.append(line.strip())  # Remove newline character before adding to the list
    return lines

def main():
    file_name = "py.txt"  # Change this to the name of your file
    lines = read(file_name)
    print("Contents of", file_name, "read into a list:")
    for line in lines:
        print(line)

if __name__ == "__main__":
    main()
