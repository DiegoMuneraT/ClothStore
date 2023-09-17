window.addEventListener("DOMContentLoaded", () => {
    const shoppingCart = document.querySelector(".product-list")

    const items = JSON.parse(localStorage.getItem("cart"));
    const shoppingList = items.map((item)=> {
        return `    <ul class="card">
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

    shoppingCart.insertAdjacentHTML("afterend", itemsRender)

});