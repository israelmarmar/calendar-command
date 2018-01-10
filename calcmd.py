import calendar
import datetime

week=["m","t","w","t","f","s","s"]

def print_month():
	for w in week:
		print w,


def main():
	today=datetime.date.today()
	y=today.year
	m=today.month
	wd=today.weekday()
	print wd
	print y
	print m
	print calendar.monthrange(y,2)[1]

print_month()
