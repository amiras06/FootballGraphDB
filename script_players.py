import csv

input_file = '/Users/saidamira/Downloads/data/players.csv' #your players data path
output_file = '/Users/saidamira/Downloads/data/players_cleaned.csv'

columns_to_keep = [0, 3, 7, 10, 5, 12, 21, 22]

with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    header = next(reader)
    writer.writerow([header[i] for i in columns_to_keep])

    for row in reader:
        writer.writerow([row[i] for i in columns_to_keep])

print(f"Fichier nettoyé généré : {output_file}")
