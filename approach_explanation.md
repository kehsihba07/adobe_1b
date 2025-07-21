### Approach Explanation

We designed a generic PDF intelligence system that extracts relevant sections for any persona and job-to-be-done. 
It uses:
- PyMuPDF for parsing PDF content
- SentenceTransformers (MiniLM) for semantic ranking of content
- A lightweight model (<200MB) that runs entirely offline on CPU

Steps:
1. Load persona and task
2. Parse text from each page
3. Rank pages based on semantic similarity to persona+task
4. Output top-ranked sections and refined summaries in a structured JSON

The system supports up to 10 PDFs, works offline (no web access), and completes processing within 60 seconds.
