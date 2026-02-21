#intelligent_resume_analyzer_hidevs/
#│
#├── main.py
#├── parser.py
#├── matcher.py
#├── reporter.py
#├── ai_module.py
#├── sample.txt
#├── requirements.txt
#└── README.md

#RESUME TEXT 
#PARSER.AI
class Candidate:
    """
    Represents a job candidate with structured resume data.
    """

    def __init__(self, name, email, skills, experience, education):
        self.name = name
        self.email = email
        self.skills = skills
        self.experience = experience
        self.education = education


def parse_resume(text):
    """
    Parses raw resume text into a Candidate object.
    Expected format:
    Name: John Doe
    Email: john@email.com
    Skills: Python, SQL, Machine Learning
    Experience: 3
    Education: B.Tech
    """

    if not text.strip():
        raise ValueError("Resume text is empty.")

    lines = text.strip().split("\n")
    data = {}

    for line in lines:
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip().lower()] = value.strip()

    name = data.get("name", "Unknown")
    email = data.get("email", "Not Provided")

    skills_raw = data.get("skills", "")
    skills = [skill.strip().lower() for skill in skills_raw.split(",") if skill.strip()]

    try:
        experience = int(data.get("experience", 0))
    except ValueError:
        experience = 0

    education = data.get("education", "Not Provided")

    return Candidate(name, email, skills, experience, education)

#MATCHER.AI
JOB_REQUIREMENTS = {
    "python": 3,
    "machine learning": 2,
    "data analysis": 2,
    "sql": 2,
    "communication": 1,
    "teamwork": 1
}


def match_candidate(candidate):
    """
    Matches candidate skills with job requirements.
    Returns match score and missing skills.
    """

    score = 0
    matched_skills = []
    missing_skills = []

    total_possible = sum(JOB_REQUIREMENTS.values())

    for skill, weight in JOB_REQUIREMENTS.items():
        if skill in candidate.skills:
            score += weight
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    percentage = (score / total_possible) * 100
    percentage = round(percentage, 2)

    return percentage, matched_skills, missing_skills

#AI_MODULE
def generate_ai_suggestions(missing_skills, experience):
    """
    Simulates AI-based resume improvement suggestions.
    """

    suggestions = []

    if missing_skills:
        suggestions.append("Consider adding the following skills:")
        for skill in missing_skills:
            suggestions.append(f"- {skill}")

    if experience < 2:
        suggestions.append("Gain more practical experience through internships or projects.")

    if not suggestions:
        suggestions.append("Your resume looks strong for this position!")

    return suggestions

#REPORTER.py
def generate_report(candidate, score, matched, missing, suggestions):
    """
    Generates formatted output report.
    """

    print("\n========== RESUME ANALYSIS REPORT ==========")
    print(f"Name: {candidate.name}")
    print(f"Email: {candidate.email}")
    print(f"Education: {candidate.education}")
    print(f"Experience: {candidate.experience} years")

    print("\nMatched Skills:")
    if matched:
        for skill in matched:
            print(f"- {skill}")
    else:
        print("None")

    print("\nMissing Skills:")
    if missing:
        for skill in missing:
            print(f"- {skill}")
    else:
        print("None")

    print(f"\nMatch Score: {score}%")

    if score >= 75:
        print("Recommendation: Highly Suitable ✅")
    elif score >= 50:
        print("Recommendation: Moderately Suitable ⚠️")
    else:
        print("Recommendation: Not Suitable ❌")

    print("\nAI Suggestions:")
    for suggestion in suggestions:
        print(suggestion)

    print("============================================\n")
#MAIN PROGRAM 



def read_resume_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Error: Resume file not found.")
        return None


def main():
    print("=== Intelligent Resume Analyzer ===")

    file_path = input("Enter resume file path (e.g., sample_resume.txt): ")

    text = read_resume_file(file_path)

    if text:
        candidate = parse_resume(text)
        score, matched, missing = match_candidate(candidate)
        suggestions = generate_ai_suggestions(missing, candidate.experience)
        generate_report(candidate, score, matched, missing, suggestions)


if __name__ == "__main__":
    main()