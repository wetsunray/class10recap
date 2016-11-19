#Midterm Statistics
#thi
"""
----------------------------------------------------------------------------------------------------------------------------------------
Problem 1:
----------------------------------------------------------------------------------------------------------------------------------------
Write a function called classGrades that takes in a string, infile, which contains the name of a file.
The file contains the following details. 


id exam1 exam2 homework attendance project1 project2 classrecap

Example:
32165487 10 70 50 40 100 80 50
21321853 52 95 72 56 95 32 56
41861235 95 12 47 32 68 92 35
84534853 58 38 84 84 89 68 74

Note: The data is tab deliminated. You can find the sample files on moodle.
The function should return a dictionairy where the key is the id, and the value is a dictioniary.
The value-dictionairy should have the following keys: id exam1 exam2 homework attendance project1 project2 classrecap
and the values which will be read in the file.

For example
{'32165487':{'id':'32165487','exam1':10,'exam2':70,'pta':30,'homework':50,'attendance':40,'project1':100,'project2':80,'classrecap':50}}

----------------------------------------------------------------------------------------------------------------------------------------
"""


def classGrades(inFile):
    inF = open(inFile, 'r')
    content = inF.read().split('\n')
    key = {0: 'id',
           1: 'exam1',
           2: 'exam2',
           3: 'homework',
           4: 'attendance',
           5: 'project1',
           6: 'project2',
           7: 'classrecap'}
    rtnDict = {}
    for line in content:
        count = 0
        if line == "":
            continue
        line = line.split()
        rtnDict[line[0]] = {}
        for word in line:
            if count == 0:
                rtnDict[line[0]][key[count]] = line[count]
            else:
                rtnDict[line[0]][key[count]] = int(line[count])
            count += 1
    inF.close()
    return rtnDict

"""
Problem 2:
----------------------------------------------------------------------------------------------------------------------------------------
Write a function called examStats that takes in a dictionary, gradeBook, and computes the average for both exam1, and exam2 and returns a
dictionary with average, median, and range for each exam. Refer to the example for a sample output.



Input will be the dictionary that problem 1 generates.
output will be the following dictionary:
{"exam1": {"average": 58, "median": 60, "range":78}, "exam2": {"average": 65, "median": 69, "range":54}}

----------------------------------------------------------------------------------------------------------------------------------------
"""
#grade number fetcher
def gradeFetcher(gradeBook, gradeType):
    rtnLst = []
    for key in gradeBook:
        rtnLst.append(gradeBook[key][gradeType])
    return rtnLst

#math functions
def average(numList):
    return sum(numList)/len(numList)
def median(numList):
    srtLst = sorted(numList)
    if len(srtLst)%2 == 1:
        median = srtLst[len(srtLst)/2]
    else:
        median = (srtLst[int(len(srtLst)/2 - 0.5)] + srtLst[int(len(srtLst)/2 + 0.5)])/2
    return median
def theRange(numList):
    srtLst = sorted(numList)
    return srtLst[-1] - srtLst[0]

def examStats(gradeBook):
    exam1grades = gradeFetcher(gradeBook, 'exam1')
    exam1average = average(exam1grades)
    exam1median = median(exam1grades)
    exam1range = theRange(exam1grades)
    exam2grades = gradeFetcher(gradeBook, 'exam2')
    exam2average = average(exam2grades)
    exam2median = median(exam2grades)
    exam2range = theRange(exam2grades)
    rtnDict = {"exam1": {"average": exam1average,
                         "median": exam1median,
                         "range": exam1range},
               "exam2": {"average": exam2average,
                         "median": exam2median,
                         "range": exam2range}
               }
    return rtnDict
    


"""
Problem 3:
----------------------------------------------------------------------------------------------------------------------------------------
Write a function called finalExamGrade that will find what a student needs to get in order to get each letter grade. This function will
take as input a dictionary called student. It will contain all the grades of a single student. The function should find out exactly what
grade the student needs to get an A, B+, B, C+, C, and D. It should return a dictionary that will map each letter to the needed grade.
You will need following information to calculate the grade:

letterGradeScale: {'A': 90, 'B+': 85, 'B':80, 'C+': 75, 'C': 70, 'D': 65}

Grading Formula:
Homework - 10%
Attendance - 4%
Exam1, Exam2 - 20% each
Final Exam - 30%
Roadmap project - Project 1 & project 2 - 5% each
Class Recap - 6%


output:
{'A': 98, 'B+': 92, 'B': 85, 'C+': 80, 'C': 74, 'D': 68}

----------------------------------------------------------------------------------------------------------------------------------------
Tips:
----------------------------------------------------------------------------------------------------------------------------------------
1.Grading formula: You can hard code these numbers in the actual calculation to keep it simple, however if you want to make this
as generic as possible, you can take in another dictionary with appropriate values.

2. You should start checking from Highest possible grade to make it simple.

3. If there is no way a person can get a specific letter grade, then assign the value "N/A" to appropriate letter grade.

----------------------------------------------------------------------------------------------------------------------------------------
"""


