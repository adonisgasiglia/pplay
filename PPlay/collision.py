# Modules import
from . import point
#from point import Point

"""A simple class to deal with basic collision methods"""
"""
Must note that the collision is inclusive, i.e.,
occurs when one enters the other effectively,
not only when in the same position of the edge.
"""
class Collision():
    """
    minN: the Point of the top left of the N rect
    maxN: the Point of the bottom right of the N rect
    """
    @classmethod
    def collided_rect(cls, min1, max1, min2, max2):
        if(min1.x >= max2.x or max1.x <= min2.x):
            return False
        if(min1.y >= max2.y or max1.y <= min2.y):
            return False
        return True

    """
    game_object1: the origin GameObject
    game_object2: the target GameObject
    """
    @classmethod
    def collided(cls, *args):
        """
        if(len(args) == 2
        and isinstance(args[0], GameObject)
        and isinstance(args[1], GameObject)):
        """
        game_object1_min = point.Point(args[0].x, args[0].y)
        game_object1_max = point.Point(args[0].x + args[0].width,
                                 args[0].y + args[0].height)

        game_object2_min = point.Point(args[1].x, args[1].y)
        game_object2_max = point.Point(args[1].x + args[1].width,
                                 args[1].y + args[1].height)

        return (Collision.collided_rect(game_object1_min, game_object1_max,
                                        game_object2_min, game_object2_max))
            
                      
            
        
    
