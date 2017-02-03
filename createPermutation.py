import csv


def cycle_lowest_digit():
    #print '>>>>>start cycle_lowest_digit'
    global row_count
    while (selection_iterator[0] <= selections_data[0]):
            print selection_iterator
            csv_as_list_of_lists.extend([selection_iterator[0:len(selection_iterator)]])
            row_count += 1
            selection_iterator[0] += 1
    #print '>>>>>end cycle_lowest_digit'

def is_next_digit_maxed(current_digit):
    #print '>>>>>is_next_digit_maxed'
    #print selection_iterator[current_digit + 1] == selections_data[current_digit + 1]
    return selection_iterator[current_digit + 1] == selections_data[current_digit + 1]

def is_next_digit_highest_digit(current_digit):
    #print '>>>>>is_next_digit_highest_digit'
    #print current_digit == len(selection_iterator) - 1
    return current_digit == len(selection_iterator) - 1

def reset_all_lower_digits(current_digit):
    #print '>>>>>start reset_all_lower_digits'
    #print 'current digit: ' , current_digit
    global row_count
    for i in range(0,current_digit + 1):
        selection_iterator[i] = 1
    #print '>>>>>end reset_all_lower_digits'



global row_count
row_count = 0
selections_data = []
selection_iterator = []
csv_as_list_of_lists = []

with open('test1.csv', 'rb') as csvfile_r:
    csvreader = csv.reader(csvfile_r,delimiter=',')
    for row in csvreader:
        option = int(row[0])
        selections_data.extend([option])


for i in range(0,len(selections_data)):
    selection_iterator.extend([1])

x = 0
while x <= 10000:
    digit = 0
    cycle_lowest_digit()
    while is_next_digit_maxed(digit):
        digit += 1
        if is_next_digit_highest_digit(digit):
            x = 10001
            break
    if x == 10001:
        break
    #print 'digit: ', digit
    selection_iterator[digit + 1] += 1
    #print selection_iterator[digit + 1]
    reset_all_lower_digits(digit)
    x += 1

print 'Row Count: ' , row_count
#print csv_as_list_of_lists

with open('test2.csv', 'wb') as csvfile_w:
    csvwriter = csv.writer(csvfile_w,delimiter=',')
    for row in csv_as_list_of_lists:
        csvwriter.writerow(row)
