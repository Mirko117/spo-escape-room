import os


def get_number_of_levels():
    '''
    Counts numner of files in app/templates/levels
    '''
    levels_path = os.path.join(os.path.dirname(__file__), "templates", "levels")
    return len([name for name in os.listdir(levels_path) if os.path.isfile(os.path.join(levels_path, name))])