import streamlit as st
import numpy as np

st.title("🔐 Matrix Encryption System")
st.markdown("### Secure Text Encryption using Matrix Transformations")

# ------------------ INPUT ------------------

text = st.text_input("Enter Text", "HELLO")

st.write("### Enter 2x2 Key Matrix")
a = st.number_input("a", value=3)
b = st.number_input("b", value=3)
c = st.number_input("c", value=2)
d = st.number_input("d", value=5)

key = np.array([[a, b], [c, d]])

# ------------------ FUNCTIONS ------------------

def text_to_numbers(text):
    text = text.upper().replace(" ", "")
    return [ord(char) - 65 for char in text]

def numbers_to_text(nums):
    return ''.join([chr(int(round(n)) + 65) for n in nums])

def create_matrix(nums, size):
    if len(nums) % size != 0:
        nums += [0] * (size - len(nums) % size)
    return np.array(nums).reshape(-1, size).T

def encrypt(text, key):
    nums = text_to_numbers(text)
    matrix = create_matrix(nums, key.shape[0])
    return np.dot(key, matrix) % 26

def decrypt(encrypted, key, length):
    # determinant
    det = int(key[0][0]*key[1][1] - key[0][1]*key[1][0]) % 26

    # find modular inverse of determinant
    det_inv = None
    for i in range(26):
        if (det * i) % 26 == 1:
            det_inv = i
            break

    if det_inv is None:
        return "❌ Invalid Key (Not invertible mod 26)"

    # adjugate matrix
    adj = np.array([
        [key[1][1], -key[0][1]],
        [-key[1][0], key[0][0]]
    ])

    key_inv = (det_inv * adj) % 26

    decrypted = np.dot(key_inv, encrypted) % 26

    return numbers_to_text(decrypted.T.flatten())[:length]

# ------------------ SESSION STORAGE ------------------

if "encrypted_data" not in st.session_state:
    st.session_state.encrypted_data = None

# ------------------ BUTTONS ------------------

col1, col2 = st.columns(2)

# Encrypt Button
with col1:
    if st.button("🔒 Encrypt"):
        encrypted = encrypt(text, key)
        st.session_state.encrypted_data = encrypted

        st.write("### 🔢 Encrypted Matrix")
        st.write(encrypted)

# Decrypt Button
with col2:
    if st.button("🔓 Decrypt"):
        if st.session_state.encrypted_data is not None:
            decrypted = decrypt(st.session_state.encrypted_data, key, len(text))

            st.write("### 🔓 Decrypted Text")
            st.success(decrypted)
        else:
            st.warning("⚠️ Please encrypt first!")

# ------------------ FOOTER ------------------

st.markdown("---")
st.caption("Built using Linear Algebra (Matrix Transformations)")