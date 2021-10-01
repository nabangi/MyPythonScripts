import random
feet_in_mile = 5280
meters_in_kilometer = 1000
mercedes = ["E350-W211", "C200-W204", "C180-W203"]

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.randint(1, num)