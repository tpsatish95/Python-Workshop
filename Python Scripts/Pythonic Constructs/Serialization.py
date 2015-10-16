# JSON
import json

dict = {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}
json_string = json.dumps(dict)
print(json_string)

print(json.loads(json_string))

# PICKLE
import pickle
pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickle.loads(pickled_string))

# Saving DataStructures as .pkl binary files
def save_obj(obj, name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f,  protocol=2)

def load_obj(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

dict = {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}
save_obj(dict, "dictSave")
