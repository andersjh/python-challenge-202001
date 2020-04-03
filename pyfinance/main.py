# import dependencies
import csv


# intialize critical variables
data_path = "budget_data.csv"

# these are used for min and max
beginning_amount = 0
end_amount = 0
max_increase = 0
max_increase_month = ""
max_decline = 0
max_decline_month = ""

# keep track of deltas for average calc
deltas = 0
total_months = 0
total_amounts = 0

# these are used for delta calcs
prev_month = 0
cur_delta = 0


with open(data_path, 'r') as fh:

    csv_reader = csv.reader(fh)

    header = next(csv_reader)
    first_row = next(csv_reader)
    # grab first row so I can save beginning 
    # and have a start point for delta
    beginning_amount = int(first_row[0])
    prev_amount = beginning_amount
    total_amounts = beginning_amount
    total_months = 1

    for row in csv_reader:
        total_months += 1
        cur_amount = int(row[0])
        total_amounts += cur_amount
        cur_month = row[1]
        cur_delta = cur_amount - prev_amount
        deltas += cur_delta
        # add to list

        if cur_delta <= 0:
            if cur_amount < max_decline:
                max_decline = cur_delta
                max_decline_month = cur_month
        else:
             if cur_amount > max_increase:
                max_increase = cur_delta
                max_increase_month = cur_month 

        prev_amount = cur_amount  

print(f"Total months: {total_months}")
total_delta = prev_amount - beginning_amount
avg_delta = deltas / ( total_months -1 )
print(f"Total amounts: {total_amounts}")
print(f"Avg delta: {round(avg_delta, 2)}")
print("max decline:\n", max_decline, max_decline_month)
print("max increase:\n", max_increase, max_increase_month)

print()
        