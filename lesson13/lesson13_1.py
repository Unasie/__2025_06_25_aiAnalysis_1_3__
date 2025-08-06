#有一個names.txt
#讀取names.txt
#請隨機取出3個名字
import random


random.seed(4561)

def sample_names_from_file(file_name: str, nums: int = 1) -> list[str]:
    """
    從指定的檔案中讀取所有姓名，並隨機取出指定數量的姓名。

    參數:
        file_name (str): 檔案名稱，檔案內容為姓名，每行一個。
        nums (int): 要隨機取出的姓名數量，預設為1。


    回傳:
        list[str]: 隨機取出的姓名列表。
    """
    with open(file_name, encoding="utf-8") as file:
        content: str = file.read()
        names: list[str] = content.split()
        return random.sample(names, nums)

def generate_scores_for_names(names: list[str]) -> list[dict]:

    """
    為每個姓名生成3個隨機分數。

    參數:
        names (list[str]): 姓名列表。

    回傳:
        list[dict]: 包含姓名和3個隨機分數的2維列表。
    """
    result_list = []
    for person_name in names:
        student_scores:dict = {"姓名":person_name}
        for subject in ["國文", "英文", "數學"]:
            student_scores[subject] = random.randint(50, 100) 
        result_list.append(student_scores)

    return result_list

def print_student_scores(students: list[dict]):

#todo:建立一個function,傳入students:list[dict]
#功能:列印出學生姓名和分數,並且增加平均分數
    """
    列印學生姓名和分數，並計算平均分數。

    參數:
        students (list[dict]): 學生分數列表。
    
    回傳:
        None
    """

    print("學生成績表:")
    print("姓名\t國文\t英文\t數學\t平均分數")
    for student in students:
        name = student["姓名"]
        scores:list[int] = [student[subject] for subject in ["國文", "英文", "數學"]]
        average = sum(scores) / len(scores)
        print(f"{name}\t{scores[0]}\t{scores[1]}\t{scores[2]}\t{average:.2f}")

def analyze_scores(students: list[dict]):
    """
    成績分析功能：
    傳入學生分數列表，計算並列印全班平均分數、最高分學生、最低分學生。

    參數:
        students (list[dict]): 學生分數列表。

    回傳:
        None
    """
    # 計算每位學生的平均分數
    averages = []
    for student in students:
        scores = [student[subject] for subject in ["國文", "英文", "數學"]]
        avg = sum(scores) / len(scores)
        averages.append({"姓名": student["姓名"], "平均分數": avg})

    # 全班平均分數
    class_avg = sum([item["平均分數"] for item in averages]) / len(averages)

    # 最高分學生
    max_student = max(averages, key=lambda x: x["平均分數"])
    # 最低分學生
    min_student = min(averages, key=lambda x: x["平均分數"])

    print("成績分析:")
    print(f"- 全班平均成績:{class_avg:.1f}分")
    print(f"- 最高分學生: {max_student['姓名']}({max_student['平均分數']:.1f}分)")
    print(f"- 最低分學生: {min_student['姓名']}({min_student['平均分數']:.1f}分)")

def main():
    print("=== 學生管理系統 ===\n\n")
    names: list[str] = sample_names_from_file("names.txt", nums=3)
    students: list[dict] = generate_scores_for_names(names)
    print_student_scores(students)
    analyze_scores(students)


if __name__ == "__main__":
    main()