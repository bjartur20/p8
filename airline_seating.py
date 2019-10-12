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

def get_rows_and_seats_in_each_row():
    ''' Asks the user for number of rows and seats in each row, returns them. '''

    rows = int(input("Enter number of rows: "))
    seats_in_each_row = int(input("Enter number of seats in each row: "))

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

def occupy_seat(seat_planning_list):
	'''  '''

	occupied_seat = input("Input seat number (row seat): ")
	row_nr_int = int(occupied_seat[0])
	seat_nr_str = occupied_seat[2]
	for row in seat_planning_list:
		index_of_row = seat_planning_list.index(row)
		if index_of_row == row_nr_int - 1:
			for seat in row:
				if seat == seat_nr_str:
					row[row.index(seat)] = "X"	

def print_plane_seating(seat_planning_list):
    ''' Takes in a liist of the seat planning and prints it in the desired format.'''

    row_num = 1
    for row in seat_planning_list:
        print("{:2}   ".format(row_num), end = "")
        for seat in row:
            print(seat, end = " ")
        print()
        row_num += 1

def main():
	rows, seats_in_each_row = get_rows_and_seats_in_each_row()
	seat_planning_list = get_seat_planning_list(rows, seats_in_each_row)
	print_plane_seating(seat_planning_list)
	occupy_seat(seat_planning_list)
	print_plane_seating(seat_planning_list)

main()