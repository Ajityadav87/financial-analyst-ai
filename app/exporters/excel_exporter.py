import pandas as pd


def generate_excel_report(
    data,
    output_path
):

    df = pd.DataFrame(data)

    df.to_excel(
        output_path,
        index=False
    )

    print(
        f"\nExcel saved at: {output_path}"
    )