from bottle import Bottle, route, request, run
import graphene
from graphene import resolve_only_args
import json

from .schema import Beach

class Query(graphene.ObjectType):
      hello = graphene.String(description='A typical hello world')
      ping = graphene.String(description='Ping someone',
                             to=graphene.String())
      beach = graphene.Field(Beach,
                             id=graphene.String())

      def resolve_hello(self, args, info):
          return 'World'

      def resolve_ping(self, args, info):
          return 'Pinging {}'.format(args.get('to'))

      @resolve_only_args
      def resolve_beach(self, id):
          return Beach(id=id, name="Beach name", score=100)

      

schema = graphene.Schema(query=Query)

simple_app = app = Bottle()


@app.route('/hello/<name>', method='POST')
def index(name):
    query_body = request.params['q']

    print query_body
    print len(query_body)
    print type(query_body)
    print dir(query_body)
    result = schema.execute(query_body)
    response = {'data': result.data,
                'errors': result.errors,
                'invalid': result.invalid}
    return json.dumps(response)


if __name__ == '__main__':
    run(host='localhost', port=8080)
