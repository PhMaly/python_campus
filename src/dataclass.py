from dataclasses import dataclass


@dataclass
class Address:
    address: str
    zip_code: str
    town: str

    def __str__(self):
        return f'Address:\nAddress : {self.address} \nZIP code : {self.zip_code} \nTown : {self.town}'


@dataclass
class Contact:
    phone_tel: int
    email: str

    def __str__(self):
        return f'Contact:\nPhone number : {self.phone_tel} \nE-mail : {self.email}'


@dataclass
class Character:
    last_name: str
    first_name: str
    birthday: str
    contact: Contact
    addresses: Address

    def __str__(self):
        return f'Character:\nName : {self.last_name} \nFirst Name : {self.first_name} \nBirthday : {self.birthday} \n{self.contact} \n{self.addresses}'


@dataclass
class Directory:
    characters: list[Character]

    def __str__(self):
        return '\n'.join(str(character) for character in self.characters)


if __name__ == '__main__':

    patrickAddress = Address(address="1 rue du rhone", zip_code="07300", town="tournon")
    patrickContact = Contact(1234, "patrick@mail")
    patrick = Character(last_name="Smith", first_name="Patrick", birthday="20/01/1994", contact=patrickContact, addresses=patrickAddress)
    repertory = Directory([patrick])
    print(repertory)

