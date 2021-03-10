#研究信息熵,不知题意是否理解正确。假设:s = 'There is a pig.', n =11= len(s去掉所有标点，去掉所有空格，只保留大小写英文字母)
#f(e) = 2,p(e)=2/11,entropy(s)=-p(t)log2p(t)+e+....

import sys
import re
import math

#除去标点和空格，字符串的长度
def lenOfCha(s):
    sc = ''
    for i in range(len(s)):
        #只能针对英文
        #t = re.search('[a-zA-Z]',s[i])
        #if t:
        #针对中英文
        t = re.search('[\u4e00-\u9fa5]|[a-zA-Z]',s[i])
        if t:
            sc += s[i]
    n = len(sc)
    #print(sc)
    return n

#字母c,s转换为小写，返回c在s中出现的频率
def fre(c,s):
    n = 0
    c = c.lower()
    s = s.lower()
    for t in s:
        if t == c:
            n += 1
    #print('fre',n)
    return n

def prob(c,s,n):
    return fre(c,s)/n

def entropy(s):
    n = lenOfCha(s)
    sett = set()
    e = 0
    p = 0
    for i in range(len(s)):
        if s[i].lower() not in sett:
            sett.add(s[i].lower())
            p =prob(s[i],s,n)
            e += -p*math.log(p,2)
    #print(sett)
    return e

