from weasyprint import CSS, HTML
import datetime


def converter_html_para_pdf(html: str) -> str:
    html = HTML(string=html)

    pathname = "./documents/" + datetime.datetime.now().isoformat() + ".pdf"

    html.write_pdf(pathname)
    return pathname
