
window.addEventListener("DOMContentLoaded", () => {
  const AddShoppingCart = document.querySelector("#btn-addCart");
  AddShoppingCart.addEventListener("click", (e) => {
    const productInfo = document.querySelector(".info-product")
    const idd = window.location.pathname.split("/").pop();
    console.log(idd)
    const item = {
      id: idd,
      name: productInfo.querySelector("h5").textContent.trim(),
      price: productInfo.querySelector(".text-muted > span.product-price").textContent,
      quantity: 1,
    };
    console.log(item)

    const cart = JSON.parse(localStorage.getItem("cart")) || [];
    const isInCart = (id, cart) => Boolean(cart.find((item) => item.id === id));
    if(!isInCart(idd, cart)){
      cart.push(item);
    }else{
      cart.forEach((item) => {
        if (item.id === idd) {
          item.quantity = parseInt(item.quantity) + 1
        }
      });
    }
    localStorage.setItem("cart", JSON.stringify(cart));
  });
});

