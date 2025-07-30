from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'L1U1_test'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    NUM_TASKS = 10

    # 1回目のタスクの確率（%）
    RISKY_PROBABILITIES = [30, 25, 50, 30, 50, 33, 40, 90, 70, 80] 

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

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    for i in range(1, C.NUM_TASKS + 1):
        locals()[f'choice{i}'] = models.StringField(choices=[['Safe', 'Safe'], ['Risky', 'Risky']])
    del i
  
    # チェック確認テスト
    check1 = models.StringField()
    check2 = models.StringField()
    check3 = models.StringField()
    check4 = models.StringField()
    check5 = models.StringField()

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
        
class Task1(Page):
    form_model = 'player'
    form_fields = ['choice1']

    @staticmethod
    def vars_for_template(player: Player):
        safe_amt = int(C.SAFE_REWARDS[0])
        risky_amt = int(C.RISKY_SUCCESS_REWARDS[0])
        risky_prob = int(C.RISKY_PROBABILITIES[0])
        return dict(
            task_number=1,
            safe_text=f"確実に {safe_amt} 万円の利益を得る",
            risky_text=f"{risky_prob}%の確率で {risky_amt} 万円の利益を得られるが、{100 - risky_prob}% の確率で失敗し、利益を得られない",
            form_field="choice1",
        )
class Task2(Page):
    form_model = 'player'
    form_fields = ['choice2']

    @staticmethod
    def vars_for_template(player: Player):
        safe_amt = int(C.SAFE_REWARDS[1])
        risky_amt = int(C.RISKY_SUCCESS_REWARDS[1])
        risky_prob = int(C.RISKY_PROBABILITIES[1])
        return dict(
            task_number=2,
            safe_text=f"確実に {safe_amt} 万円の利益を得る",
            risky_text=f"{risky_prob}%の確率で {risky_amt} 万円の利益を得られるが、{100 - risky_prob}% の確率で失敗し、利益を得られない",
            form_field="choice2",
        )
class Task3(Page):
    form_model = 'player'
    form_fields = ['choice3']

    @staticmethod
    def vars_for_template(player: Player):
        safe_amt = int(C.SAFE_REWARDS[2])
        risky_amt = int(C.RISKY_SUCCESS_REWARDS[2])
        risky_prob = int(C.RISKY_PROBABILITIES[2])
        return dict(
            task_number=3,
            safe_text=f"確実に {safe_amt} 万円の利益を得る",
            risky_text=f"{risky_prob}%の確率で {risky_amt} 万円の利益を得られるが、{100 - risky_prob}% の確率で失敗し、利益を得られない",
            form_field="choice3",
        )

class Task4(Page):
    form_model = 'player'
    form_fields = ['choice4']

    @staticmethod
    def vars_for_template(player: Player):
        safe_amt = int(C.SAFE_REWARDS[3])
        risky_amt = int(C.RISKY_SUCCESS_REWARDS[3])
        risky_prob = int(C.RISKY_PROBABILITIES[3])
        return dict(
            task_number=4,
            safe_text=f"確実に {safe_amt} 万円の利益を得る",
            risky_text=f"{risky_prob}%の確率で {risky_amt} 万円の利益を得られるが、{100 - risky_prob}% の確率で失敗し、利益を得られない",
            form_field="choice4",
        )
    
class Task5(Page):
    form_model = 'player'
    form_fields = ['choice5']

    @staticmethod
    def vars_for_template(player: Player):
        safe_amt = int(C.SAFE_REWARDS[4])
        risky_amt = int(C.RISKY_SUCCESS_REWARDS[4])
        risky_prob = int(C.RISKY_PROBABILITIES[4])
        return dict(
            task_number=5,
            safe_text=f"確実に {safe_amt} 万円の利益を得る",
            risky_text=f"{risky_prob}%の確率で {risky_amt} 万円の利益を得られるが、{100 - risky_prob}% の確率で失敗し、利益を得られない",
            form_field="choice5",
        )
class Task6(Page):
    form_model = 'player'
    form_fields = ['choice6']

    @staticmethod
    def vars_for_template(player: Player):
        safe_amt = int(C.SAFE_REWARDS[5])
        risky_amt = int(C.RISKY_SUCCESS_REWARDS[5])
        risky_prob = int(C.RISKY_PROBABILITIES[5])
        return dict(
            task_number=6,
            safe_text=f"確実に {safe_amt} 万円の利益を得る",
            risky_text=f"{risky_prob}%の確率で {risky_amt} 万円の利益を得られるが、{100 - risky_prob}% の確率で失敗し、利益を得られない",
            form_field="choice6",
        )
