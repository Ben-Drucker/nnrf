import numpy as np

def create_random_state(seed=None):
	"""
	Create a RandomState.

	Parameters
	----------
	seed : None or int or RandomState, default=None
		Initial seed for the RandomState. If seed is None,
		return the RandomState singleton. If seed is an int,
		return a RandomState with the seed set to the int.
		If seed is a RandomState, return that RandomState.

	Returns
	-------
	random_state : RandomState
		A RandomState object.
	"""
	if seed is None:
		return np.random.mtrand._rand
	elif isinstance(seed, (int, np.integer)):
		return np.random.RandomState(seed=seed)
	elif isinstance(seed, np.random.RandomState):
		return seed
	else:
		raise ValueError("Seed must be None, an int, or a Random State")

def one_hot(Y, cols=None):
	if Y.shape[1] == cols and set(Y) == set([0,1]):
		return Y
	if Y.size > len(Y) : raise ValueError("Matrix is not 1D")
	Y_ = Y.reshape(-1)
	if cols is None : cols = Y_.max() + 1
	elif cols < len(np.unique(Y)) : raise ValueError("There are more classes than cols")
	if cols > 1:
		one_hot = np.zeros((len(Y), cols), dtype=int)
		one_hot[np.arange(len(Y)), Y_] = 1
		return one_hot
	else:
		Y = np.where(Y < cols, 0, 1)
		return Y.reshape(-1, 1)