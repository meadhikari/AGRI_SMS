import web
from spell_checker import correct
urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:        
    def GET(self,name):
        user_data = web.input()
        return correct(user_data.text.replace('sapiAGRI ',''))

if __name__ == "__main__":
    app.run()

