import numpy as np
import pandas as pd;
from scipy.spatial import distance
from scipy.stats import spearmanr
from scipy.stats import pearsonr
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
pointA=np.array([2,4,6])
pointB=np.array([3,5,8])

#Euclidian distance
euclidian_dist=distance.euclidean(pointA,pointB)
print("Euclidian dist:",euclidian_dist)

#similarity 
similarity_euclidian=1/(1+euclidian_dist)
print("Euclidian similarity:",similarity_euclidian)

manhattan_dist=distance.cityblock(pointA,pointB)
print("Mnahattan:",manhattan_dist)

similarity_manhattan=1/(1+manhattan_dist)
print("Manhattan similarity:",similarity_manhattan)

#minkowski distance with p=2
minkowski_dist_p3=distance.minkowski(pointA,pointB,p=2)
print("minkowski(p=3):",minkowski_dist_p3)

similarity_minkowski=1/(1+minkowski_dist_p3)
print("Similarity:",similarity_minkowski)


minkowski_dist_p3=distance.minkowski(pointA,pointB,p=1)
print("minkowski(p=1):",minkowski_dist_p3)

similarity_minkowski=1/(1+minkowski_dist_p3)
print("Similarity:",similarity_minkowski)

 


df = pd.DataFrame({
   'X': [10, 20, 30, 40, 50], 
  'Y': [12, 24, 33, 45, 60]   }) 

corr_matrix = df.corr(method='pearson')
print("Pearson CorrelationMatrix:\n", corr_matrix)
df1 = pd.read_csv("Iris.csv")
print(df1.corr(method='pearson', numeric_only=True))
tdf = pd.DataFrame(
{ 'X': [10, 20, 30, 40, 50],
'Y': [12, 18, 33, 47, 55]}
)

corr_value, p_value = spearmanr(df['X'],df['Y'])
print(f"Spearman CorrelationCoefficient: {corr_value}")
print(f"P-value: {p_value}")
print(df1.corr(method='spearman', numeric_only=True))

df=pd.DataFrame({
  'sname':['A','B','C','D','E'],
  'DS':[12,24,33,45,60],
  'QC':[23,34,45,56,67],
  'CD':[22,33,44,55,66],
  'TOC':[77,88,99,22,33]
})
print(df.corr(method='spearman',numeric_only=True))

def hamming_distance(str1, str2):   
  if len(str1) != len(str2):        
    raise ValueError("Strings must be of equal length")
    return sum(ch1 != ch2 for ch1, ch2 in zip(str1, str2)

) 
s1 = "karolin"
s2 = "kathrin"
dist = hamming_distance(s1, s2)
print(f"Hamming Distance between '{s1}' and '{s2}': {dist}")


def jaccard_index(str1,str2):
  set1,set2=set(str1.split()),set(str2.split())
  intersection=set1.intersection(set2)
  union=set1.union(set2)
  return len(intersection)/len(union)

s1="data science is fun"
s2="data science is fun"

print("Jaccord Index:",jaccard_index(s1,s2))


vectorizer=CountVectorizer().fit([s1,s2])
vectors=vectorizer.transform([s1,s2])
cos_sim=cosine_similarity(vectors[0],vectors[1])[0][0]
print("Cosine Similarity:",cos_sim)


def lcs_length(X,Y):
  m,n=len(X),len(Y)
  dp=[[0]*(n+1) for _ in range(m+1)]
  for i in range(m):
    for j in range(n):
      if X[i]==Y[j]:
        dp[i+1][j+1]=dp[i][j]+1
      else:
        dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
  return dp[m][n]

seq1="ABCCDEF"
seq2="AEBDF"
length=lcs_length(seq1,seq2)
print(f"Longest Common Subsequence length between '{seq1}' and '{seq2}' : {length}")