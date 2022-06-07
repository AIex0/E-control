'''
 # @ Author: Alex
 # @ Create Time: 2022-06-04 13:59:57
 # @ Modified by: Alex
 # @ Modified time: 2022-06-04 14:01:09
 # @ Description:
 '''

from http_request import Request

obb = Request(url="api-gateway.oebb.at",
              request_string="/gateway/Verkaufsstelleninformation_API/1.0/vsti/opendata")

print(obb.get_formated_json())
