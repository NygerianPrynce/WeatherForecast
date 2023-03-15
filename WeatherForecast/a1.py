from urllib.request import Request, urlopen # Python 3
import json,os
def analog(s):
    """Returns a copy of s in analog form

    Parameter s: the string to slice
    Precondition: s is a string with at least one space
    """
    word = s.index(":")
    front = int(s[:word])
    back = (s[word:])
    if front > 12:
        front = front - 12
    return str(front) + str(back)
def get_time(json):
    '''Returns the lhs value in the response to a currency query

        Given a JSON response to a currency query, this returns the
        string inside double quotes (") immediately following the keyword
        "lhs". For example, if the JSON is
        '{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }'
        then this function returns '1 Bitcoin' (not '"1 Bitcoin"').

        This function returns the empty string if the JSON response
        contains an error message.

        Parameter json: a json string to parse
        Precondition: json is the response to a currency query'''

    return analog(str((json.get('current')).get("last_updated"))[11:])

def get_tempc(json):
    '''Returns the lhs value in the response to a currency query

        Given a JSON response to a currency query, this returns the
        string inside double quotes (") immediately following the keyword
        "lhs". For example, if the JSON is
        '{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }'
        then this function returns '1 Bitcoin' (not '"1 Bitcoin"').

        This function returns the empty string if the JSON response
        contains an error message.

        Parameter json: a json string to parse
        Precondition: json is the response to a currency query'''

    return json.get('current').get("temp_c")

def get_tempf(json):
    '''Returns the lhs value in the response to a currency query

        Given a JSON response to a currency query, this returns the
        string inside double quotes (") immediately following the keyword
        "lhs". For example, if the JSON is
        '{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }'
        then this function returns '1 Bitcoin' (not '"1 Bitcoin"').

        This function returns the empty string if the JSON response
        contains an error message.

        Parameter json: a json string to parse
        Precondition: json is the response to a currency query'''

    return json.get('current').get("temp_f")

def get_condition(json):
    '''Returns the lhs value in the response to a currency query

        Given a JSON response to a currency query, this returns the
        string inside double quotes (") immediately following the keyword
        "lhs". For example, if the JSON is
        '{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }'
        then this function returns '1 Bitcoin' (not '"1 Bitcoin"').

        This function returns the empty string if the JSON response
        contains an error message.

        Parameter json: a json string to parse
        Precondition: json is the response to a currency query'''

    return json.get('current').get("condition").get("text")

def get_windmph(json):
    '''Returns the lhs value in the response to a currency query

        Given a JSON response to a currency query, this returns the
        string inside double quotes (") immediately following the keyword
        "lhs". For example, if the JSON is
        '{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }'
        then this function returns '1 Bitcoin' (not '"1 Bitcoin"').

        This function returns the empty string if the JSON response
        contains an error message.

        Parameter json: a json string to parse
        Precondition: json is the response to a currency query'''

    return json.get('current').get("wind_mph")

def get_windkph(json):
    '''Returns the lhs value in the response to a currency query

        Given a JSON response to a currency query, this returns the
        string inside double quotes (") immediately following the keyword
        "lhs". For example, if the JSON is
        '{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }'
        then this function returns '1 Bitcoin' (not '"1 Bitcoin"').

        This function returns the empty string if the JSON response
        contains an error message.

        Parameter json: a json string to parse
        Precondition: json is the response to a currency query'''

    return json.get('current').get("wind_kph")

def get_winddir(json):
    '''Returns the lhs value in the response to a currency query

        Given a JSON response to a currency query, this returns the
        string inside double quotes (") immediately following the keyword
        "lhs". For example, if the JSON is
        '{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }'
        then this function returns '1 Bitcoin' (not '"1 Bitcoin"').

        This function returns the empty string if the JSON response
        contains an error message.

        Parameter json: a json string to parse
        Precondition: json is the response to a currency query'''

    return json.get('current').get("wind_dir")

def get_precipmm(json):
    '''Returns the lhs value in the response to a currency query

        Given a JSON response to a currency query, this returns the
        string inside double quotes (") immediately following the keyword
        "lhs". For example, if the JSON is
        '{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }'
        then this function returns '1 Bitcoin' (not '"1 Bitcoin"').

        This function returns the empty string if the JSON response
        contains an error message.

        Parameter json: a json string to parse
        Precondition: json is the response to a currency query'''

    return json.get('current').get("precip_mm")

def get_precipin(json):
    '''Returns the lhs value in the response to a currency query

        Given a JSON response to a currency query, this returns the
        string inside double quotes (") immediately following the keyword
        "lhs". For example, if the JSON is
        '{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }'
        then this function returns '1 Bitcoin' (not '"1 Bitcoin"').

        This function returns the empty string if the JSON response
        contains an error message.

        Parameter json: a json string to parse
        Precondition: json is the response to a currency query'''

    return json.get('current').get("precip_in")

def get_humidity(json):
    '''Returns the lhs value in the response to a currency query

        Given a JSON response to a currency query, this returns the
        string inside double quotes (") immediately following the keyword
        "lhs". For example, if the JSON is
        '{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }'
        then this function returns '1 Bitcoin' (not '"1 Bitcoin"').

        This function returns the empty string if the JSON response
        contains an error message.

        Parameter json: a json string to parse
        Precondition: json is the response to a currency query'''

    return json.get('current').get("humidity")

def get_feelc(json):
    '''Returns the lhs value in the response to a currency query

        Given a JSON response to a currency query, this returns the
        string inside double quotes (") immediately following the keyword
        "lhs". For example, if the JSON is
        '{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }'
        then this function returns '1 Bitcoin' (not '"1 Bitcoin"').

        This function returns the empty string if the JSON response
        contains an error message.

        Parameter json: a json string to parse
        Precondition: json is the response to a currency query'''

    return json.get('current').get("feelslike_c")

def get_feelf(json):
    '''Returns the lhs value in the response to a currency query

        Given a JSON response to a currency query, this returns the
        string inside double quotes (") immediately following the keyword
        "lhs". For example, if the JSON is
        '{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }'
        then this function returns '1 Bitcoin' (not '"1 Bitcoin"').

        This function returns the empty string if the JSON response
        contains an error message.

        Parameter json: a json string to parse
        Precondition: json is the response to a currency query'''

    return json.get('current').get("feelslike_f")

def weather_response(city):
    '''Returns a JSON string that is a response to a currency query.

        A currency query converts amt money in currency src to the
        currency dst. The response should be a string of the form

        '{ "ok":true, "lhs":"<old-amt>", "rhs":"<new-amt>", "err":"" }'

        where the values old-amount and new-amount contain the value
        and name for the original and new currencies. If the query is
        invalid, both old-amount and new-amount will be empty, while
        "ok" will be followed by the value false (and "err" will have
        an error message).

        Parameter src: the currency on hand (the LHS)
        Precondition: src is a string with no spaces or non-letters

        Parameter dst: the currency to convert to (the RHS)
        Precondition: dst is a string with no spaces or non-letters

        Parameter amt: amount of currency to convert
        Precondition: amt is a float'''
    url = "http://api.weatherapi.com/v1/current.json?key=120f46f0e938434ebd413636202112&q=Katy"
    url = url.replace("Katy", city)
    req = Request(url, headers={'User-Agent': 'Chrome', 'Content-Type': 'application/json'})
    response = urlopen(req).read().decode('utf-8')
    jsonfinal = json.loads(response)
    return jsonfinal

