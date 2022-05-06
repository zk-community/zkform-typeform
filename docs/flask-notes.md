# Notes:
# Access by the field type
# Works if there's only one question by field type
# for answer in formResponse['answers']:
# if answer['type'] == 'email':
#  payload['email'] = answer['email'].lower()
# if answer['type'] == 'choice':
#  payload['type'] = answer['choice']['label']
# if answer['type'] == 'text':
#  payload['content'] = answer['text']
#
# # Access by the array
# payload['email'] = formResponse['answers'][0]['email'].lower()
# payload['type'] = formResponse['answers'][1]['choice']['label']
# payload['content'] = formResponse['answers'][2]['text']

# # Access by the ref
# references = {
#   '987c7c4d-2995-4044-9bc1-0c53a20a307e': 'email',
#   '189ee103-d2c4-409f-be00-22e64cb54f09': 'type',
#   '97268ad3-f0e7-4fa6-9fe5-7f5125ce1aa7': 'content'
# }
# for answer in formResponse['answers']:
#   ref = answer['field']['ref']
#   if ref in references:
#     if references[ref] == 'email':
#       payload['email'] = answer['email'].lower()
#     if references[ref] == 'type':
#       payload['type'] = answer['choice']['label']
#     if references[ref] == 'content':
#       payload['content'] = answer['text']
