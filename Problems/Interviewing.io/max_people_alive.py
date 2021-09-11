"""
https://www.youtube.com/watch?v=Oq8HobmTY-8&t=2517s

Similar to 1353 max num events that you can attend problem


Return the year in which the most people were alive
"""


profiles = [
            {"name": "John", "birth": 1920, "death": 1925},
            {"name": "Joe", "birth": 1920, "death": 1922},
            {"name": "Oof", "birth": 1923, "death": 1923},
            {"name": "Oof", "birth": 1923, "death": 1924},
            # {"name": "Oof", "birth": 1923, "death": 1925}
        ]


import heapq
def find_max_alive_year(profiles):

    pq = []
    for p in profiles:
        # push year and alive status onto heap
        # -1 so it gets sorted first if same year as deaths
        heapq.heappush(pq, (p.get("birth"), -1))
        heapq.heappush(pq, (p.get("death"), 1))

    max_year = 0
    population = 0
    max_alive = 0

    while len(pq) > 0:
        year, alive = heapq.heappop(pq)

        population -= alive

        while len(pq) > 0 and pq[0][0] == year:
            _, alive = heapq.heappop(pq)
            population -= alive

            # if birthyear is also deathyear
            if population > max_alive:
                max_alive = population
                max_year = year

        # end of this year, check again
        if population > max_alive:
            max_alive = population
            max_year = year
    
    return max_year

print(find_max_alive_year(profiles))