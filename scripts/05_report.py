from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

pdf.set_xy(0, 0)
pdf.set_font('arial', 'B', 12)
pdf.cell(60)
pdf.cell(75, 10, "BIOS611 Final Project Report", 0, 2, 'C')
pdf.cell(75, 10, "Breast Cancer Proteomes", 0, 2, 'C')
pdf.cell(75, 10, "Julia Webb", 0, 2, 'C')

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


pdf.output('report.pdf', 'F')
