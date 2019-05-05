# File: Week8.py
# Name: Taylor Anderson
# Date: 5/5/2019
# Course: DSC 510
# Assignment: Week 8
# Summary: Finds the number of occurences of each word in a file 


#create dictionary
counts = dict()

# add words to the dictionary or increase their value by one if the entry already exists
def add_word(word):
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1


# creates a list with each word in lowercase letters
def process_line(line):
    clean_line = line.lower().replace('-',' ').replace(',', ' ').replace('.', ' ').split()
    for word in clean_line:
        add_word(word)


# print out lenth of dictionary and words in order based on occurence
def pretty_print(d):

    print(f'Length of the dictionary: {len(d)}')
    print('Word'.ljust(15)+'Count')
    print('-'*20)
    order = list(set(d.values()))[::-1]  # used to determine order to print words
    for num in order:                    # prints each word and its number of occurences in order
        for word in d:
            if d[word] == num:
                print(word.ljust(17),d[word])  # prints and keeps even spacing for each entry

    
def main():
    gba_file = open('gettysburg.txt','r')  # open file

    for line in gba_file:
        process_line(line)

    pretty_print(counts)

main()
