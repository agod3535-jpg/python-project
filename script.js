let users = JSON.parse(localStorage.getItem("users")) || {};
let books = JSON.parse(localStorage.getItem("books")) || [];

// LOGIN
function login() {
    let user = document.getElementById("username").value;
    let pass = document.getElementById("password").value;

    if (users[user] === pass) {
        document.getElementById("loginPage").classList.add("hidden");
        document.getElementById("dashboard").classList.remove("hidden");
        displayBooks();
    } else {
        alert("Invalid login");
    }
}

// SIGNUP
function signup() {
    let user = document.getElementById("newUser").value;
    let pass = document.getElementById("newPass").value;

    users[user] = pass;
    localStorage.setItem("users", JSON.stringify(users));

    alert("Signup successful");
    showLogin();
}

// SWITCH PAGES
function showSignup() {
    document.getElementById("loginPage").classList.add("hidden");
    document.getElementById("signupPage").classList.remove("hidden");
}

function showLogin() {
    document.getElementById("signupPage").classList.add("hidden");
    document.getElementById("loginPage").classList.remove("hidden");
}

// LOGOUT
function logout() {
    location.reload();
}

// ADD BOOK
function addBook() {
    let id = document.getElementById("bookId").value;
    let title = document.getElementById("title").value;
    let author = document.getElementById("author").value;

    books.push({ id, title, author });
    localStorage.setItem("books", JSON.stringify(books));

    displayBooks();
}

// DISPLAY BOOKS
function displayBooks() {
    let list = document.getElementById("bookList");
    list.innerHTML = "";

    books.forEach((book, index) => {
        let li = document.createElement("li");

        li.innerHTML = `
        ${index + 1}. ${book.id} - ${book.title} by ${book.author}
        <button class="delete-btn" onclick="deleteBook(${index})">Delete</button>
        `;

        list.appendChild(li);
    });
}

// DELETE BOOK
function deleteBook(index) {
    books.splice(index, 1);
    localStorage.setItem("books", JSON.stringify(books));
    displayBooks();
}