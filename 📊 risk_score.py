def calculate_risk(iam_issues, s3_issues, sg_issues):
    score = iam_issues * 3 + s3_issues * 3 + sg_issues * 4

    print("=== Risk Score ===")
    print("Total Risk Score:", score)

    if score > 10:
        print("🔴 High Risk")
    elif score > 5:
        print("🟠 Medium Risk")
    else:
        print("🟢 Low Risk")
