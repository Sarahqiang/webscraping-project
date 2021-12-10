import argparse
import os, sys
from pathlib import Path

import pandas as pd
import json





def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')

    args = parser.parse_args()
    inputfile = args.input

    dict = []
    df = pd.read_csv(inputfile, sep='\t', header=0, index_col=False)
    c = df.loc[df.coding == 'c', 'coding'].count()
    f = df.loc[df.coding == 'f', 'coding'].count()
    r = df.loc[df.coding == 'r', 'coding'].count()
    o = df.loc[df.coding == 'o', 'coding'].count()
    dict = {}
    dict['course-related'] = str(c)
    dict['food-related'] = str(f)
    dict['residence-related'] = str(r)
    dict['other'] = str(o)

    print(json.dumps(dict,indent=2))



if __name__ == '__main__':
    main()
