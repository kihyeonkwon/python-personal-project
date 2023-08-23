class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

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

member1 = Member("최지연", "choijiyeon", "지연123")
member2 = Member("권수민", "kwonsumin", "sumin90")
member3 = Member("윤상희", "yoonsanghee", "sangsang")


members.append(member1)
members.append(member2)
members.append(member3)


posts = []


post1 = Post("안녕하세요", "제이름은~~ 잘부탁드려요", member1.name)
post2 = Post("여기 있다보니", "코딩이 좀 재밌는거 같기도?", member1.name)
post3 = Post("점점 실력이", "느는것 같습니다.", member1.name)
posts.append(post1)
posts.append(post2)
posts.append(post3)

post4 = Post("으아아아", "이거 좀 귀찮은데", member2.name)
post5 = Post("여러분", "귀찮아도 열심히 삽시다", member2.name)
post6 = Post("돌아가는게 ", "가장 빠릅니다", member2.name)
posts.append(post4)
posts.append(post5)
posts.append(post6)

post7 = Post("반성하고 있습니다", "앞으로 열심히 하겠습니다", member3.name)
post8 = Post("하아 근데 과제가 좀", "귀찮은거같기도한데", member3.name)
post9 = Post("근데 그래야", "연습이 많이 됩니다.", member3.name)
posts.append(post7)
posts.append(post8)
posts.append(post9)

# 6-1
for post in posts:
    if post.author == "권수민":
        print(post.title)

# 6-2
certain_word = input()
for post in posts:
    if certain_word in post.content:
        print(post.title)


# **추가 도전 과제:**

# 1. input을 이용하여 Member 인스턴스 만드는것을 사용자가 터미널에서 할 수 있게 해주세요.
# 2. post도 터미널에서 생성할 수 있게 해주세요.
# 3. (심화)비밀번호 해싱이 무엇인지 공부한 후 hashlib 라이브러리를 써서 회원 비밀번호를 해시화하여 저장하게 해주세요.
