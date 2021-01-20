import math

#Find the iterations of each character in a text and print the percentage of each character based on the total text's characters
def Show_char_per(txt):
    total_odd_characters=0    
    characters_ascii=[]  #Create a list to store the equivelant ascii value of each character in the text
    dict1={}    #Create a dictionary where the KEYS are the ascii values of each character and the VALUES are their iterations 
    
    for ch in txt.lower():
        if ord(ch)>96 and ord(ch)<123: #if ascii value of character is between 96 and 123
            characters_ascii.append(ord(ch)) #Store the ascii value of the character in the list
            total_odd_characters +=1 #Increase odd character counter

        if ord(ch)>96 and ord(ch)<123 and ord(ch) % 2 ==1: #if ascii value of character is between 96 and 123 and odd
            dict1.update({ord(ch):0}) #Insert item in the dictionary and make it's value equal to zero
    
    #For every repetitive character add one 
    for ch in characters_ascii:
        if ch % 2 ==1: #if odd:
            dict1[ch]=dict1.get(ch)+1 #Increase the key's value by one (value acts like a counter in this programme)

    #For evey key(ascii character value) find the percentage of its appearance in the text based on the total characters
    for key in dict1:
        per=math.ceil(dict1[key]/total_odd_characters*100)
        print(chr(key) + ": " + "*" * per) #Convert the ascii value into the actual character and print its percentage

                    
#Create a string that will contain the user's file 
user_input=input("Enter your file name: ")

# Open file and read data
with open(user_input) as f:
    data = f.read() 

#Create a string containig all the punctuations
punctuation='''!.,;:"\<'>-[]{?}/#&$_'''

#If the file contains punctuations remove them
for item in data:
    if item in punctuation:
        data=data.replace(item, "")

print(Show_char_per(data))