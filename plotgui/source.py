import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import os
import glob

import settings



START = 0
END = 12

sname = "7 качеств"

# ofile = [_ for _ in glob.glob("*.xlsx")][0]

def make_plots(ofile, sname=sname, start=START, end=END, ofolder=None):
    sns.set(style="ticks")

    df = pd.read_excel(ofile, sheet_name=sname)
    # df = pd.read_excel(ofile)
    df = df.drop(0)

    vals = [a for a in df.columns if 'Unnamed' not in a][1:]

    df_filled = df[df['Робость - смелость'] >= 0]

    tags = ['Замкнутость-общительность',
    'Эмоциональная неустойчивость-устойчивость',
    'Склонность к подчинению-доминированию',
    'Сдержанность-экспрессивность',
    'Робость-смелость',
    'Доверчивость-подозрительность',
    'Уверенность в себе-тревожность']

    if ofolder is None:
        if not os.path.isdir('out'):
            os.mkdir('out')
    else:
        path = os.path.expanduser(os.path.join(ofolder, "out"))
        if not os.path.isdir(path):
            print(path)
            os.makedirs(path)

    for index,row in df_filled.iterrows():
        print(f"Шифр {row['Шифр']}: {list(row[vals])}")
        RESULTS = list(row[vals])
        sns.set(style="whitegrid", palette="cubehelix", font_scale=1.4)

        f, ax = plt.subplots(figsize=(13,6))


        ax.barh(list(reversed(tags)), list(reversed(RESULTS)), color='grey')
        ax.set_xlim([START, END])

        plt.tight_layout()
        if ofolder is not None:
            plt.savefig(f"{path}/{row['Шифр']}_plot.png")
        else:
            plt.savefig(f"out/{row['Шифр']}_plot.png")


