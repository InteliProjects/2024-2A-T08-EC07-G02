import pandas as pd
import numpy as np

df_fa = pd.read_excel("STATUS_PREDICTOR_ANO.xlsx")


ser = list(df_fa["KNR"])

df_re = pd.read_parquet("RESULTS.parquet",filters=[("KNR", "in", ser)])
df_re =df_re[df_re["UNIT"].isnull() == False]
df_re = df_re.reset_index()
df_re = df_re.drop(columns=["index"])

for i in range(694):
    df_temp = df_re[i*31353:(i+1)*31353]
    df_temp = pd.get_dummies(df_temp, prefix="NAME", columns= ["NAME"])
    cols = df_temp.columns
    for c in range(7,len(cols)):
        df_temp[cols[c]] = df_temp[cols[c]].astype(int)
        df_temp[cols[c]] = df_temp.groupby(["KNR","VALUE_ID"])[cols[c]].transform("sum")
    df_temp = df_temp.drop_duplicates(subset=["KNR","VALUE_ID"])
    for c in range(7,len(cols)):
        df_temp[cols[c]] = df_temp.groupby(["KNR"])[cols[c]].transform("max")
    df_temp = df_temp.drop_duplicates(subset=["KNR"])
    df_temp = df_temp.drop(columns=["ID","UNIT","VALUE_ID", "VALUE","DATA","STATUS"])
    df_temp.to_csv(f"DATASETS/Results_{i}.csv",index=False)
    print(f"Grupo {i} concluido")