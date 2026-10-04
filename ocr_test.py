import os

# Disable the problematic PIR + oneDNN CPU path
os.environ["FLAGS_enable_pir_api"] = "0"

from paddleocr import PaddleOCR

ocr = PaddleOCR(
    lang="en",
    enable_mkldnn=False
)

result = ocr.predict("sample.png")

for res in result:
    texts = res["rec_texts"]

    for text in texts:
        print(text)