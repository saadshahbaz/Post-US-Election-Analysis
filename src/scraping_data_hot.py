import requests
import json
import argparse

def get_posts(subbreddits, outputfile):
    num_posts=34
    subbreddit = subbreddits


    data = requests.get(f'http://api.reddit.com/r/{subbreddit}/hot?limit={num_posts}', headers={'User-Agent': 'windows:requests (by /u/saadshahbaz)'})
    x = json.loads(data.content.decode('utf8'))



    with open(outputfile,"a") as f:
        for k in range(num_posts):
            lines= x['data']['children'][k]['data']
            f.write(json.dumps(lines))
            f.write("\n")


    after = x['data']['after']
    i=1
    while (i<5):
        data = requests.get(f'http://api.reddit.com/r/{subbreddit}/hot?limit={num_posts}&after={after}', headers={'User-Agent': 'windows:requests (by /u/saadshahbaz)'})
        x = json.loads(data.content.decode('utf8'))

        with open(outputfile,"a") as f:
            for k in range(num_posts):
                lines= x['data']['children'][k]['data']
                f.write(json.dumps(lines))
                f.write("\n")

        after = x['data']['after']
        i+=1

        



def main():
    parser = argparse.ArgumentParser()
    #parser.add_argument('-i', '--input', help = "Enter input file")
    parser.add_argument('-o', '--output', help = "output file")
    parser.add_argument('subreddit', help="subbreddit")

    args = parser.parse_args()

    subbreddit = args.subreddit
    output = args.output
    get_posts(subbreddit, output)





if __name__ == '__main__':
    main()
