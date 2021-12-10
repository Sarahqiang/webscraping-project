import argparse
from pathlib import Path

import requests
import json
import os,sys
parser = argparse.ArgumentParser()
parser.add_argument('-s','--input')
parser.add_argument('-o','--output')
args = parser.parse_args()
limit = 100
list ='new'
def main():
        subreddit = args.input
        outputfile = args.output
        base_url = f'https://www.reddit.com/{subreddit}/{list}.json?limit={limit}'
        request = requests.get(base_url,headers = {'User-agent': 'your bot 0.1'})
        post =request.json()
        data = post['data']['children']
        for datas in data:
            with open(outputfile, 'a', encoding='utf-8') as f:
                parentdir = Path(__file__).resolve().parents[1]
                if(os.path.isdir(parentdir)==False):
                    os.mkdir(parentdir)
                json.dump(datas, f)
                f.write('\n')
if __name__ =='__main__':
        main()