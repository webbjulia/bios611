# import libraries
import pandas as pd
import re

# load in data
proteomes = pd.read_csv("data/77_cancer_proteomes_CPTAC_itraq.csv")
clinical = pd.read_csv("data/clinical_data_breast_cancer.csv")
pam50 = pd.read_csv("data/PAM50_proteins.csv")

# drop weird duplicate entries
proteomes.drop(['AO-A12D.05TCGA','AO-A12B.34TCGA', 'C8-A131.32TCGA'],axis=1,inplace=True)

# rename patient ID's in proteomes file to match clinical format
proteomes.rename(
    columns=lambda x: "TCGA-%s" % (re.split('[_|-|.]',x)[0]) 
    if bool(re.search("TCGA",x)) is True else x,inplace=True)

# drop unnecessary columns
proteomes.drop(['gene_symbol','gene_name'],axis=1,inplace=True)

# get list of patients w both data types
patients_proteomes = list(proteomes.columns[1:])
patients_clinical = list(clinical['Complete TCGA ID'])
patients_77 = list(set(patients_proteomes) & set(patients_clinical))

# rearrange proteome data
proteomes = proteomes.set_index('RefSeq_accession_number').T.rename_axis('Complete TCGA ID').reset_index()
proteomes = proteomes.rename_axis(None, axis=1)

# keep only patients in list
clinical = clinical[clinical['Complete TCGA ID'].isin(patients_77)]
clinical = clinical.sort_values(by=['Complete TCGA ID'])

# keep onluy patients in list
proteomes = proteomes[proteomes['Complete TCGA ID'].isin(patients_77)]
proteomes = proteomes.sort_values(by=['Complete TCGA ID'])

# merge proteome and clinical data into one df, save as csv
merged = proteomes.set_index('Complete TCGA ID').join(clinical.set_index('Complete TCGA ID'))
merged.to_csv('processed.csv')