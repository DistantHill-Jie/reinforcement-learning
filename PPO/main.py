import torch
import torch.nn as nn
from torch.distributions import Categorical
import gym

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
 