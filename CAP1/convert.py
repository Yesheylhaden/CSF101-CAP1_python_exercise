from docx import Document

def convert_docx_to_txt(docx_file, txt_file):
    # Load the .docx file
    doc = Document(docx_file)
    
    # Open the .txt file for writing
    with open(txt_file, 'w', encoding='utf-8') as f:
        # Iterate through each paragraph in the .docx file
        for para in doc.paragraphs:
            # Write the text of the paragraph to the .txt file
            f.write(para.text + '\n')

# Example usage
convert_docx_to_txt('dictionary.docx', 'dictionary.txt')
