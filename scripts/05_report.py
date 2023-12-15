from fpdf import FPDF

pdf = FPDF()

pdf.add_page()
pdf.set_xy(0, 0)
pdf.set_font('arial', 'B',12)
pdf.cell(60)
pdf.cell(75, 10, "BIOS611 Final Project Report", 0, 2, 'C')
pdf.cell(75, 10, "Breast Cancer Proteomes", 0, 2, 'C')
pdf.cell(75, 10, "Julia Webb", 0, 2, 'C')
pdf.cell(-50)
pdf.multi_cell(190,10,'This analysis explores the Breast Cancer Proteomes dataset from Kaggle. It contains three datafiles: clinical data from the patients, actual proteomic data from patient tumor samples, and a list of genes used for breast cancer classification.', align='left')
pdf.multi_cell(190,10,'Breast cancer classification has evolved with experimental methods, from immunohistochemistry to microarrays to the current age of sequencing.',align='left')
pdf.multi_cell(190,10,'I wanted to explore how classification changed with the amount of data considered.', align='left')
pdf.multi_cell(190,10,'In Figure 1 I look at the distribution of molecular subtypes across the patients. These were determined via clustering based off of microarray data and have remained important diagnostic tools.')
pdf.multi_cell(190,10,'There is a good even distribution of subtypes, with the most patients falling into the better prognosis luminal subtypes than in the poor prognosis basal subtype.')
pdf.multi_cell(190,10,'In Figure 2 I looked at the distribution of cell surface marker presentation among the tumor samples. ')
pdf.multi_cell(190,10,'In Figures 3 and 4 I performed dimensionality reduction using PCA followed by clustering using KNN. I wanted to see how the perfomance would vary with the amount of data used.')
pdf.multi_cell(190,10,'In Figure 3, I used all of the available proteomic data, whereas in Figure 4, I only used proteins from the PAM50 panel, which is what was originally used in the microarray studies to determine molecular subtypes.')
pdf.multi_cell(190,10,'As can be seen by the better accuracy and more explanation of variance by the principal components, using only the PAM50 proteins is a better way to predict molecular subtype than using all the available proteins.')
pdf.multi_cell(190,10,'This is counter to what I expected, but in retrospect it makes sense as the majority of the proteome is likely not altered between subtypes, so using all of the data retains a lot of unnecessary noise.')

pdf.add_page()
fig1 = 'figures/figure1.png'
pdf.image(fig1, x=50, y=20, w=100, h=100)
pdf.cell(30, 225, 'Figure 1')
pdf.cell(30,245,'Prevalence of breast cancer molecular subtypes within cohort')


pdf.add_page()
fig2 = 'figures/figure2.png'
pdf.image(fig2, x=50, y=20, w=100, h=100)
pdf.cell(30, 225, 'Figure 2')
pdf.cell(30,245,'Prevalence of cell surface markers within cohort')

pdf.add_page()
fig3 = 'figures/figure3.png'
pdf.image(fig3, x=50, y=20, w=100, h=100)
pdf.cell(30, 225, 'Figure 3')
pdf.cell(30,245,'PCA and KNN using all proteins')


pdf.add_page()
fig4 = 'figures/figure4.png'
pdf.image(fig4, x=50, y=20, w=100, h=100)
pdf.cell(30, 225, 'Figure 4')
pdf.cell(30,245,'PCA and KNN using only PAM50 proteins')

pdf.add_page()
pdf.multi_cell(190,10,'Overall, this analysis emphasized the idea that using a smaller amount of data with known biological significance can be more effective than using a larger amount of data with unknown relevance to the question.')
pdf.multi_cell(190,10,'Moving forward, I would be interested to search for other proteins outside the PAM50 list that contribute to better sample classification. These proteins would likely be interesting for further experimental validation in their relevance to breast cancer phenotypes.')

pdf.output('report.pdf', 'F')
