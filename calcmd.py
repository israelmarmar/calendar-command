import calendar
import datetime
import subprocess
import sys

week=["s","m","t","w","t","f","s"]

month_lst = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 
              'August', 'September', 'October', 'November', 'December']

def create_table():
	table=[]
	for i in range(0,7):
		table.append([])
		for j in range(0,7):
			table[i].append(" ")
	return table


def print_table(table):

	row_format ="{:>3}" * (len(week) + 1)

	for row in table:
                print (row_format.format("",*row))

def create_month(month,year,today,tmonth):
	table=create_table()

	table[0]=week

	j=1
	d=1
	wd=0
	enday=calendar.monthrange(year,month)[1]

	if calendar.weekday(year, month, d)+1<7:
			wd = calendar.weekday(year, month, d)+1
	else:
		wd=0

	while (d < enday+1):

		table[j][wd]=d

		if d==today and month==tmonth:
			table[j][wd]="\033[47;30m "+str(d)+"\033[m"
		d=d+1
		wd=wd+1

		if wd==7:
		   j=j+1
		   wd=0

	return table

def print_month(month,year,today,tmonth):

	table=create_month(month,year,today,tmonth)

	print ("     "+month_lst[month-1]+" "+str(year))
	print_table(table)

def print_year(year,today,tmonth):
	print ("     "+str(year))
	for m in range(1,13):
		print_month(m,year,today,tmonth)


def main():
	today=datetime.date.today()
	y=today.year
	m=today.month

	"""
	print_month(m,y,today.day,m)
	"""
	print sys.argv
	if len(sys.argv)==1:
		print_month(m,y,today.day,m)
	elif len(sys.argv)==2:
		print_year(int(sys.argv[1]),today.day,m)
	elif len(sys.argv)==3:
		print_month(int(sys.argv[1]),int(sys.argv[2]),today.day,m)
main()
