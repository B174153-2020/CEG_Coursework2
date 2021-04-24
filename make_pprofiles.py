#!/usr/bin/python3

# Convert OrthoFinder output to phylogenetic profiles
# Process Orthofinder gene count output file to create tab-delimited
# phylogenetic profiles. This script generates one line of output per
# orthogroup. Each row contains the orthogroup name, followed by
# tab-delimited fields containing "1" if the orthogroup is present in
# the taxon and "0" otherwise.


# Load library
import pandas as pd

# Read file into a dataframe
df=pd.read_csv("data/OrthoFinder/Results_Apr24/Orthogroups/Orthogroups.GeneCount.tsv",sep="\t",header=0,index_col="Orthogroup")
df.index.name=None

# Drop the "Total" column which we do not use
df=df.drop(["Total"],axis=1)

# Def a function to return 1 if the gene count is nonzero
# or 0 for the gene count is zero
def profile(x):
    if x>0:
        return 1
    else:
        return 0

# Apply profile function into every value in the dataframe
df_profile=df.applymap(profile)

# Save the new dataframe as a tsv file
df_profile.to_csv("phylogenetic_profiles.tsv",sep="\t",header=1)
