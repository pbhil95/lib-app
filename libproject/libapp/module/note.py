# pylint:disable=E1101

"""def registers(request):
	if request.method=="POST":
		nm=request.POST["name"]
		passwd=request.POST["pwd"]
		cpasswd=request.POST["cpwd"]
		rollno=request.POST["roll"]
		imge=request.FILES["img"]
		dates=date.today()
		if (passwd==cpasswd):
			p=models.register(name=nm,roll=rollno,pwd=passwd,img=imge,date=dates)
			p.save()
			return render(request,"main.html")
	return HttpResponse(request,"loginform.html")
	#return render (request, "login.html",{"name":name,"pwd":pwd,"cpwd":cpwd,"mobile":mobile})
def login(request):
	login_check=True
	login_flag={"login_status":login_check}
	if (request.method=="POST"):
		rollno=request.POST["roll"]
		passwd=request.POST["pwd"]
		c1=Q(roll=rollno)
		c2=Q(pwd=passwd)
		if(models.register.objects.filter(c1&c2)):
			login_check=False
			request.session["roll"]=rollno
			#return render(request,"tab.html")
			#displayuser(request)
			if(request.session.has_key("roll")):
				rno=request.session["roll"]
				x=models.register.objects.filter(roll=rno)
				for i in x:
					user={
						"name":i.name,
						 "roll":i.roll,
						  "img":i.img
					   }
				return render(request,"tab1.html",user)
	return render(request,"login.html" ,login_flag)"""
