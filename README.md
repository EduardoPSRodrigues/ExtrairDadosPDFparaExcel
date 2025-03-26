## Extração de Dados de PDFs

Este projeto permite a extração de tabelas de arquivos PDF e exportação dos dados para um arquivo CSV, facilitando a cópia e manipulação no Excel.

### Requisitos
Antes de rodar o código, certifique-se de ter instalado os seguintes pacotes Python:

- `pdfplumber`
- `pandas`

Você pode instalá-los executando o seguinte comando no terminal:

```sh
pip install pdfplumber pandas
```

### Como Usar
1. Certifique-se de que o arquivo PDF que deseja processar esteja na mesma pasta do script Python.
2. Edite o código para garantir que o nome do arquivo PDF correto esteja na variável `pdf_path`.
3. Execute o script com o comando:

```sh
python extrair_dados_PDF_to_CSV.py
```

4. O script gerará um arquivo chamado `dados_extraidos.csv` com os dados extraídos.
5. Você pode abrir o CSV no Excel ou copiar diretamente a saída do terminal para uma planilha.

### Observação
O código processará todas as páginas do PDF e extrairá apenas tabelas detectadas pelo `pdfplumber`. Se o documento não estiver corretamente formatado como tabela, pode ser necessário um ajuste manual.

