#! /usr/local/bin/python
import os
import json
import sys
import re
#from pprint import pprint

def calculateScore(file_name, keyword_to_score_map):
    file = open(file_name, 'rU')
    key_words = set()
    score = 0
    for line in file:
        for word in re.split("\W", line):
            word_lower = word.lower()
            if keyword_to_score_map.__contains__(word_lower) and (not key_words.__contains__(word_lower)):
                key_words.add(word_lower)
                score = score + keyword_to_score_map.get(word_lower)     
    return score


def FileCheck(file_name):
    try:
        open(file_name,'r')
        return True
    except IOError:
        return False    


def generateScoreCard(config_map, directory):
    score_map = {}
    for file_name in os.listdir(directory):
        if file_name.endswith(".txt"):
            user_score = calculateScore(file_name, config_map['keyword_to_score'])
            file_name_pdf = file_name.replace('.txt', '.pdf')
            file_name = file_name_pdf if FileCheck(file_name_pdf) else file_name
            score_map[file_name] = user_score
            
    return score_map

def move_shortlisted_ones(result_file, threshold):
    origin = os.getcwd()
    destination = os.path.join(os.getcwd(), 'shortlisted')
    if not os.path.exists(destination):
        os.makedirs(destination)

    scores = json.load(open(result_file, 'r'))
    [os.rename(os.path.join(origin, i), os.path.join(destination, i)) for i in scores if scores[i] >= threshold]

def main():
    config = 'config.json' 
    result_file = 'result.json'
    if len(sys.argv) > 1: 
        config = sys.argv[1]
    if len(sys.argv) > 2: 
        result_file = sys.argv[2]
    
    config_map = json.load(open(config))
    directory = os.getcwd()

    score_map = generateScoreCard(config_map, directory)
    json.dump(score_map, open(result_file, 'w'))
    move_shortlisted_ones(result_file, config_map['threshold'])

main()
