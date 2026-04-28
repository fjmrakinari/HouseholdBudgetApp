from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///kakeibo.db"
db = SQLAlchemy(app)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    category = db.Column(db.String(50))
    date = db.Column(db.String(20))
    memo = db.Column(db.String(100))

@app.route("/delete/<int:id>")
def delete(id):
    t = Transaction.query.get(id)
    if t:
        db.session.delete(t)
        db.session.commit()
    return redirect("/")


@app.route("/")
def home():
    month = request.args.get("month")  # 例: 2026-04

    if month:
        transactions = Transaction.query.filter(Transaction.date.like(f"{month}%")).all()
    else:
        transactions = Transaction.query.all()

    total = sum(t.amount for t in transactions)

    return render_template("index.html", transactions=transactions, total=total, month=month)


@app.route("/add", methods=["POST"])
def add():
    t = Transaction(
        amount=int(request.form["amount"]),
        category=request.form["category"],
        date=request.form["date"],
        memo=request.form["memo"]
    )
    db.session.add(t)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)