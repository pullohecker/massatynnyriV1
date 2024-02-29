import os
import argparse

parser = argparse.ArgumentParser("simple_example")
parser.add_argument("arg1", help="Polku tiedostoon, jossa on lista kohteista", type=str)
args = parser.parse_args()
tied = args.arg1

file1 = open(tied, 'r')
Lines = file1.readlines()
komento = "./hiisi.sh"

for i in range(len(Lines)):
    komento = komento + " " + str(Lines[i]).strip()

print(komento)
os.system(komento)
