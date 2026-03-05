class DiagnosisEngine:
    def __init__(self):
        pass
    def diagnose(self, answers: list) -> str:
        """
        Ставит диагноз по списку ответов пациента

        Args:
            answers (list): список булевых ответов (True=да, False=нет)

        Returns:
            str: текст диагноза
        """
        # todo: реализовать diagnose до конца
        if answers[0] == True and answers[1] == True:
            return "Грипп"
        if answers[0] == False and answers[1] == False:
            return "Здоров"
        return "Простуда"