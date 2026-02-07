from MadLibsStory import MadLibsStory

replay = True
while replay == True:
    print("Welcome to Murder Mystery Mad Libs! Please choose one of the following stories to complete: ")
    print("1. I Want to Solve a Murder Mystery")
    print("2. Humanity's greatest serial killer")
    print("3. Murder Uno Reverse")
    print("4. The Mahjong Murder")
    while True:
        try:
            storyNum = int(input("Enter your selection (story number) here: "))
        except ValueError:
            print("Please input a valid story selection.")
        else:
            if storyNum > 4 or storyNum < 1:
                print("Please input a valid story selection.")
            else:
                break
    s = MadLibsStory(storyNum) #Initialize class
    userWords, story = s.getWords() #Create two variables to be passed into the 'makeStory' method using the returns of 'getWords'
    s.makeStory(userWords,story)
    if input("Would you like to make another story? Enter 'y' to continue: ") != 'y':
        replay = False
        print("Awww... you could have had so much fun. Your life must be so sad and depressing. Bye Bye.")
    

