class DiagnosisEngine:
    def __init__(self):
        pass
    def diagnose(self, answers: list) -> str:
        # todo: реализовать diagnose до конца
        if answers[0] == False and answers[1] == False:
            return "Здоров"
        return "Простуда"