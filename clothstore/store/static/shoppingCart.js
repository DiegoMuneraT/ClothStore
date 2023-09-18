import { MemoryCart } from "./storage.js";

window.addEventListener("DOMContentLoaded", () => {

    const data = new MemoryCart();
    const shoppingCart = document.querySelector(".product-list")
    shoppingCart.addEventListener("change", (ev)=>{
        const total_id_ref = ev.target.dataset.id
        const price_id_ref = ev.target.dataset.priceId

        const price = parseInt(document.querySelector(`#${price_id_ref}`).textContent)
        const quantity = ev.target.value
        document.querySelector(`#${total_id_ref}`).textContent = price * quantity
        data.updateQuantity(ev.target.dataset.idProduct, quantity)
    });

    shoppingCart.addEventListener("click", (eve)=>{
        const delete_id_ref = eve.target.dataset.ulId
        const deleted_item = document.querySelector(`#${delete_id_ref}`)
        shoppingCart.removeChild(deleted_item)
        data.deleteById(eve.target.dataset.idProduct)
        console.log(eve.target.dataset)

    });

    const items = data.getAll();
    const values = Object.values(items)
    const shoppingList = values.map((item)=> {
        return /*html*/`    <ul id="product-id-${item.id}"class="card shoppingItem-${item.id}">
        <li>
            name: ${item.name}
        </li>
        <li>
            price: <span id="priceId-${item.id}">${item.price}</span>
        </li>
        <li>
            <label for="quantity"> quantity:  </label>
            <input type="number" name="quantity" data-id-product="${item.id}" data-id="totalId-${item.id}" data-price-id="priceId-${item.id}" value="${item.quantity}"
            min="1"
             />
             <button type="button" id="deleteId-${item.id}" data-ul-id="product-id-${item.id}" data-id-product="${item.id}" class="btn btn-primary btn-sm"  href="#" role="button">Eliminar</button>  
        </li>
        <li>
            total_price: <span id="totalId-${item.id}">${parseFloat(item.price) * parseInt(item.quantity)}</span>
        </li>
        </ul> `
    });
    

    /* const selectItem = document.querySelector(".shoppingItem")
    const itemQuantity = document.querySelector(".quantity")
    selectItem.addEventListener("change", (ev)=>{
        itemQuantity = `${ev.target.value}`;
    }); */

    const itemsRender = shoppingList.join(" ");
    shoppingCart.insertAdjacentHTML("afterbegin", itemsRender)

});