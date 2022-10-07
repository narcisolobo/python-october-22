class Show:
    def __init__(self, id, title, genre, description, rating, release_date):
        self.id = id
        self.title = title
        self.genre = genre
        self.description = description
        self.rating = rating
        self.release_date = release_date
    
    def __repr__(self):
        return f'<Anime: {self.title}>'