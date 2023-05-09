import csv

# Open the CSV file for writing
with open('filename.csv', 'w', newline='') as file:
    # Create a writer object
    writer = csv.writer(file)

    # Write a row to the CSV file
    writer.writerow(['Name', 'Age', 'City'])

    # Write multiple rows to the CSV file
    writer.writerows([
        ['John', '25', 'New York'],
        ['Jane', '30', 'Los Angeles'],
        ['Bob', '35', 'Chicago']
    ])
