###############  HW  Functions      HW  Functions         HW  Functions       ###############
#%%
# ######  QUESTION 1   First, review Looping    ##########
# Write python codes to print out the four academic years for a typical undergrad will spend here at GW. 
# Starts with Sept 2021, ending with May 2025 (total of 45 months), with printout like this:
# Sept 2021
# Oct 2021
# Nov 2021
# ...
# ...
# Apr 2025
# May 2025
# This might be helpful:
# If you consider Sept 2021 as a number 2021 + 8/12, you can continue to loop the increament easily 
# and get the desired year and month. (If the system messes up a month or two because of rounding, 
# that's okay for this exercise).
# And use this (copy and paste) 
# monthofyear = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec')
# to simplify your codes.


month_of_year = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec') #month-of-year-tuple
year_of_school = ('2021','2022','2023','2024','2025') #year-of-school-tuple

months = 46

for month in range(months):
    output = "{month} {year}".format(month=month_of_year, year=year_of_school)
    print(output)




###############  Now:     Functions          Functions             Functions       ###############
# We will now continue to complete the grade record that we were working on in class.

#%%
###################################### Question 2 ###############################
# let us write a function find_grade(total) 
# which will take your course total (0-100), and output the letter grade (see your syllabus)
# have a habbit of putting in the docstring
total = 62.1 

def find_grade(total):
    """
    The following is the if statments to determine letter GPA.
    """
    if total <60 :
        grade = "F"
    elif total <70 :
        grade = "D"
    elif total <73 :
        grade = "C-"
    elif total <77 :
        grade = "C"
    elif total <80 :
        grade = "C+"
    elif total <83 :
        grade = "B-"
    elif total <87 :
        grade = "B"
    elif total <90 :
        grade = "B+"
    elif total <93 :
        grade = "A-"
    elif total <100 :
        grade = "A"

    return grade

print(find_grade(total))


# Also answer these: 
# What is the input (function argument) data type for total? 
# What is the output (function return) data type for find_grade(total) ?


#%%
###################################### Question 3 ###############################
# next the function to_gradepoint(grade)
# which convert a letter grade to a grade point. A is 4.0, A- is 3.7, etc
grade = 'C-'

def to_gradepoint(grade):
  if grade == "A" :
    gradepoint = 4.0
  elif grade == "A-" :
    gradepoint = 3.7
  elif grade == "B+" :
    gradepoint = 3.3
  elif grade == "B" :
    gradepoint = 3.0
  elif grade == "B-" :
    gradepoint = 2.7
  elif grade == "C+" :
    gradepoint = 2.3
  elif grade == "C" :
    gradepoint = 2.0
  elif grade == "C-" :
    gradepoint = 1.7
  elif grade == "D+" :
    gradepoint = 1.3
  elif grade == "D" :
    gradepoint = 1.0
  elif grade == "F" :
    gradepoint = 0.0
  # write an appropriate and helpful docstring
  # ??????    fill in your codes here, be sure you have all A, A-, ... thru D, and F grades completed.
  # gradepoint = ???
  return gradepoint

# Try:
print(to_gradepoint(grade))

# What is the input (function argument) data type for find_grade? 
# What is the output (function return) data type for find_grade(grade) ?


#%%
###################################### Question 4 ###############################
# next the function to_gradepoint_credit(course)
# which calculates the total weight grade points you earned in one course. Say A- with 3 credits, that's 11.1 total grade_point_credit
course = { "class":"IntroDS", "id":"DATS 6101", "semester":"spring", "year":2018, "grade":'B-', "credits":3 } 

def to_gradepoint_credit(course):
  if course["grade"] == "A" :
    grade_point_credit = 4.0 * course["credits"]
  elif course["grade"] == "A-" :
    grade_point_credit = 3.7 * course["credits"]
  elif course["grade"] == "B+" :
    grade_point_credit = 3.2 * course["credits"]
  elif course["grade"] == "B" :
    grade_point_credit = 3.0 * course["credits"]
  elif course["grade"] == "B-" :
    grade_point_credit = 2.7 * course["credits"]
  elif course["grade"] == "C+" :
    grade_point_credit = 2.3 * course["credits"]
  elif course["grade"] == "C" :
    grade_point_credit = 2.0 * course["credits"]
  elif course["grade"] == "C-" :
    grade_point_credit = 1.7 * course["credits"]
  elif course["grade"] == "D+" :
    grade_point_credit = 1.3 * course["credits"]
  elif course["grade"] == "D" :
    grade_point_credit = 1.0 * course["credits"]
  elif course["grade"] == "F" :
    grade_point_credit = 0.0 * course["credits"]

  # write an appropriate and helpful docstring
  # ??????    fill in your codes here
  # grade_point_credit = ?????
  # eventually, if you need to print out the value to 2 decimal, you can 
  # try something like this for floating point values %f
  # print(" %.2f " % grade_point_credit)
  return grade_point_credit

