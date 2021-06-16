# encoding: utf-8
import requests, json
import uuid

url = "http://10.169.130.249/httpInvoke/saas/invoke"


def randomUUID():
    return str(uuid.uuid4())


settleParam = [{
    "userPin": "jdpos",
    "orderSouceType": 51,
    "storeId": 282079,
    "addressParam": {
        "addressId": -1,
        "name": "测试",
        "log": "116.399975",
        "lat": "39.899202",
        "mobileEnc": "a-gjvauHtRMa5b5PTC9sUOEg\u003d\u003d",
        "mobile": "155*****031",
        "addressDesc": "测试地址",
        "addressSummary": "",
        "provinceId": 110000,
        "provinceName": "北京市",
        "cityId": 110100,
        "cityName": "市辖区",
        "districtId": 110101,
        "districtName": "东城区"
    },
    "invoiceParam": {
        "isNeedInvoice": 0
    },
    "orderParam": {
        "payType": 2,
        "freight": 0,
        "isPack": False,
        "isUseBalance": False,
        "isAutoDeduction": False,
        "correction": 0,
        "userIdentity": {
            "name": "测试",
            "identificationNoEnc": "oliylfBvk8nj3Gy-buVXz-Qw",
            "identificationNoMask": "46**************14",
            "certificateType": 1
        },
        "freeTaxSign": 1,
    },
    "shipmentParam": {
        "deliveryType": 2,
        "supportSelf": "true",
        "deliveryTimeStyleEnum": "IRREGULAR"
    },
    "outOfStockStrategy": 0,
    "skuInfoList": [
        {
            "skuUuid": "3fc389bd-3d03-4660-b3d9-ead0c0561da8",
            "skuId": 102516962,
            "skuNum": 1,
            "services": [

            ],
            "isVirtualSuit": False,
            "isAddMoneyBuy": False,
            "isJDBuy": False,
            "isGift": False,
            "isFast": False,
            "isPiece": False,
            "isBox": False,
            "paid": False,
            "isXSuit": False,
            "haveInstallService": False,
            "selectInstallService": False
        }
    ],
    "isCheckPrice": 0,
    "platformTypeEnum": "POS",
    "platformId": 10017,
    "switchStore": False,
    "paidMember": False,
    "calPackagingFee": False,
}, ]


def submit():
    settleParam[0]["orderGuid"] = randomUUID()

    clientInfo = {
        "ip": "182.138.181.11",
        "appVersion": "3.2.42009290450",
        "deviceFingerprintingId": "eidI05678122c0s8RrUAUBtgTYm5UW1nf3WmRka1Ab2byvsgtT/anbdjmMWP0DQr1mx893JnNxcx4l+8FsW3f6lsdxpLIkJhnS/k1JRjKprr9snTD+BR",
        "deviceId": "UE6J4SJrybMujMGsozjihc7ydf",
        "imei": "UE6J4SJrybMujMGsozjihc7ydf",
        "wifiIp": "111.202.148.49",
        "deviceModel": "iPhone11,2",
        "imei": "2961e0205594421c9e092917d60fe3c7",
        "osystem": "13.6",
        "posParam": {
            "posParam": {
                "casher": "SelfCheckout",
                "posNum": "131215-Z04",
                "posTypeEnum": "SELF",
                "tranasDate": "2021-06-11",
                "tranasDocNo": "1de0dfb0-b76d-4b1c-b3a1-b74c4e611790"
            }
        },
    }

    params = {
        "service": "spring.commonSettlementFacadeSaasImpl",
        "method": "submitOrder",
        "methodId": "0",
        "pwd": "38bced94a36a4fede2ad28eeea5a87c0",
        "jsonData": json.dumps([1, settleParam, clientInfo, None]),
    }

    c = requests.get(url, params=params)
    print(c.text)


if __name__ == "__main__":
    submit()
