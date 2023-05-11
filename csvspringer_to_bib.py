import csv

# Define a função para formatar o autor no estilo BibTeX
def format_author(author):
    last_name, first_name = author.split(" ", 1)
    return "{}, {}".format(last_name, first_name)

# Abre o arquivo .csv de entrada
with open('SearchResults.csv', mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # Abre o arquivo .bib de saída
    with open('base_springer.bib', mode='w', encoding='utf-8') as bib_file:

        # Percorre cada linha do arquivo .csv
        for row in csv_reader:

            # Cria uma string para armazenar os autores formatados
            authors = ""

            # Percorre cada autor separado por vírgula
            for author in row["Authors"].split(","):
                # Formata o autor e adiciona na string
                authors += format_author(author) + " and "

            # Remove o último " and " da string de autores
            authors = authors[:-5]

            # Escreve a entrada no arquivo .bib
            bib_file.write("@article{{{0},\n".format(row["Item DOI"]))
            bib_file.write("title = {{{0}}},\n".format(row["Item Title"]))
            bib_file.write("journal = {{{0}}},\n".format(row["Publication Title"]))
            bib_file.write("volume = {{{0}}},\n".format(row["Journal Volume"]))
            bib_file.write("number = {{{0}}},\n".format(row["Journal Issue"]))
            bib_file.write("year = {{{0}}},\n".format(row["Publication Year"]))
            bib_file.write("doi = {{{0}}},\n".format(row["Item DOI"]))
            bib_file.write("author = {{{0}}},\n".format(authors))
            bib_file.write("url = {{{0}}},\n".format(row["URL"]))
            bib_file.write("}\n\n")
