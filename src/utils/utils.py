import pickle


def serialize(obj, name):
    filename = f"{name}.pkl"
    with open(filename, 'wb') as fid:
        pickle.dump(obj, fid)
