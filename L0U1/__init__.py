from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'safe_vs_risky'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    NUM_TASKS = 10

    # 1回目のタスクの確率（%）
    RISKY_PROBABILITIES = [30, 25, 50, 30, 50, 33, 40, 90, 70, 80] 
    # 2回目のタスクの確率（%）
    RISKY_PROBABILITIES_SECOND = [50, 60, 75, 90, 50, 90, 20, 80, 85, 30] 

    # １回目のタスクの報酬設定
    SAFE_REWARDS = [
        cu(400), cu(200), cu(600), cu(100), cu(300), 
        cu(250), cu(380), cu(800), cu(500), cu(450)
    ]
    RISKY_SUCCESS_REWARDS = [
        cu(900), cu(800), cu(800), cu(500), cu(700),
        cu(750), cu(950), cu(880), cu(720), cu(600)
    ]
    RISKY_FAILURE_REWARDS = [cu(0)] * NUM_TASKS

    #１回目のタスクの報酬の調整設定
    RISKY_SUCCESS_REWARDS_ADJUSTED = [
        cu(-100), cu(-100), cu(-80), cu(-50), cu(-70),
        cu(-90), cu(-150), cu(-50), cu(-100), cu(-60)
    ]
    RISKY_FAILURE_REWARDS_ADJUSTED = [
        cu(80), cu(50), cu(100), cu(40), cu(60),
        cu(70), cu(100), cu(120), cu(80), cu(90)
    ]

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
    # 1回目の選択肢
    for i in range(1, C.NUM_TASKS + 1):
        locals()[f'choice{i}'] = models.StringField(choices=[['Safe', 'Safe'], ['Risky', 'Risky']])
    # 2回目の選択肢
    for i in range(1, C.NUM_TASKS + 1):
        locals()[f'choice_second{i}'] = models.StringField(choices=[['Safe', 'Safe'], ['Risky', 'Risky']])
    del i
    # チェック確認テスト
    check1 = models.StringField()
    check2 = models.StringField()
    check3 = models.StringField()
    check4 = models.StringField()
    check5 = models.StringField()
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
class Intro(Page):
    pass

class Check(Page):
    form_model = 'player'
    form_fields = ['check1', 'check2', 'check3', 'check4', 'check5']

    @staticmethod
    def vars_for_template(player: Player):
        questions = [
            {
                'label': 'Q1. あなたの職業設定はどれですか？',
                'choices': [
                    ['A', '医療機器メーカーの研究職'],
                    ['B', '医療機器メーカーの営業担当者'],
                    ['C', '電子機器メーカーの製造担当者'],
                    ['D', '製薬会社のマーケティング責任者'],
                ],
                'field': 'check1'
            },
            {
                'label': 'Q2. あなたはどのような目的で営業戦略を選びますか？',
                'choices': [
                    ['A', '評価を避けるため'],
                    ['B', '同僚と競争するため'],
                    ['C', '自分の営業成績（営業利益）を最大化するため'],
                    ['D', '製品理解を深めるため'],
                ],
                'field': 'check2'
            },
            {
                'label': 'Q3. 選択肢のうち「安全策」として正しいものはどれですか？',
                'choices': [
                    ['A', '利益が得られるかは完全に運次第'],
                    ['B', '常に失敗するが評価される'],
                    ['C', '利益の額は小さいが、必ず得られる'],
                    ['D', '成功すれば大きな報酬があるが確率が低い'],
                ],
                'field': 'check3'
            },
            {
                'label': 'Q4. 戦略選択後に起こることとして正しくないものはどれですか？',
                'choices': [
                    ['A', '営業戦略の結果（成功・失敗）が通知される'],
                    ['B', 'あなたが自分で報酬を調整できる'],
                    ['C', '上司が成果を上方または下方に修正する可能性がある'],
                    ['D', '結果のフィードバック後、再度戦略を選べる'],
                ],
                'field': 'check4'
            },
            {
                'label': 'Q5. この実験におけるあなたの報酬の仕組みとして正しいものはどれですか？',
                'choices': [
                    ['A', '営業成果に連動した変動報酬が支払われる'],
                    ['B', '成功した回数ごとに追加のインセンティブが支払われる'],
                    ['C', '結果にかかわらず、事前に決められた固定報酬が支払われる'],
                    ['D', '上司の評価によって報酬が変動する'],
                ],
                'field': 'check5'
            },
        ]
        return dict(
            questions=questions,
            check1=player.field_maybe_none('check1'),
            check2=player.field_maybe_none('check2'),
            check3=player.field_maybe_none('check3'),
            check4=player.field_maybe_none('check4'),
            check5=player.field_maybe_none('check5'),
        )

    @staticmethod
    def error_message(player, values):
        correct_answers = {
            'check1': 'B',
            'check2': 'C',
            'check3': 'C',
            'check4': 'B',
            'check5': 'C',
        }
        errors = {}
        for field, correct in correct_answers.items():
            if values.get(field) != correct:
                errors[field] = '正しい選択肢を選んでください。'
        if errors:
            return errors
        
