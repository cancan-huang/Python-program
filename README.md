# Python-program
## Day 1
Day 1 include two parts of codes
*1st,The code to convert inch to cm, and cm to inch*
```
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
```

*2nd, The code to caculate couse grade in LSE*

```
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
```
