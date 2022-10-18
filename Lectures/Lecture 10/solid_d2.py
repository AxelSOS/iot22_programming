class CurrencyConverter:
    def convert(self, from_currency, to_currency, amount):
        raise NotImplementedError

class FXConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount):
        print("Using FXConverter")
        print(f"{amount} {from_currency} = {amount * 1.2} {to_currency}")
        return amount * 1.2

class ForexConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount):
        print("Using ForexConverter")
        print(f"{amount} {from_currency} = {amount * 1.22} {to_currency}")
        return amount * 1.22
    
class Program:
    def __init__(self, converter):
        self.converter = converter
    
    def start(self):
        self.converter.convert('EUR', 'GBP', 10)


if __name__ == '__main__':
    converter = ForexConverter()
    p = Program(converter)
    p.start()
