import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def execute():
    data = pd.read_csv('AssignmentExcel.csv')

    ##################
    # 1) How many employees submitted ideas?
    print(len(pd.unique(data['Idea Submitter Username'])))
    # I am using usernames as those are likely to be unique in the situation of two employees with similar names.
    # answer is 102 employees submitted ideas.

    ##################
    # 2) How many ideas were submitted in 2018?
    data['Date Submitted'] = pd.to_datetime(data['Date Submitted'])
    num_ideas_2018 = len(data[(data['Date Submitted'] >= '01-01-2018') & (data['Date Submitted'] <= '12-31-2018')])
    print(num_ideas_2018)
    print(num_ideas_2018/len(data))
    # answer is 128 ideas were submitted in 2018 (84.2% of all ideas in the dataset)

    ##################
    # 3) Create a pie chart that shows the breakout of all ideas by department of person submitting the idea.
    print(pd.unique(data['Idea Submitter Department'])) # looks like 4 different departments in this dataset
    counts = data.groupby(['Idea Submitter Department']).size().reset_index(name='counts').sort_values(by='counts', ascending=False)
    counts.set_index('Idea Submitter Department', inplace=True)
    fig1, ax1 = plt.subplots()
    ax1.pie(list(counts.counts), labels=list(counts.index), autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.legend(counts.counts, title='Count per Department', loc='lower left')
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Ideas by Submitter Department')
    plt.savefig('pie_chart.png')

    ##################
    # 4) Of the ideas that were implemented, which two departments benefited most?
    # Segment down to the implemented ideas first
    implemented_ideas = data[data['Idea Status'] == '5 Implemented']
    # Count and sort
    count = implemented_ideas.groupby(['Primary Benefiting Department']).size().reset_index(name='count').sort_values(by='count', ascending=False)
    print(count.head(2))
    # Answer is Production with 8 implemented ideas, and Human Resources with 7 Implemented Ideas.


if __name__ == '__main__':
    execute()
