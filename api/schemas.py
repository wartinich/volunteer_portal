import graphene
from graphene_django import DjangoObjectType

from assistance.models import Category, Assistance


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name')


class AssistanceType(DjangoObjectType):
    class Meta:
        model = Assistance
        fields = (
            'id',
            'image',
            'name',
            'description',
            'category',
            'status',
            'payment_url',
        )


class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    assistance = graphene.List(AssistanceType)

    def resolve_assistance(root, info, **kwargs):
        # Querying a list
        return Assistance.objects.all()

    def resolve_categories(root, info, **kwargs):
        # Querying a list
        return Category.objects.all()


schema = graphene.Schema(query=Query)
