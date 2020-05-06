
def main():

	weeks = input("For how many weeks do you have hours? ")
	weeks_int = int(weeks)
	counter = 1
	hours_file = open ("hours.txt", "a")


#silmukka, joka toistetaan viikkojen verran
	while weeks_int > 0:
        	this_week = input("Enter the hours for week #" + str(counter) + ": " )
        	counter = counter + 1
        	weeks_int = weeks_int - 1
        	hours_file.write(this_week + "\n")
	hours_file.close()
	print("You worked x hours" )
main()
