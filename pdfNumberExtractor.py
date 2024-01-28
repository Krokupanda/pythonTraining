import os
import fitz  # PyMuPDF library

def extract(pdf_path):
    # Open the PDF file
    doc = fitz.open(pdf_path)
    
    # Initialize an empty string to store extracted text
    extracted_text = ""
    
    # Iterate over each page in the PDF
    for page in doc:
        # Extract text from the page
        text = page.get_text()
        # Append extracted text to the overall extracted_text string
        extracted_text += text
    
    # Close the PDF file
    doc.close()
    
    return extracted_text

def search_expressions(extracted_text):
    import re
    match1 = re.search(r'HKA(\d+)', extracted_text)
    match2 = re.search(r'Totals', extracted_text)
    match3 = None
    next_line = None
    if match2:
        lines = extracted_text.split('\n')
        index_totals = lines.index(match2.group()) if match2 else -1
        if index_totals != -1 and index_totals + 1 < len(lines):
            next_line = lines[index_totals + 1]
        if index_totals != -1 and index_totals + 2 < len(lines):
            match3 = lines[index_totals + 2]
            # Check if match3 contains numbers
            if match3:
                # Change decimal sign '.' to ','
                match3 = match3.replace('.', ',')
                # Remove thousands separators if found
                # match3 = re.sub(r'(\d)(\.)(?=\d)', r'\1', match3)
                # Remove first comma in numbers from '1000' and up
                match3 = re.sub(r'(?<=\d),(?=\d{3,})', '', match3)
    return match1.group() if match1 else '', match2.group() if match2 else '', match3 if match3 else '', next_line if next_line else ''

def process_pdfs(folder_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_file_path = os.path.join(output_folder, "output.txt")

    with open(output_file_path, 'w') as output_file:
        for filename in os.listdir(folder_path):
            if filename.endswith('.pdf'):
                pdf_path = os.path.join(folder_path, filename)
                contents = extract(pdf_path)
                matches = search_expressions(contents)
                output_line = f"{matches[0]}\t\t{matches[3]}\t\t{matches[2]}\n"
                #output_line = f"{matches[0]}\t\t{matches[1]}\n"
                output_file.write(output_line)

            
if __name__ == "__main__":
    folder_path = "C:\\Users\\Alexander\\Desktop\\WebDevTraining\\Python training\\pdfTest\\input"  # Update with your actual folder path
    output_folder = "C:\\Users\\Alexander\\Desktop\\WebDevTraining\\Python training\\pdfTest\\output"  # Update with your desired output folder path

    process_pdfs(folder_path, output_folder)

