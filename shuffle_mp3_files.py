#! /usr/bin/python

import os
import random


def shuffle_mp3_songs():

    dir_path = os.path.dirname(os.path.realpath(__file__))

    all_mp3_files = [
        file_
        for file_ in os.listdir(dir_path)
        if file_.lower().endswith('.mp3')
    ]

    passed_ = list()
    while len(passed_) != len(all_mp3_files):
        random_index = random.randint(1, len(all_mp3_files))
        if random_index not in passed_:
            passed_.append(random_index)

            print 'shuffling ... {}'.format(all_mp3_files[random_index -1]),
            os.rename(
                all_mp3_files[random_index -1],
                '{0:04d}::{1}'.format(
                    len(passed_),
                    all_mp3_files[random_index - 1].split('::')[-1]
                )
            )

            print ' ... SUCCESS'


shuffle_mp3_songs()
