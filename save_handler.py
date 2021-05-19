from json import dump, load
#this is in a seperate script because there is an issue with json interacting with files
#that I cannot (as far as I know) fix unless I make the save file within a different script

def create_save(save_dir):
    save = open(save_dir, "w+")
    save.write('{"save": []}')
    save.close

def load_save_data(save_dir):
    save_data = load(open(f"./{save_dir}", "r"))
    return save_data

def append_save_data(save_append_data, save_dir):
    dump(save_append_data, open(f"./{save_dir}", "w"), indent=4)
