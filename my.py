#import pandas
import csv
with open('bball40.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row

