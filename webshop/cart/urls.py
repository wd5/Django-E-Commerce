# -*- coding: utf-8 -*-
#!/usr/bin/env python
from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('cart.views',
	# Просмотр корзины
	url(r'^$', 'cart_view', {'template_name':'cart/cart.html'}, name='show_cart'),

)
