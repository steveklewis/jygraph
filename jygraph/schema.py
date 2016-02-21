import graphene
from graphene import resolve_only_args

class Beach(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    score = graphene.Int()


