<!DOCTYPE html>
<html>
<head>
    <title>My Cart</title>
</head>
<body>

<h1>Shopping Cart</h1>
<a href="{% url 'checkout' %}">
    <button>Checkout</button>
</a>
{% for item in cart_items %}
    <div>
        <h3>{{ item.product.name }}</h3>
        <p>Price: ₹{{ item.product.price }}</p>
        <p>Quantity: {{ item.quantity }}</p>
    </div>
    <hr>
{% endfor %}

<h2>Total: ₹{{ total }}</h2>

<a href="/">Continue Shopping</a>

</body>
</html>