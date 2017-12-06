from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *
from django.utils import translation
from .forms import ContactForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.translation import ugettext as _
from django.conf import settings
from django.shortcuts import redirect
from django.core.cache import cache
import datetime
from django.core.mail import send_mail
from itertools import chain
from django.http import Http404

def handle_post(request, context):
	if request.method == "POST":
		if request.POST.get('search_text' , ""):
			search_text = request.POST.get('search_text', "")
			people_search = Person.objects.filter(name__contains=search_text)
			content_search1 = Content.objects.filter(title__contains=search_text)
			content_search2 = Content.objects.filter(description__contains=search_text)
			content_search = set(list(chain(content_search1, content_search2)))
			context["people_search"] = people_search
			context["content_search"] = content_search
			return True
		elif request.POST.get("email", ""):
			form = ContactForm(request.POST)
			if form.is_valid():
				name = request.POST.get("name", "")
				email = request.POST.get("email", "")
				if len(Message.objects.filter(email=email))>2:
					user_messages = Message.objects.filter(email=email).order_by("created_at")
					for item in user_messages:
						if len(Message.objects.filter(email=email))>2:
							item.delete()
				message = request.POST.get("message", "")
				Message.objects.create(name=name, email=email, message=message)
				message = _("Thank you! We received your message!")
				context["message"] = message

				# Send Mail
				subject = 'Message from TransLog site'
				message = "Author: " + name + "\n\n" + "Email: " + email + "\n\n" "Message: " + "\n" + request.POST.get("message", "")
				# message = '%s %s' %(message, name)
				emailFrom = email
				emailTo = ["tbasos@hotmail.com"]
				send_mail(
					subject, 
					message, 
					emailFrom, 
					emailTo, 
					fail_silently=False,
				)
			else:
				message = _("Message was not sent")
				context["message"] = message
		return False

def handle_research_search(request, context):
	research_type = request.POST.get("research-type", "")
	research_category = request.POST.get("research-category", "")
	if research_category == "":
		research_category = "default"
	date_from = request.POST.get("date_from", "date_from")
	date_to = request.POST.get("date_to", "date_to")
	subject = request.POST.get("subject", "subject")

	if research_type == "Δημοσιεύσεις":
		research_type = "Publications"
	if research_type == "Πρότζεκτς":
		research_type = "Projects"
	if research_type == "Όλα":
		research_type = "All"
	if research_category == "Τρέχουσες Δημοσιεύσεις":
		research_category = "Working Papers"
	if research_category == "Δημοσιεύσεις Περιοδικών":
		research_category = "Journal Papers"
	if research_category == "Δημοσιεύσεις Κοινότητας":
		research_category = "Conference Papers"
	if research_category == "Βιβλία":
		research_category = "Books"
	if date_from == "Όλα":
		date_from = "All"
	if date_to == "Όλα":
		date_to = "All"
	if subject == "Όλα":
		subject = "All"
	if subject == "Προβλήματα Δρομολόγησης Οχημάτων":
		subject = "Vehicle Routing Problems"
	if subject == "Προβλήματα Προγραμματισμού":
		subject = "Scheduling Problems"
	if subject == "Προβλήματα δρομολόγησης επικίνδυνων υλικών":
		subject = "Hazardous Material Logistical Problems"
	if subject == "Πρόβλημα οικολογικής δρομολόγησης οχημάτων":
		subject = "Green Vehicle Routing Problem"
	if subject == "Πρόβλημα δρομολόγησης αποθεμάτων":
		subject = "Inventory Routing Problem"
	if subject == "Πρόβλημα οικολογικής δρομολόγησης αποθεμάτων":
		subject = "Green Inventory Routing Problem"

	search_list = [research_type, research_category, int(date_from), int(date_to), subject]
	if research_type == "Publications" and research_category == "default":
		if subject != "default" and subject != "All":
			content = Content.objects.filter(content=research_type, year__gte=date_from, year__lte=date_to, subject=subject)
		else:
			content = Content.objects.filter(content=research_type, year__gte=date_from, year__lte=date_to)
	elif research_type == "Publications" and research_category != "default":
		if subject != "subject" and subject != "default" and subject != "" and subject != "All":
			content = Content.objects.filter(sub_category=research_type, year__gte=date_from, year__lte=date_to, subject=subject)
		if subject == "subject" or subject == "default" or subject == "" or subject == "All":
			content = Content.objects.filter(sub_category=research_category, year__gte=date_from, year__lte=date_to)
	elif research_type == "Projects":
		if subject != "default" and subject != "default" and subject != "" and subject != "All":
			content = Content.objects.filter(sub_category=research_type, year__gte=date_from, year__lte=date_to, subject=subject)
		else:
			content = Content.objects.filter(sub_category=research_type, year__gte=date_from, year__lte=date_to)
	else:
		if subject != "default" and subject != "default" and subject != "" and subject != "All":
			
			content1 = Content.objects.filter(content="Publications", year__gte=date_from, year__lte=date_to, subject=subject)
			content2 = Content.objects.filter(sub_category="Projects", year__gte=date_from, year__lte=date_to, subject=subject)
		else:
			print(search_list)
			content1 = Content.objects.filter(content="Publications", year__gte=date_from, year__lte=date_to)
			content2 = Content.objects.filter(sub_category="Projects", year__gte=date_from, year__lte=date_to)
		content = list(chain(content1, content2))
	return content, search_list

