import pandas as pd 
import os
import glob
import matplotlib
from matplotlib import colormaps

def load_data():
    a1 = pd.read_csv("in/a1_emissions.csv")
    a2_logreg = pd.read_csv("in/a2_logreg_emissions.csv")
    a2_neunet = pd.read_csv("in/a2_neunet_emissions.csv")
    a3 = pd.read_csv("in/a3_emissions.csv")
    a4 = pd.read_csv("in/a4_emissions.csv")

    dataframes = [a1, a2_logreg, a2_neunet, a3, a4]

    df = pd.concat(dataframes)

    return df

def plot_assignment_emissions(df):
    
    plot = df.plot.bar(x='project_name', y='emissions', colormap = 'Pastel2', title = "Kg CO2eq per assignment", ylabel = "kg CO2eq")
    outpath = os.path.join("out", "assignment_emission.png")
    fig = plot.get_figure()
    fig.tight_layout()
    fig.savefig(outpath)

def load_tasks():
    
    tasks = os.path.join("in", "tasks", "*.csv")
    all_tasks = glob.glob(tasks) 
  
    task_df = pd.concat(map(pd.read_csv, all_tasks), ignore_index=True)

    task_df = task_df.sort_values('task_name')
    return task_df

def plot_task_emissions(task_df):
    
    plot = task_df.plot.bar(x='task_name', y='emissions', colormap = 'Pastel2', title = "Kg CO2eq per task", ylabel = "kg CO2eq")
    outpath = os.path.join("out", "task_emission.png")
    fig = plot.get_figure()
    fig.tight_layout()
    fig.savefig(outpath)

def main():
    df = load_data()
    plot_assignment_emissions(df)
    task_df = load_tasks()
    plot_task_emissions(task_df)



if __name__ == "__main__":
    main()