import logging
from io import BytesIO

#from PyPDF2.pdf import PdfFileReader
#from PyPDF2.utils import PyPdfError
from PyPDF2 import PdfFileReader
#from PyPDF2 import PyPdfError
from bs4 import BeautifulSoup

_LOGGER = logging.getLogger(__file__)


def _parse_htm(content: bytes, encoding: str) -> str:
    return BeautifulSoup(content, "lxml", from_encoding=encoding).get_text("\n\n")


def _parse_xml(content: bytes, encoding: str) -> str:
    return BeautifulSoup(content, "xml", from_encoding=encoding).get_text("\n\n")


def _parse_txt(content: bytes, encoding: str) -> str:
    return content.decode(encoding)


def _parse_pdf(content: bytes, _: str) -> str:
    #try:
    return "\n".join(page.extractText() for page in PdfFileReader(BytesIO(content)).pages)
    # except PyPdfError as e:
    #     _LOGGER.exception(e)
    #     return ""
    #@except:
        #return ""
