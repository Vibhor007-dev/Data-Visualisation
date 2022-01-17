import pandas as pd
import plotly.graph_objects as go
import plotly_express as pf
import csv

df = pd.read_csv("studentData.csv")
mean=df.groupby(["student_id","level"],as_index=False)["attempt"].mean()
fig=pf.scatter(mean,x="student_id",y="level",size="attempt",color="attempt")
fig.show()