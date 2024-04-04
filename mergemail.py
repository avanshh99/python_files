import os


with open('mail1.txt') as f1, open('mail2.txt') as f2:
    # Read the contents of each file using read() method
    # f1.write("This is file 1")
    mail1_content = f1.read()
    # f1.write("This is file 2")
    mail2_content = f2.read()
    # Combining the contents of both mail files with a delimiter 
    merged_mail = mail1_content + mail2_content

# Write the merged content to a new file
with open('new_mail.txt', 'w') as f:
    f.write(merged_mail)
