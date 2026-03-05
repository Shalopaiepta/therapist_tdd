from src.symptom_database import SymptomDatabase
from src.diagnosis_engine import DiagnosisEngine
from src.therapist import Therapist


def main():
    db = SymptomDatabase()
    therapist = Therapist()
    answers = []

    print("=== Электронный Терапевт ===")
    print("Ответьте на вопросы (да/нет)\n")

    for i in range(db.get_size()):
        question = db.get_question(i)
        print(question)
        response = input("Ваш ответ: ").strip().lower()
        answers.append(response in ['да', 'yes', 'y', 'd'])

    answers = therapist.ask_all(answers)
    diagnosis = therapist.get_result(answers)

    print(f"\nДиагноз: {diagnosis}")


if __name__ == '__main__':
    main()