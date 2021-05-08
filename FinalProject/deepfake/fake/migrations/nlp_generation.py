''' This will be the class that uses nlp to generate text based on the input corpuses (being artists and or politicians)
The available artists/bands and their songs are:
1.) Taylor Swift (Country Genre)
    1.a - You belong with me
    1.b - Shake it off
    1.c - All too Well
    1.d - Love Story
    1.e - Fifteen
2.) Luke Bryan (Country Genre)
    2.a - Drunk on You
    2.b - Country Girl
    2.c - Kiss Tomorrow Goodbye
    2.d - I don't want this night to end
    2.e - Muckalee Creek Water
3.) Blake Shelton (Country Genre)
    3.a - God's Country
    3.b - Ol' Red
    3.c - Nobody But You
    3.d - Austin
    3.e - God gave me you
4.) REO Speedwagon (Classic Rock Genre)
    4.a - Can't Fight this feeling
    4.b - Take it on the run
    4.c - I Do' Wanna Know
    4.d - Live Every Moment
    4.e - Gotta Feel More
5.) Journey (Classic Rock Genre)
    5.a - Dont Stop Believin
    5.b - Faithfully
    5.c - Separate Ways
    5.d - Anyway you want it
    5.e - Open Arms
6.) Toto (Classic Rock Genre)
    6.a - Africa
    6.b - Hold the Line
    6.c - Ill Supply the love
    6.d - Rosanna
    6.e - Georgy Porgy


The available politicians and their speeches are:
1.) Donald Trump
    1.a - 2021 CPAC Speech
    1.b - Farewell Address
    1.c - Covid Diagnoses Update
2.) Joe Biden
    2.a - 2021 Amtrak Anniversary Speech
    2.b - 2021 Joint Session Speech
    2.c - 2021 Covid Update
3.) Barack Obama
    3.a - Inaugural address
    3.b - Election Night Victory Speech
    3.c - 2002 Speech Against the Iraq War
4.) George Bush
    4.a - Inaugural address
    4.b - Post 9/11 Joint Congress Session
    4.c - First State of the Union
'''

#import statements necessary
import markovify
import re
import os

#input here is a list of all of the files used, returns a string
def make_deep_fake(files, num_verses):
    #string to represent all text
    complete_corpus_text = ""


    #file path stuff 
    os.chdir("fake") 
    os.chdir("corpus")

    for file in files:
        with open(file, encoding='cp437') as f:
            text = f.read()
            #print(str(file))
            complete_corpus_text += text

    #Now we markovify (i.e. make the model, use newline delineators)
    text_model = markovify.NewlineText(complete_corpus_text)

    #create the song and store it in a string
    deep_fake = ""
    for i in range(num_verses):
        deep_fake += text_model.make_short_sentence(140)
        deep_fake += "\n"


    os.chdir("../..") 
    deep_fake = deep_fake.replace("ΓÇö", ",")
    deep_fake = deep_fake.replace("ΓÇÖ", "'")
    deep_fake = deep_fake.replace("ΓÇ¥", "!")
    deep_fake = deep_fake.replace("ΓÇ¥", ",")
    return deep_fake

#returns a list of all of the file names
def parse_input(input):
    files = []
    input = input.lower()

    #parse input string for all possible artists
    if "luke bryan" in input:
            files.append("lukebryan.txt")
    if "taylor swift" in input:
            files.append("taylorswift.txt")
    if "blake shelton" in input:
            files.append("blakeshelton.txt")
    if "reo speedwagon" in input:
            files.append("reo.txt")
    if "journey" in input:
            files.append("journey.txt")
    if "toto" in input:
            files.append("toto.txt")
    #parse input string for all possible artists
    if "donald trump" in input:
            files.append("trump.txt")
    if "barack obama" in input:
            files.append("obama.txt")
    if "george bush" in input:
            files.append("bush.txt")
    if "joe biden" in input:
            files.append("biden.txt")
    return files
    

#returns a list of all of the people
def get_people(input):
    people = []
    input = input.lower()
   
    #parse input string for all possible artists
    if "luke bryan" in input:
        people.append("luke bryan")
    if "taylor swift" in input:
        people.append("taylor swift")
    if "blake shelton" in input:
        people.append("blake shelton")
    if "reo speedwagon" in input:
        people.append("reo speedwagon")
    if "journey" in input:
        people.append("journey")
    if "toto" in input:
        people.append("toto")
    if "donald trump" in input:
        people.append("donald trump")
    if "barack obama" in input:
        people.append("barack obama")
    if "george bush" in input:
        people.append("george bush")
    if "joe biden" in input:
        people.append("joe biden")
    
    return people


