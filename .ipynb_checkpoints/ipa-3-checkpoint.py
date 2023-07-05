'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if from_member in social_graph and to_member in social_graph: # Checks if both members have a relationship.
        if to_member in social_graph[from_member]['following'] and from_member in social_graph[to_member]['following']: #Checks if both members follow each other.
            return "friends"
        elif to_member in social_graph[from_member]['following']: # Checks if from_member follows to_member.
            return "follower"
        elif from_member in social_graph[to_member]['following']: # Checks if to_member follows from_member.
            return "followed by"
        
    return "no relationship"

def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    size = len(board)
    
    for row in board: # Checks for a win on the rows
        if all(cell == row[0] and cell != '' for cell in row): # Checks for each cell in a row and checks if it does not have empty cells.
            return row[0]
        
    for col in range(size): # Checks for a win on the columns.
        if all(board[row][col] == board[0][col] and board[0][col] != '' for row in range(size)): # Checks for each cell in the column and checks if it does not have empty cells.
            return board[0][col]
        
    if all(board[i][i] == board[0][0] and board[0][0] != '' for i in range(size)): # Checks for a win on the negative diagonal.
        return board[0][0]
    
    if all(board[i][size - 1 - i] == board[0][size - 1] and board[0][size - 1] != '' for i in range(size)): # Checks for a win on the positive diagonal.
        return board[0][size - 1]
    
    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    stops = set()
    for leg in route_map['legs']:
        stops.add(leg[0]) # Gets where the shuttle comes from.
        stops.add(leg[1]) # Gets where the shuttle goes to.
        
    stops = sorted(list(stops)) 
    
    first_stop_index = stops.index(first_stop) # Gets the index of where the shuttle comes from.
    second_stop_index = stops.index(second_stop) # Gets the index of where the shuttle goes to.
    
    num_stops = len(stops) # Counts the number of stops so the shuttle correctly circles around.
    
    estimated_time = 0
    
    if second_stop_index > first_stop_index: # If the shuttle goes to a stop before it needs to circle back.
        for i in range(first_stop_index, second_stop_index):
            leg = route_map['leg'][(stops[i], stops[i + 1])]
            estimated_time += leg['travel_time_mins']
    else # If the shuttle goes to a stop that it needs to circle back to.
        for i in range(first_stop_index, first_stop_index + num_stops):
            leg = route_map['legs'][(stops[i % num_stops], stops[(i + 1) % num_stops])]
            estimated_time += leg['travel_time_mins']
            
    return estimated_time