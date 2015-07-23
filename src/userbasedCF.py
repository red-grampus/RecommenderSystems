import numpy as np

class UserBasedCF(objcet):
    def __init__(self,u):
        self.user_ratings = u
        self.userN = len(self.user_ratings)
        
