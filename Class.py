# Comment isminde bir sınıf oluşturunuz.
# Comment sınıfı username, text, likes, dislikes isminde özelliklere sahip olsun.
# 5 adet farklı comment oluşturup döngü yardımıyla yorumları ekrana yazdırınız.

class Comment:
    def __init__(self, username, text, likes=0, dislikes=0):
        self.username = username
        self.text = text
        self.likes = likes
        self.dislikes = dislikes


c1 = Comment("harunaydeniz", "Güzel araba")
c2 = Comment("ahmetyilmaz", "çok güzel araba")
c3 = Comment("mahmutdöner", "idare eder bir araba", 50, 10)
c4 = Comment("michealpetis", "I don't like this car", 0, 10)
c5 = Comment("elifbiter", "süper bir araba olmuş", 1000)

comments = [c1, c2, c3, c4, c5]

for c in comments:
    print(f"{c.username}: {c.text}")
    print(f"likes: {c.likes} - dislikes: {c.dislikes}")
