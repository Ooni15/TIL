def get_deposit_products():


# 본인의 API KEY 로 수정합니다.
api_key = "a34e300044963bd2b1a55d803a9103e1"

# 요구사항에 맞도록 이곳의 코드를 수정합니다.
url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
params = {
    'auth': api_key,
    # 금융회사 코드 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
    'topFinGrpNo': '020000',
    'pageNo': 1
}
response = requests.get(url, params=params).json()['result']
baselist = response['baseList']
optionlist = response['optionList']

result = []
for base in baselist:
    new_dict = {}
    new_dict['금리정보'] = []

    for opt in optionlist:
        opt_dict = {}
        if opt['fin_prdt_cd'] == base['fin_prdt_cd']:
            opt_dict['저축 금리'] = opt['intr_rate']
            opt_dict['저축 기간'] = opt['save_trm']
            opt_dict['저축금리유형'] = opt['intr_rate_type']
            opt_dict['저축금리유형명'] = opt['intr_rate_type_nm']
            opt_dict['최고 우대금리'] = opt['intr_rate2']
            new_dict['금리정보'].append(opt_dict)

    new_dict['금융상품명'] = base['fin_prdt_nm']
    new_dict['금융회사명'] = base['kor_co_nm']

    result.append(new_dict)

return result

if name == 'main':

# json 형태의 데이터 반환
result = get_deposit_products()
# prrint.prrint(): json 을 보기 좋은 형식으로 출력
pprint.pprint(result)