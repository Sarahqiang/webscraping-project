import os,sys
import re
from pathlib import Path
import  hashlib
import  json
import wget
import bs4


def get_data(file):


    #config_json ="/Users/yaoqiangwu/Desktop/hw6/submission_template/src/config-file.json"
    with open(file,"r") as f:
         parentdir = Path(__file__).resolve().parents[1]
         jsondata =json.load(f)
         names = jsondata["target_people"]
         path = jsondata["cache_dir"]
         cachedir = os.path.join(parentdir,path)
         if (os.path.isdir(cachedir)==False) :
            os.mkdir(cachedir)
         dict = {}
         for name in names:
             hashname = hashlib.sha1(name.encode("UTF-8")).hexdigest()
             namefilepath =os.path.join(cachedir+'/'+hashname)
             url = f'https://www.whosdatedwho.com/dating/{name}'
             if(os.path.isfile(namefilepath) == False):
                 wget.download(url,out=namefilepath)
             soup = bs4.BeautifulSoup(open(namefilepath,'r'),'html.parser')
             #table = soup.find_all(id="ff-dating-history-table")
             table =soup.find_all('table')
             fact=table[3].find_all('a')
             relations = []

             for i in fact:
                 if(i == fact[0]):
                     continue
                 relations.append(i.getText())
                 dict[name]=relations

         #print(dict)
         outputfile =sys.argv[4]
         with open(outputfile,'w')as r:
             result=json.dumps(dict,indent=4)
             r.write(result)









def main():
    config_json = sys.argv[2]
    parentdir = Path(__file__).parents[0]
    get_data(config_json)


if __name__ == '__main__':
    main()

