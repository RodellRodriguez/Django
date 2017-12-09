import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError

from links.models import Link, Vote
from users.schema import get_user, UserType

from django.db.models import Q

class LinkType(DjangoObjectType):
	class Meta:
		model = Link


class VoteType(DjangoObjectType):
	class Meta:
		model = Vote

class Query(graphene.ObjectType):
	# Add the first and skip parameters for pagination
	links = graphene.List(
		LinkType, 
		search=graphene.String(),
		first=graphene.Int(),
		skip=graphene.Int(),
	)
	votes = graphene.List(VoteType)

	# Use the first and skip parameters to slice the Django queryset
	def resolve_links(self, info, search=None, first=None, skip=None, **kwargs):
		qs = Link.objects.all()

		# The value sent with the search paramter will be on the args variable
		if search:
			filter = (
				Q(url__icontains=search) |
				Q(description__icontains=search)
			)
			qs = qs.filter(filter)

		if skip:
			qs = qs[skip::]

		if first:
			qs = qs[:first]

		return qs

	def resolve_votes(self, info, **kwargs):
		return Vote.objects.all()


class CreateLink(graphene.Mutation):
	# Defines the output of this mutation
	id = graphene.Int()
	url = graphene.String()
	description = graphene.String()
	posted_by = graphene.Field(UserType)

	# Defines the data you can send to the server, this being url and description
	class Arguments:
		url = graphene.String()
		description = graphene.String()

	# Mutation method: creates a link on the database using the data sent by the use via url and description parameters
	def mutate(self, info, url, description):
		user = get_user(info) or None

		link = Link(url=url, description=description, posted_by=user,)
		link.save()

		return CreateLink(
			id=link.id,
			url=link.url,
			description=link.description,
			posted_by=link.posted_by,
		)


class CreateVote(graphene.Mutation):
	user = graphene.Field(UserType)
	link = graphene.Field(LinkType)

	class Arguments:
		link_id = graphene.Int()

	def mutate(self, info, link_id):
		user = get_user(info) or None
		if not user:
			raise GraphQLError('You must be logged to vote!')


		link = Link.objects.filter(id=link_id).first()
		if not link:
			raise Exception('Invalid Link!')


		Vote.objects.create(
			user=user,
			link=link,
		)

		return CreateVote(user=user, link=link)

# Creates a mutation class with a field to be resolved, which points to our mutation defined before
class Mutation(graphene.ObjectType):
	create_link = CreateLink.Field()
	create_vote = CreateVote.Field()