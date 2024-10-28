from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.conf import settings
from .forms import ContactForm
from django.contrib import messages
from .models import Post, Category
def index(request):
	posts = Post.objects.all().order_by('-created_at')
	context = {
	'posts' : posts
	}
	return render(request,'blog/index.html', context)

def post(request,id):
	post =Post.objects.get(id=id)
	context = {
		'post' : post
	}
	return render(request,'blog/post.html', context)

def category(request,foo):
	# Replace hyphens with spaces
	foo = foo.replace('-',' ')
	try:
		category = Category.objects.get(name=foo)
		posts = Post.objects.filter(category=category)
		context = {
		'posts' : posts,
		'category' : category
		}
		return render(request,'blog/category.html', context)
	except:
		messages.warning(request,"The Category does not exist")
		return redirect('home')

def contact(request):

	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			message = form.cleaned_data["message"]
			try:
				# send_mail(
				# 	f"New Contact form submission from {name}",
				# 	message,
				# 	email,
				# 	['testingpycread15@zohomail.in'],
				# 	fail_silently = False
				# 	)
				email_msg = EmailMessage(
					subject = f"You have got new message from {name}",
					body = message,
					from_email = "testingpycread15@zohomail.in",
					to = ["testingpycread15@zohomail.in"],
					reply_to = [email]
					)
				email_msg.send()
				messages.success(request,"Your message has been sent successfully!!")
				return redirect("contact")
			except BadHeaderError:
				messages.error(request, "Invalid Header found.")
		else:
			messages.error(request,"Please correct the error.")
	else:
		form = ContactForm()

	return render(request,'blog/contact.html',{'form':form})






	


