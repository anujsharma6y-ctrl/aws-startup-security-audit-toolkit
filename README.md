# AWS Startup Security Audit Toolkit

A lightweight security audit toolkit designed to simulate a real-world AWS security review for early-stage startups.

## 🔍 Problem

Most early-stage startups focus heavily on product velocity and often overlook foundational cloud security configurations.

Misconfigurations — not advanced exploits — are the leading cause of breaches in cloud environments.

## 🎯 What This Toolkit Checks

- Over-permissive IAM users (AdministratorAccess detection)
- Public S3 bucket exposure
- Security groups open to 0.0.0.0/0
- Basic risk scoring model

## 🛠 Technologies Used

- Python
- Boto3
- AWS IAM
- AWS EC2
- AWS S3

## 🚀 How to Run

1. Configure AWS CLI credentials
2. Install requirements:
   pip install -r requirements.txt
3. Run scripts individually:
 python iam_audit.py python s3_audit.py python security_group_audit.py
## 📊 Risk Model

Risk score is calculated based on severity weight:
- IAM Issues (3 points each)
- S3 Exposure (3 points each)
- Security Group Exposure (4 points each)

## ⚠ Disclaimer

This toolkit is intended for educational and audit simulation purposes.

---

If you're building on AWS — audit before you scale.
⚖️ License & Legal Information
This project is primarily licensed under the MIT License, with specific modules covered under Apache 2.0 and GPL v3.

License: MIT License: Apache 2.0 License: GPL v3 Python 3.8+

Key Permissions:
✅ Commercial Use: You can use this code for business purposes.
✅ Modification: You can change the code however you like.
✅ Distribution: You can share the code with others.
✅ Private Use: You can use it privately.
Conditions:
⚠️ Notice: You must include the original copyright and license notice in any copy of the software/source code.
Warranty:
🛡️ No Warranty: The software is provided "as is", without any warranty of any kind. The author is not liable for any claims or damages.
For more details, view the Full LICENSE File

👨‍💻 Author Anuj Sharma AWS cloud Security Automation Enthusiast | IT Automation Specialist | Python for SecOps
