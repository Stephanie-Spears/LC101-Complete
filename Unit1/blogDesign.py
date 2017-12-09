"""Blog Design Module"""

class Post:
    """user posts on blog"""
    def __init__(self, title, author, body):
        self.title = title
        self.author = author
        self.body = body
        self.likes = 0

    def like(self):
        """Allow people to "like" posts"""
        self.likes += 1

    def __str__(self):
        return self.title + " by " + self.author


class VideoPost(Post):
    """video type media post"""
    def __init__(self, title, author, url):
        #super().__init__([args]) #Better method, in cases where each class has multiple parent classes, each of the superclasses is invoked in order
        Post.__init__(self, title, author, None)
        self.video_url = url
        self.plays = 0

    def play(self):
        """"track plays of video"""
        self.plays += 1

    def __str__(self):
        return self.title + " played " + str(self.plays) + " times"

class ImagePost(Post):
    """image type media post"""
    def __init__(self, title, author, file_name):
        Post.__init__(self, title, author, None)
        self.file_name = file_name

class LinkPost(Post):
    """link type media post"""
    def __init__(self, title, author, url):
    #super().__init__([args]): # vs Post.__init__(self, [args])
        Post.__init__(self, title, author, None)
        self.link_clicks = 0
        self.link_url = url

    def click(self):
        """click method"""
        self.link_clicks += 1

    def __str__(self):
        return self.title + " clicked " + str(self.link_clicks) + " times"


plain_post = Post("10 Best Albums of 2016", "Chris Bay", "1. Little Scream - Cult Following 2. ...")
vid_post = VideoPost("Little Scream - Love As a Weapon", "Chris Bay", "https://youtu.be/Tq4Vw4MB6eA")
pic_post = ImagePost("Cats in space", "Crystal Martin", "spacecats.gif")
url_post = LinkPost("LaunchCode's LC101", "LaunchCode Staff", "https://www.launchcode.org/lc101")

vid_post.play()
vid_post.play()
url_post.click()

print(vid_post)
print(plain_post)
print(pic_post)
print(url_post)
