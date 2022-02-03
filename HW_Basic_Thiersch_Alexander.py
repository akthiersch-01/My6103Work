#%%
# print("Hello world!")

print("Hello Word!")

#%%[markdown]
# Question 1: Create a Markdown cell with the followings:
# Two paragraphs about yourself. In one of the paragraphs, give a hyperlink of a website 
# that you want us to see. Can be about yourself, or something you like.
#
#My name is Alex Thiersch. I am a current grad student at GWU pursuing a M.S. in Applied Economics.
#I am interested in working in the fields of Health Economics, Social Epidemiology, or Health Policy.
#My hobbies include listening to music and collecting sneakers.
#  
#I am originally from Seattle, WA. When I am in Washington I enjoy skiing and hiking.
#Additionally, I enjoy driving to Whistler, Canada in the summer and the winter for vacation.
#Here is a link to my favorite gondola ride in Whistler called the Peak2Peak Gondola: <https://www.google.com/search?q=whistler+peak+to+peak+view&tbm=isch&ved=2ahUKEwjtyry27t31AhV4n3IEHc-kDL0Q2-cCegQIABAA&oq=whistler+peak+to+peak+view&gs_lcp=CgNpbWcQAzoFCAAQgAQ6BAgAEEM6BggAEAcQHjoGCAAQCBAeOgQIABAeOgYIABAFEB5QrQZYqw9gsRFoAHAAeACAASqIAdEBkgEBNpgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=PtH4Ye2zG_i-ytMPz8my6As&bih=923&biw=1324&client=safari&safari_group=9#imgrc=4daSr8mloDIb7M>.



#%%
# Question 2: Create
# a list of all the class titles that you are planning to take in the data science program. 
# Have at least 6 classes, even if you are not a DS major
# Then print out the last entry in your list.

DS_class_list = ["DATS 6101: Intro to Data Science ", "DATS 6102: Data Warehousing", "DATS 6103: Intro to Data Mining", "DATS 6202: Machine Learning I", "DATS 6203: Machine Learning II", "DATS 6401: Visualization of Complex Data"]
print(DS_class_list[5])


#%%
# Question 3: After you completed question 2, you feel Intro to data mining is too stupid, so you are going 
# to replace it with Intro to Coal mining. Do that in python here.

DS_class_list = ["DATS 6101: Intro to Data Science", "DATS 6102: Data Warehousing", "DATS 6103: Intro to Data Mining", "DATS 6202: Machine Learning I", "DATS 6203: Machine Learning II", "DATS 6401: Visualization of Complex Data"]
DS_class_list[2] = "DATS ????: Intro to Coal Mining"
print(DS_class_list)
print(DS_class_list[2])

#%%
# Question 4: Before you go see your acadmic advisor, you are 
# asked to create a python dictionary of the classes you plan to take, 
# with the course number as key. Please do that. Don't forget that your advisor 
# probably doesn't like coal. And that coal mining class doesn't even have a 
# course number.

DS_class_dict = {
    6101 : "Intro to Data Science",
    6102 : "Data Warehousing",
    6103 : "Intro to Data Mining",
    6202 : "Machine Learning I",
    6203 : "Machine Learning II",
    6401 : "Visualization of Complex Data"
}

DS_class_dict[6202]

#%%
# Question 5: print out and show your advisor how many 
# classes (print out the number, not the list/dictionary) you plan 
# to take.

DS_class_total = len(DS_class_dict)

print("The number of Data Science classes I will take is:", DS_class_total)

#%%
# Question 6: Using loops 
# Goal: print out the list of days (31) in Jan 2022 like this
# Sat - 2022/1/1
# Sun - 2022/1/2
# Mon - 2022/1/3
# Tue - 2022/1/4
# Wed - 2022/1/5
# Thu - 2022/1/6
# Fri - 2022/1/7
# Sat - 2022/1/8
# Sun - 2022/1/9
# Mon - 2022/1/10
# Tue - 2022/1/11
# Wed - 2022/1/12
# Thu - 2022/1/13
# ...
# You might find something like this useful, especially if you use the remainder property x%7

import datetime

day_of_week_tuple = ('Mon','Tue','Wed','Thu','Fri','Sat','Sun') # day-of-week-tuple

year = 2022
month = 1
start_day = 1

days = 31

for day in range(days):
    weekday = datetime.date(year, month, day+1).weekday()
    output = "{weekday} - {year}/{month}/{day}".format(weekday=day_of_week_tuple[weekday], year=year, month=month, day=day+1)
    print(output)






# %%[markdown]
# # Additional Exercise: 
# Choose three of the five exercises below to complete.
#%%
# =================================================================
# Class_Ex1: 
# Write python codes that converts seconds, say 257364 seconds,  to 
# (x Hour, x min, x seconds)
# ----------------------------------------------------------------

def convert(seconds):
    seconds = seconds % (24*3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)

seconds = 257364
print(convert(seconds))



#%%
# =================================================================
# Class_Ex2: 
# Write a python codes to print all the different arrangements of the
# letters A, B, and C. Each string printed is a permutation of ABC.
# Hint: one way is to create three nested loops.
# ----------------------------------------------------------------

def permute(str):
    if len(str) == 0:
        return['']
    prev_list = permute(str[1:len(str)])
    next_list = []
    for i in range(0,len(prev_list)):
        for j in range(0,len(str)):
            new_str = prev_list[i][0:j]+str[0]+prev_list[i][j:len(str)-1]
            if new_str not in next_list:
                next_list.append(new_str)
    return next_list

print(permute('ABC'))



#%%
# =================================================================
# Class_Ex3: 
# Write a python codes to print all the different arrangements of the
# letters A, B, C and D. Each string printed is a permutation of ABCD.
# ----------------------------------------------------------------
def permute(str):
    if len(str) == 0:
        return['']
    prev_list = permute(str[1:len(str)])
    next_list = []
    for i in range(0,len(prev_list)):
        for j in range(0,len(str)):
            new_str = prev_list[i][0:j]+str[0]+prev_list[i][j:len(str)-1]
            if new_str not in next_list:
                next_list.append(new_str)
    return next_list

print(permute('ABCD'))




#%%
# =================================================================
# Class_Ex4: 
# Suppose we wish to draw a triangular tree, and its height is provided 
# by the user, like this, for a height of 5:
#      *
#     ***
#    *****
#   *******
#  *********
# ----------------------------------------------------------------





#%%
# =================================================================
# Class_Ex5: 
# Write python codes to print prime numbers up to a specified 
# values, say up to 200.
# ----------------------------------------------------------------

def prime_num_list(num):
    for number in range(num+1):
        if number > 1:
        
            for factor in range(2,number):
                if number%factor == 0:
                    break
            else:
                print(number)


prime_num_list(200)

# =================================================================

# %%