# Try:
print(" %.2f " % to_gradepoint_credit(course) )

# What is the input (function argument) data type for to_gradepoint_credit? 
# What is the output (function return) data type for to_gradepoint_credit(course) ?


#%%
###################################### Question 5 ###############################
# next the function gpa(courses) to calculate the GPA 
# It is acceptable syntax for list, dictionary, JSON and the likes to be spread over multiple lines.
courses = [ 
  { "class":"Intro to DS", "id":"DATS 6101", "semester":"spring", "year":2020, "grade":'B-', "credits":3 } , 
  { "class":"Data Warehousing", "id":"DATS 6102", "semester":"fall", "year":2020, "grade":'A-', "credits":4 } , 
  { "class":"Intro Data Mining", "id":"DATS 6103", "semester":"spring", "year":2020, "grade":'A', "credits":3 } ,
  { "class":"Machine Learning I", "id":"DATS 6202", "semester":"fall", "year":2020, "grade":'B+', "credits":4 } , 
  { "class":"Machine Learning II", "id":"DATS 6203", "semester":"spring", "year":2021, "grade":'A-', "credits":4 } , 
  { "class":"Visualization", "id":"DATS 6401", "semester":"spring", "year":2021, "grade":'C+', "credits":3 } , 
  { "class":"Capstone", "id":"DATS 6101", "semester":"fall", "year":2021, "grade":'A-', "credits":3 } 
  ]


def find_gpa(courses):
  """insert docstrings here"""
  total_grade_point_credit = 0  # initialize
  total_credits = 0  # initialize
  for course in courses:
    total_grade_point_credit += to_gradepoint_credit(course)
    total_credits += course["credits"]

  gpa = total_grade_point_credit/total_credits

  return gpa
  
  # write an appropriate and helpful docstring
  # ?????? fill in your codes here
  # gpa = ?????

# Try:
print(" %.2f " % find_gpa(courses) )

# What is the input (function argument) data type for find_gpa? 
# What is the output (function return) data type for find_gpa(courses) ?


#%%
###################################### Question 6 ###############################
# Write a function to print out a grade record for a single class. 
# The return statement for such functions should be None or just blank
# while during the function call, it will display the print.
course = { "class":"IntroDS", "id":"DATS 6101", "semester":"spring", "year":2018, "grade":'B-', "credits":3 } 

def printCourseRecord(course):
    GPC = " %.2f " %to_gradepoint_credit(course)
    output = "{year} {semester} - {id} : {class_name} ({credits} credits) {grade} Grade point credits: {GPC}".format(year=course["year"], semester=course["semester"], id=course["id"], class_name=course["class"], credits=course["credits"], grade=course["grade"], GPC = GPC)
    print(output)
  # write an appropriate and helpful docstring
  # use a single print() statement to print out a line of info as shown here
  # 2018 spring - DATS 6101 : Intro to DS (3 credits) B-  Grade point credits: 8.10 
  # ??????    fill in your codes here
    return  # or return None
  
# Try:
printCourseRecord(course)

# What is the input (function argument) data type for printCourseRecord? 
# What is the output (function return) data type for printCourseRecord(course) ?


#%%
###################################### Question 7 ###############################
# write a function (with arguement of courses) to print out the complete transcript and the gpa at the end
# 2018 spring - DATS 6101 : Intro to DS (3 credits) B-  Grade point credits: 8.10 
# 2018 fall - DATS 6102 : Data Warehousing (4 credits) A-  Grade point credits: 14.80 
# ........  few more lines
# Cumulative GPA: ?????
courses = [ 
  { "class":"Intro to DS", "id":"DATS 6101", "semester":"spring", "year":2020, "grade":'B-', "credits":3 } , 
  { "class":"Data Warehousing", "id":"DATS 6102", "semester":"fall", "year":2020, "grade":'A-', "credits":4 } , 
  { "class":"Intro Data Mining", "id":"DATS 6103", "semester":"spring", "year":2020, "grade":'A', "credits":3 } ,
  { "class":"Machine Learning I", "id":"DATS 6202", "semester":"fall", "year":2020, "grade":'B+', "credits":4 } , 
  { "class":"Machine Learning II", "id":"DATS 6203", "semester":"spring", "year":2021, "grade":'A-', "credits":4 } , 
  { "class":"Visualization", "id":"DATS 6401", "semester":"spring", "year":2021, "grade":'C+', "credits":3 } , 
  { "class":"Capstone", "id":"DATS 6101", "semester":"fall", "year":2021, "grade":'A-', "credits":3 } 
  ]

