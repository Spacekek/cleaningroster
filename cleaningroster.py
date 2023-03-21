# create cleaning roster
# data is stored in people.txt and tasks.txt
# people.txt is a list of people, one per line
# tasks.txt is a list of tasks followed by how many people should do the task each week, one per line
# output is csv file with people and tasks for each week

import random
import pandas as pd
import datetime as dt

def get_people():
    people = []
    with open('people.txt') as f:
        for line in f:
            people.append(line.strip())
    return people

def get_tasks():
    tasks = []
    with open('tasks.txt') as f:
        for line in f:
            tasks.append(line.split(' ')[0])
    return tasks

if __name__ == '__main__':
    people = get_people()
    tasks = get_tasks()
    # put in following format in csv file:
    # date                  task3\n person3\n person4       empty       empty
    # task1\n person1       task4\n person5\n person6       empty       empty
    # task2\n person2       task5\n person7\n person8       empty       empty

    df = pd.DataFrame(index=[], columns=tasks)
    for i in range(0, 104, 3):
        # tasks 1 and 2 cycle while the rest are random from the remaining people
        people_copy = people.copy()
        person_task1 = people_copy.pop(i%len(people_copy))
        person_task2 = people_copy.pop(i%len(people_copy))
        date = dt.date(2023, 3, 21) + dt.timedelta(days=i/3*7)
        # first line: date  task3\n person3\n person4       empty       empty
        df.loc[i, tasks[0]] = date.strftime('%d/%m/%Y')
        df.loc[i, tasks[1]] = tasks[2]
        df.loc[i, tasks[2]] = people_copy.pop(random.randint(0, len(people_copy)-1)) + '\n' + people_copy.pop(random.randint(0, len(people_copy)-1))
        # second line: task1\n person1       task4\n person5\n person6       empty       empty
        df.loc[i+1, tasks[0]] = tasks[0] + '\n' + person_task1
        df.loc[i+1, tasks[1]] = tasks[3]
        df.loc[i+1, tasks[2]] = people_copy.pop(random.randint(0, len(people_copy)-1)) + '\n' + people_copy.pop(random.randint(0, len(people_copy)-1))
        # third line: task2\n person2       task5\n person7\n person8       empty       empty
        df.loc[i+2, tasks[0]] = tasks[1] + '\n' + person_task2
        df.loc[i+2, tasks[1]] = tasks[4]
        df.loc[i+2, tasks[2]] = people_copy.pop(random.randint(0, len(people_copy)-1)) + '\n' + people_copy.pop(random.randint(0, len(people_copy)-1))
    df.to_csv('cleaningroster.csv')
