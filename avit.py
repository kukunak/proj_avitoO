import requests

def get_html(mark):
    url = 'https://www.avito.ru/moskva/muzykalnye_instrumenty/gitary_i_drugie_strunnye?'
    params = {
        'p': 1,
        'q': mark
    }
    result = requests.get(url, params = params)
    '''if 'data' in result:
        if 'current_condition' in result['data']:
            try:
                return result['data']['current_condition']
            except (IndexError, TypeError):
                return False
    '''
    return result
   
if __name__ == '__main__':
    print (get_html('Ibanez'))

    #avito_url = 'https://www.avito.ru/moskva/muzykalnye_instrumenty/gitary_i_drugie_strunnye?'
    #page_count = 'p='
    #query_p = '&q=ibanez'
    
    #total_pages = get_total_pages(get_html(url))

    #for i in range(1, total_pages):
        #url_gen = avito_url + page_count + str(i) + query_p
        #print(url_gen)
