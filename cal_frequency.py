from parsivar import FindStems
import pandas as pd
import numpy as np
my_stemmer = FindStems()


my_d = open('/content/top1m.txt')
def load_data():
    return open('/content/top1m.txt')

def data_generator():
    """Define a datagenerator 

    Yields:
        list: each row of data
    """
    hm = load_data()
    for d in hm:
        yield d.replace('\n', '').split('\t')


hm_blog = data_generator()
def filter_hmb(i):
    """Get root of each word

    Args:
        i (string): word

    Returns:
        string: root
    """
    l = next(hm_blog)
    root = my_stemmer.convert_to_stem(l[0])
    return [root,int(l[1])]


numbers = range(1000000)
new_hmb = map(filter_hmb, numbers)


# conver to DataFrame
df = pd.DataFrame(new_hmb,columns=['word','frequency'])
# sum all word's frequency with the same root 
df = df.groupby(['word'], as_index=False)['frequency'].sum()
# get log of frequency
df['log_frequency'] = np.log(df['frequency'])


dic_df = dict(zip(df['word'],df['log_frequency']))
import pickle #credits to stack overflow user= blender

with open('frequency_log_set.pkl', 'wb') as handle:
    pickle.dump(dic_df, handle, protocol=pickle.HIGHEST_PROTOCOL)
