# Murder Mystery Mad Libs
## A Project By Ethan Tang and Mo Spiegel
### Description
This project is an application written in Python with text-based Terminal interaction in which the user enters a series of inputs to generate a mad lib based off of custom story templates. The templates are all themed around 'Murder Mystery', with some more loosely following this initial concept than others. 
  
&nbsp;

This project is broken into two Python files: a main file containing the welcome message, story selection, and replay mechanism, inside of which the MadLibStory class is initialized and its member methods are called, and a class file which houses the MadLibStory class that contains all of the logic for taking user inputs and substituting them into the mad lib templates.
  
&nbsp;

1. **Main File**:
   - Calls for a user numeric input to determine which mad lib template is selected; this input is stored as the integer 'storyNum'
   - Contains try-except statements to prevent non-integer inputs for 'storyNum'
   - Initializes an instance of the MadLibStory class, passing in 'storyNum' into the argument
   - Calls the MadLibStory member methods, including 'getWords' (which obtains user inputs), whose returns are passed into the member 'makeStory' method also called in the main file
   - Uses the boolean 'replay', which can be toggled by the user once the program finishes, to determine whether to loop through the program again
  
&nbsp;

2. **MadLibStory Class**:
   - Constructor contains the parameter 'sNum', which is set in the main file as 'storyNum'
   - Within the 'getWords' method, the two lists 'userWords' and 'story' are initialized
     - The 'story' list contains four strings for all four mad lib template stories, each of which contain special characters that mark where user inputs are to be substituted
     - Within the 'story' list, individual stories are retrieved using their index (which is determined by 'sNum')
   - The getWords method utilizes while loops to cycle through one of the strings in the story list, identifying the special character markers and calling for a user input for each (which is then appended to 'userWords'), slicing the filler text between the special character markers and replacing them with a placeholder
     - This method returns the modified story list and the userWords list
   - The makeStory method (which takes the 'story' asnd 'userWords' lists as parameters) iterates through the 'userWords' list and replaces the placeholders in the story with its elements (which are in corresponding order)
     - The method then prints the final story
  
&nbsp;

### Contributions
1. **Ethan Tang**
   - Wrote 2 mad lib templates, including 'I Want to Solve a Muder Mystery' and 'Humanity's Greatest Serial Killer'
   - Developd preliminary conceptual algorithm for the MadLibStory class
   - Programmed most of the MadLibStory class
  
&nbsp;

2. **Mo Spiegel**
   - Wrote 2 mad lib templates, including 'Murder Uno Reverse' and 'The Mahjong Murder'
   - Programmed the main file
   - Helped program some of the MadLibStory class
   - Created the readme file
  
&nbsp;

### Source Files
* [Source Code](https://github.com/Mo59471/Murder_Mystery_Mad_Libs/tree/main/src/MadLibs)
     
