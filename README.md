# Explorando os Recursos de IA Generativa com Copilot e OpenAI

## Visão Geral
Este projeto explora o uso de IA Generativa, especificamente as capacidades do OpenAI e do Copilot, para reconhecimento e processamento de imagens contendo texto. Utilizamos técnicas de OCR (Optical Character Recognition) para extrair informações de imagens e demonstramos como a IA pode ser aplicada para automação e análise de conteúdo visual.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
/explorando_ia_generativa
│-- inputs/     # Contém as imagens utilizadas no projeto
│-- output/     # Contém os resultados do reconhecimento de texto
│-- readme.md   # Documentação do projeto
│-- script.py   # Script para processamento das imagens
```

### Inputs
Na pasta `inputs/`, adicionamos imagens que contêm texto manuscrito, impresso ou em placas de sinalização. Essas imagens são utilizadas como entrada para o processamento de OCR.

### Outputs
Na pasta `output/`, salvamos os arquivos com os textos extraídos das imagens. Cada imagem de entrada tem um correspondente arquivo de saída contendo o texto reconhecido pela IA.

### Script de Processamento
Criamos um script utilizando a API da OpenAI para realizar o reconhecimento de texto a partir das imagens fornecidas. O script faz uso de bibliotecas como `pytesseract` para OCR e `Pillow` para manipulação de imagens.

## Como Rodar o Projeto

1. Clone este repositório:
   ```sh
   git clone https://github.com/seuusuario/explorando_ia_generativa.git
   ```
2. Instale as dependências necessárias:
   ```sh
   pip install pytesseract pillow openai
   ```
3. Execute o script para processar as imagens:
   ```sh
   python script.py
   ```
4. Os resultados serão salvos na pasta `output/`.

## Insights e Aprendizados
- O uso de IA Generativa e OCR pode automatizar processos manuais de extração de dados.
- OpenAI pode complementar o OCR tradicional ao interpretar textos extraídos de forma mais inteligente.
- O Copilot facilita a escrita de código ao sugerir trechos eficientes para reconhecimento e manipulação de imagens.

---
Este projeto demonstra como combinar OpenAI e Copilot para criar soluções eficientes de análise e reconhecimento de texto a partir de imagens, aplicáveis em diversas áreas como digitalização de documentos e acessibilidade digital.

