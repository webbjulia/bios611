.PHONY: clean all

all : figures/01_figure1.pdf figures/02_figure2.pdf\
 figures/03_figure3.pdf figures/04_figure4.pdf

clean:
	rm figures/*

figures/01_figure1.pdf: scripts/01_figure1.py
	python scripts/01_figure1.py


figures/02_figure2.pdf: scripts/01_figure1.py
	python scripts/02_figure2.py

figures/03_figure3.pdf: scripts/01_figure1.py
	python scripts/03_figure3.py

figures/04_figure4.pdf: scripts/01_figure1.py
	python scripts/04_figure4.py