"""
Application for INS Quebec: Administrateur(trice), plateforme d'apprentissage numerique (Docebo LMS).
Montreal (Parc olympique), permanent full-time, hybrid, $55,937-$78,978, start Nov 2026, posting closes
2026-10-19. Apply by email to rh@insquebec.org with the job title in the subject line. Posting text pasted
by the candidate.

Output (docx/): insquebec_lmsadmin_application.docx / .pdf
  Page 1   : cover letter in FRENCH (posting is French)
  Pages 2-3: CV in ENGLISH (per CV-language policy)

Company facts verified on insquebec.org (fetched 2026-10-13 with browser headers): mission "propulser la
performance humaine"; science, innovation, expertise, collaboration; 600+ high-level athletes, ~2,000
next-generation athletes, thousands of coaches and practitioners; expertise deployed across Quebec;
2026-2030 strategic plan announced 22 Sept 2026.

SCORM, Articulate 360 and Docebo experience is stated by the candidate (not in the profile files); it is
placed in skills/competencies, not attributed to a specific employer. xAPI is NOT claimed. Gaps stated in the
letter: Docebo is secondary to Moodle, sport-sector knowledge.
"""
import os
from app_render import build_all
from generate_brp_datagov_advisor import ADDITIONAL, EDUCATION, PUBLICATIONS

os.makedirs("docx", exist_ok=True)

PARAS = [
    "Je pose ma candidature au poste d'administrateur de la plateforme d'apprentissage numérique. Vous cherchez "
    "une référence technique principale, capable de configurer le LMS, d'y intégrer des contenus e-learning et "
    "d'expliquer le tout à des équipes non techniques. C'est le travail que je fais depuis plusieurs années, "
    "surtout avec Moodle, et j'ai aussi de l'expérience avec Docebo, SCORM et la suite Articulate 360.",

    "L'INS Québec a pour mission de propulser la performance humaine en misant sur la science, l'innovation, "
    "l'expertise et la collaboration, et son réseau soutient des milliers d'entraîneurs et d'intervenants partout "
    "au Québec. Une plateforme de formation bien structurée est un outil concret pour cette mission, et le "
    "lancement de votre plan stratégique 2026-2030 est le bon moment pour la faire évoluer. J'aime travailler "
    "dans une organisation à mandat public, au sein d'une équipe multidisciplinaire.",

    "Au cours de mes deux derniers contrats, j'ai travaillé directement sur des LMS. Comme analyste Moodle chez "
    "Premergency, j'ai assuré la coordination entre les clients et les équipes de développement, migré des "
    "systèmes d'apprentissage existants vers Moodle et géré les exigences de conformité de déploiements "
    "gouvernementaux. Chez KnowledgeOne, j'ai développé des fonctionnalités de LMS pour des clients actifs "
    "(Moodle, LAMP++), et j'ai évalué des outils d'IA en contexte de formation, dont Claude Code, ce qui rejoint "
    "votre volet de veille technologique. Au Centre d'imagerie cérébrale McConnell (Université McGill), j'ai conçu "
    "un portail de formation libre-service sur Moodle, relié à l'authentification unique (SSO) et à LDAP, puis "
    "formé les utilisateurs au moyen d'ateliers, de guides et d'une base de connaissances. J'analyse les "
    "données d'utilisation avec SQL, Python, R et Tableau, et mon développement web (HTML/CSS, jQuery, Bootstrap) "
    "me permet de diagnostiquer les problèmes d'intégration moi-même.",

    "Je veux être direct sur deux points. Docebo n'est pas ma plateforme principale : mon expérience la plus "
    "approfondie est avec Moodle, dont les notions d'administration (rôles, groupes, inscriptions, rapports, "
    "suivi de progression SCORM) se transposent bien. Je ne connais pas non plus le milieu sportif de "
    "l'intérieur; je compte sur ma capacité à comprendre rapidement les besoins de vos équipes de contenu et de "
    "vos concepteurs pédagogiques.",

    "Je suis bilingue en français et en anglais, je vis à Montréal et je suis disponible pour une entrée en "
    "fonction en novembre. Je serais heureux de discuter de la façon dont je peux soutenir votre plateforme et "
    "vos équipes. Merci de considérer ma candidature.",
]

