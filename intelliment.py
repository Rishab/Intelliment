import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def generate_graphs():
    df = pd.read_excel('dataset.xlsx').sort_values(
        by='Second', ascending=True)

    # happiness graph
    happy = df[df['Emotion'] == 'HAPPY']
    plt.figure(figsize=(11.55555, 2.77778))
    happy.plot(kind='scatter', x='Second', y='Confidence', color='red')
    plt.xlim([0, df.count()['Second']])
    plt.savefig('./static/graphs/happy.png')

    # sadness graph
    sad = df[df['Emotion'] == 'SAD']
    plt.figure(figsize=(11.55555, 2.77778))
    sad.plot(kind='scatter', x='Second', y='Confidence', color='red')
    plt.xlim([0, df.count()['Second']])
    plt.savefig('./static/graphs/sad.png')

    # calm graph
    calm = df[df['Emotion'] == 'CALM']
    plt.figure(figsize=(11.55555, 2.77778))
    calm.plot(kind='scatter', x='Second', y='Confidence', color='red')
    plt.xlim([0, df.count()['Second']])
    plt.savefig('./static/graphs/calm.png')

    # angry graph
    angry = df[df['Emotion'] == 'ANGRY']
    plt.figure(figsize=(11.55555, 2.77778))
    happy.plot(kind='scatter', x='Second', y='Confidence', color='red')
    plt.xlim([0, df.count()['Second']])
    plt.savefig('./static/graphs/angry.png')

    # confused graph
    confused = df[df['Emotion'] == 'CONFUSED']
    plt.figure(figsize=(11.55555, 2.77778))
    confused.plot(kind='scatter', x='Second', y='Confidence', color='red')
    plt.xlim([0, df.count()['Second']])
    plt.savefig('./static/graphs/confused.png')

    # pie chart
    plt.figure(figsize=(11.55555, 11.55555))
    plt.pie(
        # using data total)arrests
        list(df.groupby("Emotion").count()['Second']),
        # with the labels being officer names
        labels=list(df.groupby("Emotion").count().index),
        # with no shadows
        shadow=False,
        # with the start angle at 90%
        startangle=90,
        autopct='%1.1f%%'
    )

    plt.savefig('pie.png')
