import argparse
import csv

if __name__ == "__main__":
    parser = argparse.ArgumentParser('Input source molecule')
    parser.add_argument('-name', type=str)
    parser.add_argument('-inchi', type=str)
    parser.add_argument('-sourceFile', type=str)
    params = parser.parse_args()
    with open(params.sourceFile, 'w') as fi:
        csv_writer = csv.writer(fi, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['Name', 'InChI'])
        csv_writer.writerow([params.name, params.inchi])
