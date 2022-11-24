from difPy import dif
import os
datasets_path = r'C:\xampp\htdocs\PA\PA_KB_B2_20_5\raw_datasets'
# Get the list of files and directory in datasets
for dir_ in os.listdir(dataset_path):
    # check if it's a directory
    if os.path.isdir(os.path.join(dataset_path, dir_)):
        # delete similar/duplicates images
        search = dif(os.path.join(dataset_path, dir_), silent_del=True, similarity="low")
        print(search.result)