"""
Application for Pomerleau: Training Coordinator (Training Administrator), Talent, Culture and Leadership team.
Montreal, hybrid (corporate role), full-time. LinkedIn job 4474490182, first seen 2026-10-14. No deadline or
salary stated. Asks for 2-5 years in administration, training and development or HR administration; LMS
knowledge (Cornerstone an asset); Microsoft Office; "champion a learner mindset in testing and adopting new
AI technologies". English posting.

Output (docx/): pomerleau_trainingcoord_application.docx / .pdf
  Page 1   : cover letter in ENGLISH
  Pages 2-3: CV in ENGLISH

Company fact verified on pomerleau.ca (article "Pomerleau redefines continuing training in companies",
29 Aug 2019): PX3 launched as a pan-Canadian training ecosystem with a training centre in Quebec City, part of
the FOX transformation program. Not used: employee/site counts (not re-verified), "Top 100 Employers" (posting).

Gaps stated in the letter, NOT claimed on the CV: Cornerstone, vendor management and invoicing for corporate
training programs, ROI evaluation of training programs. Moodle admin tasks are claimed as Moodle tasks
(users, enrolments, reports), consistent with the INS application. The role is below the candidate's recent
level; the letter says so briefly.
"""
import os
from app_render import build_all
from generate_brp_datagov_advisor import ADDITIONAL, EDUCATION, PUBLICATIONS

os.makedirs("docx", exist_ok=True)

PARAS = [
    "I am applying for the Training Coordinator position on the Talent, Culture and Leadership team. The role "
    "combines three things I have done in practice: coordinating workshops and training sessions from invitation "
    "to follow-up, administering a learning management system, and giving learners and colleagues a clear first "
    "point of contact. I am also interested in the posting's call to test and adopt new AI technologies.",

    "Pomerleau launched PX3 as a pan-Canadian training ecosystem with a dedicated training centre in Quebec "
    "City, and I would like to support a team that treats training as a company-wide investment. Most of my "
    "work has been in teams like that: I have worked in LMS and training roles, from administering Moodle "
    "for government clients at Premergency, to developing LMS features at KnowledgeOne, to designing a "
    "self-serve Moodle education portal at The Neuro (McGill University).",

    "On coordination, I designed and ran training workshops for faculty and graduate students at the Tanenbaum "
    "Open Science Institute, and I founded and ran a neighbourhood arts school that hosted 150 workshop groups "
    "with 20 teachers, which meant coordinating schedules, teachers and participants. On the LMS side, my "
    "Moodle work covers enrolments, reporting and keeping course content current. I evaluated and adopted AI tools, including Claude Code, in enterprise learning contexts "
    "at KnowledgeOne.",

    "I want to be direct about the gaps. I have not used Cornerstone, and I have not managed external training "
    "vendors, invoicing or ROI evaluation of programs, so those are areas where I would learn your process "
    "first. I also recognize that this role is more administrative than my recent contracts, and I am applying "
    "knowing that, because I want a stable role inside a training team and I am comfortable doing the "
    "detailed, service-oriented work it requires.",

    "I am bilingual in English and French, based in Montreal, available now, and comfortable with a hybrid "
    "model. I would welcome the chance to discuss how I can support your training team. Thank you for your "
    "consideration.",
]

PROFILE = (
    "Learning technology and training professional with hands-on Moodle administration and development "
    "experience, workshop design and delivery, and knowledge-base writing. Coordinates between learners, "
    "trainers and developers, documents processes, and answers questions from non-technical users. Evaluated "
    "AI tools in enterprise learning contexts, including Claude Code. Proficient in Microsoft Office. "
    "Bilingual (EN/FR), Montreal-based."
)

COMPETENCIES = [
    ("LMS administration",
     ": Moodle administration and development; users, enrolments, usage reporting and "
     "content maintenance; migration of legacy LMS content to Moodle"),
    ("Training coordination",
     ": designed and delivered workshops for faculty and students; ran a school hosting 150 workshop "
     "groups with 20 teachers, coordinating schedules, teachers and participants"),
    ("Training content and resources",
     ": designed workshops, user guides and a public knowledge base on data management and open science"),
    ("Service and first-line support",
     ": first point of contact for researchers and staff; answered requests and routed questions to the "
     "right specialists"),
    ("Reporting",
     ": Excel, SQL, Python, R and Tableau; usage and participation reporting for stakeholders"),
    ("AI adoption",
     ": evaluated and adopted AI tools in enterprise learning contexts, including Claude Code; bilingual "
     "(EN/FR) communication"),
]

EXPERIENCE = [
    ("07/2025 – 01/2026", "Moodle Analyst", "Premergency Inc.", "Canada", [
        "Coordinated between client and development teams to deliver LMS solutions for government clients",
        "Migrated legacy LMS systems to Moodle and designed bespoke learning and development solutions for clients",
        "Managed regulatory compliance requirements for government LMS deployments",
    ]),
    ("01/2024 – 10/2024", "Full Stack Developer", "KnowledgeOne", "Montreal, QC", [
        "Developed LMS features for active clients in LAMP++, Moodle, and LXD",
        "Evaluated and adopted AI tools in enterprise learning contexts, including Claude Code",
    ]),
    ("08/2020 – 10/2021", "Data Management and Sharing Coordinator (p/t)", "Tanenbaum Open Science Institute, The Neuro, McGill University", "Montreal, QC", [
        "Designed and administered training workshops for faculty and students",
        "Built an online knowledge base that translates open science concepts into practical guidance for non-specialists",
    ]),
    ("09/2016 – 10/2021", "Manager of Data Resources", "McConnell Brain Imaging Centre, The Neuro, McGill University", "Montreal, QC", [
        "Designed and launched a Moodle-based self-serve education portal",
        "Trained researchers and staff through hands-on workshops, guides, and communities of practice",
        "Managed data workflows for one of Canada's leading brain imaging centres, supporting dozens of principal investigators and hundreds of researchers",
    ]),
]

SKILLS = ("Moodle, LXD, Microsoft Office (Excel, Word, PowerPoint, Teams), SQL, Python, R, Tableau, Git, Docker, "
          "AWS, Azure, SSO, LDAP, Drupal, WordPress, Agile/Scrum, training design and facilitation.")

if __name__ == "__main__":
    build_all(dict(
        out="docx/pomerleau_trainingcoord_application",
        cover=dict(contact="Montreal, Quebec  |  514-475-2374  |  ted.strauss@gmail.com  |  linkedin.com/in/tedstrauss-63b01821",
                   date="October 15, 2026",
                   subject="Subject: Application: Training Coordinator",
                   salutation="Dear Hiring Team,", paras=PARAS,
                   closing="Kind regards,"),
        cv=dict(profile=PROFILE, competencies=COMPETENCIES, experience=EXPERIENCE, additional=ADDITIONAL,
                education=EDUCATION, skills=SKILLS, publications=PUBLICATIONS)))
