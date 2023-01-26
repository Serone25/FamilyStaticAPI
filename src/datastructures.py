
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Sequence, DateTime, update, desc, func,

db = SQLAlchemy()

class FamilyStructure(db.Model):
    id = db.column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(40), nullable = False)
    last_name = db.Column(db.String(40), nullable = False)
    age = db.Column(db.Integer, CheckConstraint("age > 0"))
    lucky_numbers = db.Column(db.Array(Integer))
    
    def __init__(self,first_name, last_name,age,lucky_numbers):
        self.last_name = last_name

        # example list of members
        self._members = [{
            "id":self._generateId(),
            "first_name":first_name,
            "last_name":last_name,
            "age":age,
            "lucky_numbers":lucky_numbers
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member,data):
        add_member_member = FamilyStructure(id = self._generateId(),
                                            first_name = data['first_name'],
                                            last_name = data['last_name'],
                                            age = data['age'],
                                            lucky_numbers = data['lucky_numbers'],)
        return

    def delete_member(self, id):
        self.query.filter_by(id=id).delete()
        return "Miembro borrado con éxito"

    def get_member(self, id):
        # fill this method and update the return
        return self.query.filter_by(id=id).first()

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