def printTranscript(courses):
  # write an appropriate and helpful docstring
 
  for course in courses:
    printCourseRecord(course)

    # print out each record as before
  
  # after the completion of the loop, print out a new line with the gpa info
  print("Cumulative GPA:", " %.2f " %find_gpa(courses))
  return # or return None

# Try to run, see if it works as expected to produce the desired result
# courses is already definted in Q4
printTranscript(courses)
# The transcript should exactly look like this: 
# 2020 spring - DATS 6101 : Intro to DS (3 credits) B- Grade point credits: 8.10
# 2020 fall - DATS 6102 : Data Warehousing (4 credits) A- Grade point credits: 14.80
# 2020 spring - DATS 6103 : Intro Data Mining (3 credits) A Grade point credits: 12.00
# 2020 fall - DATS 6202 : Machine Learning I (4 credits) B+ Grade point credits: 13.20
# 2021 spring - DATS 6203 : Machine Learning II (4 credits) A- Grade point credits: 14.80
# 2021 spring - DATS 6401 : Visualization (3 credits) C+ Grade point credits: 6.90
# 2021 fall - DATS 6101 : Capstone (3 credits) A- Grade point credits: 11.10
# Cumulative GPA: 3.37

# What is the input (function argument) data type for printTranscript?
#  
# What is the output (function return) data type for printTranscript(courses) ?



#%% 
# ######  QUESTION 8   Recursive function   ##########
# Write a recursive function that calculates the Fibonancci sequence.
# The recusive relation is fib(n) = fib(n-1) + fib(n-2), 
# and the typically choice of seed values are fib(0) = 0, fib(1) = 1. 
# From there, we can build fib(2) and onwards to be 
# fib(2)=1, fib(3)=2, fib(4)=3, fib(5)=5, fib(6)=8, fib(7)=13, ...
# Let's set it up from here:

def fib(n):

  """
  Finding the Fibonacci sequence with seeds of 0 and 1
  The sequence is 0,1,1,2,3,5,8,13,..., where 
  the recursive relation is fib(n) = fib(n-1) + fib(n-2)
  :param n: the index, starting from 0
  :return: the sequence
  """
  if n <= 1:
    return n
  return fib(n-1) + fib(n-2)
  # assume n is positive integer
  # ??????    fill in your codes here

  return # return what ????


# Try:
for i in range(12):
  print(fib(i))  



#%% 
# ######  QUESTION 9   Recursive function   ##########
# Similar to the Fibonancci sequence, let us create one (say dm_fibonancci) that has a  
# modified recusive relation dm_fibonancci(n) = dm_fibonancci(n-1) + 2* dm_fibonancci(n-2) - dm_fibonancci(n-3). 
# Pay attention to the coefficients and their signs. 
# And let us choose the seed values to be dm_fibonancci(0) = 1, dm_fibonancci(1) = 1, dm_fibonancci(2) = 2. 
# From there, we can build dm_fibonancci(3) and onwards to be 1,1,2,3,6,10,...
# Let's set it up from here:

def dm_fibonancci(n):
  """
  Finding the dm_Fibonacci sequence with seeds of 1, 1, 2 for n = 0, 1, 2 respectively
  The sequence is 0,1,1,2,3,5,8,13,..., where 
  the recursive relation is dm_fibonancci(n) = dm_fibonancci(n-1) + 2* dm_fibonancci(n-2) - dm_fibonancci(n-3)
  :param n: the index, starting from 0
  :return: the sequence
  """
  if n == 0:
    return n + 1
  elif 1 <= n <= 2:
     return n
  return dm_fibonancci(n-1) + 2*dm_fibonancci(n-2) - dm_fibonancci(n-3)
for i in range(12):
  print(dm_fibonancci(i))  # should gives 1,1,2,3,6,10,...




#%%