class Task7(Page):
    form_model = 'player'
    form_fields = ['choice7']

    @staticmethod
    def vars_for_template(player: Player):
        safe_amt = int(C.SAFE_REWARDS[6])
        risky_amt = int(C.RISKY_SUCCESS_REWARDS[6])
        risky_prob = int(C.RISKY_PROBABILITIES[6])
        return dict(
            task_number=7,
            safe_text=f"確実に {safe_amt} 万円の利益を得る",
            risky_text=f"{risky_prob}%の確率で {risky_amt} 万円の利益を得られるが、{100 - risky_prob}% の確率で失敗し、利益を得られない",
            form_field="choice7",
        )
class Task8(Page):
    form_model = 'player'
    form_fields = ['choice8']

    @staticmethod
    def vars_for_template(player: Player):
        safe_amt = int(C.SAFE_REWARDS[7])
        risky_amt = int(C.RISKY_SUCCESS_REWARDS[7])
        risky_prob = int(C.RISKY_PROBABILITIES[7])
        return dict(
            task_number=8,
            safe_text=f"確実に {safe_amt} 万円の利益を得る",
            risky_text=f"{risky_prob}%の確率で {risky_amt} 万円の利益を得られるが、{100 - risky_prob}% の確率で失敗し、利益を得られない",
            form_field="choice8",
        )
class Task9(Page):
    form_model = 'player'
    form_fields = ['choice9']

    @staticmethod
    def vars_for_template(player: Player):
        safe_amt = int(C.SAFE_REWARDS[8])
        risky_amt = int(C.RISKY_SUCCESS_REWARDS[8])
        risky_prob = int(C.RISKY_PROBABILITIES[8])
        return dict(
            task_number=9,
            safe_text=f"確実に {safe_amt} 万円の利益を得る",
            risky_text=f"{risky_prob}%の確率で {risky_amt} 万円の利益を得られるが、{100 - risky_prob}% の確率で失敗し、利益を得られない",
            form_field="choice9",
        )
class Task10(Page):
    form_model = 'player'
    form_fields = ['choice10']

    @staticmethod
    def vars_for_template(player: Player):
        safe_amt = int(C.SAFE_REWARDS[9])
        risky_amt = int(C.RISKY_SUCCESS_REWARDS[9])
        risky_prob = int(C.RISKY_PROBABILITIES[9])
        return dict(
            task_number=10,
            safe_text=f"確実に {safe_amt} 万円の利益を得る",
            risky_text=f"{risky_prob}%の確率で {risky_amt} 万円の利益を得られるが、{100 - risky_prob}% の確率で失敗し、利益を得られない",
            form_field="choice10",
        )

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
        success_tasks = [1, 2, 4, 6, 9]
        tasks_adjusted_data = []
        for i in range(1, C.NUM_TASKS + 1):
            choice = getattr(player, f'choice{i}')
            safe_amt = int(C.SAFE_REWARDS[i - 1])
            risky_amt = int(C.RISKY_SUCCESS_REWARDS[i - 1])
            risky_prob = C.RISKY_PROBABILITIES[i - 1]
            success_adj = int(C.RISKY_SUCCESS_REWARDS_ADJUSTED[i - 1])
            safe_text = f"確実に {safe_amt} 万円の利益を得る"
            risky_text = f"{risky_prob}%の確率で {risky_amt} 万円の利益を得られるが、{100 - risky_prob}% の確率で失敗し、利益を得られない"

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
                    # 成功のみ下方修正
                    original_amount = risky_amt
                    adjusted_amount = risky_amt + success_adj
                    diff = success_adj
                    diff_colored = f'<span style="color: red;">{diff}</span>'
                    remark = f"運の要素が大きいと判断され、評価が{diff_colored}万円分、下方修正されました"
                    outcome_str = '<span style="color: red;">（成功）</span>'
                else:
                    # 失敗は調整なし
                    original_amount = 0
                    adjusted_amount = 0
                    diff = 0
                    diff_colored = f'<span>{diff}</span>'
                    remark = "修正はありませんでした"
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

page_sequence = [Intro, Check, Task1, Task2, Task3, Task4, Task5, Task6, Task7, Task8, Task9, Task10, Outcome, AdjustmentNotice, Adjustment]