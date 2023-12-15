# Hi, this is my 611 Data Science Project.

This project will explore the public dataset "Breast Cancer Proteomes" from Kaggle (https://www.kaggle.com/datasets/piotrgrabo/breastcancerproteomes/data) , which features proteome profiling of 77 breast cancer patients.

The source data consist of three files: 77_cancer_proteomes_CPTAC_itraq.csv, clinical_data_breast_cancer.csv, and PAM50_proteins.csv.

## Build and run Docker image
`docker build . -t bios`<br />
`docker run --rm -p 8787:8787 -it -v $(pwd):/home/project py /bin/bash`

## Running the analysis
This project uses Make, which will automatically generate all figures, reports, etc.  
You need to create some folders the first time you use it:
`make folders`<br />
You can remove any existing outputs with:
`make clean`<br />
Once that's done, just run:
`make`
or
`make all`
