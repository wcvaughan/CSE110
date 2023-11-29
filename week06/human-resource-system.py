# Download the file and save it to your computer. 

# In VS Code, open the folder that contains this 

# file. Then, create a new Python script in that folder.

# Have your program open the HR System file, read through

# it line by line, and at this point, simply display the line to the screen.

# Split the line into parts and change your display,

# so that it shows only the names (instead of the whole line).

# For each line, get the name and the job title for each

# person, and display those to the screen.

with open("week06\hr_system.txt") as hr_data:
    for line in hr_data:
        line = line.strip()
        line = line.split()
        name = line[0]
        id_number = int(line[1])
        job_title = line[2]
        salary = float(line[3])
        print(f'Name: {name}, (ID: {id_number}), Title: {job_title} - ${salary:.2f} ')


# Strip off any leading and trailing whitespace from each line.

# In addition to the name and the job title, also access the salary

# and the ID number and save them into variables. Display all 

# four values in this format: name (ID: id_number), job_title - 

# $salary. Don't forget to convert the salary to a number and 

# display it with two decimals.

# The following shows the first few lines of expected output at this point.

# Instead of displaying the salary information, calculate and 

# display a paycheck amount for the employee. Assume that they are paid twice a month.

# Change the program so that it generates bonuses for anyone 

# who is an engineer. For each of these employees, add $1000 to their paycheck amount.

with open("week06\hr_system.txt") as hr_data:
    for line in hr_data:
        line = line.strip()
        line = line.split()
        name = line[0]
        id_number = int(line[1])
        job_title = line[2]
        salary = float(line[3])
        biweekly_salary = salary / 24
        if job_title.upper() == "ENGINEER":
            biweekly_salary += 1000 
        print(f'Name: {name}, (ID: {id_number}), Title: {job_title} - ${biweekly_salary:.2f} ')
