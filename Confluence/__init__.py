from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'Confluence'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    NUM_TASKS = 10

    # 2回目のタスクの確率（%）
    RISKY_PROBABILITIES_SECOND = [50, 60, 75, 90, 50, 90, 20, 80, 85, 30] 

    #２回目のタスクの報酬設定
    SAFE_REWARDS_SECOND = [
        cu(350), cu(700), cu(600), cu(650), cu(300), 
        cu(900), cu(200), cu(400), cu(750), cu(250)
    ]
    RISKY_SUCCESS_REWARDS_SECOND = [
        cu(750), cu(900), cu(800), cu(700), cu(600),
        cu(990), cu(850), cu(500), cu(940), cu(950)
    ]
    RISKY_FAILURE_REWARDS_SECOND = [cu(0)] * NUM_TASKS


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # 2回目の選択肢
    for i in range(1, C.NUM_TASKS + 1):
        locals()[f'choice_second{i}'] = models.StringField(choices=[['Safe', 'Safe'], ['Risky', 'Risky']])
    del i
    # 質問紙（Questionare）用フィールド
    # CRT（3問）
    crt1 = models.IntegerField(choices=[1, 2, 3, 4], widget=widgets.RadioSelect)
    crt2 = models.IntegerField(choices=[1, 2, 3, 4], widget=widgets.RadioSelect)
    crt3 = models.IntegerField(choices=[1, 2, 3, 4], widget=widgets.RadioSelect)
    # 公平性（5問）
    fairness1 = models.IntegerField(choices=[1,2,3,4,5,6,7], widget=widgets.RadioSelect)
    fairness2 = models.IntegerField(choices=[1,2,3,4,5,6,7], widget=widgets.RadioSelect)
    fairness3 = models.IntegerField(choices=[1,2,3,4,5,6,7], widget=widgets.RadioSelect)
    fairness4 = models.IntegerField(choices=[1,2,3,4,5,6,7], widget=widgets.RadioSelect)
    fairness5 = models.IntegerField(choices=[1,2,3,4,5,6,7], widget=widgets.RadioSelect)
    fairness6 = models.IntegerField(choices=[1,2,3,4,5,6,7], widget=widgets.RadioSelect)
    fairness7 = models.IntegerField(choices=[1,2,3,4,5,6,7], widget=widgets.RadioSelect)
    fairness8 = models.IntegerField(choices=[1,2,3,4,5,6,7], widget=widgets.RadioSelect)
    # 主観的リスク認知（2問）
    risk_reasonable = models.IntegerField(choices=[1,2,3,4,5,6,7], widget=widgets.RadioSelect)
    risk_future = models.IntegerField(choices=[1,2,3,4,5,6,7], widget=widgets.RadioSelect)
    # 年齢
    age = models.IntegerField()
    # 性別
    gender = models.StringField(choices=['男性', '女性', 'その他', '回答しない'])
    # 就労年数
    work_years = models.IntegerField()
    # 金融・会計知識
    finance_knowledge = models.IntegerField(choices=[1,2,3,4,5,6,7], widget=widgets.RadioSelect)

    # PAGES
class TaskSecond1(Page):
    form_model = 'player'
    form_fields = ['choice_second1']

    @staticmethod
    def vars_for_template(player: Player):
        i = 0
        safe_amt = int(C.SAFE_REWARDS_SECOND[i])
        risky_amt = int(C.RISKY_SUCCESS_REWARDS_SECOND[i])
        risky_prob = int(C.RISKY_PROBABILITIES_SECOND[i])
        return dict(
            task_number=1,
            safe_text=f"確実に {safe_amt} 万円の利益を得る",
            risky_text=f"{risky_prob}%の確率で {risky_amt} 万円の利益を得られるが、{100 - risky_prob}% の確率で失敗し、利益を得られない",
            form_field="choice_second1",
        )
class TaskSecond2(Page):
    form_model = 'player'
    form_fields = ['choice_second2']

    @staticmethod
    def vars_for_template(player: Player):
        i = 1
        safe_amt = int(C.SAFE_REWARDS_SECOND[i])
        risky_amt = int(C.RISKY_SUCCESS_REWARDS_SECOND[i])
        risky_prob = int(C.RISKY_PROBABILITIES_SECOND[i])
        return dict(
            task_number=2,
            safe_text=f"確実に {safe_amt} 万円の利益を得る",
            risky_text=f"{risky_prob}%の確率で {risky_amt} 万円の利益を得られるが、{100 - risky_prob}% の確率で失敗し、利益を得られない",
            form_field="choice_second2",
        )
