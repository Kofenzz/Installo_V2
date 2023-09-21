// ADD TO CART FUNCTIONALITY

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');


// Function to handle adding a product to the cart
function addToCart(e) {
    // Prevent the default behavior of the link (preventing navigation)
    e.preventDefault();

    // Get the product.id from a data attribute in the button
    const productId = e.target.getAttribute('data-product-id');

    // Sending the ID to the view in  products/views.py
    let url = 'add-to-cart/'

    let data = {id: productId}

    fetch(url, {
        method: 'POST',
        headers: {"Content-Type": "application/json", 'X-CSRFToken': csrftoken},
        body: JSON.stringify(data)
    })

        .then(res => res.json())
        .then(data => {
            document.getElementById('num_of_items').innerHTML = data
            console.log(data)
        })
        .catch(error => {
            console.log(error)
        })

}

// Select all buttons with the class "addToCart"
const addToCartButtons = document.querySelectorAll(".addToCart");

// Add click event listeners to each button
addToCartButtons.forEach(button => {
    button.addEventListener('click', addToCart);
});


// END ADD TO CART FUNCTIONALITY

// Function to update the quantity when the "Decrease Quantity" button is clicked

function increase_or_decrease(data, item_id) {


    let url = window.location.origin + '/update-cart-quantity/'


    const quantityInput = $("#quantity-" + item_id).val()// Get the input field
    const currentValue = parseInt(quantityInput);

    if (currentValue >= 1) {

        fetch(url, {
            method: 'POST',
            headers: {"Content-Type": "application/json", 'X-CSRFToken': csrftoken},
            body: JSON.stringify(data)
        })

            .then(res => res.json())
            .then(respose => {
                let current_number_of_items = parseInt($("#num_of_items").text())
                if (data['increase'] === true) {
                    $("#quantity-" + item_id).val(currentValue + 1);
                    $("#num_of_items").text(current_number_of_items + 1)
                } else {
                    if (currentValue > 1) {
                        $("#num_of_items").text(current_number_of_items - 1)
                        $("#quantity-" + item_id).val(currentValue - 1);
                    }
                }

                let unit_price = $("#unit_price_" + item_id).text();
                let quantity = $("#quantity-" + item_id).val();
                let amount = parseInt(unit_price) * parseInt(quantity);
                $("#amount_" + item_id).text(amount + " RON");
            })
            .catch(error => {
                console.log(error)
            })
    }
}

function decreaseQuantity(item_id) {
    const productId = $("#quantity-" + item_id).data('product_id');
    const cartId = $("#quantity-" + item_id).data('cart_id');

    let data = {
        cart_id: cartId,
        product_id: productId,
        increase: false,
    };


    increase_or_decrease(data, item_id);
}

// Function to update the quantity when the "Increase Quantity" button is clicked
function increaseQuantity(item_id) {
    const productId = $("#quantity-" + item_id).data('product_id');
    const cartId = $("#quantity-" + item_id).data('cart_id');

    let data = {
        cart_id: cartId,
        product_id: productId,
        increase: true,
    };
    increase_or_decrease(data, item_id);
    //
    // const quantityInput = $(item); // Get the input field
    // const currentValue = parseInt(quantityInput.val());
    // quantityInput.val(currentValue + 1);
    // let current_number_of_items = parseInt($("#num_of_items").text())
    // $("#num_of_items").text(current_number_of_items + 1)
}

// Add event listeners for "Decrease Quantity" and "Increase Quantity" buttons
// const decreaseButtons = document.querySelectorAll(".decrease-quantity"); // Use the correct class
// const increaseButtons = document.querySelectorAll(".increase-quantity"); // Use the correct class

// decreaseButtons.forEach(button => {
//     button.addEventListener('click', decreaseQuantity);
// });

// increaseButtons.forEach(button => {
//     button.addEventListener('click', increaseQuantity);
// });

// Add event listener for Enter keypress on quantity input fields
const quantityInputs = document.querySelectorAll(".quantity-input");

quantityInputs.forEach(input => {
    input.addEventListener('keypress', function (e) {
        if (e.key === "Enter") {
            e.preventDefault(); // Prevent the form from submitting
            // You can add code here to send the updated quantity to your server if needed.
        }
    });
});
