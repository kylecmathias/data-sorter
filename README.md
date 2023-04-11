### data_analyzer version 1.0 12/9/2022
____
## Contact information 
https://github.com/kylecmathias
___
## Description

This program takes a data sheet (in csv formating) of students containing the information of their: School, Age, Health, Failures, Absences, G1, G2, and G3. The program can sort the data, make a histogram of specfic attributes, get the worst or best grades depending on which attribute you chose. Note you must load the data first. 
___
## Installation
___
### Make sure you have Python 3.6 installed and every other basic file needed.
___
### Installing Pip the Package manager [Pip](https://pip.pypa.io/en/stable/installation/) (version 22.3.1)
___
1. Open CMD Once in CMD make sure you have pip and python installed
```
python -m pip install -U pip
```
2. Check if pip and python are installed correctly

### Checking Python

```
python --version
```
### Checking Pip
```
pip -V
```
___
### Installing Matplotlib (version 3.6.2), NumPy (version 1.23.5), SciPy (version 1.9.3)
___

3. Still in CMD install Matplotlib
#### We do this by using pip
```
pip install matplotlib
```
4. Install NumPy  

#### Still using pip
```
pip install matplotlib
```
5. Install SciPy


#### Still using pip

```
pip install scipy
```
___
### If you have downloaded all the previous items and have not taken any file out of the package this README was in you will now be able to run the file. 
___
### Make sure your data set is in the file, it must be in the file to run the data set. 
___
## Usage
This program has two ui's you can use; theres a batch file and a text ui.
___  
To use the text ui open the file labled: text_ui.py  
Once opened in your perfered python interpreter click the run button and the following code in the command prompt should show up. 
```
The available commands are:

1. L)oad Data

2. S)ort Data
'School' 'Age' 'StudyTime' 'Failures' 'Health' 'Absences' 'G1' 'G2' 'G3' 'G_Avg'

3. H)istogram
'School' 'Age' 'StudyTime' 'Failures' 'Health' 'Absences'

4. W)orst _____ for Grades
 'Age' 'StudyTime' 'Failures' 'Health' 'Absences'

5. B)est _____ for Grades
 'Age' 'StudyTime' 'Failures' 'Health' 'Absences'

6. Q)uit

Please type your command:
```
Figure 1  
Hint: Use the Load data first and make sure your file you are trying to load is in the same folder as all the programs.
Hint 2: To use a command type the first letter then a bracket e.g. 
```
Please type your commmand: L)
```
e.g.2 how to use a command. Once you input a command the following will show up.
```
Please type your commmand: L)

Please enter the name of file: <file name here>

Please enter the attribute to use as a key: <attribuite here>

Data Loaded 
<original command prompt in figure 1 is shown>
```
Figure 2  
Hint: the attributes usable are as follows: Age, School, Health, Failures.
___
To use the batch file open the filed named batch_ui.py  
Once opened run the file and it will prompt you with 
```
Please enter the name of the file where your commands are stored:
```
To use this file you need a text file which has a list of commands. For example of a text file you could use. 
```
L; <data file goes here>
s Health N
b Age
W Health
q
w Age
B Failures
```
Figure 3  
Hint: L; has to go first, and the commands are the same as the ones in the text_ui, see figure 1 for examples, this time they are just the letters  
It will print the desired outcomes, for example 'h' will make a histogram (same with the text_ui).
___
## [License](https://www.gnu.org/licenses/gpl-3.0.en.html)
___

