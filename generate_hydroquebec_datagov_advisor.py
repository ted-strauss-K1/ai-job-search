"""
Application for Hydro-Quebec: Conseiller(ere) Gestion donnees II - Gouvernance (competition 189169).
Montreal (1001 Robert-Bourassa), temporary / indefinite duration, 35 h/week, hybrid telework program,
salary $81,112-$135,187, posting closes 2026-10-19. Posting text pasted by the candidate.

Output (docx/): hydroquebec_datagov_advisor_application.docx / .pdf
  Page 1   : cover letter in FRENCH (posting is French)
  Pages 2-3: CV in ENGLISH (per CV-language policy)

Company facts verified on hydroquebec.com/about (fetched 2026-10-09): "over 75 years" generating,
transmitting and distributing electricity; clean, renewable energy. NOT used: the 1944 founding
year (only in the posting text and a social handle) or the "data as a strategic asset" claim as a
company fact (attributed to the posting instead).

Gaps stated in the letter, NOT claimed on the CV: 6-9 years bar (5 dedicated years), Microsoft
Purview / Unity Catalog, DAMA-DMBOK, translating Law 25 into controls.
"""
import os
from app_render import build_all
from generate_brp_datagov_advisor import ADDITIONAL, EDUCATION, PUBLICATIONS

os.makedirs("docx", exist_ok=True)

PARAS = [
    "Je pose ma candidature au poste de conseiller Gestion données II, Gouvernance (concours 189169). Votre "
    "affichage précise que les mécanismes de gouvernance permettent d'accélérer la valorisation des données de "
    "manière responsable : définir les processus et les principes, bâtir le référentiel et les normes de "
    "qualité, puis former et accompagner les gestionnaires pour que cela s'applique. C'est le travail que j'ai "
    "mené pendant cinq ans comme gestionnaire des ressources de données au Centre d'imagerie cérébrale McConnell "
    "(The Neuro, Université McGill), l'un des principaux centres d'imagerie cérébrale au Canada.",

    "Hydro-Québec produit, transporte et distribue de l'électricité propre et renouvelable depuis plus de 75 ans "
    "au service du Québec. Je suis attiré par les organisations à mandat public où la gouvernance des données "
    "doit gagner la confiance de nombreuses équipes, et où il faut mobiliser des parties prenantes sans lien "
    "d'autorité, ce que je fais depuis des années. Une division qui intègre la gouvernance dès la conception de "
    "projets technologiques d'envergure a besoin de quelqu'un qui sait la rendre applicable au quotidien.",

    "Au Centre McConnell, j'ai défini les normes de métadonnées, les définitions de données, les rôles "
    "d'intendance et les politiques de cycle de vie pour des dizaines de chercheurs principaux et des centaines "
    "de chercheurs, et je les ai intégrés au flux d'acquisition quotidien plutôt que de les émettre comme des "
    "documents de politique séparés. J'ai travaillé avec Collibra, LDAP et l'authentification unique (SSO), et "
    "j'ai fait adopter ces pratiques par la formation : ateliers pratiques, guides, base de connaissances "
    "publique et communautés de pratique. J'ai aussi représenté le centre au sein de Portage, du CONP et de la "
    "Research Data Alliance, où j'ai coordonné des normes avec des établissements qui ne relevaient pas de moi. "
    "Plus récemment, j'ai géré des exigences de conformité réglementaire pour des systèmes gouvernementaux et "
    "évalué des outils d'IA en contexte d'entreprise, dont Claude Code, en tenant compte du traitement des "
    "données.",

    "Je veux être direct sur les écarts avec votre affichage. Mon expérience de gouvernance s'est construite en "
    "recherche, avec cinq ans de travail dédié, en deçà de votre fourchette de 6 à 9 ans, complétée par du travail "
    "ultérieur en conformité et en plateformes. Je connais Collibra, mais je n'ai pas déployé Microsoft Purview "
    "ni Unity Catalog sur Databricks. Je n'ai pas appliqué formellement le cadre DAMA-DMBOK, et je n'ai pas "
    "traduit la Loi 25 en contrôles de gouvernance vérifiables; mon expérience réglementaire porte sur la "
    "conformité de systèmes gouvernementaux et sur la gouvernance des données de recherche. Je m'appuie sur ma "
    "pratique des principes (rôles, métadonnées, qualité, cycle de vie) pour monter rapidement en compétence "
    "sur ces éléments.",

    "Je suis bilingue en français et en anglais, avec une compétence professionnelle dans les deux langues, et je "
    "vis à Montréal. J'aimerais discuter de la façon dont je peux soutenir la gouvernance des données de votre "
    "division. Merci de considérer ma candidature.",
]

