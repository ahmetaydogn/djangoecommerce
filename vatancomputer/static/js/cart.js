var updateButtons = document.getElementsByClassName("update-cart")
console.log(updateButtons.item)
for (var i=0; i < updateButtons.length; i++){
    updateButtons[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId: ', productId, 'action: ', action)
        
        if (user === "AnonymousUser"){
            console.log("User isn't logged in")
        }
        else {
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action){
    var url = '/update_item/'

    fetch(url, {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'productId':productId, 'action':action })
    })

    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.log('data: ', data)
        location.reload()
    })
}

login_button = document.getElementById("form-login-button");

if (user !== "AnonymousUser") {
    login_button.className += "hide"
    console.log(user)
}