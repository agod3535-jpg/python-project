import streamlit as st
import os

# ---------- FILE SETUP ----------
if not os.path.exists("data"):
    os.makedirs("data")

USER_FILE = "data/users.txt"

# ---------- SESSION ----------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "books" not in st.session_state:
    st.session_state.books = []

# ---------- USER FUNCTIONS ----------
def save_user(username, password):
    with open(USER_FILE, "a") as f:
        f.write(f"{username},{password}\n")

def check_user(username, password):
    if not os.path.exists(USER_FILE):
        return False

    with open(USER_FILE, "r") as f:
        users = f.readlines()
        for user in users:
            u, p = user.strip().split(",")
            if u == username and p == password:
                return True
    return False

# ---------- SIGN UP ----------
def signup():
    st.title("📝 Sign Up")

    new_user = st.text_input("Username")
    new_pass = st.text_input("Password", type="password")

    if st.button("Create Account"):
        if new_user and new_pass:
            save_user(new_user, new_pass)
            st.success("Account created! Go to Login")
        else:
            st.warning("Fill all fields")

# ---------- LOGIN ----------
def login():
    st.title("🔐 Login")

    user = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if check_user(user, password):
            st.session_state.logged_in = True
            st.session_state.username = user
            st.success("Login Successful")

            st.rerun()
            
        else:
            st.error("Invalid credentials")

# ---------- LOGOUT ----------
def logout():
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""

# ---------- MAIN APP ----------
def app():
    st.title("📚 Digital Library System")

    st.write(f"Welcome, {st.session_state.username} 👋")
    logout()

    # ---------- ADD BOOK ----------
    st.header("➕ Add Book")

    book_id = st.text_input("Book ID")
    title = st.text_input("Book Title")
    author = st.text_input("Author Name")

    if st.button("Add Book"):
        if book_id and title and author:
            st.session_state.books.append({
                "id": book_id,
                "title": title,
                "author": author
            })
            st.success("Book added!")
        else:
            st.warning("Fill all fields")

    # ---------- UPLOAD NOTES / PDF ----------
    st.header("📂 Upload Notes / PDF")

    uploaded_file = st.file_uploader("Upload File", type=["pdf", "txt"])

    if uploaded_file:
        file_path = os.path.join("data", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("File uploaded successfully!")

    # ---------- SHOW BOOKS ----------
    st.header("📖 Available Books")

    if st.session_state.books:
        for book in st.session_state.books:
            st.write(f"📘 {book['title']} by {book['author']} (ID: {book['id']})")
    else:
        st.info("No books available")

    # ---------- SHOW FILES ----------
    st.header("📄 Available Notes / PDFs")

    files = os.listdir("data")

    if files:
        for file in files:
            if file != "users.txt":
                st.write(f"📄 {file}")
    else:
        st.info("No files uploaded")

# ---------- MAIN ----------
menu = st.sidebar.selectbox("Menu", ["Login", "Sign Up"])

if st.session_state.logged_in:
    app()
else:
    if menu == "Login":
        login()
    else:
        signup()