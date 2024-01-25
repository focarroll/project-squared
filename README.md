# Welcome to Project-Squared!

This is the first Open-Source project for the Xaverian Brothers High School Computer Science Club!

# Introduction

While coding can seem very daunting, this project is meant to serve as a **real-world example** of contributing to an Open-Source project! 
Many Open-Source projects already have most of their functionality put into place, but we will be trying to take a more ground-up approach and learn as we contribute.

**IMPORTANT:** If you are seeing this much further into the project lifespan, don't worry, you will still be able to contribute!

# The Idea

Mainly, this project will be a combination of mini-projects and helpful programs all designed to help a user accomplish something all made by the Xaverian community!

# Onboarding (Mainly for people who were not present at the first two meetings)

For any questions email 25pbrausch@xbhs.net, 25tholloway@xbhs.net, 25kdhingra@xbhs.net, or deggli@xbhs.com.

1. Install Visual Studio Code or another editor of your choice. (https://code.visualstudio.com/)

2. Install Python from either a direct online download or from the Microsoft store. (https://www.python.org/downloads/)
   - If using Visual Studio, also install the Python extension in the extension tabs on the left bar.
    
3. Install Git Bash from a direct download link to access this project's repository. (https://www.git-scm.com/downloads).

4. Install GitHub Desktop.

5. On the code section of this page click the green code button open it with GitHub Desktop and clone the repository.

6. The repository will now be copied into your files.

7. Open Visual Studio Code click "file" and "open folder" and locate the project-squared folder and open it. It should be located under documents\github\project-squared.
   
8. Now that you have a working directory, you need to download any dependencies. Currently, dependencies are found in requirements.txt. Open a new terminal in the Project-Squared folder and run "pip install -r requirements.txt" to download the current dependencies.

9. The project's main functionality exists in main.py which is how you run the file. There should be an arrow in the top right which allows you to run the file when having the main.py file opened.

10. When looking into the main.py file there is not much going on in the main method. This is because most of the code is just selecting what "mini" programs you want to run. These programs exist in different .py files found in the root-programs folder. Go ahead and see that each has a function which is what the main.py file calls them when selecting which program you want to call.

11. To create your own mini-programs go ahead and add a new file in the root-programs folder. For now, add your name and class number as a comment at the start of the file. Then add functionality in a main function to print "Hello World!". To add this program to be selectable from the main.py program go ahead and import your program function at the top of the main.py file which you should be able to do by copying others' syntax. Once completed run the main.py file and select your program. You should see Hello World being displayed in the terminal. Go ahead and play around with your program more until satisfied.

12. Keep in mind, that you can add more functionality to other mini-programs that aren't your own, but these changes will have to be reviewed by leaders of the club and the original owner of the program.

13. Once the changes look good, open the GitHub desktop and try to commit your changes. You should receive a message to fork the repository and do so. Now recommit your changes.

14. Go back to GitHub and click your profile picture and then repositories. Open your project-squared repository. This is your own version of the parent repository. You can now click contribute to the forked repository and create a pull request. 

16. This request for these changes will be reviewed by the current leaders of the club who can be contacted above.

17. Periodically make sure to sync your Github fork on your forked repository and click fetch origin on your Github desktop. This may cause a thing called merge conflict, but you should overwrite your own changes as it is much harder to resolve them yourself.

18. Have fun!
