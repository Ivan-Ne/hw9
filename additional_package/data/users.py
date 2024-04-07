import dataclasses


@dataclasses.dataclass
class User:
    firstName: str
    lastName: str
    userEmail: str
    userNumber: str
    userGender: str
    year: int
    month: int
    date: int
    subject: str
    hobby: int
    fileName: str
    currentAddress: str
    state: str
    city: str
