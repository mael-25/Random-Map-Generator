class Node:
    def __init__(self, pos:tuple, connections:list=[], unchecked_directions:list=[]) -> None:
        self.pos = pos
        self.connections:list[Node] = connections
        self.unchecked_directions = unchecked_directions

    def __str__(self) -> str:
        return "({}), connected to [{}]".format(self.str_pos, ", ".join([x.str_pos for x in self.connections]))
    
    @property
    def str_pos(self):
        return "({}, {})".format(self.pos[0], self.pos[1])
    
    def __le__(self, other): # less or equal
        """Less or equal"""
        if self.pos[0] < other.pos[0]:
            return True
        elif self.pos[0] == other.pos[0]:
            if self.pos[1] <= other.pos[1]:
                return True
            else:
                return False
        else:
            return False
    def __le__(self, other): # less or equal
        """Less or equal"""
        if self.pos[0] < other.pos[0]:
            return True
        elif self.pos[0] == other.pos[0]:
            if self.pos[1] <= other.pos[1]:
                return True
            else:
                return False
        else:
            return False
        
    def __lt__(self, other): # less than
        """Less than"""
        if self.pos[0] < other.pos[0]:
            return True
        elif self.pos[0] == other.pos[0]:
            if self.pos[1] < other.pos[1]:
                return True
            else:
                return False
        else:
            return False
        

    def __me__(self, other): # more or equal
        """Less or equal"""
        if self.pos[0] > other.pos[0]:
            return True
        elif self.pos[0] == other.pos[0]:
            if self.pos[1] >= other.pos[1]:
                return True
            else:
                return False
        else:
            return False
        
    def __mt__(self, other): # more than
        """More than"""
        if self.pos[0] > other.pos[0]:
            return True
        elif self.pos[0] == other.pos[0]:
            if self.pos[1] > other.pos[1]:
                return True
            else:
                return False
        else:
            return False