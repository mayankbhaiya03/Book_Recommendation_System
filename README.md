# 📚 Book Recommendation System

> A machine learning–based system that recommends books to users based on their preferences, ratings, and similarity to other readers.

---

## 👥 Team Information

**Course:** ECSP5004 – Machine Learning Lab  
**Institute:** Shri Ramdeobaba College of Engineering and Management, Nagpur  
**Semester:** V (2025–26)

**Group ID:** 19_ML_Lab_V_A  

| Member | Roll No. | Contribution |
|---------|-----------|--------------|
| Mayank Bhaiya | A-40 | Model development, evaluation, and documentation |
| Shubhra Sahu | A-52 | Data preprocessing, visualization, and report writing |

---

## 🎯 Project Overview

The **Book Recommendation System** predicts and recommends books to users by analyzing their reading patterns and preferences.  
The system combines **collaborative filtering** and **content-based filtering** approaches to suggest the most relevant books.  

The goal is to provide a personalized reading experience that helps users discover new books similar to those they’ve enjoyed in the past.

---

## 📦 Dataset

**Source:** [Book-Crossing Dataset – Kaggle](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset)  
**License:** CC BY-SA 4.0  

The dataset contains user ratings for thousands of books.

| File | Description |
|------|--------------|
| `BX-Books.csv` | Contains book titles, authors, and publication details |
| `BX-Book-Ratings.csv` | Contains user IDs, book ISBNs, and corresponding ratings |
| `BX-Users.csv` | Contains demographic information about users |

---

## ⚙️ Methodology

### 🧹 Data Preprocessing
- Removed duplicate and inconsistent user ratings  
- Handled missing book titles and author names  
- Merged datasets on common attributes (`ISBN`, `User-ID`)  
- Normalized rating scale and filtered users/books with sufficient activity  

### 🧠 Model Development
Two recommendation techniques were implemented and compared:

| Type | Algorithm | Description |
|------|------------|--------------|
| Collaborative Filtering | K-Nearest Neighbors (KNN) | Recommends based on similar users' preferences |
| Content-Based Filtering | TF-IDF Vectorization + Cosine Similarity | Recommends based on book content similarity |

### 🧾 Evaluation Metrics
- Precision@K  
- Recall@K  
- RMSE (for rating prediction tasks)

| Model | Metric | Score |
|--------|---------|-------|
| KNN (Collaborative) | Precision@10 | 0.78 |
| TF-IDF (Content-Based) | Precision@10 | **0.83** |

The **Content-Based Filtering** approach achieved better overall accuracy and personalization.

---



### 🔗 Links
- **Live Demo:**https://bookrecommendationsystem-4qc6cwmazsyj2sfdzpvswp.streamlit.app/*  
- **GitHub Repo:** https://github.com/mayankbhaiya03/Book_Recommendation_System 
- **Colab Notebook:**https://colab.research.google.com/drive/1CK2C1XS6iSiidW1giqawSxD04-urRS2p?usp=sharing

---

## 🧩 Installation & Usage

### 🔧 Requirements
```bash
pip install -r requirements.txt
python app.py
Reproducibility Checklist

✅ Dataset link provided
✅ Notebook with training & visualization results
✅ Saved model (.pkl) included
✅ Environment reproducible via requirements.txt
✅ Web app tested and working

📈 Results & Insights

TF-IDF + Cosine Similarity produced the most accurate recommendations.

The system can efficiently suggest books even for new users with minimal data.

Demonstrates how recommender systems enhance user engagement and personalization.

🚧 Limitations & Future Work

Currently works on static dataset; real-time user feedback integration pending

Cold-start problem can be mitigated with hybrid modeling

Future plan: integrate with Google Books API or Goodreads API for dynamic content

🤖 AI Tools Used
Tool	Purpose
ChatGPT	Code debugging and documentation assistance
Gemini	Report structuring and section drafting
Grammarly	Grammar and clarity improvements
QuillBot	Rewriting and paraphrasing

Total AI involvement: ≈ 42%

🏁 Acknowledgments

Faculty mentors: Prof. V. R. Gupta, Prof. P. A. Dwaramwar

Department of Electronics Engineering, RCOEM Nagpur

Dataset providers and open-source contributors

📜 Citation

Book-Crossing Dataset. Kaggle Dataset, 2024.
https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset

© 2025 Group_19_ML_Lab_V_A — All rights reserved
