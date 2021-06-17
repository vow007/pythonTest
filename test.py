# encoding:utf-8
import requests
import json
import uuid
import time

# MUJI业务走POS，先提单后支付，走通用提单
url = "http://11.26.80.137/httpInvoke/saas/invoke"

uuid = str(uuid.uuid4())
print("------>>>>>> uuid：{}".format(uuid))

tenantId = 1

upcCode = "226691"
skuId = 226691

# 外单号，获取不到，用时间戳代替，有风险
mujiOrderId = str(int(time.time()))
print("------>>>>>> mujiOrderId：{}".format(mujiOrderId))

# 即时提单:54，离线提单:55
orderSouceType = 55
storeId = 131215
userPin = "JDpos"

jsondata = [
    tenantId,
    {
        "calPackagingFee": False,
        "isCheckPrice": 0,
        "skuInfoList": [
            {
                "addMoneyBuy": False,
                "box": False,
                "fast": False,
                "gift": False,
                "haveInstallService": False,
                "jDBuy": False,
                "paid": False,
                "piece": False,
                "selectInstallService": False,
                "services": [],
                "virtualSuit":False,
                "xSuit":False,
                "extInfo":{
                    "upcCode": upcCode
                },
                "price": "12.00",
                "skuId": skuId,
                "skuNum": "1.0",
                "skuUuid": "af0aa2d3-0fd5-41ee-a77b-67ab65f75b4c"
            }
        ],
        "orderParam": {
            "autoCancelTime": 3600000,
            "autoDeduction": False,
            "eCardPayInfo": {
                "used": False
            },
            "extField": {
                "posSettleType": 1,
                "workMeal": False,
                "outerOrderPropertyList": [
                    {
                        "key": "mujiOrderId",
                        "value": mujiOrderId
                    },
                    {
                        "key": "BanAfterSaleAppOnline",
                        "value": "0"
                    }
                ]
            },
            "pack": False,
            "pinSourceEnum": "FRESH_APP",
            "prepaidCardPayInfo": {
                "used": False
            },
            "staffCardInfo": {
                "used": True
            },
            "useBalance": True,
            "useECard": False,
            "usePrepaidCard": False,
            "useStaffCard": True,
            "userIdentityAllFilled": False,
            "correction": 0,
            "payType": 2,
            "totalPrice": 12.00
        },
        "invoiceParam": {
            "isNeedInvoice": 0
        },
        "paidMember": False,
        "switchStore": False,
        "platformId": tenantId,
        "orderSouceType": orderSouceType,
        "outOfStockStrategy": 0,
        "orderGuid": uuid,
        "storeId": storeId,
        "userPin": userPin,
    },
    {
        "posParam": {
            "casher": "SelfCheckout",
            "posNum": "131215-Z04",
            "posTypeEnum": "SELF",
            "tranasDate": "2021-06-11",
            "tranasDocNo": "1de0dfb0-b76d-4b1c-b3a1-b74c4e611790"
        }
    },
    {}
]

params = {
    "service": "spring.commonSettlementFacadeSaasImpl",
    "method": "submitOrder",
    "methodId": "0",
    "pwd": "38bced94a36a4fede2ad28eeea5a87c0",
    "jsonData": json.dumps(jsondata),
}

response = requests.get(url, params=params)
print(response.text)
# if response.status_code == 200:
#     print(json.dumps(json.loads(response.content), indent=2))
# else:
#     print("调用失败")
#     print(response.content)