from Pages.Login import LoginPage
from Pages.InventoryPage import InventoryPage
from Pages.AddtoCart import CartPage
from Pages.CheckoutPage import CheckoutPage


def test_complete_cart_flow(page):

    login = LoginPage(page)
    inventory = InventoryPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    # Login
    login.goto_saucedemo_web()
    login.login("standard_user", "secret_sauce")

    # Select items
    selected_items = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light"
    ]

    # Add items
    for item in selected_items:
        inventory.add_item_to_cart(item)

    # Verify cart badge
    assert inventory.get_cart_count() == str(len(selected_items))

    # Open cart
    inventory.open_cart()

    # Verify items order
    cart_items = cart.get_cart_items()
    assert cart_items == selected_items

    # Verify price calculations
    prices = cart.get_cart_prices()
    quantities = [int(q) for q in cart.get_cart_quantities()]

    for i in range(len(prices)):
        assert prices[i] * quantities[i] == prices[i]

    # Remove item
    cart.remove_first_item()
    assert len(cart.get_cart_items()) == 1

    # Checkout
    cart.proceed_to_checkout()
    checkout.fill_shipping_details()

    # Verify order summary
    summary_items = checkout.get_summary_items()
    assert summary_items == cart.get_cart_items()

    # Verify subtotal
    item_total = checkout.get_item_total()
    calculated_total = sum(cart.get_cart_prices())
    assert item_total == calculated_total

    # Verify tax
    tax = checkout.get_tax()
    assert tax > 0

    # Verify final total
    total = checkout.get_total()
    assert total == round(item_total + tax, 2)

    # Complete order
    checkout.complete_order()

    # Verify confirmation
    assert checkout.get_confirmation_message() == "Thank you for your order!"

    # Verify order text exists
    assert "Your order has been dispatched" in checkout.get_order_text()
