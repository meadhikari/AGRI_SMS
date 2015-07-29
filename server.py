import web
        
urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:        
    def GET(self,name):
	user_data = web.input()
        return user_data.keyword+":::"+user_data.text

if __name__ == "__main__":
    app.run()

