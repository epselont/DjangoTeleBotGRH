from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Button
# Create your views here.

class GetList(APIView):
	def get(self, request):
		data = {'list':[]}
		button = Button.objects.all()
		for i in button:
			data['list'].append({'name':i.button})
		return Response(data)

	def post(self, request):
		pass