print("--------------------------------------------------------------------------")

# The amount customer is paying 
amount = float(input(f"Please enter the cost of your meal:"))   #float function used to converts values into floating point numbers

#function to calculate tip, sales tax and total cost

def calc_total(cost): #paranthesis - cost
	tip = round(0.18 * cost, 2) #tip is 18% of meal cost
	tax = round(0.07 * cost, 2) #Sales tax is 7% of meal cost
	total_cost = round(cost + tip + tax, 2)
	  
    # using f-string
	return f"""
	Tip is ${tip}
	Sales tax is ${tax}
	Total amount to be paid is ${total_cost}
	Thank you.....
	"""

print(calc_total(amount))

print("--------------------------------------------------------------------------")