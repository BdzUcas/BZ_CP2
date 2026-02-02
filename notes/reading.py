import csv as csv


try:
    with open('notes/sample.csv', mode = 'r') as sample:
        reader = csv.reader(sample, delimiter='L')
        header = next(reader)
        header = header[0].split(',')
        for line in reader:
            line = line[0].split(',')
            user = {}
except:
    print('ERROR 404')
    while 404:
        print('Unexpected System Error. Please delete your PC')
else:
    print('done')