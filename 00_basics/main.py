from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI()

# Interfaces
class Contact(BaseModel):
    name: str
    email: Optional[str]= None
    phone: str
    address: Optional[str] = None

# Contact API endpoints
contacts: List[Contact] = []

@app.get("/")
def read_root():
    return {"Hello": "World"}


# CREATE CONTACT
@app.post("/contacts")
def create_contact(contact: Contact):
    contacts.append(contact)
    return contact


# READ CONTACTS
@app.get("/contacts")
def read_contacts():
    return contacts


# UPDATE CONTACT
@app.put("/contacts/{contact_id}")
def update_contact(contact_id: int, updated_contact: Contact):
    if contact_id < 0 or contact_id >= len(contacts):
        return {"error": "Contact not found"}
    contacts[contact_id] = updated_contact
    return updated_contact


# DELETE CONTACT
@app.delete("/contacts/{contact_id}")
def delete_contact(contact_id: int):
    if contact_id < 0 or contact_id >= len(contacts):
        return {"error": "Contact not found"}
    deleted_contact = contacts.pop(contact_id)
    return deleted_contact