import PyPDF2
import json


def pdf_to_json(pdf_path, json_path):
    pdf = open(pdf_path, 'rb')
    reader = PyPDF2.PdfReader(pdf)

    data = []

    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text = page.extract_text()
        title = get_title(text)

        data.append({
            'title': title,
            'page_number': page_num + 1,
            'text': text
        })

    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    pdf.close()


def get_title(text):
    for line in text.splitlines():
        clean_line = line.strip()
        if not clean_line:
            continue
        if clean_line.isdigit():
            continue
        return clean_line
    
    return "Untitled"


if __name__ == "__main__":
    pdf_path = '../data/errata.pdf'
    json_path = '../data/errata.json'
    pdf_to_json(pdf_path, json_path)

