from django.shortcuts import render
from .models import RequestCallBack,SubscribeNow
# Create your views here.
def index(request):
	if request.method == "POST":

		if request.POST["formName"]  == "form1":
			user_name = request.POST["Name"]
			user_mail = request.POST["Email"]
			user_number = request.POST["Phone"]
			user_element = request.POST["select_item"]
			user_message = request.POST["Message"]
			print(user_name)
			print(user_mail)
			print(user_number)
			print(user_element)
			print(user_message)


			object_call = RequestCallBack(
				user_names = user_name,
				user_mails = user_mail,
				user_numbers = user_number,
				user_elements = user_element,
				user_messages = user_message
				)
			object_call.save()


		if request.POST["formName"] == "form2":
			user_mail = request.POST["mail"]
			print(user_mail)

			object_call = SubscribeNow(
				customer = user_mail,
				)
			object_call.save()
	return render(request,"index.html")

def about(request):
	return render(request,"about.html")

def services(request):
	return render(request,"services.html")

def contact(request):
	return render(request,"contact.html")

def read(request):
	object_readall=RequestCallBack.objects.all()
	print(object_readall)
	return render(request,"read.html",locals())

def readfile(request):
	if request.method =="POST":
		user_num=request.POST["Mobilenumber"]
		print(user_num)

		object_file=RequestCallBack.objects.get(user_numbers=user_num)
		print(object_file)
	return render(request,"readfile.html",locals())