def main():
    s = 'There is a pig.'
    #lenOfCha(s)
    #print(fre('e',s))
    #print(fre('t',s))
    print(entropy(s))
    s1 = '这有只猪。'
    print(entropy(s1))
    
    s2 = "Circuit breaker tightened.China's circuit breaker arrangement for international passenger flights was tightened on Wednesday to contain the spread of COVID-19.According to the Civil Aviation Administration of China, starting on Wednesday, if there are five passengers on a flight who test positive, the airline's flights will be suspended for two weeks."
    s3 ='国际航班熔断措施调整。为做好新冠肺炎疫情防控工作，我国12月16日起收紧对国际客运航班的熔断措施。民航局宣布，自即日起，航空公司同一航线航班，入境后核酸检测结果为阳性的旅客人数达到5个的，暂停该公司该航线运行2周。'
    print(entropy(s2))
    print(entropy(s3))

    s4 = '''Greek MPs have passed a controversial package of tax and pension reforms, vital for the receipt of the next installment of national bailout funds. Finance Ministers of Eurozone countries are meeting on Monday to discuss the payout. Yogita Limaye reports from Athens. All 153 MPs of the ruling Syriza Party voted in favor of new austerity measures. That'll passed by Greece's 300-member parliament. They include economic reforms that will see people paying more taxes and pensions being cut. The law had been strongly opposed by Labour Unions who had held mass protests in Athens for two days in a row. Greece's government has said the measures were necessary for the country to be eligible for more money from the bailout package it signed with the Eurozone last year.The Philippines is holding a presidential election in which the established political order could be overturned by a little known local mayor. Rodrigo Duterte's brash campaign has galvanized voters. Jonathan Head reports from outside a polling station in Manila. This has been a very hard-fought presidential campaign. The clear front-runner in the last few weeks we've seen, the mayor of Davao, the southern city. This mayor Rodrigo Duterte, a very controversial man, very outspoken, very blunt spoken. With quite a lot of controversial policy platforms, things like federalism, for example, let alone, an incredibly tough attitude to crime. He surged into the lead, and that's given a real freesome to contest with the other four presidential candidates with some of them, in the last stages, even suggesting they should form an alliance, although it has not yet happened to try and block Mayor Duterte.
The South Korean government has dismissed as propaganda suggestions made by the North that the two countries should meet for talks. Steve Evans reports from Pyongyang. North Korea's supreme leader, as he's called, said that representatives from Seoul and Pyongyang should meet to find ways of easing the tension along the highly militarized border. South Korea's Unification Ministry responded that the suggestion was merely a propaganda drive with no sincerity. The pattern of relations between South and North over recent years is for tensions to ratchet up and then be eased as both sides tone down their rhetoric only for the process to be repeated.Officials in western Canada say the huge wild fire which has now been raging for a week may have reached a turning point. A spokesman for Wild Fire Management in the province of Alberta said cooler temperatures had improved conditions for fire fighting. Alberta's premiere Rachel Notley said the blaze was now growing more slowly. She cast the estimated areas affected to just over 1500 square kilometers. It's expected to be the most expansive natural disaster in Canadian history. One estimate of insurance losses is about 7 billion dollars. This is the latest world news from the BBC.

Panama has agreed to transfer nearly 4000 Cubans who are hoping to reach the United States through a town in northern Mexico. The Cubans have been stranded in Panama for months hoping to reach the US under a decades-old law which gives them privileged entry and a fast-track to residency. Officials in Panama said daily flights to Ciudad Juarez would begin on Monday.

The Bolivian president Evo Morales has criticized Chili for building a military base close to the two countries' shared border. Mr Morales said it went against international norms. Firstly, this military base is illegal. If we take into consideration the international agreements, military bases can only be built 50 kilometers from the border between countries. But 15 kilometers, what's the aim? But the Chilean Foreign ministry has denied its established base saying to step up its military patrols in the area to tackle drug trafficking. Chili and are Bolivian are contesting access to the waters of the River Silala which flows through both countries.

The Invictus Games for injured service men and women are beginning in the city of Orlando in the United States. The event has the backing of Britain's prince Harry and follows the inaugural games in London in 2014. During the 5-day tournament, more than 500 athletes from 14 countries will compete in a range of sports. The main guests of the opening ceremony will be Prince Harry and the US first lady Michelle Obama.

A statue of kneeling of Adolf Hitler by the Italian sculptor Maurizio Cattelan has been sold for 17.2 million dollars at auction in New York, a record for the artist's work. The boy-sized figure made of wax and resin and entitled 'Him' shows the Nazi leader in a suit gazing upward with his hands crossed. The work is one of a number being sold by Christie's auctioneers. BBC news.'''

    s5 = '''希腊议会通过备受争议的税收及养老金改革法案，该法案对下一笔救助贷款债权人至关重要。周一，欧元区各财长就债务问题进行讨论。请听尤金那·利马耶为您从雅典发回的报道。执政联盟的所有153名议员均就新紧缩措施投了赞成票。法案将得到300名议会成员通过。法案包括经济改革，增加税收征收力度，缩减养老金。该法案遭到工会组织强烈反对，连续两天在雅典街头抗议。据希腊政府表示，希腊于去年与欧盟区签订援助计划，为获取更多救援资金，该法案势在必行。

菲律宾大选激战正酣，某当地市长恐将打破现存政治秩序。他大胆而偏激的竞选让选民吃惊。请听乔纳森·黑德为您从马尼拉投票站外发回的报道。此次竞选活动十分惨烈。根据前几周选票结果，南部城市达沃市市长一马当先。杜特尔特此人备受争议，常常是直言不讳。像联邦主义等政策纲领备受争议，对打击犯罪也是采取强硬态度。此次竞选他一马当先，其余四名候选人望尘莫及，在选举最后阶段，甚至有候选人结成联盟，但杜特尔特阻击战并没有到来。

就朝方建议双边对话一事，韩国政府打破传言。请听史蒂夫·埃文斯从平壤发回的报道。据朝鲜最高领导人表示，朝韩应为缓解边境紧张关系寻求出路。韩国统一部回应称，此建议实为政治宣传，并非真心实意。近几年以来，朝韩紧张关系逐步升温，待双边唇枪舌战降温后，两国关系才得以缓解。

加拿大西部大火已经持续一周，官方称或将迎来转机。据阿尔伯塔省火灾事故管理发言人表示，冷空气为消防工作提供便利。阿尔伯塔省省长瑞秋·诺特利表示，大火蔓延速度逐渐变缓。称过火面积预计只有1500多平方公里。此次灾情或将成为加拿大史上规模最大的一次。预计保险损失约70亿美金。BBC全球新闻。

通过墨西哥北部中转城，巴拿马同意移交近4000名入美移民。古巴移民已在巴拿马滞留数月，根据数十年前的一项法律规定，古巴移民将获入境特权，并可快速落户。据巴拿马官方表示，周一将开通飞往华瑞兹的每日航班。

智利总统埃沃·莫拉莱斯指责智利在两国边界建立军事基地。莫拉莱称此举违反国际准则。首先，建立军事基地为违法行为。根据现存国际协定，军事基地只能设在边境50公里外。但该基地却设在了15公里以里，其目的是什么？智利外交部给与否认，称此举旨在加强军事巡逻，打击毒品走私。就锡拉拉河边境水源主权，两国一直喋喋不休。

伤残军人运动会在美国奥兰多市打响。该项赛事由哈利王子发起，2014年，伦敦曾举办首届“勇士”运动会。在这项为期五天的赛事中，来自14个国家的500多名勇士将展开角逐。开幕式嘉宾为哈里王子，美国第一夫人米歇尔·奥巴马。

意大利雕塑家莫瑞吉奥·卡特兰作品在纽约拍卖，希特勒跪像拍出1720万美元高价，刷新该艺术家拍价记录。雕像名为《他》，制作材料为蜡和树脂，小孩般大小，身着西服的希特勒凝视上方，双手交叉。这也是佳士得拍卖行拍卖的众多作品之一。BBC新闻。'''
    print('s4:',entropy(s4))
    print('s5:',entropy(s5))
    

if __name__ == '__main__':
    main()
