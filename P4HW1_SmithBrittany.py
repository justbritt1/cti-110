# CTI-110
# P4HW1 - Score List
# Brittany Smith 
# 7/5/2022
#

def main():
    grade = 0
    total = 0
    grade_list = []
    
    num = int(input("How many scores do you want to enter: "))
    
    for i in range(0, num):
        grade = float(input('Enter score #' + str(i + 1)+':' ))
        while grade < 0 or grade > 100:
            print('INVALID Score entered!!!!')
            print('Score should be between 0 and 100')
            grade = float(input('Enter score #' + str(i + 1)+':' ))
        grade_list.append(grade)
    lowest = min(grade_list)
    grade_list.remove(lowest)
    average = sum(grade_list)/len(grade_list)
    if average >= 90:
        letter = 'A'
    elif average >= 80:
        letter = 'B'
    elif average >= 70:
        letter = 'C'
    elif average >= 60:
        letter = 'D'
    else:
        letter = 'F'
    print('-------Results-------')
    print('Lowest Score:    ', lowest)
    print('Modified List:   ', grade_list)
    print('Scores Average:  ',format(average,",.2f"))
    print('Grade:           ', letter)
        
    
main()
