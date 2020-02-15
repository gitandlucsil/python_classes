import cherrypy

class Root(object):

    @cherrypy.expose
    def index(self):
        return "Olá Mundo!"

cherrypy.quickstart(Root())