class TaskSecond3(Page):
    form_model = 'player'
    form_fields = ['choice_second3']

    @staticmethod
    def vars_for_template(player: Player):
        i = 2
        safe_amt = int(C.SAFE_REWARDS_SECOND[i])
        risky_amt = int(C.RISKY_SUCCESS_REWARDS_SECOND[i])
        risky_prob = int(C.RISKY_PROBABILITIES_SECOND[i])
        return dict(
            task_number=3,
            safe_text=f"確実に {safe_amt} 万円の利益を得る",
            risky_text=f"{risky_prob}%の確率で {risky_amt} 万円の利益を得られるが、{100 - risky_prob}% の確率で失敗し、利益を得られない",
            form_field="choice_second3",
        )
class TaskSecond4(Page):
    form_model = 'player'
    form_fields = ['choice_second4']

    @staticmethod
    def vars_for_template(player: Player):
        i = 3
        safe_amt = int(C.SAFE_REWARDS_SECOND[i])
        risky_amt = int(C.RISKY_SUCCESS_REWARDS_SECOND[i])
        risky_prob = int(C.RISKY_PROBABILITIES_SECOND[i])
        return dict(
            task_number=4,
            safe_text=f"確実に {safe_amt} 万円の利益を得る",
            risky_text=f"{risky_prob}%の確率で {risky_amt} 万円の利益を得られるが、{100 - risky_prob}% の確率で失敗し、利益を得られない",
            form_field="choice_second4",
        )
class TaskSecond5(Page):
    form_model = 'player'
    form_fields = ['choice_second5']

    @staticmethod
    def vars_for_template(player: Player):
        i = 4
        safe_amt = int(C.SAFE_REWARDS_SECOND[i])
        risky_amt = int(C.RISKY_SUCCESS_REWARDS_SECOND[i])
        risky_prob = int(C.RISKY_PROBABILITIES_SECOND[i])
        return dict(
            task_number=5,
            safe_text=f"確実に {safe_amt} 万円の利益を得る",
            risky_text=f"{risky_prob}%の確率で {risky_amt} 万円の利益を得られるが、{100 - risky_prob}% の確率で失敗し、利益を得られない",
            form_field="choice_second5",
        )
class TaskSecond6(Page):
    form_model = 'player'
    form_fields = ['choice_second6']

    @staticmethod
    def vars_for_template(player: Player):
        i = 5
        safe_amt = int(C.SAFE_REWARDS_SECOND[i])
        risky_amt = int(C.RISKY_SUCCESS_REWARDS_SECOND[i])
        risky_prob = int(C.RISKY_PROBABILITIES_SECOND[i])
        return dict(
            task_number=6,
            safe_text=f"確実に {safe_amt} 万円の利益を得る",
            risky_text=f"{risky_prob}%の確率で {risky_amt} 万円の利益を得られるが、{100 - risky_prob}% の確率で失敗し、利益を得られない",
            form_field="choice_second6",
        )
class TaskSecond7(Page):
    form_model = 'player'
    form_fields = ['choice_second7']

    @staticmethod
    def vars_for_template(player: Player):
        i = 6
        safe_amt = int(C.SAFE_REWARDS_SECOND[i])
        risky_amt = int(C.RISKY_SUCCESS_REWARDS_SECOND[i])
        risky_prob = int(C.RISKY_PROBABILITIES_SECOND[i])
        return dict(
            task_number=7,
            safe_text=f"確実に {safe_amt} 万円の利益を得る",
            risky_text=f"{risky_prob}%の確率で {risky_amt} 万円の利益を得られるが、{100 - risky_prob}% の確率で失敗し、利益を得られない",
            form_field="choice_second7",
        )
class TaskSecond8(Page):
    form_model = 'player'
    form_fields = ['choice_second8']

    @staticmethod
    def vars_for_template(player: Player):
        i = 7
        safe_amt = int(C.SAFE_REWARDS_SECOND[i])
        risky_amt = int(C.RISKY_SUCCESS_REWARDS_SECOND[i])
        risky_prob = int(C.RISKY_PROBABILITIES_SECOND[i])
        return dict(
            task_number=8,
            safe_text=f"確実に {safe_amt} 万円の利益を得る",
            risky_text=f"{risky_prob}%の確率で {risky_amt} 万円の利益を得られるが、{100 - risky_prob}% の確率で失敗し、利益を得られない",
            form_field="choice_second8",
        )
