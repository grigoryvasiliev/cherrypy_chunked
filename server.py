import cherrypy
from cherrypy import expose,response
import time 
import simplejson

class Root:
	@expose
	def TestStreaming1(self):
		cherrypy.response.headers['Content-Type'] = 'text/plain'
		def content():
			for i in range(30):
				print 'next chunk %i' % i
				yield simplejson.dumps( ''.join( ['z' for i in xrange(100 * 1024) ] ) ) + '\n'				
		return content()
	TestStreaming1._cp_config = {'response.stream': True}
		
def Register():

	root = Root()
	app = cherrypy.tree.mount(root)
	cherrypy.config.update( {'server.socket_port' : 8081 } )
	cherrypy.config.update( {'server.socket_host' : "0.0.0.0" } )
	cherrypy.engine.start()
	cherrypy.engine.block()

if __name__ == '__main__':
	Register()
	
	
	


	
	
