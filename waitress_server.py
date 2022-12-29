# from waitress import serve
from waitress import serve


from web_report.wsgi import application

if __name__ == '__main__':
    serve(application, port='8000')