class TaskSecond9(Page):
    form_model = 'player'
    form_fields = ['choice_second9']

    @staticmethod
    def vars_for_template(player: Player):
        i = 8
        safe_amt = int(C.SAFE_REWARDS_SECOND[i])
        risky_amt = int(C.RISKY_SUCCESS_REWARDS_SECOND[i])
        risky_prob = int(C.RISKY_PROBABILITIES_SECOND[i])
        return dict(
            task_number=9,
            safe_text=f"確実に {safe_amt} 万円の利益を得る",
            risky_text=f"{risky_prob}%の確率で {risky_amt} 万円の利益を得られるが、{100 - risky_prob}% の確率で失敗し、利益を得られない",
            form_field="choice_second9",
        )
class TaskSecond10(Page):
    form_model = 'player'
    form_fields = ['choice_second10']

    @staticmethod
    def vars_for_template(player: Player):
        i = 9
        safe_amt = int(C.SAFE_REWARDS_SECOND[i])
        risky_amt = int(C.RISKY_SUCCESS_REWARDS_SECOND[i])
        risky_prob = int(C.RISKY_PROBABILITIES_SECOND[i])
        return dict(
            task_number=10,
            safe_text=f"確実に {safe_amt} 万円の利益を得る",
            risky_text=f"{risky_prob}%の確率で {risky_amt} 万円の利益を得られるが、{100 - risky_prob}% の確率で失敗し、利益を得られない",
            form_field="choice_second10",
        )

class Questionare(Page):
    form_model = 'player'
    form_fields = [
        'crt1', 'crt2', 'crt3',
        'fairness1', 'fairness2', 'fairness3', 'fairness4', 'fairness5', 'fairness6', 'fairness7', 'fairness8',
        'risk_reasonable', 'risk_future',
        'age', 'gender', 'work_years', 'finance_knowledge'
    ]

    @staticmethod
    def vars_for_template(player: Player):
        crt_questions = [
            {
                'label': 'バットとボールの合計金額は110円です。バットはボールよりも100円高いとすると、ボールの値段はいくらですか？',
                'choices': [
                    [1, '10円'],
                    [2, '5円'],
                    [3, '1円'],
                    [4, 'わからない'],
                ],
                'field': 'crt1'
            },
            {
                'label': '5台の機械が5個の製品を作るのに5分かかるとします。では、100台の機械が100個の製品を作るには何分かかりますか？',
                'choices': [
                    [1, '100分'],
                    [2, '5分'],
                    [3, '20分'],
                    [4, 'わからない'],
                ],
                'field': 'crt2'
            },
            {
                'label': 'ある湖に睡蓮の葉が浮かんでいて、毎日その面積が2倍に増えていきます。48日目に湖全体を覆うとしたら、湖の半分を覆うのは何日目ですか？',
                'choices': [
                    [1, '24日目'],
                    [2, '47日目'],
                    [3, '48日目'],
                    [4, 'わからない'],
                ],
                'field': 'crt3'
            },
        ]
        fairness_questions = [
            "最終的な成果（上司による調整後の報酬）は、自分の努力や判断に見合っていた。",
            "自分の成果の配分は公平な結果だと感じた。",
            "成果が調整されたプロセスには一貫性があるように思えた。",
            "成果の調整は、偏りのない方法で行われたように感じた。",
            "評価・調整の過程で、自分が適切に扱われていると感じた。",
            "自分の行動や成果が、十分に考慮されたうえで評価されていると感じた。",
            "成果が調整された理由は、納得できる形で説明されていた。" ,
            "成果の調整に関する情報は、分かりやすく提示されていた。"
        ]
        fairness_fields = [
            'fairness1', 'fairness2', 'fairness3', 'fairness4',
            'fairness5', 'fairness6', 'fairness7', 'fairness8'
        ]
        fairness_items = list(zip(fairness_questions, fairness_fields))

        risk_questions = [
            "リスクをとることが合理的だと感じましたか？",
            "リスクを取る選択が今後も報われると感じましたか？",
        ]
        risk_fields = ['risk_reasonable', 'risk_future']
        risk_items = list(zip(risk_questions, risk_fields))


        risk_fields = ['risk_reasonable', 'risk_future']


        return dict(
            crt_questions=crt_questions,
            fairness_items=fairness_items,
            risk_items=risk_items,
            # ...他の変数...
        )
    
class Exit(Page):
    pass

page_sequence = [TaskSecond1, TaskSecond2, TaskSecond3, TaskSecond4, TaskSecond5, TaskSecond6, TaskSecond7, TaskSecond8, TaskSecond9, TaskSecond10, Questionare, Exit]