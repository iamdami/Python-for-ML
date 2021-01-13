from collections import defaultdict
from collections import OrderedDict


d = defaultdict(object)  # Create a default dictionary
d = defaultdict(lambda: 1)  # set Default value 0
print(d["first"])  # 1

text = """Forget Cristiano Ronaldo, Lionel Messi and Robert Lewandowski. 
Tottenham's Son Heung-min has delivered a statistical anomaly that sets him out as the deadliest finisher in Europe. 
The way Son is performing in comparison to his expected goals is simply remarkable and eclipses all of football's top marksmen since 2016. Not Son. 
His consistent ability to score more times than the chances predict, according to the expected goals measure (see green box below), is actually on the rise. 
The statistics below, as compiled by understat.com and reported in the Independent, show Son is scoring a jaw-dropping 44 per cent above his xG since August 2016, a period in which he's netted 61 times. 
Next on the list is team-mate Harry Kane, who is almost level with Lionel Messi at 21.3 per cent. 
Some of the players regarded as the most incisive in front of goal have actually performed worse than their xG, putting Son's measurement on another level. """.lower().split()

print(text)  # ['forget', 'cristiano', 'ronaldo,', 'lionel', 'messi', 'and', 'robert', 'lewandowski.', "tottenham's", 'son', 'heung-min', 'has', 'delivered', 'a', 'statistical', 'anomaly', 'that', 'sets', 'him', 'out', 'as', 'the', 'deadliest', 'finisher', 'in', 'europe.', 'the', 'way', 'son', 'is', 'performing', 'in', 'comparison', 'to', 'his', 'expected', 'goals', 'is', 'simply', 'remarkable', 'and', 'eclipses', 'all', 'of', "football's", 'top', 'marksmen', 'since', '2016.', 'not', 'son.', 'his', 'consistent', 'ability', 'to', 'score', 'more', 'times', 'than', 'the', 'chances', 'predict,', 'according', 'to', 'the', 'expected', 'goals', 'measure', '(see', 'green', 'box', 'below),', 'is', 'actually', 'on', 'the', 'rise.', 'the', 'statistics', 'below,', 'as', 'compiled', 'by', 'understat.com', 'and', 'reported', 'in', 'the', 'independent,', 'show', 'son', 'is', 'scoring', 'a', 'jaw-dropping', '44', 'per', 'cent', 'above', 'his', 'xg', 'since', 'august', '2016,', 'a', 'period', 'in', 'which', "he's", 'netted', '61', 'times.', 'next', 'on', 'the', 'list', 'is', 'team-mate', 'harry', 'kane,', 'who', 'is', 'almost', 'level', 'with', 'lionel', 'messi', 'at', '21.3', 'per', 'cent.', 'some', 'of', 'the', 'players', 'regarded', 'as', 'the', 'most', 'incisive', 'in', 'front', 'of', 'goal', 'have', 'actually', 'performed', 'worse', 'than', 'their', 'xg,', 'putting', "son's", 'measurement', 'on', 'another', 'level.']

word_count = {}
for word in text:
    if word in word_count.keys():
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)  # {'forget': 1, 'cristiano': 1, 'ronaldo,': 1, 'lionel': 2, 'messi': 2, 'and': 3, 'robert': 1, 'lewandowski.': 1, "tottenham's": 1, 'son': 3, 'heung-min': 1, 'has': 1, 'delivered': 1, 'a': 3, 'statistical': 1, 'anomaly': 1, 'that': 1, 'sets': 1, 'him': 1, 'out': 1, 'as': 3, 'the': 10, 'deadliest': 1, 'finisher': 1, 'in': 5, 'europe.': 1, 'way': 1, 'is': 6, 'performing': 1, 'comparison': 1, 'to': 3, 'his': 3, 'expected': 2, 'goals': 2, 'simply': 1, 'remarkable': 1, 'eclipses': 1, 'all': 1, 'of': 3, "football's": 1, 'top': 1, 'marksmen': 1, 'since': 2, '2016.': 1, 'not': 1, 'son.': 1, 'consistent': 1, 'ability': 1, 'score': 1, 'more': 1, 'times': 1, 'than': 2, 'chances': 1, 'predict,': 1, 'according': 1, 'measure': 1, '(see': 1, 'green': 1, 'box': 1, 'below),': 1, 'actually': 2, 'on': 3, 'rise.': 1, 'statistics': 1, 'below,': 1, 'compiled': 1, 'by': 1, 'understat.com': 1, 'reported': 1, 'independent,': 1, 'show': 1, 'scoring': 1, 'jaw-dropping': 1, '44': 1, 'per': 2, 'cent': 1, 'above': 1, 'xg': 1, 'august': 1, '2016,': 1, 'period': 1, 'which': 1, "he's": 1, 'netted': 1, '61': 1, 'times.': 1, 'next': 1, 'list': 1, 'team-mate': 1, 'harry': 1, 'kane,': 1, 'who': 1, 'almost': 1, 'level': 1, 'with': 1, 'at': 1, '21.3': 1, 'cent.': 1, 'some': 1, 'players': 1, 'regarded': 1, 'most': 1, 'incisive': 1, 'front': 1, 'goal': 1, 'have': 1, 'performed': 1, 'worse': 1, 'their': 1, 'xg,': 1, 'putting': 1, "son's": 1, 'measurement': 1, 'another': 1, 'level.': 1}