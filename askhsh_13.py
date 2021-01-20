#Create a string that will contain the user's file 
user_input=input("Enter your file name: ")

# Open file and read data
with open(user_input) as f:
    data = f.read()

#Create a string containig all the punctuations
punctuation='''!.,;:"\<'>-[]{?}()/#&$_'''

#If the file contains punctuations remove them
for item in data:
    if item in punctuation:
        data=data.replace(item, "")

#Split words and save them in a list
words=data.split()

#Initialize the counter that will track the items removed from the list
counter=0

#For each word in the list with a lenght of n characters, find one that has a lenght of 20-n characters
#Print these two words 
#Remove these two words 
for i in range(len(words)):
    word=words[i-counter]  #Subtract from i the counter to prevent the list index from going out of range
    for w in words:
        if (len(w)+len(word)==20) and (w!=word):
            print('Word "' + word + '" and word "' + w + '" have a lenght of 20 characters')
            words.remove(word)
            words.remove(w)
            counter += 2  #Another pair of two words have been removed
            break #Go to the next word of the list

