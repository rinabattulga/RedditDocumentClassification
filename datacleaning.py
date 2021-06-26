import pandas as pd
import pprint as pp
import glob
pd.set_option('display.max_rows', 590)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 150)


files = glob.glob('data/*.csv')
print(files)
for name in files:

    file = open(name,'r',encoding="utf8")
    file_out = open(name+'_cleaned' +'.csv','w')
    pd_file= pd.read_csv(file)


    pd_file = pd.DataFrame([pd_file.pop(x) for x in ['q','a']]).T
    pd_file['subreddit'] = 'jokes'
    #pd_file.pop('class')


    pp.pprint(pd_file.head(5))
    output = pd_file.to_csv()

    file_out.write(output)