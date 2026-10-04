import os

# Fix for PaddlePaddle 3.3.1 + Windows CPU
os.environ["FLAGS_enable_pir_api"] = "0"

from paddleocr import PaddleOCR


def classify_document(text):
    text = text.lower()

    if "date of birth" in text or "place of birth" in text:
        return "Birth Certificate"

    if "annual income" in text or "income certificate" in text:
        return "Income Certificate"

    if "caste" in text or "scheduled caste" in text or "scheduled tribe" in text:
        return "Caste Certificate"

    if "residence" in text or "domicile" in text or "residential address" in text:
        return "Residence Certificate"

    if "scholarship" in text or "academic year" in text:
        return "Scholarship Application"

    return "Unknown"


# Initialize OCR
ocr = PaddleOCR(
    lang="en",
    enable_mkldnn=False
)

# Run OCR
result = ocr.predict("sample.png")

# Extract text
texts = []

for res in result:
    texts.extend(res["rec_texts"])

# Combine OCR text
extracted_text = "\n".join(texts)

print("\n--- EXTRACTED TEXT ---")

print(extracted_text)

# Classify document
document_type = classify_document(extracted_text)

print("\n--- DOCUMENT CLASSIFICATION ---")
print("Document Type:", document_type)