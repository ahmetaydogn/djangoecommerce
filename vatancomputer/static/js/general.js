login_button = document.getElementById("form-login-button");

if (user !== "AnonymousUser") {
    login_button.className += "hide"
    console.log(user)
}