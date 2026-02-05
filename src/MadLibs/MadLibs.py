from MadLibsStory import MadLibsStory

replay = True
while replay == True:
    print("Welcome to Murder Mystery Mad Libs! Please choose one of the following stories to complete: ")
    print("1. Story 1")
    print("2. Story 2")
    print("3. Story 3")
    print("4. Story 4")
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
    MadLibsStory(storyNum)
    if input("Would you like to make another story? Enter 'y' to continue: ") != 'y':
        replay == False
        print("Awww... you could have had so much fun. Your life must be so sad and depressing. Bye Bye.")
    

