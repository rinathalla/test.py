import csv


def searchbyBranch():
    branch=str(input('Enter branch name : '))
    csv_file=csv.reader(open('C:/Users/Administrator/Desktop/SalesData.csv','r'))

    for row in csv_file:
        if branch==row[0]:
         print(row)

def searchbyDate():
    year=str(input('Enter date to  show data : '))
    csv_file=csv.reader(open('C:/Users/Administrator/Desktop/SalesData.csv','r'))

    for row in csv_file:
        if year in row[1]:
         print(row)

print('Choose 1 to search by branch or 2 to search by date')


src=int(input('Enter number here : '))

if src==1:
    searchbyBranch()
elif src==2:
    searchbyDate()
else:
    print('end')