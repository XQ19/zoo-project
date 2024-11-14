class Zoo:
    def get_ticket_price(self, age):
        if age < 0  : 
             return "Don't waste money on ticket"
        elif age >= 0  and age <= 12:
            return 50
        elif age >= 13 and age <= 20:
            return 100
        elif age >= 21 and age <= 60:
            return 150
        elif age > 60:
            return 100