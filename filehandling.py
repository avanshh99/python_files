import os

def create_file(file_name):
    with open(file_name, 'w') as file:
        print(f"File '{file_name}' created successfully.")

def write_to_file(file_name, content):
    with open(file_name, 'w') as f:
        f.write(content)
        print(f"Content written to '{file_name}' successfully.")

def read_file(file_name):
    with open(file_name, 'r') as file:
        file.read()
        print(f"Reading then Content of '{file_name}':")
        print(content)

def append_to_file(file_name, content):
    with open(file_name, 'a') as file:
        file.write(content)
        print(f"Content appended to '{file_name}' successfully.")

def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"File '{file_name}' deleted successfully.")
    else:
        print(f"File '{file_name}' does not exist.")

# Example usage
file_name = 'example.txt'
# create_file(file_name)

content = "Hello, welcome to py.\n"
# write_to_file(file_name, content)
content='appended content added'
append_to_file(file_name,content)
# delete_file(file_name)

# read_file(file_name)