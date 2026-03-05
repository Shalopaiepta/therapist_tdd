class SymptomDatabase:
    def __init__(self):
        pass
    def get_question(self, index:int)->str:
        """
        Возвращает вопрос по индексу из базы симптомов
        Аргументы: index(int): индекс вопроса
        Возвращает: str: текст вопроса
        """
        #todo: Надо сделать нормально get_question
        if index==1:
            return "У вас есть кашель?"
        return "У вас есть температура?"
    def get_size(self) -> int:
        # todo: реализовать get_size до конца
        return 2