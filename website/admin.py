from django.contrib import admin
from .models import *
from django.conf import settings

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
	list_display = ("name", "faculty_en", "address", "phone", "mobile", "email", "social", "created_at", "updated_at")
	fields = ["name_en", "name_el", "faculty_en", "faculty_el", "address", "phone", "mobile", "description_en", "description_el", "email", "cv_en", "cv_gr", "social", "image", "order"]
	ordering = ("-name",)
	readonly_fields = ('created_at', "updated_at")

# @admin.register(Page)
# class PageAdmin(admin.ModelAdmin):
# 	list_display = ("title", "friendlyurl", "order")
# 	fields = ["title_en", "title_el", "short_title_en", "short_title_el", "long_title_en", "long_title_el", "friendlyurl_en", "friendlyurl_el", "views", "order"]
# 	ordering = ["order"]

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
	list_display = ("name", "lang_code", "order", "default",)
	fields = ["name", "lang_code", "order", "default", "image"]

@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
	list_display = ("owner", "facebook", "twitter", "youtube", "linkedin", "scopus", "github", "other_link1", "other_link2")
	fields = ["owner", "facebook", "twitter", "youtube", "linkedin", "scopus", "github", "other_link1", "other_link2", "research_gate"]

@admin.register(LabDetails)
class LabDetailsAdmin(admin.ModelAdmin):
	list_display = ("name", "created_at", "updated_at", "fax", "email", "social", "address", "phone", "mobile",)
	fields = ["name_en", "name_el", "description_en", "description_el", "email", "fax", "social", "logo", "address_en", "address_el" , "phone", "mobile"]

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
	list_display = ("name", "email", "created_at", "updated_at")
	fields = ["name", "email", "message"]

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
	list_display = ("title", "created_at", "updated_at")
	fields = ["title", "description", "image"]

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
	list_display = ("title", "content", "sub_category", "year", "duration")
	fields = ["content", "sub_category", "sub_sub_category", "funded", "title_en", "title_el", "description_en",
	 		  "description_el", "year", "duration", "author_en", "author_el", "location", "url", "image", "views",
	 		  "journal", "level", "volume", "number", "publisher"]
	list_filter = ['content', "sub_category"]

