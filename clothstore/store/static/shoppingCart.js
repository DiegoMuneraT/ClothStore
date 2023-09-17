window.addEventListener("DOMContentLoaded", () => {
    const shoppingCart = document.querySelector("#ct-content")
    const cart = document.querySelector("#cart-template")

    const items = JSON.parse(localStorage.getItem("cart"));
    const shoppingList = items.map((item)=> {
        return `    <ul>
        <li>
            name: ${item.name}
        </li>
        <li>
            price: ${item.price}
        </li>
        <li>
            quantity: ${item.quantity}
        </li>
        <li>
            total_price: ${parseFloat(item.price) * parseInt(item.quantity)}
        </li>
        </ul> `
    });
    const itemsRender = shoppingList.join(" ");

    shoppingCart.insertAdjacentHTML("beforeend", itemsRender)

});