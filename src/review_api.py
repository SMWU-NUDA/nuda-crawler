# -*- coding: utf-8 -*-

import json
import csv
import os

response_text = """
{
    "status": "SUCCESS",
    "code": 200,
    "message": "요청에 성공하였습니다.",
    "pagination": null,
    "data": [
        {
            "reviewId": 53581299,
            "content": "옛날 뻣뻣한 재질의 화이트 생각하면 안 돼요\r\n화이트 하면 흡수력인데 좋은느낌급의 부드러움까지 느낄 수 있어요\r\n착용감도 좋아요",
            "goodsDto": {
                "goodsNumber": "A000000160616",
                "itemNumber": "001",
                "legacyGoodsNumber": "8801166238762",
                "goodsName": "[흡수과학] 화이트 수퍼흡수 생리대 5종 택 1",
                "optionName": "수퍼흡수 중형 18P"
            },
            "reviewScore": 5,
            "hasPhoto": true,
            "isRepurchase": false,
            "isMonthUseReview": false,
            "isMonthOverReview": true,
            "reviewType": "NORMAL",
            "usefulPoint": 756.0,
            "photoReviewList": [
                {
                    "imageSequence": 1,
                    "imagePath": "2025/12/28/d91b1d6c60114989a865caf849957ad71766925069685.png"
                },
                {
                    "imageSequence": 2,
                    "imagePath": "2025/12/28/c9b99c2b54f849658e0aa12cfc79c7c51766925094674.png"
                },
                {
                    "imageSequence": 3,
                    "imagePath": "2025/12/28/40980c3f81024916974991dd9c8269301766925152713.png"
                }
            ],
            "profileDto": {
                "memberNickname": "우디기",
                "profileImageUrl": "2025/09/28/1759039026237.png",
                "isShutterbrity": false,
                "isTopReviewer": true,
                "reviewerRank": 840,
                "profileKey": "YlNVY1J6UE5SVkpJMzA2bFNkV29pdz09",
                "skinType": "A02",
                "skinTone": "B06",
                "skinTrouble": [
                    "C02",
                    "C08"
                ],
                "isSkinTypeMatched": false,
                "isSkinToneMatched": false
            },
            "createdDateTime": "2025.12.28",
            "recommendCount": 1,
            "isMyReview": false,
            "isRecommended": false
        },
        {
            "reviewId": 53422205,
            "content": "화이튜\r\n이거 너무 좋아요!\r\n항상 재구매 하고 있습니다 ♥️\r\n행사 많이 해주시면 좋겠어용♥️♥️",
            "goodsDto": {
                "goodsNumber": "A000000160616",
                "itemNumber": "001",
                "legacyGoodsNumber": "8801166238762",
                "goodsName": "[흡수과학] 화이트 수퍼흡수 생리대 5종 택 1",
                "optionName": "수퍼흡수 중형 18P"
            },
            "reviewScore": 5,
            "hasPhoto": true,
            "isRepurchase": false,
            "isMonthUseReview": false,
            "isMonthOverReview": false,
            "reviewType": "NORMAL",
            "usefulPoint": 396.0,
            "photoReviewList": [
                {
                    "imageSequence": 1,
                    "imagePath": "2025/12/24/5b86f6530e234434904dd83e09d351aa1766522925917.png"
                }
            ],
            "profileDto": {
                "memberNickname": "밤순희",
                "profileImageUrl": "2024/11/06/1730896723627.png",
                "isShutterbrity": false,
                "isTopReviewer": true,
                "reviewerRank": 622,
                "profileKey": "c3lXTWdpZEJlMjd5WHFHTUZNTmJMdz09",
                "skinType": "A03",
                "skinTone": "B02",
                "skinTrouble": [
                    "C04",
                    "C05"
                ],
                "isSkinTypeMatched": false,
                "isSkinToneMatched": false
            },
            "createdDateTime": "2025.12.24",
            "recommendCount": 3,
            "isMyReview": false,
            "isRecommended": false
        },
        {
            "reviewId": 52468682,
            "content": "1+1이라 부담없이 가성비 좋게 구매할 수 있어서 만족스러운 제품이에요 굿",
            "goodsDto": {
                "goodsNumber": "A000000160616",
                "itemNumber": "001",
                "legacyGoodsNumber": "8801166238762",
                "goodsName": "[흡수과학] 화이트 수퍼흡수 생리대 5종 택 1",
                "optionName": "수퍼흡수 중형 18P"
            },
            "reviewScore": 5,
            "hasPhoto": true,
            "isRepurchase": false,
            "isMonthUseReview": false,
            "isMonthOverReview": true,
            "reviewType": "NORMAL",
            "usefulPoint": 378.0,
            "photoReviewList": [
                {
                    "imageSequence": 1,
                    "imagePath": "2025/12/06/e5248fb578c5438f8c502fad322f08f11764982367168.png"
                },
                {
                    "imageSequence": 2,
                    "imagePath": "2025/12/06/7555b2429c6e4103b909c7e38b7a17ad1764982371593.png"
                },
                {
                    "imageSequence": 3,
                    "imagePath": "2025/12/06/a1ba65cea1f142c8bf8a761fb4f27fdb1764982375901.png"
                }
            ],
            "profileDto": {
                "memberNickname": "야호호호",
                "profileImageUrl": "2021/02/09/1612797248201.png",
                "isShutterbrity": false,
                "isTopReviewer": true,
                "reviewerRank": 415,
                "profileKey": "UEZHSnl5cHRodGNPOGcyZzA3V3A3dz09",
                "skinType": "A02",
                "skinTone": "B04",
                "skinTrouble": [
                    "C06",
                    "C07"
                ],
                "isSkinTypeMatched": false,
                "isSkinToneMatched": false
            },
            "createdDateTime": "2025.12.06",
            "recommendCount": 2,
            "isMyReview": false,
            "isRecommended": false
        },
        {
            "reviewId": 52468375,
            "content": "1+1이라 부담없이 가성비 좋게 구매할 수 있어서 만족스러운 제품이에요 굿",
            "goodsDto": {
                "goodsNumber": "A000000160616",
                "itemNumber": "001",
                "legacyGoodsNumber": "8801166238762",
                "goodsName": "[흡수과학] 화이트 수퍼흡수 생리대 5종 택 1",
                "optionName": "수퍼흡수 중형 18P"
            },
            "reviewScore": 5,
            "hasPhoto": true,
            "isRepurchase": false,
            "isMonthUseReview": false,
            "isMonthOverReview": true,
            "reviewType": "NORMAL",
            "usefulPoint": 378.0,
            "photoReviewList": [
                {
                    "imageSequence": 1,
                    "imagePath": "2025/12/06/f3ace509120146a7865c6893c90f9a831764981747112.png"
                },
                {
                    "imageSequence": 2,
                    "imagePath": "2025/12/06/a35c6beded854e3485a9d3bb670b07ca1764981751232.png"
                },
                {
                    "imageSequence": 3,
                    "imagePath": "2025/12/06/3c8fa5f9750f4a6f89dffc1334eff6181764981755029.png"
                }
            ],
            "profileDto": {
                "memberNickname": "야호호호",
                "profileImageUrl": "2021/02/09/1612797248201.png",
                "isShutterbrity": false,
                "isTopReviewer": true,
                "reviewerRank": 415,
                "profileKey": "UEZHSnl5cHRodGNPOGcyZzA3V3A3dz09",
                "skinType": "A02",
                "skinTone": "B04",
                "skinTrouble": [
                    "C06",
                    "C07"
                ],
                "isSkinTypeMatched": false,
                "isSkinToneMatched": false
            },
            "createdDateTime": "2025.12.06",
            "recommendCount": 2,
            "isMyReview": false,
            "isRecommended": false
        },
        {
            "reviewId": 54290283,
            "content": "생리대에서 저늠 흡수력을 제일 많이 보는데 이게 퇴고인 것 같습니다",
            "goodsDto": {
                "goodsNumber": "A000000160616",
                "itemNumber": "001",
                "legacyGoodsNumber": "8801166238762",
                "goodsName": "[흡수과학] 화이트 수퍼흡수 생리대 5종 택 1",
                "optionName": "수퍼흡수 중형 18P"
            },
            "reviewScore": 5,
            "hasPhoto": false,
            "isRepurchase": false,
            "isMonthUseReview": false,
            "isMonthOverReview": false,
            "reviewType": "NORMAL",
            "usefulPoint": 72.0,
            "photoReviewList": [],
            "profileDto": {
                "memberNickname": "토마텐",
                "profileImageUrl": "2023/03/05/1677994211433.png",
                "isShutterbrity": false,
                "isTopReviewer": false,
                "reviewerRank": null,
                "profileKey": "cnR0cnBxYmVKQ3U1djVQSHpNbE9tQT09",
                "skinType": null,
                "skinTone": null,
                "skinTrouble": [],
                "isSkinTypeMatched": false,
                "isSkinToneMatched": false
            },
            "createdDateTime": "2026.01.14",
            "recommendCount": 0,
            "isMyReview": false,
            "isRecommended": false
        },
        {
            "reviewId": 53366244,
            "content": "쓰던게 뭔가 편하니까\r\n그냥 이것만 쓰는중 \r\n쓰던게 뭔가 편하니까\r\n그냥 이것만 쓰는중",
            "goodsDto": {
                "goodsNumber": "A000000160616",
                "itemNumber": "001",
                "legacyGoodsNumber": "8801166238762",
                "goodsName": "[흡수과학] 화이트 수퍼흡수 생리대 5종 택 1",
                "optionName": "수퍼흡수 중형 18P"
            },
            "reviewScore": 5,
            "hasPhoto": false,
            "isRepurchase": true,
            "isMonthUseReview": false,
            "isMonthOverReview": false,
            "reviewType": "NORMAL",
            "usefulPoint": 36.0,
            "photoReviewList": [],
            "profileDto": {
                "memberNickname": "해무우",
                "profileImageUrl": "2023/01/02/1672609446985.png",
                "isShutterbrity": false,
                "isTopReviewer": false,
                "reviewerRank": null,
                "profileKey": "YXp3eFZjQWl1Yk8wZjMzZG1kSUcrUT09",
                "skinType": "A02",
                "skinTone": "B01",
                "skinTrouble": [],
                "isSkinTypeMatched": false,
                "isSkinToneMatched": false
            },
            "createdDateTime": "2025.12.22",
            "recommendCount": 0,
            "isMyReview": false,
            "isRecommended": false
        },
        {
            "reviewId": 34349709,
            "content": "요즘 진짜 여러 브랜드의 생리대가 쏟아져나오는데\r\n저는 돌고돌아 화이트입니다\r\n물론 학창시절에 쓰던 그 제품에 머물러있다면 아니었겠지만\r\n지금은 너무 스마트해졌어요\r\n\r\n‘수퍼흡수’ 라는 말이 과대광고가 아니더라고요\r\n양 많은날에 확- 쏟아져나와도 진짜 빨리 흡수돼서\r\n팬티옆라인 안쪽허벅지같은곳에 묻거나 하지않아요\r\n(뭔말인지 여성분들은 다 아실거여요…)\r\n샘방지라인도 확실하고\r\n무엇보다 패드 표면에 혈이 드러나있지않고\r\n아래쪽으로 흡수돼 들어가서\r\n일 바빠 화장실 자주 못갈때도 표면이 시뻘겋게 난리가난게아니라\r\n패드속 깊은곳에 혈이 다 흡수돼 들어가서\r\n안쪽은 분명 전부 젖었는데 겉은 티가 별로 안나는 상태?\r\n이건 뭐 사진으로 보여드리긴 어렵만.. 써보시면 알아요\r\n\r\n올영에 1+1 행사 자주해서 추가 가격할인까지 들어갈때 쟁입니다",
            "goodsDto": {
                "goodsNumber": "A000000160616",
                "itemNumber": "001",
                "legacyGoodsNumber": "8801166238762",
                "goodsName": "[흡수과학] 화이트 수퍼흡수 생리대 5종 택 1",
                "optionName": "수퍼흡수 중형 18P"
            },
            "reviewScore": 5,
            "hasPhoto": true,
            "isRepurchase": false,
            "isMonthUseReview": false,
            "isMonthOverReview": false,
            "reviewType": "NORMAL",
            "usefulPoint": 22.5,
            "photoReviewList": [
                {
                    "imageSequence": 1,
                    "imagePath": "2024/11/26/1e5e47a6d44b4c7e926479dfc662425a1732547368066.png"
                },
                {
                    "imageSequence": 2,
                    "imagePath": "2024/11/26/27a845d058c24fda8c224a52ce82d53f1732547373894.png"
                },
                {
                    "imageSequence": 3,
                    "imagePath": "2024/11/26/b9b12b66580142a6b2549e8db6502dea1732547378985.png"
                }
            ],
            "profileDto": {
                "memberNickname": "크림짱",
                "profileImageUrl": "2023/11/29/1701239813081.png",
                "isShutterbrity": false,
                "isTopReviewer": true,
                "reviewerRank": 761,
                "profileKey": "VTMwMWRpaUk2d01MVk1tRm9jUGZCQT09",
                "skinType": "A03",
                "skinTone": "B04",
                "skinTrouble": [
                    "C05",
                    "C09"
                ],
                "isSkinTypeMatched": false,
                "isSkinToneMatched": false
            },
            "createdDateTime": "2024.11.26",
            "recommendCount": 1,
            "isMyReview": false,
            "isRecommended": false
        },
        {
            "reviewId": 31142002,
            "content": "사무직이 아니고 현장직에서 일하는 사람이라\r\n필요시에 화장실을 바로바로 못가요ㅠ\r\n그래서 원랜 탐폰을 주로 쓰지만 \r\n바쁘고 양많은날엔 샐까봐 패드를 쓰기도하는데\r\n이 제품은 흡수가 빠르고 + 표면에 생리혈이 겉돌지않아 깔끔해요\r\n생리대 갈때 표면만 보면 어..? 아직 별로 안묻엇나? 싶지만\r\n뒤집어 부착면(바닥쪽)을 보면 흥건하게 흡수가된걸 볼수잇어요\r\n그만큼 표면에 안남고 싸악 흡수한단얘기\r\n이건 뭐 어떻게 후기 사진으로 보여줄수는 없지만\r\n써보세요 진짜 깔끔하고 흡수빠름",
            "goodsDto": {
                "goodsNumber": "A000000160616",
                "itemNumber": "001",
                "legacyGoodsNumber": "8801166238762",
                "goodsName": "[흡수과학] 화이트 수퍼흡수 생리대 5종 택 1",
                "optionName": "수퍼흡수 중형 18P"
            },
            "reviewScore": 5,
            "hasPhoto": true,
            "isRepurchase": false,
            "isMonthUseReview": false,
            "isMonthOverReview": true,
            "reviewType": "NORMAL",
            "usefulPoint": 22.5,
            "photoReviewList": [
                {
                    "imageSequence": 1,
                    "imagePath": "2024/08/17/1723820790101.png"
                },
                {
                    "imageSequence": 2,
                    "imagePath": "2024/08/17/1723820794486.png"
                },
                {
                    "imageSequence": 3,
                    "imagePath": "2024/08/17/1723820798779.png"
                }
            ],
            "profileDto": {
                "memberNickname": "크림짱",
                "profileImageUrl": "2023/11/29/1701239813081.png",
                "isShutterbrity": false,
                "isTopReviewer": true,
                "reviewerRank": 761,
                "profileKey": "VTMwMWRpaUk2d01MVk1tRm9jUGZCQT09",
                "skinType": "A03",
                "skinTone": "B01",
                "skinTrouble": [
                    "C05"
                ],
                "isSkinTypeMatched": false,
                "isSkinToneMatched": false
            },
            "createdDateTime": "2024.08.17",
            "recommendCount": 1,
            "isMyReview": false,
            "isRecommended": false
        },
        {
            "reviewId": 28541858,
            "content": "원터치로 편리하게 오픈가능합니다\r\n가쪽에 샘방지라인이 잘 잡혀있어서\r\n팬티에 붙일때 휨없이 바르게 잘 붙어요\r\n생리혈이 묻었을때 패드 안쪽으로 깊게 흡수돼서\r\n겉면에 최대한 덜묻도록 설계된 재질입니다\r\n편리하고 1+1도 자주해서\r\n다른패드생리대는 이제 못쓰겠어요",
            "goodsDto": {
                "goodsNumber": "A000000160616",
                "itemNumber": "001",
                "legacyGoodsNumber": "8801166238762",
                "goodsName": "[흡수과학] 화이트 수퍼흡수 생리대 5종 택 1",
                "optionName": "수퍼흡수 중형 18P"
            },
            "reviewScore": 5,
            "hasPhoto": true,
            "isRepurchase": false,
            "isMonthUseReview": false,
            "isMonthOverReview": false,
            "reviewType": "NORMAL",
            "usefulPoint": 22.5,
            "photoReviewList": [
                {
                    "imageSequence": 1,
                    "imagePath": "2024/05/30/1716994843812.png"
                },
                {
                    "imageSequence": 2,
                    "imagePath": "2024/05/30/1716994856364.png"
                },
                {
                    "imageSequence": 3,
                    "imagePath": "2024/05/30/1716994860011.png"
                }
            ],
            "profileDto": {
                "memberNickname": "크림짱",
                "profileImageUrl": "2023/11/29/1701239813081.png",
                "isShutterbrity": false,
                "isTopReviewer": true,
                "reviewerRank": 761,
                "profileKey": "VTMwMWRpaUk2d01MVk1tRm9jUGZCQT09",
                "skinType": "A03",
                "skinTone": "B01",
                "skinTrouble": [
                    "C05"
                ],
                "isSkinTypeMatched": false,
                "isSkinToneMatched": false
            },
            "createdDateTime": "2024.05.30",
            "recommendCount": 1,
            "isMyReview": false,
            "isRecommended": false
        },
        {
            "reviewId": 23586982,
            "content": "🤍 자극이 없어요!\r\n착용 시 피부에 트러블이나 가려움이 생긴 적은 없었어요.\r\n\r\n🤍 생리대 표면이 부드러워요.\r\n\r\n🩵 제품 이름처럼 흡수력이 높아요👍🏻\r\n흡수가 잘 되기 때문에 생리대가 덜 축축(?)하게 유지되고\r\n그래서 피부 자극도 덜해요🙃\r\n\r\n🩵 안정된 착용감이 느껴져요.\r\n\r\n🩵 속옷에 잘 부착되어서 움직이지 않아요.",
            "goodsDto": {
                "goodsNumber": "A000000160616",
                "itemNumber": "001",
                "legacyGoodsNumber": "8801166238762",
                "goodsName": "[흡수과학] 화이트 수퍼흡수 생리대 5종 택 1",
                "optionName": "수퍼흡수 중형 18P"
            },
            "reviewScore": 5,
            "hasPhoto": true,
            "isRepurchase": false,
            "isMonthUseReview": false,
            "isMonthOverReview": true,
            "reviewType": "NORMAL",
            "usefulPoint": 22.5,
            "photoReviewList": [
                {
                    "imageSequence": 1,
                    "imagePath": "2023/11/12/1699791220227.png"
                },
                {
                    "imageSequence": 2,
                    "imagePath": "2023/11/12/1699791224468.png"
                },
                {
                    "imageSequence": 3,
                    "imagePath": "2023/11/12/1699791228907.png"
                }
            ],
            "profileDto": {
                "memberNickname": "하늘바람별",
                "profileImageUrl": "2022/08/02/1659370129220.png",
                "isShutterbrity": false,
                "isTopReviewer": false,
                "reviewerRank": null,
                "profileKey": "VzR4SDJhYnhMQjFYNGZRZ3k2Q1NkZz09",
                "skinType": "A03",
                "skinTone": "B02",
                "skinTrouble": [
                    "C03",
                    "C05"
                ],
                "isSkinTypeMatched": false,
                "isSkinToneMatched": false
            },
            "createdDateTime": "2023.11.12",
            "recommendCount": 0,
            "isMyReview": false,
            "isRecommended": false
        },
        {
            "reviewId": 23119394,
            "content": "부드러운건 확실히 타브랜드의 순면 생리대들이 좋긴한데 가격도 가격이고... 때마침 새로운걸 써보고 싶어서 화이트 제품을 구매했어요.\r\n\r\n가격대비 무난하게 쓸거면 화이트 제품이 좋은것 같아요. 배송 빨리 왔길래..때마침 그날이기도 해서 1장 사용해봤거든요.\r\n\r\n수퍼흡수답게 양많아도 마음 놓고 사용하기 괜찮네요..저의 경우 중형이 필요해서 구매한거지만 대형도 구매해서 기존 제가 쓰던 생리대랑 섞어 쓸까해요. \r\n\r\n사용하면서 피부에 자극적이거나 딱히 불편한 점은 없었고 그냥 무난하게 쓰기 좋은 제품 같네요..",
            "goodsDto": {
                "goodsNumber": "A000000160616",
                "itemNumber": "001",
                "legacyGoodsNumber": "8801166238762",
                "goodsName": "[흡수과학] 화이트 수퍼흡수 생리대 5종 택 1",
                "optionName": "수퍼흡수 중형 18P"
            },
            "reviewScore": 5,
            "hasPhoto": true,
            "isRepurchase": false,
            "isMonthUseReview": false,
            "isMonthOverReview": false,
            "reviewType": "GIFT",
            "usefulPoint": 22.5,
            "photoReviewList": [
                {
                    "imageSequence": 1,
                    "imagePath": "2023/10/24/1698083892634.png"
                },
                {
                    "imageSequence": 2,
                    "imagePath": "2023/10/24/1698083895121.png"
                },
                {
                    "imageSequence": 3,
                    "imagePath": "2023/10/24/1698083898993.png"
                }
            ],
            "profileDto": {
                "memberNickname": "콩이맘맘",
                "profileImageUrl": "2023/12/10/1702219004055.png",
                "isShutterbrity": false,
                "isTopReviewer": false,
                "reviewerRank": null,
                "profileKey": "aFkwT0k0bm1uL2RZV2J0ZW5uS1pHZz09",
                "skinType": "A03",
                "skinTone": "B01",
                "skinTrouble": [
                    "C09"
                ],
                "isSkinTypeMatched": false,
                "isSkinToneMatched": false
            },
            "createdDateTime": "2023.10.24",
            "recommendCount": 2,
            "isMyReview": false,
            "isRecommended": false
        },
        {
            "reviewId": 22750763,
            "content": "🩵 흡수력이 좋다.\r\n🩵 표면이 부드럽다.\r\n🩵 접착력이 좋다.\r\n\r\n‘수퍼 흡수‘라는 이름처럼 흡수력이 좋은 생리대예요.\r\n빨리 흡수되는 편이고, 양 많은 날에도 넘치지 않았어요~~\r\n\r\n생리대 표면이 부드러워요!\r\n간지러움을 유발하거나 불편함을 유발하는 요소가 없어서 편하게 착용할 수 있어요.\r\n\r\n접착력이 좋아요.\r\n속옷에 잘 고정되어서 움직이지 않아서 안심히고 쓸 수 있어요😋",
            "goodsDto": {
                "goodsNumber": "A000000160616",
                "itemNumber": "001",
                "legacyGoodsNumber": "8801166238762",
                "goodsName": "[흡수과학] 화이트 수퍼흡수 생리대 5종 택 1",
                "optionName": "수퍼흡수 중형 18P"
            },
            "reviewScore": 5,
            "hasPhoto": true,
            "isRepurchase": false,
            "isMonthUseReview": false,
            "isMonthOverReview": false,
            "reviewType": "NORMAL",
            "usefulPoint": 22.5,
            "photoReviewList": [
                {
                    "imageSequence": 1,
                    "imagePath": "2023/10/06/1696589985063.png"
                },
                {
                    "imageSequence": 2,
                    "imagePath": "2023/10/06/1696589988509.png"
                },
                {
                    "imageSequence": 3,
                    "imagePath": "2023/10/06/1696589992069.png"
                }
            ],
            "profileDto": {
                "memberNickname": "하늘바람별",
                "profileImageUrl": "2022/08/02/1659370129220.png",
                "isShutterbrity": false,
                "isTopReviewer": false,
                "reviewerRank": null,
                "profileKey": "VzR4SDJhYnhMQjFYNGZRZ3k2Q1NkZz09",
                "skinType": "A03",
                "skinTone": "B02",
                "skinTrouble": [
                    "C05",
                    "C06"
                ],
                "isSkinTypeMatched": false,
                "isSkinToneMatched": false
            },
            "createdDateTime": "2023.10.06",
            "recommendCount": 0,
            "isMyReview": false,
            "isRecommended": false
        },
        {
            "reviewId": 22515540,
            "content": "이젠 생리대도 기능을 보고 선택합니다.\r\n더워지기 전엔 뽀송하게 잘썼던 생리대들도 괜시리 땀이 많아지는 계절이면 더 민감하게 느껴지고, 만족감이 떨어지기도하고 그러네요.\r\n이렇게 얇은 제품들은 추운계절보다는 확실히 여름에 쓰기 좋네요.\r\n전 출산후 거의20년이상 생리량이나 혈의 점성정도가 매우 규칙적이고 예측가능하게 거의 정해진 패턴대로 진행이되어 크게 제품을 가리지 않아도 깔끔하게 딱 4일이면 끝났었는데, 2-3개월전부터 갑자기 생리 패턴이 바뀌어 너무 힘드네요.\r\n상담받아보니 &#039;노화&#039; 의 과정이라는데ㅠㅠ\r\n생리량도 전혀예측불가고 갑자기 시작되기도하고..\r\n그래서 이제품을 가방이나 차에 가볍게 꼭 지니고다닙니다.\r\n그러다보니 저도좋지만 딸들이 급히 필요할때도 더 챙겨주게 되더라구요.\r\n사이즈도 팬티라이너보다 안정적이라 한창때인 아이들에게 반응이 아주 좋습니다.\r\n계절도 계절이지만 비치용으로는 이제품이 라이너보다 더 좋은것같아요!",
            "goodsDto": {
                "goodsNumber": "A000000160616",
                "itemNumber": "001",
                "legacyGoodsNumber": "8801166238762",
                "goodsName": "[흡수과학] 화이트 수퍼흡수 생리대 5종 택 1",
                "optionName": "수퍼흡수 중형 18P"
            },
            "reviewScore": 5,
            "hasPhoto": true,
            "isRepurchase": true,
            "isMonthUseReview": false,
            "isMonthOverReview": true,
            "reviewType": "NORMAL",
            "usefulPoint": 22.5,
            "photoReviewList": [
                {
                    "imageSequence": 1,
                    "imagePath": "2023/09/25/1695651264020.png"
                },
                {
                    "imageSequence": 2,
                    "imagePath": "2023/09/25/1695651283561.png"
                },
                {
                    "imageSequence": 3,
                    "imagePath": "2023/09/25/1695651293188.png"
                }
            ],
            "profileDto": {
                "memberNickname": "진리빛",
                "profileImageUrl": "2022/08/14/1660442702309.png",
                "isShutterbrity": false,
                "isTopReviewer": false,
                "reviewerRank": null,
                "profileKey": "ZUliNUdQVFdFMnV4VS96YVFvaTBBUT09",
                "skinType": "A02",
                "skinTone": "B03",
                "skinTrouble": [
                    "C01",
                    "C03"
                ],
                "isSkinTypeMatched": false,
                "isSkinToneMatched": false
            },
            "createdDateTime": "2023.09.25",
            "recommendCount": 0,
            "isMyReview": false,
            "isRecommended": false
        },
        {
            "reviewId": 21453313,
            "content": "여름이니 당연히 생리대에 좀더 민감해지는것 같아요.\r\n더워지기 전엔 뽀송하게 잘썼던 생리대들도 괜시리 땀이 많아지는 계절이면 더 민감하게 느껴지고, 만족감이 떨어지기도하고 그러네요.\r\n이렇게 얇은 제품들은 추운계절보다는 확실히 여름에 쓰기 좋네요.\r\n전 출산후 거의20년이상 생리량이나 혈의 점성정도가 매우 규칙적이고 예측가능하게 거의 정해진 패턴대로 진행이되어 크게 제품을 가리지 않아도 깔끔하게 딱 4일이면 끝났었는데, 2-3개월전부터 갑자기 생리 패턴이 바뀌어 너무 힘드네요.\r\n상담받아보니 &#039;노화&#039; 의 과정이라는데ㅠㅠ\r\n생리량도 전혀예측불가고 갑자기 시작되기도하고..\r\n그래서 이제품을 가방이나 차에 가볍게 꼭 지니고다닙니다.\r\n그러다보니 저도좋지만 딸들이 급히 필요할때도 더 챙겨주게 되더라구요.\r\n사이즈도 팬티라이너보다 안정적이라 한창때인 아이들에게 반응이 아주 좋습니다.\r\n계절도 계절이지만 비치용으로는 이제품이 라이너보다 더 좋은것같아요!\r\n처음 사진은 소형과 중형 비교사이즈입니다!",
            "goodsDto": {
                "goodsNumber": "A000000160616",
                "itemNumber": "001",
                "legacyGoodsNumber": "8801166238762",
                "goodsName": "[흡수과학] 화이트 수퍼흡수 생리대 5종 택 1",
                "optionName": "수퍼흡수 중형 18P"
            },
            "reviewScore": 5,
            "hasPhoto": true,
            "isRepurchase": false,
            "isMonthUseReview": false,
            "isMonthOverReview": true,
            "reviewType": "NORMAL",
            "usefulPoint": 22.5,
            "photoReviewList": [
                {
                    "imageSequence": 1,
                    "imagePath": "2023/08/12/1691827437848.png"
                },
                {
                    "imageSequence": 2,
                    "imagePath": "2023/08/12/1691827705160.png"
                },
                {
                    "imageSequence": 3,
                    "imagePath": "2023/08/12/1691827718546.png"
                }
            ],
            "profileDto": {
                "memberNickname": "진리빛",
                "profileImageUrl": "2022/08/14/1660442702309.png",
                "isShutterbrity": false,
                "isTopReviewer": false,
                "reviewerRank": null,
                "profileKey": "ZUliNUdQVFdFMnV4VS96YVFvaTBBUT09",
                "skinType": "A02",
                "skinTone": "B03",
                "skinTrouble": [
                    "C01",
                    "C03"
                ],
                "isSkinTypeMatched": false,
                "isSkinToneMatched": false
            },
            "createdDateTime": "2023.08.12",
            "recommendCount": 0,
            "isMyReview": false,
            "isRecommended": false
        },
        {
            "reviewId": 20187812,
            "content": "더운계절에 여성들에게 필수품이네요.                         \r\n수퍼흡수 생리대를 처음 써보며 느낀건데, 운동하는분들이나 오래앉아 공부하는 학생들에게는 꼭 필요한것같아요.\r\n저는 주로격한운동을 하는지라 생리량이 많은날엔 그냥 두꺼워도 안전한생리대를 착용하고 화장실을 자주가며 운동했었는데, 꼭 더운여름이 아니라도 두꺼운생리대는 땀에 아주 취약했어요.\r\n물론 피부에도 좋지않죠. 차라리 운동을 안하는편이..\r\n이번에 딸들의 요구로 이제품 구매해주며 저도 한번 사용해보았는데 신세계 그자체였습니다.\r\n얇으니 활동성도 좋고 빠르게흡수되니 찝찝함도 훨씬덜하구요.\r\n42센티 오버나이트 생리대도 그랬듯이 이제품도 알지못하면 쓰지 못하는제품인것같아요.\r\n올리브영에선 다른사이트와는달리 리뷰제도가좋아서 리뷰믿고 구매해서 쓰는 제품이 많은지라 리뷰를 길게쓰든 짧게쓰든 솔직하게 쓰게되니 좋은것같아요.\r\n이런 상호작용이 깨지지 않았으면 좋겠어요!",
            "goodsDto": {
                "goodsNumber": "A000000160616",
                "itemNumber": "001",
                "legacyGoodsNumber": "8801166238762",
                "goodsName": "[흡수과학] 화이트 수퍼흡수 생리대 5종 택 1",
                "optionName": "수퍼흡수 중형 18P"
            },
            "reviewScore": 5,
            "hasPhoto": true,
            "isRepurchase": true,
            "isMonthUseReview": false,
            "isMonthOverReview": false,
            "reviewType": "NORMAL",
            "usefulPoint": 22.5,
            "photoReviewList": [
                {
                    "imageSequence": 1,
                    "imagePath": "2023/06/13/1686625178463.png"
                },
                {
                    "imageSequence": 2,
                    "imagePath": "2023/06/13/1686625202523.png"
                },
                {
                    "imageSequence": 3,
                    "imagePath": "2023/06/13/1686625209994.png"
                }
            ],
            "profileDto": {
                "memberNickname": "진리빛",
                "profileImageUrl": "2022/08/14/1660442702309.png",
                "isShutterbrity": false,
                "isTopReviewer": false,
                "reviewerRank": null,
                "profileKey": "ZUliNUdQVFdFMnV4VS96YVFvaTBBUT09",
                "skinType": "A02",
                "skinTone": "B03",
                "skinTrouble": [
                    "C01",
                    "C03"
                ],
                "isSkinTypeMatched": false,
                "isSkinToneMatched": false
            },
            "createdDateTime": "2023.06.13",
            "recommendCount": 1,
            "isMyReview": false,
            "isRecommended": false
        },
        {
            "reviewId": 19976545,
            "content": "화이트 수퍼흡수는 아이들만 사줬던지라 저는 이번에 처음 써봤습니다.\r\n운동할때 생리대가 두께가있으면 중간중간 화장실로 뛰쳐가야하는 불상사가 있거든요ㅋㅋ\r\n다른생리대보다 얇고 흡수가 빠르긴합니다.\r\n그런데 그런 장점이 있는반면, 순면제품들만 쓰다가 써서인지는 모르겠는데 마냥 보드럽지는 않았어요.\r\n이제품은 운동시나 아이들 여름에 등교할때 사용하시기를 추천해요!",
            "goodsDto": {
                "goodsNumber": "A000000160616",
                "itemNumber": "001",
                "legacyGoodsNumber": "8801166238762",
                "goodsName": "[흡수과학] 화이트 수퍼흡수 생리대 5종 택 1",
                "optionName": "수퍼흡수 중형 18P"
            },
            "reviewScore": 4,
            "hasPhoto": true,
            "isRepurchase": false,
            "isMonthUseReview": false,
            "isMonthOverReview": false,
            "reviewType": "NORMAL",
            "usefulPoint": 22.5,
            "photoReviewList": [
                {
                    "imageSequence": 1,
                    "imagePath": "2023/06/05/1685959357615.png"
                },
                {
                    "imageSequence": 2,
                    "imagePath": "2023/06/05/1685959369589.png"
                },
                {
                    "imageSequence": 3,
                    "imagePath": "2023/06/05/1685959375849.png"
                }
            ],
            "profileDto": {
                "memberNickname": "진리빛",
                "profileImageUrl": "2022/08/14/1660442702309.png",
                "isShutterbrity": false,
                "isTopReviewer": false,
                "reviewerRank": null,
                "profileKey": "ZUliNUdQVFdFMnV4VS96YVFvaTBBUT09",
                "skinType": "A02",
                "skinTone": "B03",
                "skinTrouble": [
                    "C01",
                    "C03"
                ],
                "isSkinTypeMatched": false,
                "isSkinToneMatched": false
            },
            "createdDateTime": "2023.06.05",
            "recommendCount": 0,
            "isMyReview": false,
            "isRecommended": false
        },
        {
            "reviewId": 12335577,
            "content": "오랜만에 화이트에서  새로운 제품이 나왔길래\r\n호기심에 구매하게 되었어요\r\n거기다 1+1 행사도 해서 합리적인 가격에 좋은 제품을\r\n사용할수 있어서 좋았어요\r\n원래 피부가 민감해서 생리대 고를때 여러가지\r\n따져보고 고르는 편인데 이 제품은 대체적으로\r\n만족스러웠어요\r\n무엇보다 피부에 닿는면이  넘 부드러워서 좋았고\r\n순한 성분의 패드여서 그런지 피부에 자극이나 트러블이 전혀\r\n없어서 맘에 들었어요\r\n또 패드 두께가 적당해서 착용했을때 편안한 느낌이 들었어요\r\n특히 다른 브랜드 제품과 비교했을때\r\n패드의 접착력도 좋았고 정말 슈퍼흡수력인듯\r\n오랜시간 착용해도 샐 걱정없이 안심이 되더라요\r\n역시 화이트 브랜드 제품은 믿고 사용할수 있는것 같아요\r\n다음번엔 다른 사이즈의 제품도 사용해 보고 싶어지네요\r\n앞으로도 자주 할인행사 했으면 좋겠어요",
            "goodsDto": {
                "goodsNumber": "A000000160616",
                "itemNumber": "001",
                "legacyGoodsNumber": "8801166238762",
                "goodsName": "[흡수과학] 화이트 수퍼흡수 생리대 5종 택 1",
                "optionName": "수퍼흡수 중형 18P"
            },
            "reviewScore": 5,
            "hasPhoto": true,
            "isRepurchase": false,
            "isMonthUseReview": true,
            "isMonthOverReview": false,
            "reviewType": "NORMAL",
            "usefulPoint": 22.5,
            "photoReviewList": [
                {
                    "imageSequence": 1,
                    "imagePath": "2022/03/04/1646369763013.png"
                },
                {
                    "imageSequence": 2,
                    "imagePath": "2022/03/04/1646369880612.png"
                },
                {
                    "imageSequence": 3,
                    "imagePath": "2022/03/04/1646369894786.png"
                }
            ],
            "profileDto": {
                "memberNickname": "지니에니",
                "profileImageUrl": "2023/01/02/1672587548918.png",
                "isShutterbrity": false,
                "isTopReviewer": false,
                "reviewerRank": null,
                "profileKey": "bjZjSTdPMGt3aW5GSGtrSXVPY1pwUT09",
                "skinType": "A03",
                "skinTone": "B01",
                "skinTrouble": [
                    "C10",
                    "C13"
                ],
                "isSkinTypeMatched": false,
                "isSkinToneMatched": false
            },
            "createdDateTime": "2022.03.04",
            "recommendCount": 1,
            "isMyReview": false,
            "isRecommended": false
        },
        {
            "reviewId": 52974663,
            "content": "화이트 수퍼흡수 좋아요\r\n불편함이없고 부드러워서 마찰도없음\r\n흡수가 잘되서 생활하기편해요 굿",
            "goodsDto": {
                "goodsNumber": "A000000160616",
                "itemNumber": "001",
                "legacyGoodsNumber": "8801166238762",
                "goodsName": "[흡수과학] 화이트 수퍼흡수 생리대 5종 택 1",
                "optionName": "수퍼흡수 중형 18P"
            },
            "reviewScore": 5,
            "hasPhoto": true,
            "isRepurchase": false,
            "isMonthUseReview": false,
            "isMonthOverReview": false,
            "reviewType": "NORMAL",
            "usefulPoint": 22.0,
            "photoReviewList": [
                {
                    "imageSequence": 1,
                    "imagePath": "2025/12/12/98149949f3824a0eaea521986c479f081765510588322.png"
                }
            ],
            "profileDto": {
                "memberNickname": "hu0****",
                "profileImageUrl": null,
                "isShutterbrity": false,
                "isTopReviewer": false,
                "reviewerRank": null,
                "profileKey": "VXNUa2NMcElVOXV6R0NRa1pDZjFEdz09",
                "skinType": null,
                "skinTone": null,
                "skinTrouble": [],
                "isSkinTypeMatched": false,
                "isSkinToneMatched": false
            },
            "createdDateTime": "2025.12.12",
            "recommendCount": 0,
            "isMyReview": false,
            "isRecommended": false
        },
        {
            "reviewId": 51051932,
            "content": "1+1이라 부담없이 가성비 좋게 구매할 수 있어서 만족스러운 제품이에요 굿",
            "goodsDto": {
                "goodsNumber": "A000000160616",
                "itemNumber": "001",
                "legacyGoodsNumber": "8801166238762",
                "goodsName": "[흡수과학] 화이트 수퍼흡수 생리대 5종 택 1",
                "optionName": "수퍼흡수 중형 18P"
            },
            "reviewScore": 5,
            "hasPhoto": true,
            "isRepurchase": false,
            "isMonthUseReview": false,
            "isMonthOverReview": false,
            "reviewType": "NORMAL",
            "usefulPoint": 18.9,
            "photoReviewList": [
                {
                    "imageSequence": 1,
                    "imagePath": "2025/11/06/cd5dfd8266224f8b82f4de66cfc365b91762413350024.png"
                },
                {
                    "imageSequence": 2,
                    "imagePath": "2025/11/06/9c0384a9b1af4ed7aaa2cdf903cf43c81762413355610.png"
                },
                {
                    "imageSequence": 3,
                    "imagePath": "2025/11/06/7003125145f14a9a8920d0743cc810191762413359991.png"
                }
            ],
            "profileDto": {
                "memberNickname": "야호호호",
                "profileImageUrl": "2021/02/09/1612797248201.png",
                "isShutterbrity": false,
                "isTopReviewer": true,
                "reviewerRank": 415,
                "profileKey": "UEZHSnl5cHRodGNPOGcyZzA3V3A3dz09",
                "skinType": "A02",
                "skinTone": "B04",
                "skinTrouble": [
                    "C06",
                    "C07"
                ],
                "isSkinTypeMatched": false,
                "isSkinToneMatched": false
            },
            "createdDateTime": "2025.11.06",
            "recommendCount": 2,
            "isMyReview": false,
            "isRecommended": false
        },
        {
            "reviewId": 51051755,
            "content": "1+1이라 부담없이 가성비 좋게 구매할 수 있어서 만족스러운 제품이에요 굿",
            "goodsDto": {
                "goodsNumber": "A000000160616",
                "itemNumber": "001",
                "legacyGoodsNumber": "8801166238762",
                "goodsName": "[흡수과학] 화이트 수퍼흡수 생리대 5종 택 1",
                "optionName": "수퍼흡수 중형 18P"
            },
            "reviewScore": 5,
            "hasPhoto": true,
            "isRepurchase": false,
            "isMonthUseReview": false,
            "isMonthOverReview": false,
            "reviewType": "NORMAL",
            "usefulPoint": 18.9,
            "photoReviewList": [
                {
                    "imageSequence": 1,
                    "imagePath": "2025/11/06/aaaaabb6833741b18797345e08e83dd91762412899526.png"
                },
                {
                    "imageSequence": 2,
                    "imagePath": "2025/11/06/6754964ca4bb40839d00d6f35d7b77a11762412903657.png"
                },
                {
                    "imageSequence": 3,
                    "imagePath": "2025/11/06/1630da042c82428791acc7e2da76a8031762412912035.png"
                }
            ],
            "profileDto": {
                "memberNickname": "야호호호",
                "profileImageUrl": "2021/02/09/1612797248201.png",
                "isShutterbrity": false,
                "isTopReviewer": true,
                "reviewerRank": 415,
                "profileKey": "UEZHSnl5cHRodGNPOGcyZzA3V3A3dz09",
                "skinType": "A02",
                "skinTone": "B04",
                "skinTrouble": [
                    "C06",
                    "C07"
                ],
                "isSkinTypeMatched": false,
                "isSkinToneMatched": false
            },
            "createdDateTime": "2025.11.06",
            "recommendCount": 2,
            "isMyReview": false,
            "isRecommended": false
        }
    ],
    "totalCnt": null,
    "pageData": null
}
"""

response = json.loads(response_text,strict=False)
data = response["data"]

goodsNumber = data[0]["goodsDto"]["goodsNumber"]
option_name = data[0]["goodsDto"]["optionName"]
reviewScore = data[0]["reviewScore"]
contents = [review.get("content") for review in data]

file_path = "reviews.csv"
file_exists = os.path.isfile(file_path)

added_count = 0

with open(file_path, mode="a", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)

    if not file_exists:
        writer.writerow(["product_id", "group_name", "review_content","review_score"])

    for content in contents:
        if not content or not content.strip():
            continue
        writer.writerow([
            goodsNumber,
            option_name,
            content.strip(),
            reviewScore,
        ])
        added_count += 1

print(f"이번 실행으로 추가된 리뷰 수: {added_count}")
