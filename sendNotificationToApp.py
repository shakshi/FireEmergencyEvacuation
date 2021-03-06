
#Python Code to send Fire Alter Notification from Anduino to App
from pyfcm import FCMNotification
import sys

fireNodesList = [3,7]

#Api-key for FireDemoProject
push_service = FCMNotification(api_key="AAAAAZKyPwo:APA91bFDpKHYFZVHfcJ4k61wx1WnqkNsiRnXDlMY7QxyT1rmQLPXDRu7NaKQsSkDhSYFrzMbxTGB8BH67DjAjwsVQO6XV_62W-015lT_d4hwo74aqio6kIQZTdmmhTLhclfw3r-voK6P")


reg_id1 = "eiuwj88g8jA:APA91bHdYkFWIajcetVnhf7N78ZKnj9qWOrhcTePE-Qjhi-eZYeRTX3mXGyM7fI521fYbKHth5Q0D-D1wUrihywoI8edUrcKLRN8dPRmeZjtMNmk7DLEJBZAiC9MhXQH6N62rSlLQHFA"
reg_id2="c9VQcMBvwWI:APA91bEHKiKfzVS4J-rbpxz58b9PRazioR6slAr8MEMwzR1TsS7KjqylDB3qT_x4XQ5aud981IFT00JVXyQDwHBk1S5d5dm5IcjOUqvFfV9CGHzH5ZCkEXc7yn5EfSxTTGUiFa6LtWam"
reg_id3="dygYYQ3eQiY:APA91bE9-idFk9gg8_Z1vhPVxPAMCqJvlzBD0sETxo4Y3FG_x4eBi7Z3Jkcz69PbE_YRHYBX24M2ArPleXotK9wlhjuFI8wvwvSi4p1nnmA0rRiRfgi_zsfFex6Q1mvQNqA0h8sLcjXW"
reg_id4="d6Piim8gO3Y:APA91bF3P40evOlmNKmwgY5sJ8a-qnm_JbiUqhgZhj_L1EzkmmFSNis7DeTwiPDj9cgdk1wXudz2BUsbJ0I1X1i52Iylq_aJoNQoOJQQBZm2f8qePRst9GhXFoUxgRj85SK08ExmQpzj"
message_title = "Fire Alerts!! Evacuate the floor"
#result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=fireNodesList)

registration_ids = [reg_id1,reg_id2,reg_id3,reg_id4]
result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=fireNodesList)

print result