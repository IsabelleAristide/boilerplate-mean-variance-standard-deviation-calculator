import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    ar = np.array(list).reshape((3, 3))
    calculations = {}
    calculations['mean'] = [ar.mean(0).tolist(),ar.mean(1).tolist(),ar.mean()]
    calculations['variance'] = [np.var(ar,0).tolist(),np.var(ar,1).tolist(),np.var(ar)]
    calculations['standard deviation'] = [np.std(ar,0).tolist(),np.std(ar,1).tolist(),np.std(ar)]
    calculations['max'] = [ar.max(0).tolist(),ar.max(1).tolist(),ar.max()]
    calculations['min'] = [ar.min(0).tolist(), ar.min(1).tolist(),ar.min()]
    calculations['sum'] = [ar.sum(0).tolist(),ar.sum(1).tolist(),ar.sum()]



    return calculations