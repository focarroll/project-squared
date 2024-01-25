# Welcome to Project-Squared!

This is the first Open-Source project for the Xaverian Brothers High School Computer Science Club!

# Introduction

While coding can seem very daunting, this project is meant to serve as a **real-world example** of contributing to an Open-Source project! 
Many Open-Source projects already have most of their functionality put into place, but we will be trying to take a more ground-up approach and learn as we contribute.

**IMPORTANT:** If you are seeing this much further into the project lifespan, don't worry, you will still be able to contribute!

# The Idea

Mainly, this project will be a combination of mini-projects and helpful programs all designed to help a user accomplish something all made by yourselves!

**EXAMPLE GAME TUTORIAL:** (https://vim-adventures.com/)
**CURRENT GAME PAGE:** (https://pbbrausch.github.io/py-adventures/)

# Onboarding (Mainly for people who were not present at the first two meetings)

For any questions email 25pbrausch@xbhs.net, 25tholloway@xbhs.net, 25kdhingra@xbhs.net, or deggli@xbhs.com.

1. Install Visual Studio Code or another editor of your choice. (https://code.visualstudio.com/)
   - **Windows:** If you end up using Visual Studio, download MSYS2 from this link to install bash a command line interface. (https://www.msys2.org/)
   - **Mac:** If you end up using Visual Studio, open up Visual Studio and Open the Command Palette (Cmd+Shift+P) and type 'shell command' to find the Shell Command: Install 'code' command in PATH command and restart the application.
   - 
2. Install Python from either a direct online download or from the Microsoft store. (https://www.python.org/downloads/)
   - If using Visual Studio, also install the Python extension in the extension tabs on the left bar.
    
3. Install Git Bash from a direct download link to access this project's repository. (https://www.git-scm.com/downloads).

4. **FORK** (Not Clone) **THIS** repository to an accessible space on your computer. **Note you should be doing it on this repository, not the example one in the tutorial.** Tutorial: ([https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository))

5. Open a new terminal window by clicking new/terminal at the top bar. It should either say zsh or bash on the right side of the terminal. If not, contact us or look up a video for your specific devices for why MSYS2 didn't appear or why zsh is not selected as default.

6. Cd into your folder where you want your clone to be stored. You can easily do this by going to file/open folder and once again selecting new terminal to update the terminal's directory location.

7. Clone **YOUR** forked repository that you made to an accessible location. Tutorial: (https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#cloning-your-forked-repository)
   
8. Open Visual Studio select file in the top left and open the folder where the repository was cloned.

9. Get **YOUR** cloned repository to sync with **THIS** reposity so it recieves updates. Tutorial: (https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#configuring-git-to-sync-your-fork-with-the-upstream-repository)

10. Now that you have a working directory, you need to download any dependencies. Currently, dependencies are found in requirements.txt. Open a new terminal in the Project-Squared folder and run "pip install -r requirements.txt" to download the current dependencies.

11. The projects main functionality exists in main.py which is how you run the file. There should be a arrow in the top right which allows you to run the file when having the main.py file opened.

12. When looking into the main.py file there is not much going on in the main method. This is because most of the code is just selecting what "mini" programs you want to run. These programs exists in different .py files found in the root-programs folder. Go ahead and see that each has a function which is what the main.py file calls them when selecting which progam you want to call.

13. To create your own mini programs go ahead and add a new file in the root-programs folder. For now add you name and class number as a comment at the start of the file. Then add functionality in a main function to print "Hello World!". To add this program to be selectable from the main.py program go ahead and import your programs function at the top of the main.py file which you should be able to do by copying others syntax. Once completed run the main.py file and select you program. You should see hello world being displayed in the terminal. Go ahead and play around with your program more until satisfied.

14. Keep in mind, you are able to add more functionality to other mini-programs that aren't your own, but these changes will have to be reviewed by leaders of the club and the original owner of the program.

15. Once the changes look good, either open a new terminal window by clicking new/terminal at the top bar or open GitHub desktop. Type "git status" to view the files in your current workspace. To add changes type "git add . " After, check the status and it should show the modified files in green. Then, type in "git commit --message--" replace --message-- with your change information. If you just type "git commit," a new window should appear. Type your message there, save and close that window and it will act the same. After type "git push" to push changes to your forked repository (a window may open asking you to create a GitHub account; sign up with your personal or Xaverian email).

16. Create a pull request to push the changes to **THIS** repository. This request for these changes will be reviewed by the current leaders of the club who can be contacted above. Tutorial: (https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)

17. Have fun!
