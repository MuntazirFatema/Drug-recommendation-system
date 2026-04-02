# 💊 Drug Recommendation System

An AI-powered web application that recommends medications based on patient clinical parameters using Machine Learning.

🔗 **Live Demo:** [drug-recommendation-system-jlhi.onrender.com](https://drug-recommendation-system-jlhi.onrender.com)

---

## 🧠 What It Does

A doctor enters a patient's clinical details — age, sex, blood pressure, cholesterol, and sodium-to-potassium ratio — and the system instantly recommends the most suitable drug from 5 possible medications.

---

## 🚀 Features

- Predicts one of 5 drug classes: DrugA, DrugB, DrugC, DrugX, DrugY
- Displays clinical description, dosage instructions, and monitoring advice for each drug
- Color-coded result cards for each drug type
- Clean, professional medical UI
- Deployed live on Render

---

## 🤖 Machine Learning

| Detail | Value |
|---|---|
| Algorithm | Decision Tree Classifier |
| Dataset | Drug200 (UCI / Kaggle) |
| Training Accuracy | 100% |
| Test Accuracy | 100% |
| Features | Age, Sex, BP, Cholesterol, Na_to_K |
| Target Classes | DrugA, DrugB, DrugC, DrugX, DrugY |

### Models Compared

| Model | Test Accuracy |
|---|---|
| Logistic Regression | 45% |
| Decision Tree | **100%** ✅ |
| Random Forest | 97.5% |
| Gradient Boosting | 100% |
| XGBoost | 100% |

Decision Tree was chosen for its perfect accuracy and interpretability — doctors can read the exact rules the model uses.

### Key Insight

The strongest predictor is the **Na_to_K ratio**:
- Na_to_K > 14.83 → always DrugY (covers 45% of all cases)
- HIGH BP + Age ≤ 50 → DrugA
- HIGH BP + Age > 50 → DrugB
- LOW BP + Normal Cholesterol → DrugC
- LOW/NORMAL BP + HIGH Cholesterol → DrugX

---

## 🛠️ Tech Stack

- **Python** — ML pipeline
- **scikit-learn** — model training and evaluation
- **Flask** — web framework
- **joblib** — model serialization
- **HTML/CSS** — frontend UI
- **Render** — deployment

---

## 📁 Project Structure

```
drug-recommendation-system/
├── app.py                  # Flask backend
├── drug_model.pkl          # Trained Decision Tree model
├── requirements.txt        # Python dependencies
├── Procfile                # Render deployment config
└── templates/
    └── index.html          # Frontend UI
```

---

## ⚙️ How to Run Locally

```bash
# Clone the repository
git clone https://github.com/MuntazirFatema/Drug-recommendation-system.git

# Navigate to project folder
cd Drug-recommendation-system

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

---

## 📊 Input Parameters

| Parameter | Type | Values |
|---|---|---|
| Age | Number | 15 – 74 |
| Sex | Dropdown | Male, Female |
| Blood Pressure | Dropdown | LOW, NORMAL, HIGH |
| Cholesterol | Dropdown | NORMAL, HIGH |
| Na_to_K Ratio | Number | 6.2 – 38.2 |

---

## ⚠️ Disclaimer

This application is built for **educational purposes only**. Always consult a licensed physician before prescribing or administering any medication.

---

## 👩‍💻 Author

**Fatema** — Electronics and Communication Engineering Student
Gujarat Technological University | Aspiring ML Engineer
