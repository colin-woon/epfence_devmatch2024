def check_contribution(employer_cont, employee_cont):
    if employee_cont == "Yes" and employer_cont == "Yes":
        return True
    return False


def highlight_rows_report(row):
    color = (
        "background-color: yellow;"
        if row["Type"] == "Report"
        else "background-color: white;"
    )
    return [color] * len(row)


def highlight_rows_penalty(row):
    color = (
        "background-color: red;"
        if row["Type"] == "Penalty"
        else "background-color: green;"
    )
    return [color] * len(row)
