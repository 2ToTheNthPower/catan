from typing import Dict, List, Any
from dataclasses import dataclass
from enum import IntEnum
from random import randrange, shuffle
import dgl

@dataclass
class Resource(IntEnum):
    ROBBER = 0
    BRICK = 1
    WOOD = 2
    SHEEP = 3
    WHEET = 4
    ORE = 5

class Dice:
    @classmethod
    def roll(self, num_dice=2):
        sum_of_rolls = 0

        for roll in range(num_dice):
            sum_of_rolls += randrange(1, 7)

        return sum_of_rolls

@dataclass
class Tile:
    resource: Resource
    number: int

class Board:
    def __init__(self):
        required_numbers = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        required_resources = [Resource.WHEET, Resource.SHEEP, Resource.WOOD]*4 + \
                                    [Resource.ORE, Resource.BRICK]*3

        shuffle(required_numbers)
        shuffle(required_resources)

        # Insert robber at random position
        robber_position = randrange(0, 18)
        required_numbers.insert(robber_position, 7)
        required_resources.insert(robber_position, Resource.ROBBER)
        

    def build(self):

        # Define the node data for each type
        tiles_data = {'tile': (19, {})}  # 2 users
        city_data = {'city': (3, {})}  # 3 items
        road_data = {'road': (3, {})}

        # Define the edge data for each type
        follows_data = ('user', 'follows', 'user', [(0, 1)])  # user 0 follows user 1
        buys_data = ('user', 'buys', 'item', [(0, 1), (1, 2)])  # user 0 buys item 1, user 1 buys item 2

        # Create the heterogeneous graph
        g = dgl.heterograph({
            follows_data: None,
            buys_data: None
        }, num_nodes_dict={**user_data, **item_data})

        print(g)

