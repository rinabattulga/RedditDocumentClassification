import pandas as pd
import pprint as pp
import glob
pd.set_option('display.max_rows', 590)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 150)

files = glob.glob('data/*.csv')

for name in files:

    file = open(name,'r',encoding="utf8")

    pd_file= pd.read_csv(file)
    pp.pprint(pd_file.head(5))
    #a_dataframe["AB"] = a_dataframe["A"] + a_dataframe["B"]
    # pd_file["post_title"] = pd_file['post_title'].astype(str)+"\n"+pd_file['comment_body'].astype(str)
    pd_file = pd_file[pd_file.body!='[removed]']
    pd_file.rename(columns={'body':'text'}, inplace=True)
    pd_file.pop('Unnamed: 0')

    # pd_file.pop('post_title')
    pp.pprint(pd_file.head(5))
    output = pd_file.to_csv()

    file_out = open(name + '_merged' + '.csv', 'w')
    file_out.write(output)