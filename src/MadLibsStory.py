class MadLibsStory:
    def __innit__ (self,story,sNum,userWords):
        self.story=["Hello, my name is |name|. I love to eat |noun|. Today I went to the (place) and ate (noun) again.  "]
        self.story.append("")
        self.story.append("")
        self.story.append("")
        self.sNum=sNum
        self.userWords=userWords
    def makeStory( self):
        i=0 
        while "|" in self.s1:
            s1=s1[0:s1.index("|")]+self.userWords[i]+s1[s1.index("|")+1:]
        return s1