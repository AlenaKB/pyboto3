'''

The MIT License (MIT)

Copyright (c) 2016 WavyCloud

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

'''

def can_paginate(operation_name=None):
    """
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    """
    pass

def generate_presigned_url(ClientMethod=None, Params=None, ExpiresIn=None, HttpMethod=None):
    """
    Generate a presigned url given a client, its method, and arguments
    
    :type ClientMethod: string
    :param ClientMethod: The client method to presign for

    :type Params: dict
    :param Params: The parameters normally passed to\nClientMethod.

    :type ExpiresIn: int
    :param ExpiresIn: The number of seconds the presigned url is valid\nfor. By default it expires in an hour (3600 seconds)

    :type HttpMethod: string
    :param HttpMethod: The http method to use on the generated url. By\ndefault, the http method is whatever is used in the method\'s model.

    """
    pass

def get_paginator(operation_name=None):
    """
    Create a paginator for an operation.
    
    :type operation_name: string
    :param operation_name: The operation name. This is the same name\nas the method name on the client. For example, if the\nmethod name is create_foo, and you\'d normally invoke the\noperation as client.create_foo(**kwargs), if the\ncreate_foo operation can be paginated, you can use the\ncall client.get_paginator('create_foo').

    :rtype: L{botocore.paginate.Paginator}
ReturnsA paginator object.


    """
    pass

def get_waiter(waiter_name=None):
    """
    Returns an object that can wait for some condition.
    
    :type waiter_name: str
    :param waiter_name: The name of the waiter to get. See the waiters\nsection of the service docs for a list of available waiters.

    :rtype: botocore.waiter.Waiter


    """
    pass

def put_events(trackingId=None, userId=None, sessionId=None, eventList=None):
    """
    Records user interaction event data.
    See also: AWS API Documentation
    
    Exceptions
    
    :example: response = client.put_events(
        trackingId='string',
        userId='string',
        sessionId='string',
        eventList=[
            {
                'eventId': 'string',
                'eventType': 'string',
                'properties': 'string',
                'sentAt': datetime(2015, 1, 1)
            },
        ]
    )
    
    
    :type trackingId: string
    :param trackingId: [REQUIRED]\nThe tracking ID for the event. The ID is generated by a call to the CreateEventTracker API.\n

    :type userId: string
    :param userId: The user associated with the event.

    :type sessionId: string
    :param sessionId: [REQUIRED]\nThe session ID associated with the user\'s visit.\n

    :type eventList: list
    :param eventList: [REQUIRED]\nA list of event data from the session.\n\n(dict) --Represents user interaction event information sent using the PutEvents API.\n\neventId (string) --An ID associated with the event. If an event ID is not provided, Amazon Personalize generates a unique ID for the event. An event ID is not used as an input to the model. Amazon Personalize uses the event ID to distinquish unique events. Any subsequent events after the first with the same event ID are not used in model training.\n\neventType (string) -- [REQUIRED]The type of event. This property corresponds to the EVENT_TYPE field of the Interactions schema.\n\nproperties (string) -- [REQUIRED]A string map of event-specific data that you might choose to record. For example, if a user rates a movie on your site, you might send the movie ID and rating, and the number of movie ratings made by the user.\nEach item in the map consists of a key-value pair. For example,\n\n{'itemId': 'movie1'}{'itemId': 'movie2', 'eventValue': '4.5'}\n{'itemId': 'movie3', 'eventValue': '3', 'numberOfRatings': '12'}\n\nThe keys use camel case names that match the fields in the Interactions schema. The itemId and eventValue keys correspond to the ITEM_ID and EVENT_VALUE fields. In the above example, the eventType might be \'MovieRating\' with eventValue being the rating. The numberOfRatings would match the \'NUMBER_OF_RATINGS\' field defined in the Interactions schema.\n\nsentAt (datetime) -- [REQUIRED]The timestamp on the client side when the event occurred.\n\n\n\n\n

    :returns: 
    PersonalizeEvents.Client.exceptions.InvalidInputException
    
    """
    pass

