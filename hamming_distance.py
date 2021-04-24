#!/usr/bin/python3

# Calculate the Hamming distance between phylogenetic profiles and output discovered orthogroups


# Load library
import pandas as pd

# Read the phylogenetic profiles file into dataframe
df_profile=pd.read_csv("phylogenetic_profiles.tsv",sep="\t",header=None, index_col=0)
df_nifH=df_profile.loc[["OG0001597"]]

# Def a function to calculate the Hamming distance
def Hammingdistance(s1, s2):
    d=0
    for i in range(len(s1)):
        if s1[i] !=s2[i]:
            d+=1
    return d

# Apply Hammingdistance function and get the output
hd=[]
for i in df_profile.values.tolist():
    hd.append(Hammingdistance(i, df_nifH.values.tolist()[0]))
df_hd=pd.DataFrame({"Hammingdistance":pd.Series(hd)})
df_hd.index=df_profile.index
df_hd=df_hd[(df_hd["Hammingdistance"]==0)]
orthogroups=df_hd.index.tolist()

# Save the output
File=open("orthogroups.txt","w")
File.write("\n".join(orthogroups))
File.close()
