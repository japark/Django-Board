from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Member
from .forms import LoginForm

# Create your views here.

def home(request):
	user_id = request.session.get('user')
	# if user_id:
	# 	user = Member.objects.get(pk=user_id)
		# return HttpResponse(user.username)
	return render(request, 'home.html')
	# return HttpResponse('Home!')


def logout(request):
	if request.session.get('user'):
		del request.session['user']
	return redirect('/')


def login(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			request.session['user'] = form.user_id
			return redirect('/')
	else:
		form = LoginForm()
	return render(request, 'login.html', {'form':form})

	# if request.method == 'GET':
	# 	return render(request, 'login.html')
	# elif request.method == 'POST':
	# 	username = request.POST.get('username', None)
	# 	password = request.POST.get('password', None)
	# 	res_data = {}
	# 	if not (username and password):
	# 		res_data['error'] = '모든 값을 입력해야합니다.'
	# 	else:
	# 		user = Member.objects.get(username=username)
	# 		if check_password(password, user.password):
	# 			request.session['user'] = user.id
	# 			return redirect('/')
	# 		else:
	# 			res_data['error'] = '비밀번호가 틀렸습니다.'

	# 	return render(request, 'login.html', res_data)

def register(request):
	if request.method == 'GET':
		return render(request, 'register.html')
	elif request.method == 'POST':
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		useremail = request.POST.get('useremail', None)
		re_password = request.POST.get('re-password', None)

		res_data = {}

		if not (username and useremail and password and re_password):
			res_data['error'] = '모든 값을 입력해야 합니다.'
		elif password != re_password:
			res_data['error'] = '비밀번호가 다릅니다.'
		else:
			member = Member(
				username=username,
				password=make_password(password),
				useremail=useremail
			)
			member.save()

		return render(request, 'register.html', res_data)