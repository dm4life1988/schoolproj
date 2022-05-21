totalcost = [{ 'Base Fee' : 40 }, # dictionary nested inside of a list for my cost and the base fee for cleaning 
         {'Bedroom' : 10 },
         {'Bathroom' : 20 },
         {'Living Room' : 15 }, 
         {'Kitchen' : 20 } , 
         {'Dining Room' : 15 } ,
         {'Laundry Room' : 10 } , 
         {'Hallway' : 10 } ,
]
def estimate(totalcost): # defined the function for the estimate of the cleaning company with a prarameter of totalcost
    try: # try statement to have my except statement if the user enters a string instead of integer
        total = totalcost[0]['Base Fee'] # my total cost variable that the function iterates through and updates to create the estimate
        total += int(input('How many Bedrooms?: ')) * totalcost[1]['Bedroom']
        total += int(input('How many Bathrooms?: ')) * totalcost[2]['Bathroom']
        total += int(input('How many Living Rooms does this house have?: ')) * totalcost[3]['Living Room']    
        total += int(input('How many kitchens?: ')) * totalcost[4]['Kitchen']    
        total += int(input('How many Dining Rooms?: ')) * totalcost[5]['Dining Room']
        total += int(input('How many Laundry Rooms?: ')) * totalcost[6]['Laundry Room']
        total += int(input('How many Hallways?: ')) * totalcost[7]['Hallway'] # lines 13-19 asks the user how many rooms we will be cleaning then updating the total variable
    except ValueError: # error for if user inters a string instead of integer
        print('Must use a number value for the rooms.') # statement letting the user know need to enter a integer value
        return False
    return total # returns the total for the job estimate
print('Good day') # opening print to welcome the user
x = input('Would you like a quote today?: ') # prompts to recieve a quote today and saves the input to x
if x == 'yes' or 'Yes' or 'YES': # added multiple yes's 
    i = estimate(totalcost) # creates a i varable to intiatiate the function created above
    if i != False: # if not equal to False try the estimate function created 
        print(f"It will cost ${i} to clean your house.") # use the f statement to create literal string to insert the i variable created which points to the function
print('Thank You') # Thank You Message 