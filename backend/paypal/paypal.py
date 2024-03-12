#!/usr/bin/python3

"""
paypal module
"""

import paypalrestsdk

# Configure PayPal SDK with Client ID and Secret
paypalrestsdk.configure({
    "mode": "sandbox", # or "live"
    "client_id": "YOUR_CLIENT_ID",
    "client_secret": "YOUR_CLIENT_SECRET"
})

def create_payment(amount, currency):
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": "http://return.url",
            "cancel_url": "http://cancel.url"
        },
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": "Movie Subscription",
                    "sku": "001",
                    "price": str(amount),
                    "currency": currency,
                    "quantity": 1
                }]
            },
            "amount": {
                "currency": currency,
                "total": str(amount)
            },
            "description": "Movie Subscription"
        }]
    })
    return payment