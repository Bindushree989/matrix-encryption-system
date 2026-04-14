# 🔐 Matrix Encryption System

An interactive encryption system based on **Linear Algebra (Matrix Transformations)** that securely encodes and decodes text using a key matrix.

---

## 📌 Overview

This project demonstrates the application of linear algebra in cryptography using a matrix-based encryption technique (similar to the Hill Cipher).  
Text is converted into numerical form, encrypted using matrix multiplication, and decrypted using the modular inverse of the key matrix.

---

## 🚀 Features

- 🔒 Matrix-based encryption using modular arithmetic  
- 🔓 Accurate decryption using modular inverse  
- 🧠 Handles padding for variable-length input  
- 🎨 Interactive user interface built with Streamlit  
- ⚡ Real-time encryption and decryption  

---

## 🛠️ Tech Stack

- Python  
- NumPy  
- Streamlit  

---

## ⚙️ How It Works

1. Convert text into numerical values (A=0 to Z=25)  
2. Arrange numbers into matrix form  
3. Multiply with a key matrix (Encryption)  
4. Apply modulo 26 operation  
5. Use modular inverse of key matrix for decryption  

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python -m streamlit run app.py