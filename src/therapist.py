from src.diagnosis_engine import DiagnosisEngine


class Therapist:
    def __init__(self):
        # todo: подключить SymptomDatabase
        self.engine = DiagnosisEngine()

    def ask_all(self, answers: list) -> list:
        """
        Принимает ответы пациента на все вопросы

        Args:
            answers (list): список булевых ответов (True=да, False=нет)

        Returns:
            list: список ответов
        """
        # todo: реализовать интерактивный опрос через SymptomDatabase
        return answers

    def get_result(self, answers: list) -> str:
        """
        Возвращает диагноз на основе ответов пациента

        Args:
            answers (list): список булевых ответов (True=да, False=нет)

        Returns:
            str: текст диагноза
        """
        # todo: реализовать get_result до конца
        return self.engine.diagnose(answers)