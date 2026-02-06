class MadLibsStory:

    def __init__(self,sNum):
        self.sNum = sNum #Indicates chosen story
    
    def getWords(self):
        userWords = [] #User inputs are stored in a list

        #All four stories are stored in a string list, and referred to using their indexes
        story = [
"""I want to solve a murder mystery. Why I wish to solve one is something I don’t know. I simply want to, almost as if this desire was the result of a mood. The murder-mystery-mood, I suppose. The sky today was quite clear and blue — Oh, I suppose that this must bore the reader. Topics regarding the weather are generally accepted as a sign of idle boredom, after all. Very well, let's try something innovative instead: the concrete of the sidewalk firmly pressed into my feet; today’s ground was much more rigid than usual. Perhaps it was reassuring to know that the ground was a firm support always at arm’s, or rather leg’s length; to know that the ground will be forever-

@expression of suprise*

Huh. This must be what they call @saying*. Wait, what is this nonsense? Apologies, it seems that I stuttered; I meant “The art of being wise is the art of knowing what to overlook.” What does that mean? I have no idea, it seems that my author was unable to find a suitable, well established saying to express my sentiment, after all, if anything, I am not wise. Either way, to think that I would find something to satiate my murder-mystery-mood so quickly; it makes me wonder: am I in this situation because I am lucky or because I was actively looking for it?

What stood in front of me, or rather, on the other side of the road were a few funeral flowers. The meaning was clear: the flowers were for the person that died while crossing the very road I was standing on. Not quite the murder mystery, but close enough.

On second thought, what I was experiencing couldn’t be further away from a murder mystery; after all, there was no murderer to find. After spending some time lamenting my disappointment and scolding my cognitive bias for jumping to such a far-fetched conclusion, I squatted, as if asking the heavens didn’t yield a result and I brought myself to the ground to ask the bad place under it for an answer instead. My hair fluttered as a car passed by, bringing the glint of the morning sun reflected into my eyes. The morning rush hour had passed, but vehicles still passed by on the asphalt regularly, their metallic glint resembling the blade of an executioner flattening someone’s shoulders. What was I even doing here? Now that I think about it, I was supposed to be attending a funeral of my own, one for someone that had passed on so mundanely that I immediately developed a desire to immerse myself in another’s death that was much more extraordinary. I turned my gaze to the sky, perhaps hoping that such an inherently boring action would allow me to forcefully accept and embrace the boredom I had been running away from. Today’s sky really was @color*.

Epilogue:

Now for the punchline, or rather, the slap to my face. After standing for a while, I decided to inspect the flowers more carefully. I walked to the other side of the road, after checking both directions, obviously (I did not want to end up like the person the flowers were offered to). I first decided to touch the flowers, and upon doing so, they wilted, for they had begun melting in my hands. How could flowers melt? It seems that the flowers were not flowers, but flower-shaped chocolate made by the people on the internet that make realistic objects with chocolate. The entire time, the “flowers” were not there to honor a deceased person but to warn against crossing the road, and I, the fool, had fallen for the hook, line and sinker and then reeled myself in. And to think that I had been denied the simple dignity of being deceived by real, genuine flowers and had instead been bamboozled by chocolate! It truly was as if someone slapped my face and then decided to stomp on it. I slowly stood up and walked away, as if I was running away from an unpleasant experience not metaphorically, but literally, yet I doubted that distance could erase my memories of this.

"Nonsense."
"""
]  
        
        #The '*' and '@' mark the placeholder words in the mad lib to be cut and substituted with user inputs
        while "*" in story[self.sNum-1]:

            #Takes a user input and appends it to the 'userWords' list. The input message is determined by the placeholder words.
            userWords.append(input("Input a " + story[self.sNum-1][story[self.sNum-1].index("@")+1:story[self.sNum-1].index("*")] + " here: "))

            #Slices the placeholder words in the story, replaces with the '|' placeholder character
            story[self.sNum-1]=story[self.sNum-1][:story[self.sNum-1].index("@")] + "|" + story[self.sNum-1][story[self.sNum-1].index("*")+1:]
        
        return userWords, story
    
    def makeStory(self, userWords, story):
        i=0 
        while "|" in story[self.sNum-1]: #Detects placeholder '|' characters, replaces them with elements in the 'userWords' list (user inputs)
            story[self.sNum-1]=story[self.sNum-1][0:story[self.sNum-1].index("|")]+userWords[i]+story[self.sNum-1][story[self.sNum-1].index("|")+1:]
            i +=1 #Increments through elements/user inputs in 'userWords'
        print("Your story is: ")
        print(story[self.sNum-1])
