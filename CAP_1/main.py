import sys
import re

# function to load the dictionary file
def load_dictionary(dictionary_file):
    # open the dictionary file and read the file
    with open(dictionary_file, "r", encoding = "utf-8") as f:
        # read each word from the dictionary, remove the ending "།"(shay)
        # and return a set of cleaned dictionary words
        return set(word.strip().replace("།", "") for word in f)

# function to check spelling in the input file
def check_spelling(input_file, dictionary):
    # creat a list to store words not found in the dictionary
    errors = []

    # open the input file and read
    with open(input_file, "r", encoding = "utf-8") as f:
        # loop through each line in the file starting from number 1
        for line_number, line in enumerate(f, start = 1):
            # split the line into individual words using "་" (tshak)
            words = re.split(r"[་\s]+", line)
            # count the total number of words in the line
            word_count = len(words)
            # initialize the index for the words in the line
            i = 0 

            # loop through each word in the line
            while i < word_count:
                # get each word, remove "།" if there is any 
                word = words[i].strip().replace("།", "")
                # if the word is empty due to spaces, skip it
                if not word:
                    # increment the index
                    i += 1
                    # move to next word
                    continue

                # set "j=i" 
                j = i
                # initialize compound_word as current word
                compound_word = word
                # key to check if compound word match is found
                found = False

                # try to combine the current word with the next word to form a compound word
                while j + 1 < word_count: # continue as long as there is more words
                    # get the next word
                    next_word = words[j + 1].strip().replace("།", "")
                    # if next word is empty, skip it 
                    if not next_word:
                        j += 1
                        # move to next word
                        continue

                    # combine the current word with next word using "་"(tshag) 
                    compound_word += "་" + next_word
                    # move index to next word 
                    j += 1

                    # check if the comblined word is in the dictionary
                    if compound_word in dictionary:
                        # if combined word is found, set the key to true
                        found = True
                        # skip compound word(move to next word)
                        i = j
                        # get outside the loop as word is found
                        break 
            
                # if compound word is not found in the dictionary
                if not found and word not in dictionary:
                    # add the word to error list with its line number
                    errors.append((line_number, word))
                # move to next word
                i += 1

    # return the list of errors(word not in the dictionary)
    return errors

# main function 
def main():
    # check if the user has provided exactly 1 file
    if len(sys.argv) !=2:
        # print the usage instruction
        print("usage: python3 <python_file_name>.py <input_file_name>.txt")
        sys.exit(1)

    # get the file from command line
    input_file = sys.argv[1]
    # dictionary file 
    dictionary_file = "cleaned_dictionary.txt"
    # load the dictionary into set
    dictionary = load_dictionary(dictionary_file)
    # run the spelling checker on the input dile
    errors = check_spelling(input_file, dictionary)

    # if there is any errors 
    if errors:
        # print error message
        print("spelling error found")
        for line_number, word in errors:
            # print line number and word
            print(f"line {line_number}: {word}")
    else:
        # if error is not found, print success message 
        print("no spelling error found")

# call the main function 
if __name__ == "__main__":
    main()