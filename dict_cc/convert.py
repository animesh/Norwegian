import sys
import pandas as pd

def read_csv(file_name):
    for chunk in pd.read_csv(file_name, skiprows=8, chunksize=10, delimiter='\t', header=None, encoding='utf-8', usecols=[0, 1]):
        yield chunk


if len(sys.argv) < 3:
    print("Missing arguments")
    exit(22)

#empty file
open(sys.argv[2], 'w').close()

index = 0
for df in read_csv(sys.argv[1] ):
    df.to_csv(sys.argv[2], mode="a", header=None, index=False)

print("finished")