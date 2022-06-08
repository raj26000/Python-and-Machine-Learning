# PDF Ingestion Pipeline
Pipeline for reading all PDF files from a directory and returning a single list of dictionaries with pre-defined keys using all the files.

## Salient Features: 
* Config driven extraction of model names and file metadata by mapping the PDF filenames. Refer **`config.json`**.
* Header and Footer extraction and removal(using font size) enabled after parsing PDFs.
* Generalized pipeline to extract required output from any given directory of PDF files.
* Filters out Contents pages from PDFs and merges short paragraphs having < 10 tokens.

## Files Required 
```
 - ingest.py
 - config.json
 ```
 
 ## Usage
 ```
 from ingest import PDFIngestionPipeline
 pipe = PDFIngestionPipeline('PATH_TO_PDF_DIR')
 data = pipe.getall_pdf_data()
 ```
 Where the output `data` can be interpreted as follows (for each dictionary):
 ```
 [
		{
		"id": "<model_name>_page_<pagenum>_block_<blocknum>",
		"page_id": <model_name>_page_<pagenum>",
		"block_attr": ["ocrx_block"],
		"model": "model name” if present,
		"file_metadata": [model name, other related metadata information]
		},
		....
]
```