# encoding:utf-8
import requests
import json
import uuid
import time

# MUJI业务走POS，先提单后支付，走通用提单
url = "http://10.172.2.115/httpInvoke/saas/invoke"

uuid = str(uuid.uuid4())
print("------>>>>>> uuid：{}".format(uuid))

tenantId = 10010

upcCode = "226691"
skuId = 100019723

# # 即时提单:54，离线提单:55
# orderSouceType = 55
# storeId = 131215
# userPin = "JDpos"

jsondata = [
    tenantId,
    {
        "addressParam": {
            "addressId": -1,
            "lat": "29.3374",
            "log": "104.77728",
            "mobile": "138****3137",
            "mobileEnc": "a-MHVsW/4g4XiAXkPwD5i4Fw==",
            "name": "ceshibu3"
        },
        "calPackagingFee": False,
        "classifiedSkuIdParamList": [
            {
                "addressParam": {
                    "addressId": -1,
                    "lat": "29.3374",
                    "log": "104.77728",
                    "mobile": "138****3137",
                    "mobileEnc": "a-MHVsW/4g4XiAXkPwD5i4Fw==",
                    "name": "ceshibu3"
                },
                "classifyTypeEnum": "NORMAL",
                "shipmentParam": {
                    "deliveryPlatform": 1,
                    "deliveryTimeStyleEnum": "IRREGULAR",
                    "deliveryType": 3
                },
                "skuUuidSet": [
                    "93428f8e-9647-4fd9-be29-ae6b73ded0b9"
                ]
            }
        ],
        "couponParamList": [],
        "invoiceParam": {
            "isNeedInvoice": 0
        },
        "isCheckPrice": 0,
        "orderGuid": "c67ae235-96e0-4c03-a56e-071d718e7545",
        "orderParam": {
            "autoCancelTime": 86400000,
            "autoDeduction": False,
            "correction": 0,
            "eCardPayInfo": {
                "used": False
            },
            "extField": {
                "posSettleType": 1,
                "wanJiaInfo": {
                    "merchantId": 40112911,
                    "orderPin": "ceshibu3",
                    "posId": "50020941-J100",
                    "salerId": -1,
                    "salerName": "店主",
                    "shopName": "测试所用店铺-0001"
                },
                "customExtInfoList": [
                    {
                        "key": "orderSaleType",
                        "value": "1"
                    }
                ],
                "workMeal": False
            },
            "freight": 0,
            "orderDate": 1623232234548,
            "pack": False,
            "payType": 2,
            "pinSourceEnum": "FRESH_APP",
            "rePrice": 0,
            "remark": "基础建设二期",
            "reservationCodes": [],
            "staffCardInfo": {
                "used": False
            },
            "totalPrice": 1000,
            "useBalance": True
        },
        "orderSouceType": 43,
        "outOfStockStrategy": 0,
        "paidMember": False,
        "platformId": 10010,
        "promotionParamList": [],
        "skuInfoList": [
            {
                "addMoneyBuy": False,
                "box": False,
                "depositType": "NO_DEPOSIT",
                "discount": 1000,
                "extInfo": {
                    "immediateGift": "1"
                },
                "fast": False,
                "gift": False,
                "jDBuy": False,
                "paid": False,
                "piece": False,
                "price": 1000,
                "promotionInfoList": [],
                "saleType": "STOCK",
                "sendType": "SELF_GET",
                "serialNumberList": [],
                "skuId": skuId,
                "skuNum": 1,
                "skuUuid": "93428f8e-9647-4fd9-be29-ae6b73ded0b9",
                "virtualSuit": False,
                "xSuit": False
            }
        ],
        "storeId": 50020941,
        "switchStore": False,
        "userPin": "ceshibu3"
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
    "posParam": {
        "casher": "ceshibu3",
        "posNum": "50020941-J100",
        "posTypeEnum": "H5",
        "tranasDate": "2021-06-09",
        "tranasDocNo": "58345483-7076-4505-86fb-5b7b3d432a93"
    }
}

response = requests.get(url, params=params)
print(response.text)
# if response.status_code == 200:
#     print(json.dumps(json.loads(response.content), indent=2))
# else:
#     print("调用失败")
#     print(response.content)





if __name__ == "__main__":
    response
