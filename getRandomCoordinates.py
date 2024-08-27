import random

#genering random coordinates inside dedicated square area (x1, y1, x2, y2) to (x_random, y_random)
def getRandomCoordinates(coordinates):
    #print(coordinates)
    x1, y1, x2, y2 = coordinates
    x_random = random.randint(x1, x2)
    y_random = random.randint(y1, y2)
    random_coordinates = x_random, y_random
    return random_coordinates