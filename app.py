from boilerplate import create_app

if __name__ == "__main__":
    app = create_app("config.json")
    app.run(debug=True)
