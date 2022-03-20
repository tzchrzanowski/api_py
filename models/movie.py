movies_list = []

def get_id():
    if movies_list:
        last_item = movies_list[-1]
        return last_item.id + 1
    else:
        return 1


class Movie:
    def __init__(self, title, year, description):
        self.id = get_id()
        self.title = title
        self.year = year
        self.description = description

    @property
    def data(self):
        return {
            'id': self.id,
            'title': self.title,
            'year': self.year,
            'description': self.description
        }
