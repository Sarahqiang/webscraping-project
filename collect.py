import requests
import json
subreddit1 =['funny','AskReddit','gaming','aww','pics','Music','science','worldnews','videos','todayilearned']
subreddit2=['AskReddit','memes','politics','nfl','nba','wallstreetbets','teenagers','PublicFreakout','leagueoflegends','unpopularopinion']
limit = 100
list ='new'
def main():
    #data =[]
    for tag in subreddit1:
        base_url = f'https://www.reddit.com/r/{tag}/{list}.json?limit={limit}'
        request = requests.get(base_url,headers = {'User-agent': 'your bot 0.1'})
        post =request.json()
        data = post['data']['children']

        for datas in data:
            with open("../sample1.json", 'a', encoding='utf-8') as f:
                #print(datas['data']['title'])
                json.dump(datas,f)
                f.write('\n')

    for tag in subreddit2:
            base_url = f'https://www.reddit.com/r/{tag}/{list}.json?limit={limit}'
            request2 = requests.get(base_url, headers={'User-agent': 'your bot 0.1'})
            post2 = request2.json()
            data2 = post2['data']['children']
            for datas2 in data2:
                with open("../sample2.json", 'a', encoding='utf-8') as f:
                    #print(datas['data']['title'])
                    json.dump(datas2, f)
                    f.write('\n')

if __name__ =='__main__':
        main()