class MadLibsStory:
    story = ["Hello my name is @name*. I like to eat @food*."]
    userWords = []

    def __init__(self,sNum):
        self.sNum = sNum
    
    def story(self,story,userWords):
        while "*" in story[self.sNum-1]:
            userWords.append(input("Input a " + story[self.sNum-1][story[self.sNum-1].index("@")+1:story[self.sNum-1].index("*")] + "here: "))
            story[self.sNum-1]=story[self.sNum-1][:story[self.sNum-1].index("@")] + " | " + story[self.sNum-1][story[self.sNum-1].index("*")+1:]
        return(userWords)

