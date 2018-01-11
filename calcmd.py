import calendar
import datetime
import subprocess

week=["s","m","t","w","t","f","s"]

def create_table():
	table=[]
	for i in range(0,7):
		table.append([])
		for j in range(0,7):
			table[i].append("0")
	return table


def print_table(table):

	for i in range(0,7):
		for j in range(0,7):
			print table[i][j]+" ",
		print '\n'


def print_month(month,year):

	table=create_table()


	for i in range(0,7):
		table[0][i]=week[i]

	print(calendar.weekday(2016, 5, 15))

	"""
	i=0
	j=1
	d=1

    while True:
    	d=d+1
    	table[i][j]=d
    	"""



	print_table(table)


def main():
	today=datetime.date.today()
	y=today.year
	m=today.month
	wd=today.weekday()
	print wd
	print y
	print m
	print calendar.monthrange(y,2)[1]

print_month("april",2015)
