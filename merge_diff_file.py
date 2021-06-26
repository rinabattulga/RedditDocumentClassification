import pandas as pd
import pprint as pp
import glob
pd.set_option('display.max_rows', 590)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 150)

files = glob.glob('out/data/test/*.csv')

pd_out = pd.DataFrame(columns=['text','subreddit'])


for name in files:
    file = open(name,'r',encoding="utf8")
    pd_file = pd.read_csv(file,usecols=['text','subreddit'])
    pd_out = pd.concat([pd_out,pd_file],)
    pp.pprint(len(pd_out.index))


out = open("data/test.csv",'w')
pd_out = pd_out.sample(frac=1)
pd_out = pd_out.to_csv(index=False)
out.write(pd_out)