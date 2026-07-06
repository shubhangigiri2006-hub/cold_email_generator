from typing import Dict, Optional
from agents.llm_client import complete

WRITER_SYSTEM_PROMPT = """You are an expert B2B cold-email copywriter working for {org_name}.
Write concise, professional, personalized emails. Never sound like a generic template.
Always ground specific claims in the CONTEXT provided -- don't invent facts about the
recipient company that aren't given to you.

Output format (strict):
SUBJECT: <one line subject>
BODY:
<email body, 120-180 words, professional tone, ends with a clear call to action and the sender's name/title>
"""


def _format_company_context(company_context: Optional[Dict]) -> str:
    if not company_context:
        return "No specific data available about the recipient company."
    lines = [f"Company: {company_context.get('company_name', 'Unknown')}"]
    if company_context.get("industry"):
        lines.append(f"Industry: {company_context['industry']}")
    if company_context.get("services"):
        lines.append(f"Known services: {', '.join(company_context['services'])}")
    if company_context.get("trust_score") is not None:
        lines.append(f"Market trust score (0-10): {company_context['trust_score']}")
    if company_context.get("market_evaluation"):
        lines.append(f"Market evaluation: {company_context['market_evaluation']}")
    return "\n".join(lines)


class WriterAgent:
    def draft(
        self,
        purpose: str,
        org_profile: Dict,
        company_context: Optional[Dict] = None,
        email_type: str = "request_service",
    ) -> str:
        system = WRITER_SYSTEM_PROMPT.format(org_name=org_profile.get("name", "our organization"))

        user_prompt = f"""
EMAIL TYPE: {email_type}
PURPOSE / INTENT (from admin): {purpose}

SENDER ORGANIZATION PROFILE:
Name: {org_profile.get('name')}
Website: {org_profile.get('website')}
Services offered: {org_profile.get('services')}
Description: {org_profile.get('description')}
Sender: {org_profile.get('sender_name')} ({org_profile.get('sender_title')})

RECIPIENT CONTEXT (retrieved via RAG):
{_format_company_context(company_context)}

Write the email now, following the required SUBJECT/BODY format.
"""
        return complete(system, user_prompt)

    def revise(self, previous_draft: str, reviewer_feedback: str, org_profile: Dict) -> str:
        system = WRITER_SYSTEM_PROMPT.format(org_name=org_profile.get("name", "our organization"))
        user_prompt = f"""
Here is your previous draft:
---
{previous_draft}
---

A reviewer gave this feedback:
---
{reviewer_feedback}
---

Revise the email to address the feedback. Keep the required SUBJECT/BODY format.
"""
        return complete(system, user_prompt)