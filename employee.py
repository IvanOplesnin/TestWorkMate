class Employee:
    def __init__(
            self,
            id: str,
            name: str,
            email: str,
            department: str,
            hours_worked: str,
            rate: str
            ):
        self.id: int = int(id)
        self.name = name
        self.email = email
        self.department = department
        self.hours_worked: int = int(hours_worked)
        self.rate: int = int(rate)


    @property
    def payout(self) -> int:
        return self.hours_worked * self.rate

