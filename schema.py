import graphene
import music.schema


class Query(music.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
