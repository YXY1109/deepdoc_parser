from parser import TxtParser


def test_docx_parser(file_path):
    parser = DocxParser()
    secs, tbls = parser(file_path)
    print("DOCX 解析结果：")
    print("段落内容：", secs)
    print("表格内容：", tbls)


def test_excel_parser(file_path):
    parser = ExcelParser()
    res = parser(file_path)
    print("Excel 解析结果：")
    print(res)


def test_txt_parser(file_path):
    parser = TxtParser()
    result = parser(file_path)
    print("TXT 解析结果：")
    print(result)


if __name__ == "__main__":
    txt_file = "file/demo.txt"
    test_txt_parser(txt_file)

    docx_file = "path/to/your/file.docx"
    excel_file = "path/to/your/file.xlsx"

    # test_docx_parser(docx_file)
    # test_excel_parser(excel_file)
