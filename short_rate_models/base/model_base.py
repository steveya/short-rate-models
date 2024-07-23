import numpy as np

class BaseModel:
    def drift(self):
        raise NotImplementedError

    def diffusion(self):
        raise NotImplementedError

    @property
    def dimension(self):
        raise NotImplementedError
    

class BaseDiscretization:
    def __init__(self, model, dt, T):
        self.model = model
        self.dt = dt
        self.T = T
        self.t = 0
        self.y = np.zeros(self.dimension)
        self.k = np.zeros(self.dimension)

    def step(self):
        self.t += self.dt
        self.y += self.dt * self.model.drift()
        self.k += self.dt * self.model.diffusion()