"""
 # @ Author: Your name
 # @ Create Time: 2022-06-01 12:29:00
 # @ Modified by: Your name
 # @ Modified time: 2022-06-03 11:12:55
 # @ Description:
 """

from http_request import Request



class Test(Request):
    """_summary_

    :param Request: _description_
    :type Request: _type_
    """
    def __init__(self, url: str, request_string: str) -> None:
        """_summary_

        :param url: _description_
        :type url: str
        :param request_string: _description_
        :type request_string: str
        """