#有一個names.txt
#讀取names.txt
#請隨機取出3個名字
import random

# 科目列表常數
SUBJECTS = ["國文", "英文", "數學"]


random.seed(4561)  # 固定亂數種子，確保結果可重現

def sample_names_from_file(file_name: str, nums: int = 1) -> list[str]:
    """
    從指定的檔案中讀取所有姓名，並隨機取出指定數量的姓名。

    參數:
        file_name (str): 檔案名稱，檔案內容為姓名，每行一個。
        nums (int): 要隨機取出的姓名數量，預設為1。


    回傳:
        list[str]: 隨機取出的姓名列表。
    """
    try:
        with open(file_name, encoding="utf-8") as file:
            content: str = file.read()
            names: list[str] = content.split()
            if len(names) < nums:
                raise ValueError("檔案中的姓名數量不足以隨機取出指定數量。")
            return random.sample(names, nums)
    except FileNotFoundError:
        print(f"檔案不存在: {file_name}")
        return []
    except Exception as e:
        print(f"讀取檔案時發生錯誤: {e}")
        return []

def generate_scores_for_names(names: list[str], min_score: int = 50, max_score: int = 100) -> list[dict]:

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
        for subject in SUBJECTS:
            student_scores[subject] = random.randint(min_score, max_score)
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
    header = "姓名" + "\t" + "\t".join(SUBJECTS) + "\t平均分數"
    print(header)
    for student in students:
        name = student["姓名"]
        scores:list[int] = [student[subject] for subject in SUBJECTS]
        average = sum(scores) / len(scores)
        # 使用欄寬對齊，避免排版亂掉
        print(f"{name:<6}\t" + "\t".join(f"{score:>3}" for score in scores) + f"\t{average:6.2f}")

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
    if not students:
        print("無學生資料可分析。")
        return

    student_averages = []
    highest_student = None
    lowest_student = None

    for student in students:
        scores = [student[subject] for subject in SUBJECTS]
        average_score = sum(scores) / len(scores)
        student_averages.append(average_score)

        if not highest_student or average_score > highest_student["average"]:
            highest_student = {"name": student["姓名"], "average": average_score}

        if not lowest_student or average_score < lowest_student["average"]:
            lowest_student = {"name": student["姓名"], "average": average_score}

    class_average = sum(student_averages) / len(student_averages)

    print("成績分析:")
    print(f"- 全班平均分數:{class_average:.1f}分")
    print(f"- 最高分學生: {highest_student['name']}({highest_student['average']:.1f}分)")
    print(f"- 最低分學生: {lowest_student['name']}({lowest_student['average']:.1f}分)")

def main():
    print("=== 學生管理系統 ===\n\n")
    names: list[str] = sample_names_from_file("names.txt", nums=3)
    if not names:
        print("無法取得學生名單，程式結束。")
        return
    students: list[dict] = generate_scores_for_names(names)
    print_student_scores(students)
    analyze_scores(students)


if __name__ == "__main__":
    main()