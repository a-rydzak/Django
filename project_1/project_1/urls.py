from django.conf.urls import url, include

"""project_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
	url(r'^', include('apps.first_app.urls'))
    # path('admin/', admin.site.urls),

]


# '^' Matches the following characters at the beginning of a string. Example: '^a' matches 'anna' but not 'banana'.
# '$' Matches the previous characters at the end of a string. Example: 'a$' matches 'anna' and 'banana' but not 'fan'.
# '[]' Matches any value in a range. Example: '[0-9]' matches '9' and '9s'.
# '{n}' Matches n number repetitions of the preceding pattern. Example: '[0-9]{2}' matches '91' but not '9'
# \d Matches digits.  Example: "\d" matches "8" and "877"
# \d+ matches a string with one or more digits
# \w Matches characters.
# \w+ matches a string with one or more character/word