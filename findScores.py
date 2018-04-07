#! /usr/local/bin/python
import os
import json
import sys
import re
#from pprint import pprint

def calculateScore(file_name, keyword_to_score_map):
    file = open(file_name, 'rU')
    list_of_words = open('wordList.txt', 'a')
    key_words = set()
    for line in file:
        for word in re.split("\W", line):
            list_of_words.write(word+'\n')
            word_lower = word.lower()
            if keyword_to_score_map.__contains__(word_lower):
                key_words.add(word_lower)
    score = 0
    for word in key_words:
        score = score + keyword_to_score_map.get(word)
    return score


def generateScoreCard(config_map, directory):
    score_map = {}
    for file_name in os.listdir(directory):
        if file_name.endswith(".txt"):
            user_score = calculateScore(file_name, config_map['keyword_to_score'])
            score_map[file_name] = user_score
    
    return score_map

def publishToJSON(score_map, file_name):
    with open(file_name, 'w') as fp:
        json.dump(score_map, fp)




#pprint(data)
def main():
    config = 'config.json' 
    file_name = 'result.json'
    if len(sys.argv) > 1: 
        config = sys.argv[1]
    if len(sys.argv) > 2: 
        file_name = sys.argv[2]
    
    config_map = json.load(open(config))
    directory = '.'

    score_map = generateScoreCard(config_map, directory)
    print(score_map)

    publishToJSON(score_map, file_name=file_name)

main()