def finalExamGrade(student, letterGradeScale):
    #student is a dictionary:
    #{'id': '74085657', 'project1': 6, 'homework': 44, 'exam2': 69, 'exam1': 52, 'classrecap': 21, 'project2': 87, 'attendance': 43}
    #letterGradeScale is a dictionary:
    #{'A': 90, 'B+': 85, 'B':80, 'C+': 75, 'C': 70, 'D': 65}
    """
    Grading Formula:
    Homework - 10%
    Attendance - 4%
    Exam1, Exam2 - 20% each
    Final Exam - 30%
    Roadmap project - Project 1 & project 2 - 5% each
    Class Recap - 6%
    """
    totalGrade = 0
    totalGrade += student['homework'] * 0.10
    totalGrade += student['attendance'] * 0.04
    totalGrade += student['exam1'] * 0.20
    totalGrade += student['exam2'] * 0.20
    totalGrade += student['project1'] * 0.05
    totalGrade += student['project2'] * 0.05
    totalGrade += student['classrecap'] * 0.06
    print(totalGrade)
    A = (letterGradeScale['A'] - totalGrade) / 0.30
    Bp = (letterGradeScale['B+'] - totalGrade) / 0.30
    B = (letterGradeScale['B'] - totalGrade) / 0.30
    Cp = (letterGradeScale['C+'] - totalGrade) / 0.30
    C = (letterGradeScale['C'] - totalGrade) / 0.30
    D = (letterGradeScale['D'] - totalGrade) / 0.30
    aKey = {A:'A',
            Bp:'B+',
            B:'B',
            Cp: 'C+',
            C:'C',
            D: 'D',}
    rtnDict = {}
    rnLst = [A, Bp, B, Cp, C, D]
    for grade in rnLst:
        if grade > 100:
            rtnDict[aKey[grade]] = 'N/A'
        else:
            rtnDict[aKey[grade]] = grade
    return rtnDict


    
"""
Problem 4:
----------------------------------------------------------------------------------------------------------------------------------------
Write a function called generateReport, that will take as input a dictionary gradeBook, that is generated from problem 1. This function
will write to a file all students grades, and what they need to get their best possible grade on the final exam. The file must contain
the appropriate column headers on the first line. This will be a tab deliminated file.

Output:
ID    Exam1    Exam2    Homework    Attendance    Project1    Project2    Class Recap    Final Grade    Potential Grade
32165487    10    70    50    40    100    80    50    100    D
21321853    52    95    72    56    95    32    56    100    C+
41861235    95    12    47    32    68    92    35    100    D
84534853    58    38    84    84    89    68    74    100    C


NOTE: Do not worry about making it look pretty. it should look exactly how it looks in the above example. Everything is tab deliminated,
and you have learned how to add tabs using special characters.

"""

def potentialGrade(gradeBook, ID):
    #I already made a generic version of this above
    letterGradeScale = {'A': 90, 'B+': 85, 'B':80, 'C+': 75, 'C': 70, 'D': 65}
    totalGrade = 0
    totalGrade += gradeBook[ID]['homework'] * 0.10
    totalGrade += gradeBook[ID]['attendance'] * 0.04
    totalGrade += gradeBook[ID]['exam1'] * 0.20
    totalGrade += gradeBook[ID]['exam2'] * 0.20
    totalGrade += gradeBook[ID]['project1'] * 0.05
    totalGrade += gradeBook[ID]['project2'] * 0.05
    totalGrade += gradeBook[ID]['classrecap'] * 0.06
    totalGrade += 30 #100 on the final exam, times 0.30
    if totalGrade >= 90:
        return 'A ' + str(totalGrade)
    elif totalGrade >= 85:
        return 'B+ ' + str(totalGrade)
    elif totalGrade >= 80:
        return 'B ' + str(totalGrade)
    elif totalGrade >= 75:
        return 'C+ ' + str(totalGrade)
    elif totalGrade >= 70:
        return 'C ' + str(totalGrade)
    elif totalGrade >= 65:
        return 'D ' + str(totalGrade)  
    else:
        return "failed " + str(totalGrade)
def generateReport(gradeBook):
    header = ['ID', 'Exam1', 'Exam2', 'Homework', 'Attendance', 'Project1', 'Project2', 'Class Recap', 'Final Grade', 'Potential Grade']
    outF = open("report.txt", 'w')
    firstLine = ""
    for string in header:
        firstLine += string + '\t'
    firstLine += '\n'
    outF.write(firstLine)

    headerKeys = ['exam1', 'exam2', 'homework', 'attendance', 'project1', 'project2', 'classrecap']
    for ID in gradeBook:
        eachLine = ""
        eachLine += ID
        for item in headerKeys:
            eachLine += str(gradeBook[ID][item]) + '\t'
        eachLine += str(100) + '\t'
        eachLine += potentialGrade(gradeBook, ID)
        eachLine += '\n'
        outF.write(eachLine)
        
    outF.close()


"""runtime functions below"""


def test_suite():
    ###Problem 1
    #alter the file name to test different mock data
    gradeBook = classGrades("MOCK_DATA.txt")
    print(gradeBook)

    ###Problem 2
    
    #print("\n\nclass grades:", gradeBook)
    #print("\n\ngradeFetcher:", gradeFetcher(gradeBook, "exam1"))
    #print("\n\nexamStats:", examStats(gradeBook))
    
    ###Problem 3

    student = {'id': '74085657', 'project1': 6, 'homework': 44, 'exam2': 69, 'exam1': 52, 'classrecap': 21, 'project2': 87, 'attendance': 43}
    letterGradeScale = {'A': 90, 'B+': 85, 'B':80, 'C+': 75, 'C': 70, 'D': 65}
    #print(finalExamGrade(student, letterGradeScale))

    ###Problem 4
    ###Check to make sure that file output is correct
    generateReport(gradeBook)

def main():
    test_suite()
if __name__ == "__main__":
    main()
