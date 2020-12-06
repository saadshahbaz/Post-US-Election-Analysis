import sys
import json
import argparse
import math
from operator import itemgetter 

def indiv_tfidf(dict_pony, dict_all, num_words, n):
    '''
    Can use this to do every pony's idf individually
    '''
    # tfidf = (how many times that pony used the word)*(log((number of words used in total)/(number of times that word was used)))
    top_tfidf = []
    all_tfidf = {}
    # computing the tf-idfs for all the words for this pony
    for word in dict_pony.keys():
        tf = dict_pony[word]
        overall_freq = dict_all[word]
        idf = math.log(float(n)/overall_freq)
        tfidf = tf*idf
        all_tfidf[word] = tfidf

    # returning only the top num_words
    top_n = dict(sorted(all_tfidf.items(),key=itemgetter(1), reverse = True)[0:int(num_words)])
    return list(top_n)

def compute_total_usage(json):
    ''' will takes as input the json file input, will output the total number of times each word was used
    as a dictionary
    '''
    word_freq = {}
    total_words = 0
    for pony in json.keys():
        for word in json[pony].keys():
            total_words += json[pony][word]
            if word in word_freq.keys():
                word_freq[word] += json[pony][word]
            else:
                word_freq[word] = json[pony][word]
    return word_freq, total_words

def compute_tfidf(input_file, num_words):
    word_freq, n = compute_total_usage(input_file)
    idf_dict = {}
    for pony in input_file.keys():
        top_idf = indiv_tfidf(input_file[pony], word_freq, num_words, n)
        idf_dict[pony] = top_idf

    return idf_dict

def compute_new_tfidf(input_file, num_words):
    '''
    TF stays the same 
    IDF is now log(number of ponies/number of ponies that use this word)
    '''
    num_ponies = len(input_file)
    word_freq, n = compute_total_usage(input_file)
    idf_dict = {}
    for pony in input_file.keys():
        top_idf = indiv_tfidf2(input_file[pony], input_file, num_ponies, num_words)
        idf_dict[pony] = top_idf
    return idf_dict

def indiv_tfidf2(dict_pony, input_file, num_ponies, num_words):
    '''
    Can use this to do every pony's idf individually
    '''
    # tfidf = (how many times that pony used the word)*(log((number of words used in total)/(number of times that word was used)))
    top_tfidf = []
    all_tfidf = {}
    # computing the tf-idfs for all the words for this pony
    for word in dict_pony.keys():
        tf = dict_pony[word]
        num_user = 1
        for pony in input_file.keys():
            if word in input_file[pony].keys():
                num_user += 1
        idf = math.log(float(num_ponies)/num_user)
        tfidf = tf*idf
        all_tfidf[word] = tfidf

    # returning only the top num_words
    top_n = dict(sorted(all_tfidf.items(),key=itemgetter(1), reverse = True)[0:int(num_words)])
    return list(top_n)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("num_words")
    parser.add_argument('-o', help="This is the json file that the results will be written to")
    parser.add_argument("-p", action = 'store_true')
    args = parser.parse_args()
    with open(args.input) as f:
        in_file = f.read()
    if (args.p):
        output_file = compute_new_tfidf(json.loads(in_file), args.num_words)
        output = open(args.o, 'w')
        json.dump(output_file, output)
        output.close()
    else:
        print(compute_tfidf(json.loads(in_file), args.num_words))

if __name__ == '__main__':
    main()