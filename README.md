# 🔐 ControlMind AI: GRC Control Extractor & Mapper

An AI-driven system that extracts, structures, and maps security controls across compliance frameworks like ISO 27001 and HIPAA using Large Language Models (LLMs).

---

## 🚀 Overview

Organizations often struggle to align and analyze controls across multiple compliance frameworks. This project automates:

- Extraction of controls from unstructured documents  
- Categorization into security domains  
- Mapping of similar controls across frameworks  
- Validation of mappings using similarity scoring  

---

## 🧠 Key Features

- 🤖 LLM-based control extraction (Google Gemini 2.5 Flash)  
- 📊 Structured output generation (JSON → CSV/Excel)  
- 🔗 Cross-framework control mapping  
- 📈 Similarity scoring using text matching  
- ✅ Validation layer for accuracy assessment  

---

## 🛠️ Tech Stack

- Python  
- Google Gemini API (LLM)  
- Pandas  
- Difflib (text similarity)  

---

## 📂 Project Structure

```
compliance-gpt/
│
├── data/                # Input framework text
├── src/                 # Core logic (extractor, mapper, validator)
├── output/              # Generated results
├── main.py              # Entry point
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

1. Input raw framework text (ISO / HIPAA)  
2. Extract controls using LLM  
3. Convert to structured format (description + category)  
4. Map controls using similarity scoring  
5. Validate mappings (Strong / Moderate / Weak)  
6. Export results to CSV  

---

## ▶️ Run the Project

```bash
pip install -r requirements.txt
python main.py
```

---

## 📊 Sample Output

| control_1 | control_2 | similarity_score | validation |
|----------|----------|----------------|-----------|
| Unique user ID | Each user uniquely identified | 0.82 | Strong Match |
| Role-based access | Authorized access only | 0.76 | Strong Match |

---

## 🌍 Real-World Use Case

- Automates compliance alignment across frameworks  
- Reduces manual effort in audits  
- Helps GRC teams in cybersecurity and risk management  
- Enables scalable control analysis  

---

## 🔥 Future Improvements

- Streamlit UI for visualization  
- Multi-framework support (SOC2, PCI-DSS)  
- Embedding-based semantic matching  
- Confidence scoring using LLM  

---

## 👨‍💻 Author

Built as part of preparation for AI + GRC roles, focusing on real-world applications of LLMs in compliance automation.
