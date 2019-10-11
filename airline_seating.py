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
    '''  '''

    seats_alpha_list = string.ascii_uppercase
    row_list = [seats_alpha_list[x] for x in range(seats_in_each_row)]
    seat_planning_list = [row_list for x in range(rows)]


    return seat_planning_list

def print_plane_seating(seat_planning_list):
    
    row_num = 1
    for row in seat_planning_list:
        print("{:2}".format(row_num), end = " ")
        for seat in row:
            print(seat, end=" ")
        #print("{:2} {}".format(row_num, row))
        row_num += 1

def main():
    rows, seats_in_each_row = get_rows_and_seats_in_each_row()
    seat_planning_list = get_seat_planning_list(rows, seats_in_each_row)
    print_plane_seating(seat_planning_list)

main()