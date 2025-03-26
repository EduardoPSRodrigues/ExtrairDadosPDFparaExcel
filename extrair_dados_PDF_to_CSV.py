import pdfplumber
import pandas as pd

# Insira o nome do arquivo PDF, o arquivo terá que estar na mesma pasta do programa
pdf_path = "SECSAÚDE.pdf"

# Lista para armazenar os dados extraídos
data = []

# Abrir o arquivo PDF
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        table = page.extract_table()
        if table:
            data.extend(table)

# Converter os dados para um DataFrame do pandas
df = pd.DataFrame(data)

# Exportar para formato compatível com Excel
df.to_csv("dados_extraidos.csv", sep="\t", index=False, header=False)

# Exibir saída formatada para copiar e colar no Excel
for row in df.itertuples(index=False, name=None):
    print("\t".join(map(str, row)))
