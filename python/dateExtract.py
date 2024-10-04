import datetime
class dateExtract:
    def __init__(self) -> None:
        pass

    def dateExt(self):
        exam_extract_date = (11, 12, 2024)
        d = datetime.datetime(exam_extract_date[2], exam_extract_date[1], exam_extract_date[0])
        print("The examination will start from : ", d)
        print("The examination will start from : %i/%i/%i " % exam_extract_date)


dt = dateExtract()
dt.dateExt()
