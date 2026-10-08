import weakref

class Customer:
    def __init__(self, name):
        self.name = name
        self.bank_account = None
        print(f"Customer {self.name} created.")

    def __del__(self):
        print(f"Customer {self.name} successfully deleted from memory!")

class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        # Use weakref here so it doesn't form a permanent loop!
        self._customer = None
        print(f"Bank Account {self.account_number} created.")

    @property
    def customer(self):
        # Unwrap the weak reference when we want to use the customer
        return self._customer() if self._customer else None

    @customer.setter
    def customer(self, cust):
        # Store a weak reference to the customer
        self._customer = weakref.ref(cust)

    def __del__(self):
        print(f"Bank Account {self.account_number} successfully deleted from memory!")

# --- Testing it out ---
print("--- Creating objects ---")
cust = Customer("Amina")
account = BankAccount("EQ-001")

# Tie them together
cust.bank_account = account
account.customer = cust  # This is a weak link!

print("\n--- Deleting variables ---")
del cust
del account
print("--- End of script ---")