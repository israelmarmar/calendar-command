import calendar
import datetime
import subprocess

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
		print row_format.format("",*row)



def print_month(month,year,today):

	table=create_table()

	table[0]=week

	j=1
	d=1
	wd=0
	enday=calendar.monthrange(year,month)[1]

	while (d < enday+1):
		if calendar.weekday(year, month, d)+1<7:
			wd = calendar.weekday(year, month, d)+1
		else:
			wd = 0

		table[j][wd]=d

		if d==today:
			table[j][wd]="\033[47;30m "+str(d)+"\033[m"
		d=d+1

		if wd==6:
		   j=j+1

	print "     "+month_lst[month-1]+" "+str(year)
	print_table(table)


def main():
	today=datetime.date.today()
	y=today.year
	m=today.month
	print_month(m,y,today.day)


main()
