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
posts = []


# 3. (심화)비밀번호 해싱이 무엇인지 공부한 후 hashlib 라이브러리를 써서 회원 비밀번호를 해시화하여 저장하게 해주세요.


def create_user():
    my_name = input("이름을 입력해주세요")
    my_username = input("아이디를 입력해주세요")
    my_password = input("비밀번호를 입력해주세요")

    members.append(Member(my_name, my_username, my_password))


def create_post():
    my_title = input("게시글 제목을 입력해주세요")
    my_content = input("게시글 내용을 입력해주세요")
    my_name = input("사용자 이름을 입력해주세요")

    posts.append(Post(my_title, my_content, my_name))


while True:
    print("서비스에 오신 것을 환영합니다.")
    option = input("회원가입 하시려면 1, 글을 작성하시려면 2 를 눌러주세요, 모든글을 보기 3, 모든유저보기 4")

    if option == "1":
        create_user()

    elif option == "2":
        create_post()
    elif option == "3":
        print(posts)
    elif option == "4":
        print(members)
