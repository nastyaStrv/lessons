grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

average = (sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]),
sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4]))
print(average)
students_my = sorted(students)
print(students_my)

total = ({students_my[0]:average[0], students_my[1]:average[1], students_my[2]:average[2],
          students_my[3]:average[3], students_my[4]:average[4]})
print(total)

total_2 = dict(zip(students_my,average))
print(total_2)
