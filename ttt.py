from __futrue__ import division
import random

def score(score_list,course_list,student_num):
    coures_num = len(course_list)

    every_score = [[score_list[j][i] for j in range(course_num)] for i in student_num ]

    every_total = [sum(erery_score[i]) for i in range(student_num)]

    ave_coures = [sum(score_list[i]/len(score_list[i]) for i in range(len(score_list))]

    return (every_score,every_total,ave_coures)

if __name__ == "__main__":

    courese_list = ["C++","Java","Servlet","jsp","Ejb"]
    student_num = 20

    score_list = [[random.randint(0,100) for i in range(student_num)]]

from collections import deque

queue = deque(["Eric","John","Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft()
queue.popleft()

squares = []
for x in range(10):
    squares.append(x**2)

squares

squares = [x**3 for x in range(10)]

squares = list(map(lambda x: x**2,range(10)))

[(x,y) for x in [1,2,3] for y in [3,1,4] ]

combs =[]
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x,y))

combs