import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

pca = PCA(0.8)

file_name="dotnet.csv"
df = pd.read_csv(file_name)
x = df.loc[:,df.columns != 'Benchmark ']

x = StandardScaler().fit_transform(x)

principalComponents = pca.fit_transform(x)

#principalDf = pd.DataFrame(data = principalComponents
#                     , columns = ['principal component 1', 'principal component 2', 'principal component 3', 'principal component 4'])
#print principalDf
print pca.explained_variance_ratio_

