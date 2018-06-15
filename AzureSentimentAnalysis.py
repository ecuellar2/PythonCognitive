print("Time to have fun with python and sentiment analysis ")

import urllib.request
import json
import xlrd

# Configure API access
apiKey = 'xxxxxx'
sentimentUri = 'https://regiongoeshere.api.cognitive.microsoft.com/text/analytics/versionnumbergoeshere/sentiment'
# This data set was all English
language = 'en'
headers = {}
headers['Ocp-Apim-Subscription-Key'] = apiKey
headers['Content-Type'] = 'application/json'
headers['Accept'] = 'application/json'

rec_id = '1'        
sampleText = 'blah'
# In this case had table export from RDBMS into Excel file. Excel file had 2 columns, primary key and text.
book = xlrd.open_workbook('sentiment1.xlsx')
f = open('output1.txt','w') // for now going to write output of sentiment API into a flat file
sheet = book.sheet_by_index(0)
for rownum in range(sheet.nrows):
    rec_id = sheet.cell(rownum,0).value
    sampleText = sheet.cell(rownum,1).value
    # Determine sentiment
    postData2 = json.dumps({"documents":[{"id":rec_id, "language":language, "text":sampleText}]}).encode('utf-8')
    request2 = urllib.request.Request(sentimentUri, postData2, headers)
    response2 = urllib.request.urlopen(request2)
    response2json = json.loads(response2.read().decode('utf-8'))
    sentiment = response2json['documents'][0]['score']
    f.write('\n' +str(rec_id)+":::"+str(sentiment))
    #I now have the sentiment for each primary key in my file

f.close()
print("All done folks")