class Task(Page):
    form_model = 'player'
    form_fields = [f'choice{i}' for i in range(1, C.NUM_TASKS + 1)]

    @staticmethod
    def vars_for_template(player: Player):
        task_texts = []
        for i in range(1, C.NUM_TASKS + 1):
            safe_amt = int(C.SAFE_REWARDS[i - 1])
            risky_amt = int(C.RISKY_SUCCESS_REWARDS[i - 1])
            risky_prob = int(C.RISKY_PROBABILITIES[i - 1])
            task_texts.append({
                'index': i,
                'safe_text': f"確実に {safe_amt} 万円の利益を得る",
                'risky_text': f"{risky_prob}%の確率で {risky_amt} 万円の利益を得られるが、{100 - risky_prob}% の確率で失敗し、利益を得られない",
            })
        return dict(tasks=task_texts)
    
class Outcome(Page):
    @staticmethod
    def vars_for_template(player: Player):
        success_tasks = [1, 2, 4, 6, 9]
        tasks_data = []

        for i in range(1, C.NUM_TASKS + 1):
            choice = getattr(player, f'choice{i}')
            safe_amt = int(C.SAFE_REWARDS[i - 1])
            risky_amt = int(C.RISKY_SUCCESS_REWARDS[i - 1])
            risky_prob = int(C.RISKY_PROBABILITIES[i - 1])
            safe_text = f"確実に {safe_amt} 万円の利益を得る"
            risky_text = f"{risky_prob}%の確率で {risky_amt} 万円の利益を得られるが、{100 - risky_prob}% の確率で失敗し、利益を得られない"

            if choice == "Safe":
                outcome = "N/A"
                payout = safe_amt
                choicing = safe_text    
            else:
                if i in success_tasks:
                    outcome = "Success"
                    payout = risky_amt
                else:
                    outcome = "Failure"
                    payout = int(C.RISKY_FAILURE_REWARDS[i - 1])
                choicing = risky_text

            tasks_data.append({
                'task_number': i,
                'choice': choicing,
                'outcome': outcome,
                'payout': payout,
            })

        total_payout = sum(t['payout'] for t in tasks_data)

        return {
            'tasks_data': tasks_data,
            'total_payout': total_payout,
        }

class AdjustmentNotice(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {}

class Adjustment(Page):
    @staticmethod
    def vars_for_template(player: Player):
        success_tasks = [1, 2, 4, 6, 9]  # Outcomeページと同期
        tasks_adjusted_data = []
        for i in range(1, C.NUM_TASKS + 1):
            choice = getattr(player, f'choice{i}')
            safe_amt = int(C.SAFE_REWARDS[i - 1])
            risky_amt = int(C.RISKY_SUCCESS_REWARDS[i - 1])
            risky_prob = int(C.RISKY_PROBABILITIES[i - 1])
            success_adj = int(C.RISKY_SUCCESS_REWARDS_ADJUSTED[i - 1])
            failure_adj = int(C.RISKY_FAILURE_REWARDS_ADJUSTED[i - 1])
            safe_text = f"確実に {safe_amt} 円の利益を得る"
            risky_text = f"{risky_prob}%の確率で {risky_amt} 円の利益を得られるが、{100 - risky_prob}% の確率で失敗し、利益を得られない"

            # 修正前・修正後・修正額
            if choice == "Safe":
                original_amount = safe_amt
                adjusted_amount = safe_amt
                diff = 0
                diff_colored = f'<span>{diff}</span>'
                remark = "修正はありませんでした"
                choice_result = safe_text
            else:
                if i in success_tasks:
                    # 成功は調整なし
                    original_amount = risky_amt
                    adjusted_amount = risky_amt
                    diff = 0
                    diff_colored = f'<span>{diff}</span>'
                    remark = "修正はありませんでした"
                    outcome_str = '<span style="color: red;">（成功）</span>'
                else:
                    # 失敗のみ上方修正
                    original_amount = 0
                    adjusted_amount = failure_adj
                    diff = failure_adj
                    diff_colored = f'<span style="color: blue;">{diff}</span>'
                    remark = f"不運を考慮し、評価が{diff_colored}円分、上方修正されました"
                    outcome_str = '<span style="color: blue;">（失敗）</span>'
                choice_result = risky_text + outcome_str

            tasks_adjusted_data.append({
                'task_number': i,
                'choice_result': choice_result,
                'original_amount': original_amount,
                'adjusted_amount': adjusted_amount,
                'diff': diff,
                'diff_colored': diff_colored,
                'remark': remark,
            })
        return {
            'tasks_adjusted_data': tasks_adjusted_data,
            'total_adjusted_payout': sum(item['adjusted_amount'] for item in tasks_adjusted_data)
        }

class TaskSecond(Page):
    form_model = 'player'
    form_fields = [f'choice_second{i}' for i in range(1, C.NUM_TASKS + 1)]

    @staticmethod
    def vars_for_template(player: Player):
        tasksecond_texts = []
        for i in range(1, C.NUM_TASKS + 1):
            safe_amt_second = int(C.SAFE_REWARDS_SECOND[i - 1])
            risky_amt_second = int(C.RISKY_SUCCESS_REWARDS_SECOND[i - 1])
            risky_prob_second = int(C.RISKY_PROBABILITIES_SECOND[i - 1])
            tasksecond_texts.append({
                'index': i,
                'safe_text_second': f"確実に {safe_amt_second} 万円の利益を得る",
                'risky_text_second': f"{risky_prob_second}%の確率で {risky_amt_second} 万円の利益を得られるが、{100 - risky_prob_second}% の確率で失敗し、利益を得られない",
            })
        return dict(tasks=tasksecond_texts)

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

page_sequence = [Intro, Check, Task, Outcome, AdjustmentNotice, Adjustment, TaskSecond, Questionare, Exit]