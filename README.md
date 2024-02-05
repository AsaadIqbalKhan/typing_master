Introduction
This Python script is designed to create a simple typing test application. Users can take a typing test, and their speed and accuracy will be recorded in a leaderboard. The application utilizes a JSON file ("ranking.json") to store and update user scores.

Features
Typing Test: Users can take a typing test with randomly selected paragraphs from the provided material.
Leaderboard: Users can view the leaderboard, which displays the rank, speed, and accuracy of each participant.
User Registration: New users can register by creating a username, while existing users can log in to maintain their records.
Score Recording: The script records the speed and accuracy of users in the leaderboard.


How to Use
Run the Script: Execute the script in a Python environment.
Choose an Option:
Type 1 to start a typing test.
Type 2 to view the leaderboard.
Type 3 to exit the application.


User Registration:
If it's the user's first time, they will be prompted to create a new username.
Existing users need to enter their username to maintain their records.
Take the Test: Users will be provided with a paragraph to type. The script calculates their typing speed and accuracy.


Leaderboard Display: Users can view the leaderboard at any time to see their rank, speed, and accuracy.
Exit: Type 3 to exit the application.
Files
ranking.json: JSON file to store user data (leaderboard).
typing_test.py: The main Python script.


Note
Ensure that you have the necessary libraries installed (random, time, json) to run the script.
The script updates the "ranking.json" file with user scores.
