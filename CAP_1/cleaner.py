def clean_dictionary(input_file, output_file):
    # create an empty list to store refined words
    cleaned_words = []

    # open the input file and reat line by line
    with open(input_file, "r", encoding = "utf-8" ) as file:
        for line in file:
            # split each line into words by spaces
            words = line.split()
            # if the line contains at least one word
            if words:
                dzongkha_word = words[0] # take the word from the line
                cleaned_words.append(dzongkha_word) # add to the list of cleaned words

    # open the output file and write the cleaned words  in it
    with open(output_file , "w", encoding = "utf-8")  as file:
        # loop through every word 
        for word in cleaned_words:
            file.write(word + "\n")  # write each cleaned word on new line

        # print a result 
        print(f"cleaned words saved to {output_file}")

input_file = "dictionary.txt" # raw file
output_file = "cleaned_dictionary.txt" # name of output file
clean_dictionary(input_file, output_file) # calling out the function