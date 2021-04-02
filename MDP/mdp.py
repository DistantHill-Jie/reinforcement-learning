import csv
import sys

Transitions = {}
Reward = {}

# gamma is the discount factor
if len(sys.argv) > 1:
    gamma = float(sys.argv[1])
else:
     gamma = 0.9

# the maximum error allowed in the utility of any state
if len(sys.argv) > 2:
    epsilon = float(sys.argv[2])
else:
    epsilon = 0.001


def read_file():
    with open('data/transitions.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        for row in reader:
            print(row[0])
        return

        print(reader)


read_file()
       