PROFILE = (
    "Data governance specialist who defines governance processes, data definitions and quality standards, and "
    "trains and coaches the people who apply them. Led data governance and metadata management at the McConnell "
    "Brain Imaging Centre (The Neuro, McGill University) for dozens of principal investigators and hundreds of "
    "researchers, worked with Collibra, SSO and LDAP, and contributed to national data governance bodies "
    "(Portage, CONP, RDA). Mobilizes stakeholders without hierarchical authority. Bilingual (EN/FR), "
    "Montreal-based."
)

COMPETENCIES = [
    ("Data governance processes and principles",
     ": defined governance principles, stewardship roles and responsibilities, metadata standards, "
     "classification, and lifecycle policies for a national-scale research data environment"),
    ("Data definitions and quality",
     ": built data definitions and standards into the daily acquisition workflow; developed brain imaging "
     "data pipelines and policies in an Agile team"),
    ("Training, guides, and coaching",
     ": designed and delivered workshops, guides, and a public knowledge base; coached researchers and "
     "stakeholders in applying governance practices"),
    ("Stakeholder mobilization",
     ": coordinated standards across institutions that did not report to me (Portage, CONP, Research Data "
     "Alliance); bilingual (EN/FR) communication with technical and institutional audiences"),
    ("Governance tools",
     ": worked with Collibra alongside OwnCloud, LDAP, and SSO to support access, roles, and self-serve data "
     "management; SQL, Python, R, Tableau"),
    ("Compliance and AI",
     ": managed regulatory compliance requirements for government LMS deployments; evaluated and adopted AI "
     "tools in enterprise settings, including Claude Code, assessing data handling implications"),
]

EXPERIENCE = [
    ("09/2016 – 10/2021", "Manager of Data Resources", "McConnell Brain Imaging Centre, The Neuro, McGill University", "Montreal, QC", [
        "Led data governance and metadata management for one of Canada's leading brain imaging centres, supporting dozens of principal investigators and hundreds of researchers",
        "Defined metadata standards, data definitions, stewardship workflows, and lifecycle policies, and built them into the daily acquisition workflow",
        "Grew governance adoption through hands-on training, guides, and communities of practice rather than enforcement; launched an OwnCloud portal and a Moodle-based education portal for self-serve data management",
        "Worked across Collibra, OwnCloud, LDAP, and SSO to support access control, roles, and data management",
        "Represented the centre on Portage, CONP, and Research Data Alliance committees, coordinating standards across institutions and contributing to national research policy",
    ]),
    ("08/2020 – 10/2021", "Data Management and Sharing Coordinator (p/t)", "Tanenbaum Open Science Institute, The Neuro, McGill University", "Montreal, QC", [
        "Supported the launch of a new academic unit focused on Open Science; designed and administered training workshops on data management practices for faculty and graduate students",
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

SKILLS = ("Collibra, SQL, Python, R, Git, Docker, AWS, Azure, SSO, LDAP, Moodle, OwnCloud, Drupal, Tableau, "
          "Agile/Scrum, training design and facilitation.")

if __name__ == "__main__":
    build_all(dict(
        out="docx/hydroquebec_datagov_advisor_application",
        cover=dict(contact="Montréal (Québec)  |  514-475-2374  |  ted.strauss@gmail.com  |  linkedin.com/in/tedstrauss-63b01821",
                   date="9 octobre 2026",
                   subject="Objet : Candidature au poste de conseiller Gestion données II, Gouvernance (concours 189169)",
                   salutation="Madame, Monsieur,", paras=PARAS,
                   closing="Veuillez agréer, Madame, Monsieur, mes salutations distinguées,"),
        cv=dict(profile=PROFILE, competencies=COMPETENCIES, experience=EXPERIENCE, additional=ADDITIONAL,
                education=EDUCATION, skills=SKILLS, publications=PUBLICATIONS)))
