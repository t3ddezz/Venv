##!/usr/bin/env python
# -*- coding: utf-8 -*-


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#
#python heatmap.py --input *.tsv --output heatmap.pdf


import argparse

parser = argparse.ArgumentParser(description = 'creation of heatmap')
parser.add_argument('--input',nargs='*', required = True, help = 'tsv from phagelist')
parser.add_argument('--output', required=True)
args = parser.parse_args()


tool_name_list = list(args.input)
# erstellst dictionary und liest csv files
#dfs dictionary, df dataframe
extended_df_of_all_tools = []
tool_name_list_kopie = []
dfs = {}
for tools in tool_name_list:
  df = pd.read_csv(tools, sep ='\t|/t', engine ='python',  header=None) #sep ='\t|/t'
  sep = '_'
  toolname = tools.split(sep, 1)[0]
  
  df = df.sort_values([0],ignore_index=True)
  df['toolname'] = toolname
  df.columns = ['name', 'value','toolname']
  extended_df_of_all_tools.append(df) 
extended_df_of_all_tools = pd.concat(extended_df_of_all_tools)


sns.set(rc={'figure.figsize':(16,8)})

final_heatmap = extended_df_of_all_tools.pivot('name', "toolname", 'value')

if args.output:
  #to save the plot in a png as figure
  sns.heatmap(final_heatmap, annot=True,cmap="Blues").figure.savefig(args.output)

print('heatmap generated sucessfully')