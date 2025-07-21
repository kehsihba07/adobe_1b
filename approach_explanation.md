## Project Title: PDF Intelligence – Round 1B

### Objective

The main aim of this project was to develop a simple yet effective tool that could read PDFs, understand their content, and pick out the most important parts of the text. We wanted to make it easier for students or professionals to focus only on key information rather than reading the entire document. This tool is especially helpful for exam preparation or research, where time is limited.

---

### Methodology

We started by creating two folders – one for input and one for output. The user can simply place PDF files into the `input/` folder, and once the script runs, the processed output is saved in the `output/` folder. This keeps everything organized and clean.

To extract text from the PDFs, we used a Python library called `PyMuPDF`. It lets us go through each page and pull out all the readable text. We kept the extraction page-wise so we could rank individual pages based on their importance later.

For understanding the meaning of the text, we used a machine learning model from the `sentence-transformers` package. This model converts text into numerical vectors that help compare how similar or relevant each page is to a specific query. In our case, we used a scenario like a "Chemistry student preparing for exams" to guide what kind of information the script should prioritize.

Each page was scored based on how relevant it was to that context. The top-scoring pages were collected and added to the final JSON file along with some summary details like page number, rank, and a short snippet from that page.

To make the project easy to share and run on any machine, we also built a Docker container. This ensures that even if someone has a different operating system or Python version, the script will still run the same way.

---

### Final Thoughts

This project was built with simplicity in mind. It doesn’t try to be overly fancy or complicated, but it does its job well. The structure is modular, so it can be improved later—for example, by adding support for scanned PDFs or multiple languages. The goal was to save time and help users quickly understand what matters in large PDF documents.

