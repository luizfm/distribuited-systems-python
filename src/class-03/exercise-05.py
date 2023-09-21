import graphene

users = []

class User(graphene.ObjectType):
    name = graphene.String()
    age = graphene.Int()

class Query(graphene.ObjectType):
    user = graphene.Field(User)

    def resolve_user(self, info):
        firstUser = users[0]
        return firstUser
    
class CreateUser(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        age = graphene.Int()

    user = graphene.Field(User)

    def mutate(self, info, name, age):
        user = User(name=name, age=age)
        users.append(user)
        return CreateUser(user=user)
    
class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

mutation_string = 'mutation { createUser(name: "Luiz", age: 27) { user { name } }}'
result = schema.execute(mutation_string)
print(result)

query_string = '{ user { name }}'
result = schema.execute(query_string)
print(result)