from html_para_pdf import converter_html_para_pdf

mock__html = '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Document</title>
        <style type="text/css">
            body {
                font-family: sans-serif;
                background-color: #141414 !important;
                color: #fff !important;
            }
        </style>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <small></small>
    </body>
</html>
'''

print('Converter arquivo .html para .pdf')
print('  > deve retornar o caminho do arquivo pdf gerado a partir do book.html')


def describe_converter_book_html_para_pdf():
    caminho_pdf = converter_html_para_pdf(mock__html)
    return caminho_pdf


caminho = describe_converter_book_html_para_pdf()

print('  > caminho registrado como “' + caminho + '”')
