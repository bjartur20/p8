# Author: Bjartur Thorhallsson
# Date: 14.10.2019

'''
1. Ask the user for number of rows and seats in each row.
2. Create a list of lists from the input ([['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D']])
3. Print the seat planning (the list).
4. Ask the user for a seat number.
5. Replace the seat with an X for take.
6. Print the seat plan with the taken seat (x).
7. Reapeat until user does not want to take more seats or the airplane is full.
'''

import string

def get_rows_and_seats_in_each_row(row_prompt, seats_prompt):
    ''' Asks the user for number of rows and seats in each row, returns them. '''

    rows = int(input(row_prompt))
    seats_in_each_row = int(input(seats_prompt))

    return rows, seats_in_each_row

def get_seat_planning_list(rows, seats_in_each_row):
    ''' 
    Takes in a number of rows and seats in each row. Returns a list of lists (airplane seats) 
    where each list in the list represents a row of seats in the airplane. 
    '''

    seats_alpha_list = string.ascii_uppercase							# Create a list of possible seat "names".
    row_list = [seats_alpha_list[x] for x in range(seats_in_each_row)]	# Create a list of seat numbers (one row).
    hallway = len(row_list)//2                      					# Find the hallway in the airplane.
    row_list = row_list[:hallway] + [" "] + row_list[hallway:]			# Add a hallway to the row list.
    seat_planning_list = [row_list for x in range(rows)]				# Add the row list to the seat planning list.

    return seat_planning_list

def occupy_seat(seat_planning_list, prompt, taken_seats_list, valid_letters = string.ascii_uppercase):
	''' 
	Takes in the airplane seat planning list and returns a new list where a seat has been replaced with an "X".
	Also makes sure the seat that the user wants is not taken and does exist.
	 '''

	occupied_list = []
	while True:
		occupied_seat = input(prompt)
		row_nr_str, seat_nr_str = tuple(occupied_seat.strip().split(" "))
		if (row_nr_str, seat_nr_str) not in taken_seats_list:														# Makes sure that the seat is not already taken.
			if seat_nr_str in valid_letters and int(row_nr_str) <= len(seat_planning_list) and int(row_nr_str) > 0:	# Makes sure that the seat exists.
				taken_seats_list.append(tuple(occupied_seat.strip().split(" ")))									# Keeps track of taken seats.
				for index, row in enumerate(seat_planning_list):													# For loop which finds the seat and replaces it with an "X"
					occupied_row_list = []
					if index + 1 == int(row_nr_str):
						for seat in row:
							if seat == seat_nr_str:
								occupied_row_list.append("X")
							else: 
								occupied_row_list.append(seat)
					else:
						occupied_row_list = row[:]
					occupied_list.append(occupied_row_list)
				return occupied_list
			else:
				print("Seat number is invalid!")
		else:
			print("That seat is taken!")
	
def print_plane_seating(seat_planning_list):
    ''' Takes in the list of the seat planning and prints it in the desired format.'''

    row_num = 1
    for row in seat_planning_list:
        print("{:2}   ".format(row_num), end = "")
        for seat in row:
            print(seat, end = " ")
        print()
        row_num += 1

def main():
	rows, seats_in_each_row = get_rows_and_seats_in_each_row("Enter number of rows: ", "Enter number of seats in each row: ")
	seat_planning_list = get_seat_planning_list(rows, seats_in_each_row)
	print_plane_seating(seat_planning_list)
	taken_seats_list = []
	occupied_seats_list = occupy_seat(seat_planning_list, "Input seat number (row seat): ", taken_seats_list, string.ascii_uppercase[:int(seats_in_each_row)])
	print_plane_seating(occupied_seats_list)

	more = input("More seats (y/n)? ").lower()
	while more == "y":
		occupied_seats_list = occupy_seat(occupied_seats_list, "Input seat number (row seat): ", taken_seats_list, string.ascii_uppercase[:int(seats_in_each_row)])
		print_plane_seating(occupied_seats_list)
		# Check to see if the plane is full.
		empty_seat = False
		for row in occupied_seats_list:
			for seat in row:
				if seat != "X" and seat != " ":
					empty_seat = True
		if empty_seat:
			more = input("More seats (y/n)? ").lower()
		else:
			more = "n"

main()