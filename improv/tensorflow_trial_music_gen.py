# import collections
# import datetime
# # import fluidsynth
# import glob
# import numpy as np
import pathlib
# import pandas as pd
# # import pretty_midi
# import seaborn as sns
# # import tensorflow as tf

# from IPython import display
# from matplotlib import pyplot as plt
# from typing import Optional

# https://www.tensorflow.org/tutorials/audio/music_generation

def main():
    data_dir = pathlib.Path('../data')
    filenames = list(data_dir.glob('**/*.mid*'))
    print('Number of files:', len(filenames))


if __name__ == "__main__":
    main()
