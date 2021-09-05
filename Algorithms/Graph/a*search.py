def aStarSearch(problem, heuristic=None):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()
    return graph_search(problem, fringe, heuristic)

def graph_search(problem, fringe, heuristic=None):
    """
    Graph search algorithm provided in lecture
    """
    # initialize start node
    start = problem.getStartState()
    closed = set()
    # node includes start, list of actions, and cost
    # if priority queue, enqueue with priority cost
    start_item = (start, [], heuristic(start, problem))
    insert_fringe(start_item, fringe)
    while not fringe.isEmpty():
        state, actions, total_cost = fringe.pop()
        if problem.isGoalState(state):
            return actions

        if state not in closed:
            closed.add(state)
            for child_state, child_act, child_cost in problem.getSuccessors(state):
                true_cost = total_cost + child_cost
                f_n = true_cost+heuristic(child_state, problem)
                # create new node to store path to node and total cost
                insert_fringe((child_state, actions+[child_act], true_cost), 
                    fringe, f_n)
    return []

def insert_fringe(item, fringe, value = 0):
    is_priority = type(fringe) == type(util.PriorityQueue())
    if not is_priority:
        fringe.push(item)
    else:
        fringe.update(item, value)