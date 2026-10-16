"""
Application for: Remote Data Governance Specialist (Toronto-based SaaS client of recruiter
Bilinguallink / STACK IT). Remote, $120,000-150,000 posted. Posting source: freehire/whatjobs
aggregator listing of 2026-10-06. The end employer is unnamed, so the letter makes NO
company-specific claims; it speaks only to the role as the posting describes it.

Output (docx/): stackit_datagov_specialist_application.docx / .pdf  (EN letter + EN CV)

Targeting: leads with embedding governance in daily workflows and influence/communication (the
posting's emphasis), building a function from scratch (TOSI launch), Collibra, AI tool adoption.
Gaps stated in the letter, NOT claimed on the CV: Snowflake/Databricks, GDPR/CCPA specifics,
SaaS / financial-planning domain, preparing ML-ready data.
"""
import os
from app_render import build_all
from generate_brp_datagov_advisor import ADDITIONAL, EDUCATION, PUBLICATIONS

os.makedirs("docx", exist_ok=True)

PARAS = [
    "I am applying for the Data Governance Specialist role with your Toronto-based SaaS client. The posting "
    "describes governance that is \"not a checkbox\" exercise: standards embedded in day-to-day workflows rather "
    "than policies on paper, built through influence across teams. That is how I ran data governance for five "
    "years as Manager of Data Resources at the McConnell Brain Imaging Centre (The Neuro, McGill University), "
    "one of Canada's leading brain imaging centres.",

    "At McConnell I defined metadata standards, data definitions and lifecycle policies for dozens of "
    "principal investigators and hundreds of researchers, and I built them into the daily acquisition workflow "
    "so that following the standard was the easy path. I worked with Collibra and with access tooling (LDAP, "
    "SSO), and I grew adoption through hands-on workshops, a public knowledge base and communities of practice, "
    "because researchers adopt standards that make their own work easier. I also supported the launch of a new "
    "academic unit, the Tanenbaum Open Science Institute, so I have built a function from a blank page, "
    "which matters for a role the posting calls newly created.",

    "The posting stresses that the job is as much communication as data. Much of my career has been spent "
    "translating between technical teams and institutional or policy stakeholders: representing the centre on "
    "national bodies (Portage, CONP and the Research Data Alliance) and coordinating with people who did not "
    "report to me. On AI, I evaluated and adopted AI tools in enterprise settings, including Claude Code, "
    "weighing data handling and governance implications alongside the productivity case, which is the "
    "judgment I would bring to making data ready for AI use.",

    "I want to be direct about my gaps. I have worked in research rather than a commercial SaaS or financial "
    "analytics setting. My platform experience is with AWS and Azure, SQL, Python and Git rather than "
    "Snowflake or Databricks. My privacy and regulatory exposure is through government compliance "
    "requirements and research data privacy, not GDPR or CCPA programs specifically, and I have not prepared "
    "data for machine learning use cases myself. I learn platforms quickly, and I would start by learning "
    "your data landscape before proposing changes.",

    "I am based in Montreal, in the same time zone as Toronto, bilingual in French and English, and available "
    "immediately for a remote role. I would welcome the opportunity to discuss how I can help build your "
    "governance function. Thank you for your consideration.",
]

PROFILE = (
    "Data governance specialist who embeds standards in daily workflows and gets data owners to adopt them. "
    "Led data governance and metadata management at the McConnell Brain Imaging Centre (The Neuro, McGill "
    "University): defined data definitions, stewardship workflows and lifecycle policies, worked with "
    "Collibra, SSO and LDAP, and contributed to national data governance bodies (Portage, CONP, RDA). "
    "Has built a new function from scratch (Tanenbaum Open Science Institute launch) and bridges technical "
    "and institutional stakeholders. Bilingual (EN/FR), Montreal-based, remote-ready."
)

COMPETENCIES = [
    ("Data governance frameworks and stewardship",
     ": defined metadata standards, data definitions, classification and lifecycle policies, and "
     "stewardship workflows for a national-scale research data environment"),
    ("Embedding governance in daily workflows",
     ": built standards into the daily acquisition workflow and self-serve portals so that compliance was "
     "the easy path; grew adoption through training and communities of practice"),
    ("Stakeholder influence",
     ": coordinated standards across institutions that did not report to me (Portage, CONP, Research Data "
     "Alliance); translated between technical teams and institutional or policy stakeholders"),
    ("Data tools and platforms",
     ": Collibra, OwnCloud, LDAP, SSO; SQL, Python, R, Git; AWS and Azure; data pipelines and data "
     "applications in LAMP++"),
    ("Building a new function",
     ": supported the launch of a new academic unit focused on Open Science, including training workshops "
     "and a public knowledge base"),
    ("AI adoption and governance",
     ": evaluated and adopted AI tools in enterprise settings, including Claude Code, assessing data "
     "handling and governance implications alongside the productivity case"),
]

EXPERIENCE = [
    ("09/2016 – 10/2021", "Manager of Data Resources", "McConnell Brain Imaging Centre, The Neuro, McGill University", "Montreal, QC", [
        "Led data governance and metadata management for one of Canada's leading brain imaging centres, supporting dozens of principal investigators and hundreds of researchers",
        "Defined metadata standards, data definitions, and lifecycle policies, and built them into the daily acquisition workflow rather than issuing them as separate policy documents",
        "Worked across Collibra, OwnCloud, LDAP, and SSO to support access control, roles, and self-serve data management; developed brain imaging data pipelines in an Agile team",
        "Grew governance adoption through hands-on training and communities of practice rather than enforcement",
        "Represented the centre on Portage, CONP, and Research Data Alliance committees, contributing to national research policy",
    ]),
    ("08/2020 – 10/2021", "Data Management and Sharing Coordinator (p/t)", "Tanenbaum Open Science Institute, The Neuro, McGill University", "Montreal, QC", [
        "Supported the launch of a new academic unit focused on Open Science; designed and administered training workshops on data management practices",
        "Built an online knowledge base translating open science and data management requirements into practical guidance for non-specialists",
    ]),
    ("07/2025 – 01/2026", "Moodle Analyst", "Premergency Inc.", "Canada", [
        "Coordinated between client and development teams to deliver LMS solutions for government clients",
        "Managed regulatory compliance requirements for government LMS deployments; migrated legacy LMS systems to Moodle",
    ]),
    ("01/2024 – 10/2024", "Full Stack Developer", "KnowledgeOne", "Montreal, QC", [
        "Developed LMS features for active clients in LAMP++, Moodle, and LXD",
        "Evaluated and adopted AI tools in enterprise learning contexts, including Claude Code",
    ]),
]

SKILLS = ("Collibra, SQL, Python, R, Git, Docker, Kubernetes, AWS, Azure, SSO, LDAP, Moodle, OwnCloud, "
          "Drupal, Tableau, Agile/Scrum.")

if __name__ == "__main__":
    build_all(dict(
        out="docx/stackit_datagov_specialist_application",
        cover=dict(contact="Montreal, Quebec  |  514-475-2374  |  ted.strauss@gmail.com  |  linkedin.com/in/tedstrauss-63b01821",
                   date="October 8, 2026",
                   subject="Subject: Application: Data Governance Specialist (Remote, Toronto-based SaaS)",
                   salutation="Dear Hiring Team,", paras=PARAS, closing="Kind regards,"),
        cv=dict(profile=PROFILE, competencies=COMPETENCIES, experience=EXPERIENCE, additional=ADDITIONAL,
                education=EDUCATION, skills=SKILLS, publications=PUBLICATIONS)))
