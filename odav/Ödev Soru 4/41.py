import pandas as pd

data = [15, 15, 16, 19, 19, 20, 20, 21, 22, 28, 35, 40, 41, 42, 43, 44, 60, 61, 65]
c1 = 16
c2 = 22

df = pd.DataFrame(data, columns=['Xi'])
df['Distance1'] = abs(df['Xi'] - c1)
df['Distance2'] = abs(df['Xi'] - c2)
df['Cluster'] = df[['Distance1', 'Distance2']].idxmin(axis=1)
df['c1'] = c1
df['c2'] = c2

iteration_1 = df.copy()

c1 = iteration_1[iteration_1['Cluster'] == 'Distance1']['Xi'].mean()
c2 = iteration_1[iteration_1['Cluster'] == 'Distance2']['Xi'].mean()
iteration_1['Distance1'] = abs(iteration_1['Xi'] - c1)
iteration_1['Distance2'] = abs(iteration_1['Xi'] - c2)
iteration_1['Cluster'] = iteration_1[['Distance1', 'Distance2']].idxmin(axis=1)
iteration_1['c1'] = c1
iteration_1['c2'] = c2

iteration_2 = iteration_1.copy()

c1 = iteration_2[iteration_2['Cluster'] == 'Distance1']['Xi'].mean()
c2 = iteration_2[iteration_2['Cluster'] == 'Distance2']['Xi'].mean()
iteration_2['Distance1'] = abs(iteration_2['Xi'] - c1)
iteration_2['Distance2'] = abs(iteration_2['Xi'] - c2)
iteration_2['Cluster'] = iteration_2[['Distance1', 'Distance2']].idxmin(axis=1)
iteration_2['c1'] = c1
iteration_2['c2'] = c2

iteration_3 = iteration_2.copy()

c1 = iteration_3[iteration_3['Cluster'] == 'Distance1']['Xi'].mean()
c2 = iteration_3[iteration_3['Cluster'] == 'Distance2']['Xi'].mean()
iteration_3['Distance1'] = abs(iteration_3['Xi'] - c1)
iteration_3['Distance2'] = abs(iteration_3['Xi'] - c2)
iteration_3['Cluster'] = iteration_3[['Distance1', 'Distance2']].idxmin(axis=1)
iteration_3['c1'] = c1
iteration_3['c2'] = c2

iteration_4 = iteration_3.copy()

c1 = iteration_4[iteration_4['Cluster'] == 'Distance1']['Xi'].mean()
c2 = iteration_4[iteration_4['Cluster'] == 'Distance2']['Xi'].mean()
iteration_4['Distance1'] = abs(iteration_4['Xi'] - c1)
iteration_4['Distance2'] = abs(iteration_4['Xi'] - c2)
iteration_4['Cluster'] = iteration_4[['Distance1', 'Distance2']].idxmin(axis=1)
iteration_4['c1'] = c1
iteration_4['c2'] = c2


print(iteration_1)
print(iteration_2)
print(iteration_3)
print(iteration_4) 




