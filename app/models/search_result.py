# -*- coding: utf-8 -*-

class search_result():

    service_id = None

    client_id = 0

    # AVIA | HOTEL
    search_type = None

    search_time = None

    search_price = {'min': 0, 'max': 0}

    # start, end
    search_dates = {}

    # from, to
    search_locations = {}

    search_form_data = ''

    # {supplier: xml}
    search_content = {}

    # searhable tags
    tags = {}