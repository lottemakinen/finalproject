def main():	
	hours_list = []
	counter = 1
	weeks = int(input("How many weeks you have been working? "))
	for n in range(weeks):
		hours = int(input("Enter your work hours of the week " + str(counter) + ": "))
		counter = counter + 1
		hours_list.append(hours)
	print("Hours worked: ", sum(hours_list))
main()
