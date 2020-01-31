# Day 1 codes for practice

# flat is better than nested

# change inches to cm and change cm to inches

value = float(input('Please enter the length:'))
unit  = input('Please enter the unit:')

if unit == 'inch':
    output = 2.54 * value
    # %f means the result is float
    # %.3f means the result is float and have 3 trims
    print('%.3finches = %.3fcm' % (value, output) )

elif unit == 'cm':
    output = value / 2.54
    print('%.3fcm = %.3finches' % (value, output ))
# if end with esle, there should have no condition
else:
    print('Please enter the unit, inch or cm')

# Practice 2: The program to caculate the grades of my470 and my472
def course_grade_caculation( times , homework_per, fina_per,course_code):
    '''
    The inputs are the total times of the homework, the percent of the homeworkgrades,
    the percent of final projecs and the course_code
    the output is the final grades you get
    '''
    homework_grades = 0
    for i in range(1, times + 1):
        a = float(input('Please enter the grade of your ' +str(i)+ ' homework:'))
        homework_grades += a

    homework_grades = homework_grades * homework_per
    print('Your homework grade is :' + str(homework_grades))

    finalpro_grades = float(input('Please enter the grade of your final project:'))
    final_grades  = homework_grades + finalpro_grades * fina_per
    # accordding to the grade to decide the grade level
    if final_grades >= 70:
        level = 'Distinction'
    elif final_grades < 70 and final_grades >= 60:
        level = 'Merit'
    elif final_grades < 60 and final_grades >= 50:
        level = 'Pass'
    else:
        level = 'Fail'
    return print('Your grade of '+ str(course_code)+ ' is :' + str(final_grades)\
    +'! You get '+ level + "!" )

# test the result
MY470_grade = course_grade_caculation(10, 0.25, 0.5, 'MY470')
MY470_grade
MY472_grade = course_grade_caculation(5, 0.5, 0.5, 'MY472')
MY472_grade
