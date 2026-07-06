import re
from typing import Dict, Optional, Tuple

from agents.writer_agent import WriterAgent
from agents.reviewer_agent import ReviewerAgent
from config import MAX_REVIEW_ITERATIONS


def parse_subject_body(raw: str) -> Tuple[str, str]:
    subject_match = re.search(r"SUBJECT:\s*(.+)", raw)
    body_match = re.search(r"BODY:\s*(.+)", raw, re.DOTALL)
    subject = subject_match.group(1).strip() if subject_match else "Regarding a potential collaboration"
    body = body_match.group(1).strip() if body_match else raw.strip()
    return subject, body


class EmailOrchestrator:
    def __init__(self):
        self.writer = WriterAgent()
        self.reviewer = ReviewerAgent()

    def generate_email(
        self,
        purpose: str,
        org_profile: Dict,
        company_context: Optional[Dict] = None,
        email_type: str = "request_service",
        verbose: bool = True,
    ) -> Dict:
        draft = self.writer.draft(purpose, org_profile, company_context, email_type)

        for iteration in range(1, MAX_REVIEW_ITERATIONS + 1):
            verdict = self.reviewer.review(draft, company_context)
            if verbose:
                print(f"  [reviewer pass {iteration}] approved={verdict['approved']}")
            if verdict["approved"]:
                break
            draft = self.writer.revise(draft, verdict["feedback"], org_profile)
        else:
            if verbose:
                print("  [orchestrator] max iterations reached, using last draft.")

        subject, body = parse_subject_body(draft)
        return {"subject": subject, "body": body, "raw": draft}