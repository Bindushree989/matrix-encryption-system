import streamlit as st
import numpy as np

MOD = 128  # ASCII range

st.title("🔐 Matrix Encryption System")
#st.markdown("### Supports letters, spaces, numbers & symbols")

# ------------------ INPUT ------------------

text = st.text_input("Enter Text", "Hello World! 123")

st.write("### Enter 2x2 Key Matrix")
a = st.number_input("a", value=3)
b = st.number_input("b", value=3)
c = st.number_input("c", value=2)
d = st.number_input("d", value=5)

key = np.array([[a, b], [c, d]])

# ------------------ FUNCTIONS ------------------

def text_to_numbers(text):
    return [ord(char) for char in text]

def numbers_to_text(nums):
    return ''.join([chr(int(n) % MOD) for n in nums])

def create_matrix(nums, size):
    if len(nums) % size != 0:
        nums += [0] * (size - len(nums) % size)
    return np.array(nums, dtype=int).reshape(-1, size).T

def mod_inverse(a, m):  #(a × x) % m = 1
    t, new_t = 0, 1
    r, new_r = m, a

    while new_r != 0:
        q = r // new_r
        t, new_t = new_t, t - q * new_t
        r, new_r = new_r, r - q * new_r

    if r > 1:
        return None
    if t < 0:
        t += m

    return t

def encrypt(text, key):
    nums = text_to_numbers(text)
    matrix = create_matrix(nums, key.shape[0])
    return np.dot(key, matrix) % MOD

def decrypt(encrypted, key, length):
    det = int(key[0][0]*key[1][1] - key[0][1]*key[1][0]) % MOD
    det_inv = mod_inverse(det, MOD)

    if det_inv is None:
        return "❌ Invalid Key (Not invertible mod 128)"

    adj = np.array([
        [key[1][1], -key[0][1]],
        [-key[1][0], key[0][0]]
    ])

    key_inv = (det_inv * adj) % MOD
    decrypted = np.dot(key_inv, encrypted) % MOD

    return numbers_to_text(decrypted.T.flatten())[:length]

# ------------------ SESSION ------------------

if "encrypted_data" not in st.session_state:
    st.session_state.encrypted_data = None

# ------------------ BUTTONS ------------------

col1, col2 = st.columns(2)

with col1:
    if st.button("🔒 Encrypt"):
        encrypted = encrypt(text, key)
        st.session_state.encrypted_data = encrypted

        st.write("### 🔢 Encrypted Matrix")
        st.write(encrypted)

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
st.caption("Now supports full ASCII (spaces, symbols, numbers)")