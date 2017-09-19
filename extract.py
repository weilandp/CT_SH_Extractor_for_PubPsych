#!/usr/bin/python3
import web
import sys
sys.path.extend([r'/opt/webservices/modules'])
import pubpsych
import beautify

urls = (
    '/cte/(.*)', 'get_cte',
    '/ctd/(.*)', 'get_ctd',
    '/she/(.*)', 'get_she',
    '/shd/(.*)', 'get_shd',
)

application = web.application(urls, globals()).wsgifunc()

class get_cte:
    def GET(self, term):
        getInput = web.input(format='html')
        result = pubpsych.do_search(term, 'CTE', str(getInput.format))
        #if (getInput.format == 'html'):
        #    return beautify.beautify(result)
        #else:
        return result

class get_ctd:
    def GET(self, term):
        getInput = web.input(format='html')
        result = pubpsych.do_search(term, 'CTD', str(getInput.format))
        #if (getInput.format == 'html'):
        #    return beautify.beautify(result)
        #else:
        return result

class get_she:
    def GET(self, term):
        getInput = web.input(format='html')
        result = pubpsych.do_search(term, 'SHE', str(getInput.format))
        #if (getInput.format == 'html'):
        #    return beautify.beautify(result)
        #else:
        return result

class get_shd:
    def GET(self, term):
        getInput = web.input(format='html')
        result = pubpsych.do_search(term, 'SHD', str(getInput.format))
        #if (getInput.format == 'html'):
        #    return beautify.beautify(result)
        #else:
        return result

if __name__ == "__main__":
    application.run()