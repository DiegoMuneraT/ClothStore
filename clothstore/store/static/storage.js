class MemoryCart {

    constructor(){
        this.items = JSON.parse(localStorage.getItem("cart")) || {};
    }
    getAll(){
        return this.items
    }
    getById(id){
        return this.items[id]
    }
    setById(id, item){
        this.items[id] = item
        localStorage.setItem("cart", JSON.stringify(this.items))        
    }
    setAll(items){
        this.items = items
        localStorage.setItem("cart", JSON.stringify(this.items))
    }
    deleteById(id){
        delete this.items[id]
        localStorage.setItem("cart", JSON.stringify(this.items)) 
    }

}

export { MemoryCart }