import pandas as pd
from datetime import datetime as dt

df = pd.read_csv("0_sim_log.csv")

df["Time"] = pd.to_datetime(df["Time"])
df["Time"] = df["Time"].dt.strftime("%H")

df.groupby(["Date", "Time"]).mean().to_csv("SimUtilizationReport.csv")
