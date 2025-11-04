# Python 301 - Object-Oriented Programming

# Python 201 - Procedural Programming

## Repository Overview
This repository contains my coursework for [Python 201 - Procedural Programming](https://codingnomads.com/course/python-programming-201), the second course in the [Python Web Development Career Track](https://codingnomads.com/career-track/python-web-development-learn-python-bootcamp) by [CodingNomads](https://codingnomads.com/). This was an 80-hour course, designed to help learners deepen their understanding of Python through procedural programming concepts, debugging, and API integration. This included multiple projects and labs, including SQLAlchemy, API integration, and debugging approaches. 

---

## Table of Contents
- [Repository Overview](#repository-overview)
- [Table of Contents](#table-of-contents)
- [Concepts Covered](#concepts-covered)
- [Course Prerequisites](#prerequisites)
- [Exercises & Labs](#exercises--labs)
- [Projects](#projects)
- [API Capstone Project](#api-capstone-project)
- [To Clone This Repository](#to-clone-this-repository)
  
---

## Concepts Covered 
The following Python skills were acquired when completing this course:
- Functions: arguments, return values, and scope 
- Advanced data types: tuples, lists, sets, and dictionaries
- File input/output and managing paths effectively
- Building modules and packages 
- Dependency management, using virtual environments 
- Debugging programs using IDE features, Python PDB, web-pdb and pudb modules  
- Database integration, with SQLAlchemy
- REST API integration, with the Python `requests` package 

---

## Course Prerequisites
The [CodingNomads Python 101 course](https://github.com/franpanteli/CodingNomads-python-101) was a prerequisite for this. Other prerequisites included a Python version above 3.0 to be installed, for the completion of its pdb debugger and virtual environment sections.

---

## Exercises & Labs
One directory was created for each module in the course, from modules two to ten. Each of these directories includes two further directories, for content and practice. Course content was presented in the form of videos and webpages. Notes were made on each of these, in a .py file per video and webpage. These notes are included in each module’s `webpage_and_video_notes` directory. Labs (module exercises) were next completed. My solutions for these were annotated with comments and are published in each module’s lab folder. Links to each set of my module notes and exercise solutions are presented below. These are also found in the repository [resources](https://github.com/franpanteli/CodingNomads-python-201/tree/main/labs/resources) folder. 
- [02 More Data Types](labs/resources/02_more-datatypes)
  - [02_webpage_and_video_notes](labs/resources/02_more-datatypes/02_webpage_and_video_notes)
  - [02_labs](labs/resources/02_more-datatypes/02_labs)
- [03 File Input/Output](labs/resources/03_file-input-output)
  - [03_webpage_and_video_notes](labs/resources/03_file-input-output/03_webpage_and_video_notes)
  - [03_labs](labs/resources/03_file-input-output/03_labs)
- [04 Functions and Scopes](labs/resources/04_functions-and-scopes)
  - [04_webpage_and_video_notes](labs/resources/04_functions-and-scopes/04_webpage_and_video_notes)
  - [04_labs](labs/resources/04_functions-and-scopes/04_labs)
- [05 Virtual Environments and Packages](labs/resources/05_venvs-and-packages)
  - [05_webpage_and_video_notes](labs/resources/05_venvs-and-packages/05_webpage_and_video_notes)
  - [05_labs](labs/resources/05_venvs-and-packages/05_labs)
- [06 Advanced Python Concepts](labs/resources/06_advanced-python-concepts)
  - [06_webpage_and_video_notes](labs/resources/06_advanced-python-concepts/06_webpage_and_video_notes)
  - [06_labs](labs/resources/06_advanced-python-concepts/06_labs)
- [07 APIs and Databases](labs/resources/07_APIs_and_Databases)
  - [07_webpage_and_video_notes](labs/resources/07_APIs_and_Databases/07_webpage_and_video_notes)
  - [07_labs](labs/resources/07_APIs_and_Databases/07_labs)
- [08 Debugging](labs/resources/08_debugging)
  - [08_webpage_and_video_notes](labs/resources/08_debugging/08_webpage_and_video_notes)
  - [08_labs](labs/resources/08_debugging/08_labs)
- [09 Integrating APIs](labs/resources/09_Integrating_APIs)
- [10 Next Steps](labs/resources/10_Next_Steps)

---

## Projects

- **[Crash Blossoms CLI](https://github.com/franpanteli/CodingNomads-python-201/tree/main/labs/projects/Crash_Blossoms_CLI)**: this project was the result of following a Crash Blossoms CLI tutorial in the course. This leveraged a title-case
function to generate “Crash Blossom”-style headlines. This repeatedly asked the user for input text, which was
capitalised according to headline conventions 

- **[Python REST API Tutorial (Automation Tools)](https://github.com/franpanteli/CodingNomads-python-201/tree/main/labs/projects/Python_REST_API_Tutorial_(Automation_Tools))**: this project (webpage.py) used `HTTP` GET requests to retrieve a randomly generated dog image url a and famous
quote. These were parsed into an HTML file, outputted to the user’s desktop. These APIs were selected due to their
lack of key requirements, high potential use cases, and readable documentation. In the case that too many API
requests were made, it was recommended to use a VPN. When run in the browser, the HTML file this project
generated contained a random famous quote and a dog image  

- **[Rock Paper Scissors Game](https://github.com/franpanteli/CodingNomads-python-201/tree/main/labs/projects/Rock_Paper_Scissors_Game)**: this is a CLI-based rock-paper-scissors game. Users input a number representing their hand, and the computer
generates a random choice (its hand). The `determine_winner()` function was then defined and called to compare
these hands, print them to the console, and output the winner  

- **[File Counter](https://github.com/franpanteli/CodingNomads-python-201/tree/main/labs/projects/file_counter)**: the first purpose of this project was to analyse desktop file types. This was implemented by outputting an SQL file
to summarise desktop file counts and types. The Data_Analysis.py file outputted summary statistics of this file,
such as the most common desktop file type. The second purpose of this project was to move desktop files of the
same type that occurred in a quantity of five or more into their own desktop directory. This used the `pathlib`
module to iterate through desktop files and create relevant directories  

- **[Making the Enumerate Function](https://github.com/franpanteli/CodingNomads-python-201/tree/main/labs/projects/making_the_enumerate_function.py)**: this project recreated the Python `enumerate()` function, implementing iteration with indices. This defined a
function (`my_enumerate()`) which returned a list of tuples, that could be used in the same way as the native
Python `enumerate()` function. This project includes three .py files: my_enumerate.py (containing the defined
function), for_loops.py, and range_length.py. The latter two were written while working with the `enumerate()`
function documentation   

---

## API Capstone Project

The capstone project in the first course of this career track was a CLI-based Dungeons and Dragons game. I refactored this project three times, producing versions 1.0 - 3.0. Version 4.0 of this project was produced as the capstone project for this, the second course, in the career track. This version of the project introduces API integration, via `HTTP` `GET` requests, on two occasions. The repository containing all my versions of this project is [here](https://github.com/franpanteli/CodingNomads-python-101-capstone), and the script for Version 4.0, which I built for the capstone project in this course, is [viewable here](https://github.com/franpanteli/CodingNomads-python-101-capstone/blob/main/dungeons_and_dragon_game_4.0.py). 

### Gameplay Summary
- The player navigates through four rooms (left, right, forward, or back). As they do so, they can discover items, such as a sword or shield 
- The user's inventory is recorded via a game log 
- The user battles opponents such as dragons and goblins, with outcomes determined by a combination of weapons inventory status and a randomised dice roll
- Winning or losing a battle affects the player’s inventory 
- The game continues using, a while loop until the player chooses to exit

### Project Overview
Version 4.0 of this project integrates APIs twice:

1. **The Uzby API:** when the player starts the game, they are asked if they have a stable internet connection. The status of this is stored in the `internet_status` variable. If they have a stable connection, an `HTTP` `GET` request is made to the Uzby API. This generates a random name (stage name), whose length is the same as the user's entered name. This name is printed in the CLI. For this to work, the minimum and maximum lengths of the random name requested from the API are both set to the length of the user's entered name

2. **The Dog CEO API:** this API call implements a prize for the user, if they have a stable internet connection and defeat an opponent. This makes an `HTTP` `GET` request to generate a random dog image URL. This is presented to the user in the terminal, as a prize for defeating the opponent

This project version uses the same event logging system developed in versions 1.0 - 3.0 of the game. This logs the user's progress, choices, encounters, and outcomes in the `game_log.txt` file. This leverages the `log_status()` function to write timestamped messages. 

### Concepts Applied
- Procedural programming with function design
- File I/O, using the `open()` function in append mode to record game events  
- API integration, with the `requests` module  
- Randomisation, using the `random` module
- Game history tracking, via data logging   

---

## To Clone This Repository
```bash
git clone https://github.com/franpanteli/CodingNomads-python-301.git
