#!/usr/bin/env python
#-- coding: utf-8 --
"""
测试接口demo

"""

import unittest
import requests
import json

session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
url = 'https://aijuhr.com/hrm/account/login.do'
data = {
    'account': '18368180275',
    'password': 'jingqi123'
}
response = session.post(url, data=data, headers=headers)
class TestHandler(unittest.TestCase):

    def test_activities_list(self):
        """查询后动列表接口，调用接口weRecruitActivity/getWeActivities"""
        url = 'https://aijuhr.com/hrm/api.do'
        data = {
            'method': 'weRecruitActivity/getWeActivities',
            'param': '{}',
            'sign': 'a3b287cf19b841ed72351f2735407c1c'
        }
        response = session.post(url, data=data, headers=headers)
        data = json.loads(response.text)
        self.assertEqual(data['message'], '操作成功')


    #跳过，不执行这个case
    @unittest.skip
    def test_website(self):
        """微官网查询接口，调用接口companyWeb/getCompanyDetail"""
        url = 'https://aijuhr.com/hrm/api.do'
        data = {
            'method': 'companyWeb/getCompanyDetail',
            'param': '{}',
            'sign': '6a1668c253659aed326d9c97f4a8a692'
        }
        response = session.post(url, data=data, headers=headers)
        data = json.loads(response.text)
        self.assertEqual(data['message'], '操作成功')

    def test_recruitment_website(self):

        """测试招聘官网查询接口，接口名称：miniRecruit/getWzpIndexInfo"""
        url = 'https://aijuhr.com/hrm/api.do'
        data = {
            'method': 'miniRecruit/getWzpIndexInfo',
            'param': '{}',
            'sign': '2d95d2f38c876d7a79efa4c6c539542d'
        }
        response = session.post(url, data=data, headers=headers)
        data = json.loads(response.text)
        self.assertEqual(data['message'], '操作成功')

    def test_made_activate(self):
        """测试创建活动接口，接口名称：weRecruitActivity/createWeActivity"""
        url = 'https://aijuhr.com/hrm/api.do'
        data = {
            'method': 'weRecruitActivity/createWeActivity',
            'param': '{"template":"1","activityType":"1","theme":"test","pageTitle":"test",\
            "activityPhone":"15225675560","thumbUrl":"https://aijuhr.com/images/yidong/h5.png",\
            "activityImgUrl":"https://aijuhr.com/images/yidong/h5.png","positionIds":"402,401,282,299,281,280",\
            "titleDescription":"test","companyAddress":"test","activityEmail":"2362712780@qq.com",\
            "companyDescription":"春风轻轻地吹过南国大地，树儿长出绿叶，花儿竞相绽放，湖水泛起波纹，天空蓝蓝，白云飘飘，阳光明媚，\洒向人间，整个世界和暖而明亮。\n\n　　冬日的南国，不时落下潇潇冷雨，冬风吹过，一阵寒冷迎面扑来。那些行色匆匆的女子，也不禁裹紧外套。冬日不是不好，景色也很美，冰条挂满枝头，全世界耀眼的白。\n\n　　雨，随风潜入夜，润物细无声。而我觉得，春风是有生命的，一滴、两滴，轻轻地落在叶子上，让叶子散发出翠绿的光泽。春雨，轻吻花朵，让花儿更加美艳。春雨用它的指尖在湖面作画，在女子心里作诗。\n\n　　春日时光，是一段暖洋洋的日子。阳光，在对我们微笑，我们伸出双手，让光线穿透指尖，来一场温暖的对话。\n\n　　春天里，芒果花耀眼的开着，一朵朵，一簇簇，微笑着点缀着枝头。紫荆花也开得如火如荼，像一束束紫色的火焰，燃烧着妩媚与辉煌。\n\n　　春天，是我最喜欢的季节，柳绿花红，充满色彩，一切都那么生机勃勃。走在长长的林荫道上，抬头望望天，不禁向着阳光微笑。\n\n　　春风是四季最温柔的风。当我在烟雨中，穿着紫色的长裙，踏着高跟鞋，风轻轻吹起我的秀发，仿佛我深爱的你为我温柔地梳着头发。\n\n　　春天里，那一望无际的浅蓝，像你宽广的胸怀，让我依靠，让我撒娇，让我在滚滚红尘里找到可以依靠的怀抱。\n\n　　春雨里，我若如一朵粉色的桃花，尽管我没有倾城的容貌，没有寒梅的坚强，没有夏竹的高雅，没有秋菊的多姿，可我的心是粉红的，在你的怀抱里温柔舞蹈，只有在你的泪水里，我看见你对我的千倍怜爱，万般地疼惜。\n\n　　春天，是踏青的季节。我与你在水云间度过欢乐、美好的日子。年轻的心飞扬，你是风儿，我是沙，缠缠绵绵走天涯。我们种下桃花，你与我定下三生三世的誓言，只有天地和，才敢与君绝。蒲草韧如丝，磐石无转移。\n\n　　春天，是属于恋爱的季节。水云间好山好水好风光。与云为友，与花为怑，享受着明媚的春光，在珠帘般的春雨里吟诗作画，在春风细雨里编织美好的未来。\n\n　　爱在春色深深处。大胆去爱吧，这是个自由的年代；深情去爱吧，不要辜负了这美好的季节，这美丽动人的风景，不要错过了如此美好的时光。\n\n　　爱在春色深深处。天上人间几回闻？我们的青春应该用热忱洋溢、不忘初心来形容。爱着风、爱着雨、爱着阳光、爱着春花、爱着蓝天，彼此不离不弃，为爱付出，让我们高唱春天的歌曲，手牵手，踏遍天涯，访编春天，歌遍云和月。","companyImageUrl":"http://121.199.182.2/hrm/upload/Upload1522133746682.png","companyImageId":"14643"}',
            'sign': 'e9722db773ef43a436ef33b8c9c6c9fa'

        }
        response = session.post(url,data=data,headers=headers)
        data = json.loads(response.text)
        self.assertEqual(data['message'], '签名错误')

    def test_search_Recruitment_website(self):
        """测试候选人搜索接口，接口名称：queryResume/queryNewOrSpareRepo"""
        url = 'https://aijuhr.com/hrm/api.do'
        data = {
            'method': 'queryResume/queryNewOrSpareRepo',
            'param': '{"processStatus":1,"pageNum":3,"pageSize":10,"parameter":{"sex":"","resumeStatus":"","resumeFrom":"","interviewTimeType":"","educationLev":"","workYearHigh":"","workYearLow":""},"keyWord":"威威"}',
            'sign': '88e1483030cda89f4cb34726aa7934a7',
        }
        response = session.post(url,data=data,headers=headers)
        data = json.loads(response.text)
        self.assertEqual(data['message'],'操作成功')

    def test_position_list(self):
        """测试活动列表接口，接口名称：recruitPosition/getPositionCategoryList"""
        url = 'https://aijuhr.com/hrm/api.do'
        data = {
            'method': 'recruitPosition/getPositionCategoryList',
            'param': '{}',
            'sign': 'c5062121783365fb3d4333841e623848',
        }
        response = session.post(url, data=data, headers=headers)
        data = json.loads(response.text)
        self.assertEqual(data['message'],'操作成功')

    def test_weixin_configuration(self):
        """查看微信配置，接口名称：user/getUser"""
        url = 'https://aijuhr.com/hrm/api.do'
        data = {
            'method': 'user/getUser',
            'param': '{}',
            'sign': '9fce5ca27bfbe70c0d2ca639fc298c0c',
        }
        response = session.post(url, data=data, headers=headers)
        data = json.loads(response.text)
        php_token = data['data']['php_token']
        url = 'https://dev.aijuhr.com/api/menu/lists.json?token={}'.format(php_token)
        data = {
            'token': php_token
        }
        response = session.post(url, data=data, headers=headers)
        data = json.loads(response.text)
        self.assertEqual(data['data'][0]['name'], '微信配置')

    def test_interview_api(self):
        """测试查询面试库接口，接口名称：interviewer/getHireBeforeCount"""
        url = 'https://aijuhr.com/hrm/api.do'
        data = {
            'method': 'interviewer/getHireBeforeCount',
            'param': '{"resumeFrom":"","workYearLowest":"","workYearhighest":"","educationLev":"","postTime":"","character":""}',
            'sign': 'adcab696f1c2c1a8a461c6cdf95d7d1f'
        }
        response = session.post(url,data=data,headers=headers)
        data = json.loads(response.text)
        self.assertEqual(data['message'],'操作成功')

    def test_position_list_api(self):
        """职位列表信息接口，接口名称：recruitPosition/getPositionCategoryList"""
        url = 'https://aijuhr.com/hrm/api.do'
        data = {
            'method': 'recruitPosition/getPositionCategoryList',
            'param': '{}',
            'sign': 'c5062121783365fb3d4333841e623848',
        }
        response = session.post(url, data=data, headers=headers)
        data = json.loads(response.text)
        self.assertEqual(data['message'],'操作成功')

    def test_search_position_list_api(self):
        """查询职位列表信息接口，接口名称：recruitPosition/getPositionListByCondition"""
        url = 'https://aijuhr.com/hrm/api.do'
        data = {
            'method': 'recruitPosition/getPositionListByCondition',
            'param': '{"pageSize":10,"pageNum":1,"positionName":"测试","creatorName":"","categoryId":"","workCity":"","isUrgent":"","rewardAmount":""}',
            'sign': 'ce39df5e64b8285c7ffe3248ace3129d',
        }
        response = session.post(url, data=data, headers=headers)
        data = json.loads(response.text)
        self.assertEqual(data['message'],'操作成功')


    def  test_work_report(self):

        """测试工作汇报我收到的接口,接口名称:user/getNewUsers"""
        url = 'https://aijuhr.com/hrm/api.do'
        data = {
            'method': 'user/getNewUsers',
            'param': '{}',
            'sign': 'd9c4c690a26a2bd054c4daef4f0afd18',
        }

        response = session.post(url, data=data, headers=headers)
        data = json.loads(response.text)
        self.assertEqual(data['message'], '操作成功')

    def test_work_report_list(self):
        """测试工作汇报列表接口,接口名称:workReport/getWorkReportList"""
        url = 'https://aijuhr.com/hrm/api.do'
        data = {
            'method': 'workReport/getWorkReportList',
            'param': '{"userId":64660,"companyId":61,"pageNum":1,"pageSize":10,"from":"PC","type":2}',
            'sign': 'f0c080860ad0181a76c7ea827d501959',
        }

        response = session.post(url, data=data, headers=headers)
        data = json.loads(response.text)
        self.assertEqual(data['message'], '操作成功')


if __name__ == '__main__':
    unittest.main()