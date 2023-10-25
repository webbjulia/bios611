PHONY: clean

clean:
	rm figures/*


figures/exploratory_figs.pdf: data/clinical_data_breast_cancer.csv exploratory.R
	Rscript exploratory.R
