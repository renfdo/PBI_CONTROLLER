# PBI_CONTROLLER

Código em Python que tem o objetivo de facilitar a atualização 
dos datasets do Power BI Service.
A API do PBI necessita saber qual o ID do Workspace e Dataset para então atualizar. <br>
Com API, é necessário passar como parâmetro apenas o nome do Workspace e Dataset.
<p>
No arquivo **lib/variables.py**, 

'body = {
            "grant_type":   "password",
            "client_id":    "SERVICE_PRINCIPAL_ID",
            "resource":     "https://analysis.windows.net/powerbi/api",
            "username":     "PBI_USERNAME",
            "password":     "PBI_USERNAME_PASSWORD",
            "client_secret":"SERVICE_PRINCIPAL_KEY",
            "response_type":"code"
            }'