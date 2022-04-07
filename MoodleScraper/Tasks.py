class Task:
    def __init__(self, name, cid):
        self.tid = name
        self.cid = cid


class Assignment(Task):
    def __init__(self, name, due_date, url, cid):
        super().__init__(name, cid)
        self.due_date = due_date
        self.url = url
