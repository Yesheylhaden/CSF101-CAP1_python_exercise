# Dzongkha Spelling Checker

## Project Overview

This assignment implements a simple Dzongkha spelling chacker. It reads input text file comparing with dictionary text file which has correct words of Dzongkha. 

## Table of Contents
- [Usage](#usage)
- [Implementation Details](#implementation-details)
- [Data Structures](#data-structures)
-[Algorithms](#algorithms)
- [Challenges and Solutions](#challenges-and-solutions)
-[Future Improvements](#future-improvements)
- [References](#references)

## Usage
To use the Dzongkha spelling cheacker, use following command.

```bash
python3 main.py dzoword.txt
```

## Implementation Details
First of all process of cleaning the raw dictionary text file is done, which contain correct spelling of Dzongkha(each word per line). The code for cleaning process is written separately on "cleaner.py" file. 

The main file loads the dictionary file with valid Dzongkha words. Then it process the input file line by line splitting each word by "་" and spaces.

The algorithm used in the project is sliding window to find compound word in the text. It checks word or group of words from the dictionary. If the word is not found in the dictionary it is marked as spelling error.

## Data Structure 
1. Set: The valid word of dictionary is stored in set for fast lookups(average O(1) time complexity) to ckeck for word.
2. List: The input file is read line by line, each line is considered as list of words for precessing.
3. Tuple List: Tuple is used to store words found as errors. And it is immutable.

## Allgorithms
### Dictionary Lookup: 
The tools stores valid Dzongkha words from the dictionary in a set, which allows for quick word loopups. For each word or group of words from the input text file. Since set lookup are fast, the process runs efficiently.

### Sliding Window:
Some of the Dzongkha words are compound of multiple word. So, to find the valid compound word from dictionary sliding window is best algorithm. The algorithm starts from one word and then adds another consecutive word to form compound word, it ckecks if compound word is in the dictionary or not. If compound word is found in dictionary it skip the whole word.

### Word Cleaning
Before comparing the word which is in the dictionary, it removes "།" which is not the part of word to ensure correct matching of words.

## Challenges and Solutions
* Handling Compound words: Dzongkha has many compound words made up of many smaller words. To handle this, sliding window is implemented so that compound words are not ckecked throughly.

* Unicode Handling: Handling Dzongkha unicode character and puntuation is bit difficult. So the program removes "།" from the dictionary before comparing with text file 

* Choosing Right Data Structure: Choosing right data structure was bit comlicated as any of them acts the same.

## Future Improvements
* Improve the sliding window approach to handle complex compound word.

