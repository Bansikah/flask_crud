import csv

# Define the data to be written to the CSV file
data = [
    {'ID': 1, 'TITLE': 'The Great Gatsby', 'AUTHOR': 'F. Scott Fitzgerald', 'YEAR': 1925},
    {'ID': 2, 'TITLE': 'To Kill a Mockingbird', 'AUTHOR': 'Harper Lee', 'YEAR': 1960},
    {'ID': 3, 'TITLE': '1984', 'AUTHOR': 'George Orwell', 'YEAR': 1949},
    {'ID': 4, 'TITLE': 'Pride and Prejudice', 'AUTHOR': 'Jane Austen', 'YEAR': 1813},
    {'ID': 5, 'TITLE': 'The Catcher in the Rye', 'AUTHOR': 'J.D. Salinger', 'YEAR': 1951}
]

# Open the CSV file for writing
with open('data.csv', 'w', newline='') as csvfile:
    # Define the fieldnames for the CSV file
    fieldnames = ['ID', 'TITLE', 'AUTHOR', 'YEAR']
    
    # Create a CSV writer object
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Write the header row to the CSV file
    writer.writeheader()
    
    # Write the data to the CSV file
    for row in data:
        writer.writerow(row)