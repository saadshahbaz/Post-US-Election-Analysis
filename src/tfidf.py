import sys
import json
import argparse
import csv
import copy
# maybe check for stopwords

def file_trim(file):
    # trimming the dictionary to only have words that appear atleast 5 times
    # need to iterate over the first level of keys in the json
    # then the second level and filter only for works with that appear 5 or more times
    # also need to take out words that contain non-alpha characters
    file1 = copy.deepcopy(file) # deepycopy used to iterate over since a runtime error occured when iterating over og
    # could probably also work with the list thing as long as you keep the same thing at line 25
    for character in file1.keys():
        for word in file1[character].keys():
            if not word.isalpha() or file1[character][word] < 2:
                try:
                    file[character].pop(word)
                except:
                    continue           
    return file

def replace_better(old, new, string):
    ''' Takes a string, list of words to replace and replacement work, iterates over the words in
    old and replaces them with new returns the string that has been altered
    '''
    for word in old:
        string = string.replace(word, new)
    return string

def update_word(line, name, file):
    # add the helper function for this
    # takes the line, character name and json file
    # updates the wordcount for that character 
    # returns the whole json dictionary 
    to_replace = ["(",")",",","-",".","?","!",":",";","#","&","]","["] # may need to add quotation marks
    line = replace_better(to_replace, ' ', line)
    words = line.split()
    for word in words:
        # update the dictionary
        if word.lower() in file[name].keys():
            file[name][word.lower()] += 1
        else:
            # add the key if it isnt there yet
            file[name][word.lower()] = 1

    return file

def compute_word_counts(input_file, output):
    # opening the input file
    file_open = csv.reader(open(input_file))    
    list_of_topics = ["biden campaign", "tenure suggestions", "trump controversy", "media", "voting", "covid-19", "trump campaign"]
    # creating the json output
    output_file = {'Biden Campaign':{},'Biden Tenure':{},'Trump Controversy':{},'Covid 19':{},'Trump Campaign':{},'Voting':{}, 'Media':{}, 'Other':{}} 
    # hopefull this^ line break works fine
    for line in file_open:
        #print(line[2].lower())
        # checking to see which pony is speaking
        if line[2].lower() == list_of_topics[0]:
            # do update word with their dirctionary
            output_file = update_word(line[1],'Biden Campaign', output_file)
        elif (line[2].lower() == list_of_topics[1]):
            #print("entered")
            output_file = update_word(line[1],'Biden Tenure', output_file)
        elif line[2].lower() == list_of_topics[2]:
            output_file = update_word(line[1],'Trump Controversy', output_file)
        elif (line[2].lower() == list_of_topics[5] or line[2].lower() == "covid 19"):
            output_file = update_word(line[1],'Covid 19', output_file)
        elif line[2].lower() == list_of_topics[6]:
            output_file = update_word(line[1],'Trump Campaign', output_file)
        elif line[2].lower() == list_of_topics[4]:
            output_file = update_word(line[1],'Voting', output_file)
        elif line[2].lower() == list_of_topics[3]:
            output_file = update_word(line[1],'Media', output_file)
        elif line[2].lower() == 'other':
            output_file = update_word(line[1],'Other', output_file)
        

    # trimming the words down
    output_file = file_trim(output_file)
    for i in output_file:
        print(i , len(output_file[i]))
    # print(output_file["Biden Campaign"])
    # print(output_file["Trump Controversy"])
    # print(output_file["Trump Campaign"])
    # print(output_file["Voting"])
    # write the output file to the specified location
    output = open(output, 'w')
    json.dump(output_file, output)
    output.close()
        
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', help="This is the json file that the results will be written to")
    parser.add_argument('input')
    args = parser.parse_args()
    #print(args.input)
    compute_word_counts(args.input, args.o)

if __name__ == '__main__':
    main()