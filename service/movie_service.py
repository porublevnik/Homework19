from dao.movie_dao import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one_by_id(self, mid: int):
        return self.dao.get_one_by_id(mid)

    def get_all_by_filter(self, data):
        if data.get('genre_id') is not None:
            return self.dao.get_all_by_genre(data.get('genre_id'))
        elif data.get('director_id') is not None:
            return self.dao.get_all_by_director(data.get('director_id'))
        elif data.get('year') is not None:
            return self.dao.get_all_by_year(data.get('year'))
        else:
            return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        mid = data.get("id")
        movie = self.get_one_by_id(mid)

        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')

        return self.dao.update(movie)

    def delete(self, mid):
        movie = self.get_one_by_id(mid)
        return self.dao.delete(movie)

