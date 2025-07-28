import pandas as pd
import numpy as np

scores = np.random.randint(35, 101, size=20)

above_75 = np.sum(scores > 75)
mean_score = np.mean(scores)
std_dev = np.std(scores)

print("Scores:", scores)
print("Count > 75:", above_75)
print("Mean:", mean_score)
print("Standard Deviation:", std_dev)

df = pd.DataFrame({'Score': scores})
df.to_csv('scores.csv', index=False)
