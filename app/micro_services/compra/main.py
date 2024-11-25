from app.micro_services.compra import create_app, db

app = create_app()
app.app_context().push()

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002)