PROFILE = (
    "LMS administrator and learning technologist with hands-on Moodle experience (migration, configuration, "
    "feature development, SSO/LDAP integration) and working experience with Docebo, SCORM and Articulate 360. "
    "Coordinates between non-technical content experts and developers, documents configurations, and trains "
    "internal users through workshops, guides and knowledge bases. Evaluated AI tools in enterprise learning "
    "contexts, including Claude Code. Bilingual (EN/FR), Montreal-based."
)

COMPETENCIES = [
    ("LMS administration",
     ": Moodle (main platform) and Docebo; users, roles, groups and enrolments, system configuration, "
     "usage reporting, vendor and incident follow-up"),
    ("E-learning content integration",
     ": SCORM packages and Articulate 360 content; functional and technical testing before release; "
     "diagnosing integration and tracking problems"),
    ("Platform architecture and web",
     ": LAMP++, HTML/CSS, jQuery, Bootstrap; SaaS and cloud environments (AWS, Azure); SSO and LDAP integration"),
    ("Data and reporting",
     ": SQL, Python, R, Tableau; usage and learning-data analysis for stakeholders"),
    ("Training and documentation",
     ": designed and delivered workshops, user guides and a public knowledge base; first-line support and "
     "internal training for non-technical users"),
    ("Technical coordination",
     ": coordinated clients, content experts and development teams across multiple concurrent deliverables "
     "in Agile settings; monitored LMS, e-learning and AI-tool developments"),
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
    ("09/2016 – 10/2021", "Manager of Data Resources", "McConnell Brain Imaging Centre, The Neuro, McGill University", "Montreal, QC", [
        "Designed and launched a Moodle-based self-serve education portal; integrated platforms with SSO and LDAP",
        "Launched an OwnCloud portal for self-serve data management and built data-centric research applications in LAMP++",
        "Trained researchers and staff through hands-on workshops, guides, and communities of practice",
        "Managed data workflows for one of Canada's leading brain imaging centres, supporting dozens of principal investigators and hundreds of researchers",
    ]),
    ("08/2020 – 10/2021", "Data Management and Sharing Coordinator (p/t)", "Tanenbaum Open Science Institute, The Neuro, McGill University", "Montreal, QC", [
        "Designed and administered training workshops for faculty and students",
        "Built an online knowledge base that translates open science concepts into practical guidance for non-specialists",
    ]),
]

SKILLS = ("Moodle, Docebo, SCORM, Articulate 360, LXD, HTML/CSS, PHP, JavaScript/jQuery, Bootstrap, SQL, Python, R, "
          "Tableau, Git, Docker, AWS, Azure, SSO, LDAP, Drupal, WordPress, Agile/Scrum, training design and "
          "facilitation.")

if __name__ == "__main__":
    build_all(dict(
        out="docx/insquebec_lmsadmin_application",
        cover=dict(contact="Montréal (Québec)  |  514-475-2374  |  ted.strauss@gmail.com  |  linkedin.com/in/tedstrauss-63b01821",
                   date="13 octobre 2026",
                   subject="Objet : Candidature au poste d'administrateur·trice, plateforme d'apprentissage numérique",
                   salutation="Madame, Monsieur,", paras=PARAS,
                   closing="Veuillez agréer, Madame, Monsieur, mes salutations distinguées,"),
        cv=dict(profile=PROFILE, competencies=COMPETENCIES, experience=EXPERIENCE, additional=ADDITIONAL,
                education=EDUCATION, skills=SKILLS, publications=PUBLICATIONS)))
