import hashlib


class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        m = hashlib.sha256()
        m.update(password.encode("utf-8"))
        self.password = m.hexdigest()

    def display(self):
        print(f"회원의 이름은 {self.name}이고 아이디는 {self.username}입니다.")

    def __repr__(self):
        return f"{self.name}님의 아이디는 {self.username}"

    def __str__(self):
        return f"{self.name}님의 아이디는 {self.username}"


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __repr__(self):
        return f"{self.author}님이 작성하신 {self.title}"


members = []
posts = []

member1 = Member("최종민", "choijongmin", "jongmin123")
members.append(member1)

print(member1.name)
print(member1.password)
