from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

class GCashPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing {amount} via GCash.")
        return True

gateway = GCashPaymentProcessor()
success = gateway.process_payment(250.75)
print(f"Payment successful: {success}")