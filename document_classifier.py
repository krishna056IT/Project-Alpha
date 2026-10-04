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


sample_text = """
Name: Krishna
Date of Birth: 15/08/2005
Place of Birth: Raipur
"""

document_type = classify_document(sample_text)

print("Document Type:", document_type)