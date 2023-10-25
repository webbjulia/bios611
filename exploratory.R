library(tidyverse)
library(readr)

# load data
data_proteome = read_csv('data/77_cancer_proteomes_CPTAC_itraq.csv')
data_clinical = read_csv('data/clinical_data_breast_cancer.csv')
list_pam50 = read_csv('data/PAM50_proteins.csv')

# exploratory figures for clinical data

pdf(file="figures/exploratory_figs.pdf")

ggplot(data = data_clinical, aes(Gender)) + geom_histogram(stat="count")
ggplot(data = data_clinical, aes(data_clinical$`Age at Initial Pathologic Diagnosis`)) + geom_histogram() +
  labs(x='Age at Diagnosis')

dev.off()
# exploratory figures for proteomic data



       