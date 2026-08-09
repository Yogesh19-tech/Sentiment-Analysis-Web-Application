# Sentiment Analysis using Machine Learning and Flask

A simple **Sentiment Analysis Web Application** built using Python, Machine Learning, and Flask. The application takes a text input and predicts whether the sentiment is **Positive** or **Negative**.

The machine learning model uses **TF-IDF Vectorization** to convert text into numerical features and **Logistic Regression** for sentiment classification.

## 🚀 Features

* Text preprocessing and cleaning
* TF-IDF text vectorization
* Logistic Regression classification
* Positive/Negative sentiment prediction
* Flask-based web application
* REST API support using JSON
* Pre-trained model saved using Pickle
* Simple browser-based prediction interface

## 🛠️ Technologies Used

* Python
* Flask
* Pandas
* NumPy
* Scikit-learn
* TF-IDF Vectorizer
* Logistic Regression
* Pickle
* HTML

## 📂 Project Structure

```text
sentiment-analysis/
│
├── app.py                  # Flask application
├── train.py                # Model training script
├── sentiment_dataset.csv   # Sentiment dataset
├── model.pkl               # Trained Logistic Regression model
├── vectorizer.pkl          # Trained TF-IDF vectorizer
├── requirements.txt        # Project dependencies
├── .gitignore              # Git ignored files
└── README.md               # Project documentation
```

> **Note:** The `venv` folder should not be uploaded to GitHub. It is better to create the virtual environment locally using the instructions below.

## ⚙️ How the Project Works

The project follows these steps:

```text
User Input
    ↓
Text Preprocessing
    ↓
TF-IDF Vectorization
    ↓
Logistic Regression Model
    ↓
Sentiment Prediction
    ↓
Positive / Negative
```

### 1. Dataset

The project uses `sentiment_dataset.csv`, which contains text data and corresponding sentiment labels.

Example:

```text
text                         label
------------------------------------------------
"I love this product"          1
"This is very good"            1
"I hate this product"          0
"Very bad experience"          0
```

Where:

* `1` = Positive
* `0` = Negative

### 2. Text Preprocessing

The text is converted to lowercase and unwanted characters are removed.

Example:

```text
"I LOVE this Product!!!"
```

becomes:

```text
"i love this product"
```

### 3. TF-IDF Vectorization

The cleaned text is converted into numerical features using **TF-IDF (Term Frequency-Inverse Document Frequency)**.

This allows the machine learning model to understand the importance of words in the text.

### 4. Model Training

The project uses **Logistic Regression** as the classification algorithm.

The dataset is divided into:

* 80% Training Data
* 20% Testing Data

The trained model is evaluated using accuracy.

### 5. Model Saving

After training, the trained model and vectorizer are saved using Pickle:

```text
model.pkl
vectorizer.pkl
```

This allows the Flask application to load the trained model without training it again every time.

## 🔧 Installation

### Step 1: Clone the Repository

```bash
git clone <your-github-repository-url>
cd sentiment-analysis
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

For Linux/macOS:

```bash
source venv/bin/activate
```

### Step 4: Install Dependencies

Create a `requirements.txt` file containing:

```text
Flask
pandas
scikit-learn
```

Then install:

```bash
pip install -r requirements.txt
```

## 🧠 Train the Model

If you want to retrain the model using the dataset:

```bash
python train.py
```

The script will:

1. Load the dataset
2. Clean the text
3. Apply TF-IDF vectorization
4. Split the dataset
5. Train Logistic Regression
6. Calculate accuracy
7. Save the trained model
8. Save the TF-IDF vectorizer

After successful training, these files will be generated:

```text
model.pkl
vectorizer.pkl
```

## ▶️ Run the Flask Application

Start the Flask application:

```bash
python app.py
```

The application will run locally at:

```text
http://127.0.0.1:5000/
```

Open the URL in your browser.

## 🔮 Making a Prediction

Open:

```text
http://127.0.0.1:5000/predict
```

Enter a sentence such as:

```text
I really enjoyed this product
```

The application will return:

```text
Sentiment: Positive
```

For example:

```text
I had a very bad experience
```

The result will be:

```text
Sentiment: Negative
```

## 🔌 API Usage

The `/predict` endpoint also accepts JSON input using a POST request.

Example request:

```json
{
    "text": "I really enjoyed this product"
}
```

Example using Python:

```python
import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "text": "I really enjoyed this product"
}

response = requests.post(url, json=data)

print(response.text)
```

## 📊 Machine Learning Algorithm

### TF-IDF

TF-IDF converts text into numerical values based on the importance of words.

It considers:

* How frequently a word appears in a document
* How frequently the word appears across all documents

### Logistic Regression

Logistic Regression is used as the classification algorithm to predict one of two classes:

```text
0 → Negative
1 → Positive
```

## 📈 Model Evaluation

The model is evaluated using **Accuracy Score**.

The training script prints:

```text
Accuracy: <accuracy>
```

The actual accuracy depends on the dataset and train/test split.

## 💡 Example Predictions

| Input               | Prediction |
| ------------------- | ---------- |
| I love this product | Positive   |
| This is amazing     | Positive   |
| I really enjoyed it | Positive   |
| This is terrible    | Negative   |
| I hate this product | Negative   |
| Very bad experience | Negative   |

## 🔒 Important Files

`model.pkl` contains the trained machine learning model.

`vectorizer.pkl` contains the fitted TF-IDF vectorizer.

Both are required by `app.py` to make predictions.

## 📌 Future Improvements

The project can be improved by adding:

* Neutral sentiment classification
* Larger real-world datasets
* Better text preprocessing
* Stop-word removal
* Stemming/Lemmatization
* Confusion matrix and classification report
* Precision, Recall and F1-score
* Modern NLP models such as BERT
* Better frontend UI
* Docker deployment
* Cloud deployment
* Database integration
* Authentication and user history

## 👨‍💻 Author

**Yogesh**

B.Sc. Information Technology

Interested in:

* Artificial Intelligence
* Machine Learning
* Data Science
* Generative AI
* Python Development

## 📄 License

This project is created for educational and portfolio purposes.
