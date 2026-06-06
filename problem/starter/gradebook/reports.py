"""gradebook.reports — build a printable report from grade records."""

# TODO: use a RELATIVE import to pull from the sibling stats module.
# from .stats import average_per_student, subjects_offered, top_scorer, passing_students


def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.

    The report MUST include:
      - Total number of records
      - Sorted list of subjects offered
      - Average score for each student (alphabetical order)
      - The top scorer (name + average)
      - The list of passing students (threshold 60.0)
    """
    # TODO: implement
    pass
"""gradebook.reports — build a printable report from grade records."""

# Relative import
from .stats import (
    average_per_student,
    subjects_offered,
    top_scorer,
    passing_students,
)


def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.
    """

    report = []

    # Total records
    report.append(f"Total Records: {len(records)}")

    # Subjects offered
    subjects = subjects_offered(records)
    report.append(f"Subjects Offered: {', '.join(subjects)}")

    # Average score per student
    report.append("\nAverage Score Per Student:")
    averages = average_per_student(records)

    for student in sorted(averages):
        report.append(f"{student}: {averages[student]:.2f}")

    # Top scorer
    name, avg = top_scorer(records)
    report.append(f"\nTop Scorer: {name} ({avg:.2f})")

  
    passing = passing_students(records)
    report.append(f"Passing Students: {', '.join(passing)}")

    return "\n".join(report)