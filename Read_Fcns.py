def list_read_rvm():
    import pandas as pd
    df = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data')
    f = lambda x: 1.0 if x=='R' else 0.0
    df.iloc[:,-1:]=df.iloc[:,-1:].applymap(f)
    return df.iloc[:,:-1].to_numpy(),df.iloc[:,-1:].to_numpy(),df