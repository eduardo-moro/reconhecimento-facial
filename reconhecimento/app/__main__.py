if __name__ == "__main__":
    import os
    import sys

    file_dir = os.path.dirname(__file__)
    sys.path.append(file_dir)

    from routes import app
    app.run(debug=True, host='0.0.0.0')