class MadLibsStory:
    def __innit__ (self, s1, s2, s3, s4, sNum,userWords):
        self.s1="Hello, my name is |name|. I love to eat |noun|. Today I went to the (place) and ate (noun) again.  "
        self.s2=" "
        self.s3=""
        self.s4=" "
        self.sNum=sNum
        self.userWords=userWords
    def story( self):
        i=0 
        while "|" in self.s1:
            s1=s1[0:s1.index("|")]+self.userWords[i]+s1[s1.index("|")+1:]
        return s1