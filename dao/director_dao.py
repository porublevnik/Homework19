from .model.director import Director

class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Director).all()

    def get_one_by_id(self, did: int):
        return self.session.query(Director).get(did)

    def create(self, director_d):
        ent = Director(**director_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, did):
        director = self.get_one_by_id(did)
        self.session.delete(director)
        self.session.commit()

    def update(self, director_d):
        director = self.get_one_by_id(director_d.get("id"))
        director.name = director_d.get("name")

        self.session.add(director)
        self.session.commit()