def pagination(request, objects):
	paginator = Paginator(objects, 6)
	page = request.GET.get('page', 1)
	try:
		new_paginator = paginator.page(page)
	except PageNotAnInteger:
		new_paginator = paginator.page(1)
	except EmptyPage:
		new_paginator = paginator.page(paginator.num_pages)
	
	return new_paginator

def initial(request, lang, friendlyurl):
	translation.activate(lang)
	request.LANGUAGE_CODE = translation.get_language()

	try:
		pages = Page.objects.all()
		languages = Language.objects.all().order_by("order")
		lab_details = LabDetails.objects.all()[:1].get()
		awards = Home.objects.all().order_by("created_at")
		if friendlyurl != "":
			current_page = get_object_or_404(Page, friendlyurl=friendlyurl)
			current_page.views += 1
			current_page.save()
		else:
			current_page = get_object_or_404(Page, title_en="Home")
	except:
		raise Http404

	group_of_current_friendlyurls = [current_page.friendlyurl_en, current_page.friendlyurl_el]
	list_with_lang_codes = []
	for language in languages:
		list_with_lang_codes.append(language.lang_code)
	zipped_langs_friendlyurls = zip(list_with_lang_codes, group_of_current_friendlyurls)

	now = datetime.datetime.now()
	calendar = list(range(1995, now.year+1))

	return languages, lab_details, awards, calendar, zipped_langs_friendlyurls, current_page, pages

def index(request, lang):
	friendlyurl = ""
	languages, lab_details, awards, calendar, zipped_langs_friendlyurls, current_page, pages = initial(request, lang, friendlyurl)
	content_news = Content.objects.filter(content="News").order_by("created_at")[:3]
	content_events = Content.objects.filter(content="Event").order_by("created_at")[:3]
	context = {"languages":languages, "lab_details":lab_details, "content_news":content_news, "awards":awards,
			   "content_events":content_events, "calendar":calendar, "pages":pages, "current_page":current_page}

	form = ContactForm()
	context["form"] = form

	if handle_post(request, context):
		return render(request, "search_results.html", context)

	return render(request, 'index.html', context)

def regular_page(request, lang, friendlyurl):
	languages, lab_details, awards, calendar, zipped_langs_friendlyurls, current_page, pages = initial(request, lang, friendlyurl)

	context = {"languages":languages, "friendlyurl":friendlyurl,
	 		   "lab_details":lab_details, "awards": awards,
	 		   "zipped_langs_friendlyurls":zipped_langs_friendlyurls,
	 		   "pages":pages, "calendar":calendar, "current_page":current_page}

	form = ContactForm()
	context["form"] = form
	if handle_post(request, context):
		return render(request, "search_results.html", context)
	if request.POST.get("research-type", ""):
		content, search_list = handle_research_search(request, context)
		context["content"] = content
		context["search_list"] = search_list
		return render(request, "regular_page.html", context)

	content = Content.objects.filter(content=current_page.title_en).order_by("-title")
	if not content:
		content_category = Content.objects.filter(sub_category=current_page.title_en).order_by("-year")
		if content_category:
			content = Content.objects.filter(content=content_category[0].content)
	else:
		content_category = ""

	people = Page.objects.all().order_by("order")[2:8]
	for person in people:
		if current_page.title == person.title:
			content = Person.objects.filter(faculty_en=current_page.title_en).order_by("name")

	content_paginated = pagination(request, content)
	if content_category != "" and current_page.title_en != "Areas":
		content_category_paginated = pagination(request, content_category)
		context["content_category_paginated"] = content_category_paginated
	
	context["content"] = content
	context["content_category"] = content_category
	context["current_page"] = current_page
	context["content_paginated"] = content_paginated
	
	return render(request, "regular_page.html", context)

def regular_sub_page(request, lang, friendlyurl, id):
	languages, lab_details, awards, calendar, zipped_langs_friendlyurls, current_page, pages = initial(request, lang, friendlyurl)

	context = {"languages":languages, "friendlyurl":friendlyurl,
	 		   "lab_details":lab_details, "awards": awards,
	 		   "zipped_langs_friendlyurls":zipped_langs_friendlyurls,
	 		   "pages":pages, "calendar":calendar, "current_page":current_page}

	if handle_post(request, context):
		return render(request, "search_results.html", context)
	form = ContactForm()
	context["form"] = form

	content = Content.objects.get(id=id)
	content.views += 1
	content.save()
	people = Page.objects.all().order_by("order")[2:8]
	for person in people:
		if current_page.title_en == person.title:
			content = Person.objects.filter(id=id)
	context["content"] = content

	return render(request, "regular_subpage.html", context)


