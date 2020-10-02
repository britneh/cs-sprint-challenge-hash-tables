"""
Example:
input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21
Return indices of weights that equal the limit 
what can we store?
"""

def get_indices_of_item_weights(weights, length, limit):

    indices_wt = {}

    for i in range(length): #go through the list of weights
        indices_wt[weights[i]] = i #store dictionary key to weight items, values are index
    
    for j, weight in enumerate(weights): #for just the indices of the list
        diff = limit - weight #set what we are looking for to a variable
        if diff in indices_wt: #if found then return
            return sorted((j, indices_wt[diff]), reverse = True)


    return None
 
weights = [ 4, 6, 10, 15, 16 ]
length = 5
limit = 21
print(get_indices_of_item_weights(weights, length, limit))