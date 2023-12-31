import random

adverbs = [
    "자주", "매우", "너무", "빨리", "천천히", "계속", "보통", "가끔", "대충", "이미",
    "확실히", "완전히", "거의", "실제로", "정말", "아마", "그냥", "대체로", "딱", "여전히",
    "또", "좀", "잠시", "간단히", "이미", "점점", "비교적", "어찌됐든", "절대로", "자연스럽게",
    "뿐", "힘들게", "평범하게", "시원하게", "무조건", "필요로", "사실", "근처에", "철저하게",
    "별로", "틀리지", "훨씬", "의외로", "통째로", "상당히", "무진장", "대체로", "누군가",
    "적극적으로", "한때", "거의", "보통", "유난히", "다소", "언제나", "지극히", "아직도",
    "안그래도", "흔히", "거의", "마치", "기본적으로", "굉장히", "여간", "헛되게", "아마",
    "가끔", "어렵지", "고작", "거듭", "틀림없이", "최대한", "또한", "조용히", "비슷하게",
    "당장", "아주", "오로지", "바로", "단", "혹시", "과연", "절대로", "비교적", "거의",
    "이미", "정확히", "직접", "진심으로", "고통스럽게", "자세히", "엄청나게", "모두", "힘들게",
    "늘", "발끝까지", "무슨", "전혀"
]

verbs = [
    "뛰는", "잊는", "말하는", "움직이는", "괴롭히는", "머무르는", "감추는", "두드리는", "들려주는", "만지는",
    "창조하는", "놀라는", "덮는", "흔들리는", "아껴두는", "참는", "올라타는", "씻기는", "움직이는", "걸러내는",
    "방해하는", "예측하는", "믿는", "구경하는", "담그는", "버티는", "따르는", "준비하는", "안아주는", "닦는",
    "살아나는", "겪는", "읽히는", "드는", "걸어가는", "남는", "떠나는", "빌는", "깨닫는", "기대하는",
    "넘어지는", "비교하는", "업는", "열리는", "웃기는", "기대하는", "흐르는", "만족하는", "버리는", "던지는",
    "놓는", "발견되는", "사라지는", "꿈꾸는", "가리는", "놀랍는", "눈물나는", "불어오는", "일어나는", "듣는",
    "약속하는", "받는", "덮는", "이끌는", "서두르는", "걷는", "듣는", "안녕하는", "따르는", "들려주는",
    "약속하는", "읽는", "들어가는", "잊는", "안녕하는", "날는", "듣는", "말하는", "듣는", "느끼는",
    "듣는", "괴롭히는", "걱정하는", "기억하는", "배우는", "바라보는", "모르는", "내려가는", "섞이는", "부르는",
    "믿는", "이야기하는", "듣는", "밀는", "듣는", "행복하는", "들려주는", "살는", "기억하는", "오는",
    "읽는", "나누는", "듣는", "씻는", "믿는", "빠지는", "자는", "웃는", "잊는", "걷는"
]

animals = [
    "고양이", "강아지", "사자", "호랑이", "팬더", "코알라", "팽귄", "캥거루", "펭귄", "고릴라",
    "코끼리", "원숭이", "뱀", "악어", "기린", "물소", "캐멀", "알파카", "라마", "늑대",
    "여우", "곰", "하이에나", "불가사리", "스컹크", "오소리", "토끼", "다람쥐", "다람이", "너구리",
    "사향고양이", "표범", "치타", "바다사자", "바다표범", "바다거북", "문어", "낙지", "갈매기", "독수리",
    "참새", "오리", "앵무새", "공작새", "부엉이", "펭귄", "꼬물이", "뱁새", "고니", "코뿔소",
    "바다사람", "해마", "바다코끼리", "돌고래", "고래", "상어", "햄스터", "비버", "불독", "치와와",
    "달마시안", "셰퍼드", "세터", "푸들", "불독", "불랙", "피켄", "웰시코기", "슈나우저", "말티즈",
    "리트리버", "불도그", "불테리어", "차우차우", "허스키", "빅토리아", "바비", "블론디", "카카오", "소니",
    "삼성", "엘지", "롤리", "빅스비", "페퍼", "소피", "아이비", "아델", "헤이즐", "체리",
    "단비", "수현", "효주", "하니", "영이", "양이", "종이", "누렁이", "별이", "봄이"
]

def generate_random_sentence():
    random_adverb = random.choice(adverbs)
    random_verb = random.choice(verbs)
    random_animal = random.choice(animals)
    
    sentence = f"{random_adverb} {random_verb} {random_animal}"
    return sentence