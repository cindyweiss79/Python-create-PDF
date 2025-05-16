from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", size=12)

# Titolo
pdf.set_font("Helvetica", 'B', 14)
pdf.cell(0, 10, "Schema Schematico di Cerchiatura in Cemento Armato", ln=True, align='C')

pdf.ln(10)

# Descrizione generale
pdf.set_font("Helvetica", size=12)
pdf.multi_cell(0, 10, """\
Cerchiatura in cemento armato per vano 3.00 m x 2.00 m (luce netta), realizzata con telaio in c.a. composto da:

- Trave architrave in c.a. 30x50 cm
- Pilastri laterali in c.a. 30x30 cm
- Fondazione o cordolo di appoggio
- Collegamenti con muratura esistente tramite barre ad aderenza migliorata

Armatura (indicativa):
Trave: 4phi20 inferiori + 2phi14 superiori, staffe phi8/15
Pilastri: 4phi16 verticali, staffe phi8/15
""")

pdf.ln(5)
pdf.set_font("Helvetica", 'B', 12)
pdf.cell(0, 10, "Legenda:", ln=True)

pdf.set_font("Helvetica", size=12)
pdf.multi_cell(0, 10, """\
ARCHITRAVE      = Trave orizzontale in c.a. 30x50 cm
PILASTRO        = Montanti verticali in c.a. 30x30 cm
FONDAZIONE      = Cordolo o plinto in c.a. per scarico carichi
ARMATURA        = Ferri longitudinali e staffe secondo normativa
""")

# Disegno schematico
pdf.ln(5)
pdf.set_font("Courier", size=11)
schema = """
  +-----------------------------+
  |        ARCHITRAVE 30x50     |
  +-----------------------------+
  |                             |
  |         VANO 3.00 m         |
  |                             |
  |   |                   |     |
  |   |                   |     |
  |   |                   |     |
  |   |                   |     |
  +-------------------------+
      PILASTRI 30x30 + FONDAZIONE
"""
pdf.multi_cell(0, 6, schema)

pdf.output("cerchiatura.pdf")


import os
# Salva il PDF
pdf.output("cerchiatura.pdf")
# Apri il PDF con il visualizzatore predefinito (funziona su Mac)
os.system("open cerchiatura.pdf")
