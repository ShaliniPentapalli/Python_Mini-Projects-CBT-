from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_receipt(transaction_id, date, customer_name, items, total_amount):
    file_name = f"receipt_{transaction_id}.pdf"
    c = canvas.Canvas(file_name, pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 20)
    c.drawString(200, height - 50, "Payment Receipt")

    # Transaction Details
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 100, f"Transaction ID: {transaction_id}")
    c.drawString(50, height - 120, f"Date: {date}")
    c.drawString(50, height - 140, f"Customer Name: {customer_name}")

    # Table Header
    c.drawString(50, height - 180, "Item")
    c.drawString(250, height - 180, "Quantity")
    c.drawString(350, height - 180, "Price")
    c.drawString(450, height - 180, "Total")

    # Table Content
    y = height - 200
    for item, details in items.items():
        c.drawString(50, y, item)
        c.drawString(250, y, str(details['quantity']))
        c.drawString(350, y, f"${details['price']:.2f}")
        c.drawString(450, y, f"${details['quantity'] * details['price']:.2f}")
        y -= 20

    # Total Amount
    c.drawString(350, y - 20, "Total Amount:")
    c.drawString(450, y - 20, f"${total_amount:.2f}")

    # Footer
    c.drawString(200, y - 60, "Thank you for your purchase!")

    c.save()
    print(f"Receipt saved as {file_name}")

if __name__ == "__main__":
    transaction_id = "123456"
    date = "2024-07-04"
    customer_name = "John Doe"
    items = {
        "Item A": {"quantity": 2, "price": 10.00},
        "Item B": {"quantity": 1, "price": 15.50},
        "Item C": {"quantity": 3, "price": 7.75},
    }
    total_amount = sum(details['quantity'] * details['price'] for details in items.values())

    create_receipt(transaction_id, date, customer_name, items, total_amount)
