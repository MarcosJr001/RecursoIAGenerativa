import os
import pytesseract
from PIL import Image

# Diretórios de entrada e saída
INPUT_DIR = "inputs"
OUTPUT_DIR = "output"

# Certifique-se de que o diretório de saída existe
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Processa todas as imagens na pasta de entrada
for filename in os.listdir(INPUT_DIR):
    if filename.lower().endswith(('png', 'jpg', 'jpeg')):
        image_path = os.path.join(INPUT_DIR, filename)
        output_path = os.path.join(OUTPUT_DIR, f"{os.path.splitext(filename)[0]}.txt")
        
        # Carrega e processa a imagem
        image = Image.open(image_path)
        extracted_text = pytesseract.image_to_string(image)
        
        # Salva o texto extraído
        with open(output_path, "w", encoding="utf-8") as text_file:
            text_file.write(extracted_text)
        
        print(f"Texto extraído salvo em: {output_path}")

print("Processamento concluído!")
