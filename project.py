class Project:
    def __init__(self, id, title, short_desc, long_desc, imgURL, githubURL, technologies, learnings):
        self.id = id
        self.title = title
        self.short_desc = short_desc
        self.long_desc = long_desc
        self.imgURL = imgURL
        self.githubURL = githubURL
        self.technologies = technologies
        self.learnings = learnings