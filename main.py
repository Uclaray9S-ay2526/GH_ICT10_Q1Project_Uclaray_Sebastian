from pyscript import display, document

def create_order (e):
    document.getElementById('show').innerHTML = ""

    item1 = document.getElementById("item1")
    item2 = document.getElementById("item2")
    item3 = document.getElementById("item3")
    item4 = document.getElementById("item4")
    item5 = document.getElementById("item5")

    subtotal = float(item1.value) * item1.checked + float(item2.value) * item2.checked + float(item3.value) * item3.checked + float(item4.value) * item4.checked + float(item5.value) * item5.checked

    vat = subtotal * 0.12
    total_amount = subtotal + vat

    display(f'The VAT is {vat}', target="result")
    display(f'The total amount is {total_amount}', target="result")
    display(f'Total amount: {total_amount}', target="show")

def generate_sku (e):
    document.getElementById("sku").innerHTML = ""
    category = document.getElementById("category").value
    product = document.getElementById("product").value
    stock = document.getElementById("quantity").value
    category = category.upper()
    product = product.upper()
    char = product[:3]

    SKU = category + "-" + char + "-" + stock
    display(f'Generated SKU: {SKU}', target="sku")