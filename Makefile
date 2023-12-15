### set variables ###
FIGURES = figures

figs := $(FIGURES)/01_figure1.pdf\
		$(FIGURES)/02_figure2.pdf\
		$(FIGURES)/03_figure3.pdf\
		$(FIGURES)/04_figure4.pdf

### define fxns ### 
.PHONY: clean all

all : $(figs)

clean:
	rm figures/*
	rm processed.csv

folders:
	mkdir figures

# ### processing ###
processed.csv: scripts/00_preprocessing.py\
data/77_cancer_proteomes_CPTAC_itraq.csv\
data/clinical_data_breast_cancer.csv\
data/PAM50_proteins.csv
	python scripts/00_preprocessing.py

### figures ###
figures/01_figure1.pdf: scripts/01_figure1.py processed.csv
	python scripts/01_figure1.py

figures/02_figure2.pdf: scripts/02_figure2.py processed.csv
	python scripts/02_figure2.py

figures/03_figure3.pdf: scripts/03_figure3.py processed.csv
	python scripts/03_figure3.py

figures/04_figure4.pdf: scripts/04_figure4.py processed.csv
	python scripts/04_figure4.py