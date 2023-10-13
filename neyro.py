import pandas as pd
state_web_site_feedback = pd.read_csv("data-20150923t1145-structure-20150923t1145_4.csv")
state_web_site_feedback.describe().T
state_web_site_feedback.info()
