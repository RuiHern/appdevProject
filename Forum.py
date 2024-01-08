from User import User

class Forum(User):
    Count_ID = 0
    def __init__(self,Name,Comment,Photo):
        super().__init__(Name)
        Forum.count_id += 1
        self.Comment = Comment
        self.Photo = Photo
