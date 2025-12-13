from docling.document_converter import DocumentConverter


def main():
    source = "https://arxiv.org/pdf/2408.09869"  # file path or URL
    converter = DocumentConverter()
    doc = converter.convert(source).document

    print(doc.export_to_markdown())  # output: "### Docling Technical Report[...]"


if __name__ == "__main__":
    main()