# Invoice Extractor

An AI-powered **Invoice Extractor and Analyzer** built with **Streamlit, Google Gemini, and LangChain**.

Upload an invoice image and ask questions about its contents. Gemini's multimodal capabilities analyze the invoice image and generate answers based on the information visible in the document.

## Features

* Upload invoice images (`JPG`, `JPEG`, `PNG`)
* AI-powered invoice understanding
* Ask natural-language questions about invoices
* Extract and interpret invoice information from images
* Multimodal image + text processing
* Simple Streamlit interface

## Tech Stack

| Technology    | Purpose                   |
| ------------- | ------------------------- |
| Python        | Application logic         |
| Streamlit     | Web interface             |
| Google Gemini | Multimodal AI analysis    |
| LangChain     | LLM integration           |
| Pillow        | Invoice image processing  |
| python-dotenv | Environment configuration |

## How It Works

```text
Invoice Image
     ↓
Streamlit Upload
     ↓
Image → Base64
     ↓
LangChain HumanMessage
     ↓
Google Gemini
     ↓
Invoice Analysis
     ↓
Answer to User Question
```

The invoice image and user's question are sent together to Gemini as a multimodal request.

## Project Structure

```text
Invoice_Extractor/
│
├── app.py
├── requirements.txt
├── .env
└── .gitignore
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/sankha4567/Invoice_Extractor.git
cd Invoice_Extractor
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

**Windows PowerShell:**

```bash
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Gemini API

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key
```

### 5. Run the application

```bash
streamlit run app.py
```

Open the Streamlit URL shown in the terminal.

## Usage

1. Start the application.
2. Upload an invoice image.
3. Enter a question about the invoice.
4. Click **Tell me about the invoice**.
5. Gemini analyzes the invoice and returns the answer.

### Example Questions

```text
What is the invoice number?

What is the total amount?

What is the invoice date?

Who is the seller?

Who is the customer?

List the products mentioned in the invoice.

What taxes are included?

What is the payment due date?
```

## Multimodal AI Pipeline

The application converts the uploaded invoice image into Base64 and sends it to Gemini together with the user's question through a LangChain `HumanMessage`.

```text
User
 ↓
Invoice Image + Question
 ↓
Base64 Encoding
 ↓
LangChain HumanMessage
 ↓
Gemini 3.5 Flash
 ↓
Natural Language Response
```

## Requirements

* Python 3.10+
* Google Gemini API key
* Internet connection
* Invoice image in JPG, JPEG, or PNG format

## Limitations

* Results depend on the quality and readability of the invoice image.
* The application currently works with invoice images rather than dedicated PDF/document parsing.
* Extracted values are AI-generated and should be verified before being used for financial or accounting purposes.
* There is currently no database, authentication, invoice history, or export functionality.

## Future Improvements

* Structured invoice extraction using Pydantic
* JSON/CSV export
* PDF invoice support
* Invoice history and database storage
* Automatic field extraction
* Invoice validation
* Tax and total verification
* Multi-invoice batch processing
* Authentication and user management

## License

No license has been specified for this repository.
