# her odeme sisteminn calistiran class clas paymenfaced

class PayPalGateway:
  def process_payment(self, amount):
   return f"Payment of ${amount} processed via PayPal"

class StripeGateway:
 def pay(self, amount):
  return f"Payment of ${amount} processed via Stripe"




class CryptoGateway:
 def make_payment(self, amount):
  return f"Payment of ${amount} processed via Crypto (Bitc)"

class KopanGateway:
    def make_payment_kopen(self, amount):
        return f"Payment of ${amount} processed via given token number"



 # Step 2: Implement Facade Class
class PaymentFacade:
     def __init__(self):
         self._paypal = PayPalGateway()

         self._stripe = StripeGateway()
         self._crypto = CryptoGateway()
         self._kopen = KopanGateway()

     def process_payment(self, amount, gateway):

         """Processes payment through the selected gateway."""
         if gateway == 'paypal':
           return self._paypal.process_payment(amount)
         elif gateway == 'stripe':
           return self._stripe.pay(amount)
         elif gateway == 'crypto':
           return self._crypto.make_payment(amount)
         elif gateway == 'kopen':
           return self._kopen.make_payment_kopen(amount)
         else:
             return "Invalid gateway selection"

 # Step 3: Utilize Facade in Client Code
def main():
     # Creating PaymentFacade instance
     payment_facade = PaymentFacade()
     # Process payments through different gateways
     print(payment_facade.process_payment(100, 'paypal'))
     print(payment_facade.process_payment(150, 'stripe'))
     print(payment_facade.process_payment(200, 'crypto'))

     print(payment_facade.process_payment(777, 'kopen'))

     print(payment_facade.process_payment(300, 'invalid_gateway'))

if __name__ == "__main__":
     main()


# objeler arasinda
# abstract classinda method kendisinden uretilen butun subclasta kulanilmali



