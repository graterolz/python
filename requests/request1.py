import requests

url = 'https://ml.azure.com/fileexplorerAzNB?wsid=/subscriptions/ca435350-342b-4fcb-b791-0bd8f909d0d0/resourceGroups/poc-supervivenciaplantines/providers/Microsoft.MachineLearningServices/workspaces/mdppocml&tid=b6070b4f-a1a6-4a0a-8098-75ac434f6163&activeFilePath=Users/jonatan.aguirre.ext/models/supervivencia/20220606_1341_modelo_supervivencia.pkl'
r = requests.get(url, allow_redirects=False)

open('20220606_1341_modelo_supervivencia.pkl', 'wb').write(r.content)
print(r.content)