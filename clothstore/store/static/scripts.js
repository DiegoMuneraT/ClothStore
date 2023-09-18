import { MemoryCart } from "./storage.js";
window.addEventListener("DOMContentLoaded", () => {
  const AddShoppingCart = document.querySelector("#btn-addCart");
  AddShoppingCart.addEventListener("click", (e) => {
    const productInfo = document.querySelector(".info-product")
    const idd = window.location.pathname.split("/").pop();
    /* console.log(idd) */
    const item = {
      id: idd,
      name: productInfo.querySelector("h5").textContent.trim(),
      price: productInfo.querySelector(".text-muted > span.product-price").textContent,
      quantity: 1,
    };
    /* console.log(item) */

    const data = new MemoryCart();
    data.getAll()
    const cart = data.getAll()
    if(!Boolean(data.getById(idd))){
      data.setById(idd, item);
      console.log(data)
    }else{
      const oldItem = data.getById(idd)
      oldItem.quantity+=1
      console.log(oldItem)
      data.setById(idd, oldItem)
      };
    })
    
});


