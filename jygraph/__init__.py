from bottle import Bottle, route
import graphene

class Query(graphene.ObjectType):
      hello = graphene.String(description='A typical hello world')
      ping = graphene.String(description='Ping someone',
                             to=graphene.String())

      def resolve_hello(self, args, info):
          return 'World'

      def resolve_ping(self, args, info):
          return 'Pinging {}'.format(args.get('to'))

schema = graphene.Schema(query=Query)

simple_app = app = Bottle()


@app.route('/hello/<name>')
def index(name):

    query = '''
      query SayHello {
            hello
            ping(to:name)
      }
'''

    return str(schema.execute(query))

@app.route('/bye/<name>')
def index(name):
    return "Bye %s" % name
