from flask import Flask, render_template
from faker import Faker

faker = Faker()

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = []
    for _ in range(50):
        title = f"{faker.color_name()} {faker.word()} {faker.numerify()}"
        movies.append(title)
    print(movies)
    return render_template("homepage.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)
