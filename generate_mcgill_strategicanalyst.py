"""
Application for McGill University: Strategic Initiatives Analyst (JR0000082141), Vice-President (Research and
Innovation) portfolio, Research Systems and Planning team, James Admin. Bldg., Montreal. Full-time, MPEX Grade 05
$73,470-$110,210, up to 2 remote days/week, term ending 2027-10-31, deadline to apply 2026-10-27. English level 4.
Posting text pulled from McGill's own Workday API (not an aggregator).

Output (docx/): mcgill_strategicanalyst_application.docx / .pdf
  Page 1   : cover letter in ENGLISH (McGill is an English-language university)
  Pages 2-3: CV in ENGLISH

All company/role content comes from the posting itself; no outside company claims are made.

Gaps stated in the letter, NOT claimed on the CV: research-funding administration inside a VP Research office
(Tri-Agencies, CRC, CFI, Research Support Fund), Power BI/DAX. Not claimed anywhere: Oracle, SharePoint/Lists,
qualitative analysis tools, named bibliometric platforms (the profile lists "bibliometrics" only).
"""
import os
from app_render import build_all
from generate_brp_datagov_advisor import ADDITIONAL, EDUCATION, PUBLICATIONS

os.makedirs("docx", exist_ok=True)

PARAS = [
    "I am applying for the Strategic Initiatives Analyst position in the Research Systems and Planning team. The "
    "role rests on three things I have done in McGill's research environment: keeping data trustworthy through "
    "shared definitions and governance, turning research data into analysis that supports decisions, and teaching "
    "people to use it. For five years I managed data resources at the McConnell Brain Imaging Centre (The Neuro, "
    "McGill University), supporting dozens of principal investigators and hundreds of researchers.",

    "Your posting asks for business glossaries, data dictionaries, standardized definitions and sources, and "
    "stewardship practices promoted through training and documentation. At McConnell I defined metadata "
    "standards, data definitions, stewardship roles and lifecycle policies, and built them into the daily "
    "acquisition workflow instead of issuing them as separate policy documents. I then taught them through "
    "workshops, guides, and a public knowledge base, and I worked with Collibra for cataloguing. A unit that "
    "makes strategic metrics report consistently across a whole research sector is where this approach pays off.",

    "I also know the Canadian research ecosystem from the inside. I represented the centre on Portage, the "
    "Canadian Open Neuroscience Platform and the Research Data Alliance, contributing to national research "
    "policy, and I have nine publications (citation count 630, h-index 9), so I understand research impact "
    "indicators as a producer as well as a user, and I can explain their appropriate use. For analysis and "
    "reporting I work in SQL, Python (pandas, plotly), R and Tableau, and I enjoy making data legible for "
    "audiences who need an answer rather than a method.",

    "I want to be direct about the gaps. I have not worked inside a vice-president's research office, so "
    "funding-program data (Tri-Agencies, CRC, CFI, Research Support Fund reporting) is where I would learn "
    "fastest, helped by my familiarity with the policy side. My dashboard work has been in Tableau, Python and "
    "R, and Power BI with DAX would be new to me.",

    "I am bilingual in English and French, I live in Montreal, and I hold a McGill B.A. (Honours). I would "
    "welcome the opportunity to discuss how I can support the Research and Innovation sector's reporting and "
    "data practices. Thank you for your consideration.",
]

PROFILE = (
    "Research data governance and analytics professional with five years managing data resources at the "
    "McConnell Brain Imaging Centre (The Neuro, McGill University). Defined metadata standards, data "
    "definitions and stewardship practices, and trained researchers to apply them. Represented the centre on "
    "national bodies (Portage, CONP, RDA). Nine publications (citation count 630, h-index 9). Analysis and "
    "reporting in SQL, Python, R and Tableau. Bilingual (EN/FR), Montreal-based, McGill alumnus."
)

COMPETENCIES = [
    ("Data quality and governance",
     ": defined metadata standards, data definitions, stewardship roles and lifecycle policies for a "
     "national-scale research data environment; worked with Collibra for cataloguing"),
    ("Data analysis and reporting",
     ": SQL (MySQL, PostgreSQL), Python (pandas, plotly), R and Tableau; built data pipelines and "
     "research applications; communicated findings to technical and non-technical audiences"),
    ("Research data management",
     ": managed data workflows for dozens of principal investigators and hundreds of researchers; built "
     "self-serve data portals; contributed to the Canadian Open Neuroscience Platform"),
    ("Research ecosystem and impact",
     ": represented the centre on Portage, CONP and the Research Data Alliance; nine publications, "
     "citation count 630, h-index 9; experience with bibliometrics and grant writing"),
    ("Training and documentation",
     ": designed and delivered workshops, user guides and a public knowledge base on data management and "
     "open science"),
    ("Stakeholder collaboration",
     ": coordinated standards across institutions and units without hierarchical authority; "
     "bilingual (EN/FR) communication"),
]

EXPERIENCE = [
    ("09/2016 – 10/2021", "Manager of Data Resources", "McConnell Brain Imaging Centre, The Neuro, McGill University", "Montreal, QC", [
        "Managed data workflows for one of Canada's leading brain imaging centres, supporting dozens of principal investigators and hundreds of researchers",
        "Defined metadata standards, data definitions, stewardship workflows and lifecycle policies, and built them into the daily acquisition workflow; worked with Collibra for cataloguing",
        "Developed brain imaging data pipelines and data-centric research applications; launched an OwnCloud portal for self-serve data management",
        "Trained researchers and staff through hands-on workshops, guides and communities of practice; designed a Moodle-based self-serve education portal",
        "Represented the centre on Portage, CONP and Research Data Alliance committees, contributing to national research policy",
    ]),
    ("08/2020 – 10/2021", "Data Management and Sharing Coordinator (p/t)", "Tanenbaum Open Science Institute, The Neuro, McGill University", "Montreal, QC", [
        "Supported the launch of a new academic unit focused on Open Science; designed and administered training workshops on data management practices",
        "Built an online knowledge base translating open science and data management concepts into practical guidance for non-specialists",
    ]),
    ("07/2025 – 01/2026", "Moodle Analyst", "Premergency Inc.", "Canada", [
        "Coordinated between client and development teams to deliver LMS solutions for government clients",
        "Managed regulatory compliance requirements for government LMS deployments",
    ]),
    ("01/2024 – 10/2024", "Full Stack Developer", "KnowledgeOne", "Montreal, QC", [
        "Developed LMS features for active clients in LAMP++, Moodle and LXD",
        "Evaluated and adopted AI tools in enterprise learning contexts, including Claude Code",
    ]),
]

SKILLS = ("SQL, Python (pandas, plotly), R, Tableau, Collibra, Git, Docker, AWS, Azure, SSO, LDAP, Moodle, "
          "OwnCloud, Drupal, Agile/Scrum, bibliometrics, training design and facilitation.")

if __name__ == "__main__":
    build_all(dict(
        out="docx/mcgill_strategicanalyst_application",
        cover=dict(contact="Montreal, Quebec  |  514-475-2374  |  ted.strauss@gmail.com  |  linkedin.com/in/tedstrauss-63b01821",
                   date="October 13, 2026",
                   subject="Subject: Application: Strategic Initiatives Analyst (JR0000082141)",
                   salutation="Dear Selection Committee,", paras=PARAS,
                   closing="Sincerely,"),
        cv=dict(profile=PROFILE, competencies=COMPETENCIES, experience=EXPERIENCE, additional=ADDITIONAL,
                education=EDUCATION, skills=SKILLS, publications=PUBLICATIONS)))
