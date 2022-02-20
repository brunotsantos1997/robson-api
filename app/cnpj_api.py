import json

import requests

from app.constants import CNPJ_API


def get_cnpj_cnaes_description(cnpj):
    """
    Retorna a lista com descrição dos CNAEs vinculados ao CNPJ
    """

    url = CNPJ_API.format(cnpj)
    response = requests.get(url)
    if response.status_code == 200:
        cnaes_description = []
        content = json.loads(response.content)
        cnaes_description.append(content['cnae_fiscal_descricao'])
        for cnae in content['cnaes_secundarios']:
            cnaes_description.append(cnae['descricao'])

        return cnaes_description
    else:
        return []
