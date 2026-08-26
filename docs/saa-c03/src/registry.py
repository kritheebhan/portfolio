"""
Placeholder registry for future experiment chapters.

Experiment body text is added only after the learner supplies notes or
screenshots. This file stores index metadata used by the document builder.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ExperimentRecord:
    number: int
    name: str
    status: str
    course_section: str = "[Verification required]"
    primary_service: str = "[Verification required]"
    exam_domains: str = "[Verification required]"
    region: str = "[Verification required]"
    difficulty: str = "[Verification required]"
    notes_received: bool = False
    screenshots_received: bool = False
    errors_received: bool = False


EXPERIMENTS: list[ExperimentRecord] = [
    ExperimentRecord(
        number=1,
        name="Not yet named",
        status="Awaiting notes and screenshots",
    )
]


DOCUMENT = {
    "title": "AWS Certified Solutions Architect – Associate (SAA-C03): Practical Experiments and Study Guide",
    "short_title": "SAA-C03 Practical Experiments and Study Guide",
    "version": "0.1",
    "edition": "Foundation edition",
    "date": "26 August 2026",
    "learner": "Kritheebhan",
    "status": "Awaiting Experiment 1 materials",
}
