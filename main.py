import fitz  # PyMuPDF
import json
import os
import re
from datetime import datetime
from sentence_transformers import SentenceTransformer, util

# Load model (≤200MB, CPU-compatible)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load persona and job (hardcoded for demo, can use input args/json)
persona = "Undergraduate Chemistry Student"
job_to_be_done = "Identify key concepts and mechanisms for exam preparation on reaction kinetics"
query = f"{persona}: {job_to_be_done}"

# Collect documents
input_dir = "input"
output_dir = "output"
docs = [f for f in os.listdir(input_dir) if f.endswith(".pdf")]

results = {
    "input_documents": docs,
    "persona": persona,
    "job_to_be_done": job_to_be_done,
    "processing_timestamp": datetime.now().isoformat(),
    "sections": [],
    "subsections": []
}

def extract_text_by_page(pdf_path):
    doc = fitz.open(pdf_path)
    content = []
    for page_num, page in enumerate(doc, start=1):
        text = page.get_text()
        content.append((page_num, text))
    return content

def rank_sections(text_blocks, query, top_k=5):
    texts = [text for (_, text) in text_blocks]
    embeddings = model.encode(texts, convert_to_tensor=True)
    query_emb = model.encode(query, convert_to_tensor=True)
    scores = util.pytorch_cos_sim(query_emb, embeddings)[0]
    top_indices = scores.argsort(descending=True)[:top_k]
    ranked = [(text_blocks[i][0], texts[i], float(scores[i])) for i in top_indices]
    return ranked

for doc_name in docs:
    full_path = os.path.join(input_dir, doc_name)
    pages = extract_text_by_page(full_path)

    ranked = rank_sections(pages, query)
    for rank, (page_num, text, score) in enumerate(ranked, 1):
        title = text.strip().split('\n')[0][:80]
        results["sections"].append({
            "document": doc_name,
            "page_number": page_num,
            "section_title": title,
            "importance_rank": rank
        })
        results["subsections"].append({
            "document": doc_name,
            "page_number": page_num,
            "refined_text": text.strip()[:500],
            "importance_rank": rank
        })

# Write output
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "results.json"), "w") as f:
    json.dump(results, f, indent=2)
