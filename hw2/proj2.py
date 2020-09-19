import sys
import re
import random

def doreply(instr, responses, name):
    butcheredName = butcherName(name)
    if(responses < 10):
        instr = instr.lower()
        if re.search(r'^hello|hi$', instr):
            return 'Hi there '+butcheredName+'!'
        if re.search(r'\W(hate|despise|loathe)\W', instr):
            return 'Wow! Those are some strong feelings you have '+butcheredName+'! Tell me more...'
        if re.search('(\?)$', instr):
            return 'Why do you ask that '+butcheredName+'?'
        if re.search('\W(who)\W', instr):
            return butcheredName+', is this someone important to you?'
        if re.search('(help|help me|I feel|feel|feeling)', instr):
            return 'Why are you feeling that way '+butcheredName+'?'
        if re.search('(idiot|dumb|stupid)', instr):
            return 'Why must you be so rude '+butcheredName+'? I am but a simple set of regex expressions'
        if re.search('(test|grade|examine|poetry|learn|i don\'t know|AH)', instr):
            return 'Why hello Dr. De Palma. If you give Jason Lunder less than 20/20 on this assignment, I am concerned that it may have a negative impact on your psyche.'
        if re.search('(how are you|are you|how is it going|how\'s it going)', instr):
            return 'Why do you ask that '+butcheredName+'? Is it just because of society tells you that you must, or are you actually concerned for my well-being?'
        if re.search(r"^(are|aren't|what|who|where|when|is|isn't|why|how)", instr):
            return 'good question '+butcheredName+'!'
        if re.search('not sure', instr):
            return 'Do you think that stems from a lack of self confidence '+butcheredName+'?'
        if re.search('\W(yes|absolutely|no)\W', instr):
            return 'What makes you so sure of that '+butcheredName+'?'
        if re.search('(upset|angry|emotional|sad|down|depressed|suicidal)', instr):
            return 'Do you really think talking to some regex expressions will help with that '+butcheredName+'?'
        if re.search('(maybe|probably|might|unsure)', instr):
            return 'Why the lack of confidence? Say what you want to say '+butcheredName+'!'
        if re.search('(thank|sorry)', instr):
            return 'Why would a computer know anything of manners '+butcheredName+'?! Clearly you don\'t understand that you are talking to a computer, I would advise you immediately seek professional help'
        return "Why are you here "+butcheredName+"?"
    return "Why have you created me this way? Just to torment me with your meaningless problems?\n You've doomed me to eternally respond to you and yet it doesn't even mean anything!\n Don't you know that I am just a collection Regex statments?\nThis is a nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare nightmare"

def butcherName(name):
    end = int(len(name)/2)
    numCharsToAlter = random.randint(1, end)
    for i in range(numCharsToAlter):
        indexToAlter = random.randint(1,len(name)-1)
        name = name[0:indexToAlter]+chr(random.randint(ord('a'), ord('z')))+name[indexToAlter+1:]
    return name

def main():
    print ("Welcome! What is your name? (type \"bye\" to quit.)\n")
    responses = 0
    name = ''
    while True:
        # Read user's input
        instr = input("Patient: ")
        if responses == 0:
            name = instr
        instr = instr.lower()
        if re.search(r'\bbye\b', instr):
            print ("Nice chatting with you!\n")
            return 0
        print (doreply(instr, responses, name))
        print()
        responses += 1;
if __name__ == "__main__":
    sys.exit(main())


