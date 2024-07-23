import numpy as np

from ..base import BaseModel

class MertonModel(BaseModel):
    def __init__(self, mu, sigma, lam=0):
        self.mu = mu
        self.sigma = sigma
        self.lam = lam

    def drift(self):
        return self.mu
    
    def diffusion(self):
        return self.sigma
    
    def __repr__(self):
        return f"MertonModel(mu={self.mu}, sigma={self.sigma})"
    
    def __str__(self):
        return self.__repr__()
    
    def __hash__(self):
        return hash(("Merton", self.mu, self.sigma))
    
    def __eq__(self, other):
        if isinstance(other, MertonModel):
            return self.mu == other.mu and self.sigma == other.sigma
        return False
    
