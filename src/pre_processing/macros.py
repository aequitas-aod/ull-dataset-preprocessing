import os

import os
from data import PATH as DATA_PATH
from data.split import PATH as DATA_SPLIT_PATH
from data.pre_processed import PATH as DATA_PREPROC_PATH

HOME_PATH = os.path.join("/", "home")
ORIGINAL_DATASET_NAME = "original.csv"

column_groups = {
    "identifiers": [
        "id_student_original",
        "id_year",
        "id_grade",
        "id_class_group",
        "id_school",
        "id_student_16_19",
        "id_school_16_19",
    ],
    "info": [
        "student_questionnaire",
        "principals_questionnaire",
        "family_questionnaire",
        "teachers_questionnaire",
        "census",
        "scores",
    ],
    "student_scores": [
        "score_MAT",
        "level_MAT",
        "score_LEN",
        "level_LEN",
        "score_ING",
        "level_ING",
    ],
    "student_questionnaire": [
        "a1",
        "a2",
        "a3a",
        "a3b",
        "living_with_father_mother",
        "a3c",
        "a3d",
        "a3et",
        "a3f",
        "a4",
        "repeater",
        "a5",
        "a6nm",
        "a7",
        "a8a",
        "a8b",
        "a8c",
        "a09a",
        "a09b",
        "a09c",
        "a09d",
        "a09e",
        "a9a",
        "a9b",
        "a9c",
        "a9d",
        "a9e",
        "a9f",
        "a9g",
        "a10a",
        "a10b",
        "a10c",
        "a10d",
        "a10e",
        "a10f",
        "a10g",
        "a10h",
        "a10i",
        "a10j",
        "a10k",
        "a10l",
        "a10m",
        "a10n",
        "a11a",
        "a11b",
        "a11c",
        "a11d",
        "a11e",
        "a11f",
        "a11g",
        "a11h",
        "a12a",
        "a12b",
        "a12c",
        "a12d",
        "a12e",
        "a12f",
        "a12g",
        "a12h",
        "a12i",
        "a13a",
        "a13b",
        "a13c",
        "a13d",
        "a13e",
        "a14a",
        "a14b",
        "a14c",
        "a14d",
        "a14e",
        "a14f",
        "a14g",
        "a14h",
        "a15a",
        "a15b",
        "a15c",
        "a15d",
        "a15e",
        "a15f",
        "a15g",
        "a15h",
        "a15i",
        "a15j",
        "a16a",
        "a16b",
        "a16c",
        "a16d",
        "a16e",
        "a16f",
        "a16g",
        "a16h",
        "a16i",
        "a16j",
        "a16k",
        "a16l",
        "a17a",
        "a17b",
        "a17c",
        "a17d",
        "a17e",
        "a17f",
        "a17g",
        "a17h",
        "a20a",
        "a20b",
        "a20c",
        "a20d",
        "a20e",
        "a21a",
        "a21b",
        "a21c",
        "a21d",
        "a21e",
        "a22a",
        "a22b",
        "a22c",
        "a22d",
        "a23a",
        "a23b",
        "a23c",
        "a23d",
        "a23e",
        "a23f",
        "a23g",
        "a23h",
        "a23i",
        "a23j",
        "a23k",
        "a24",
        "a40a",
        "a40b",
        "a40c",
        "a40d",
        "a41",
        "a42",
        "a51",
        "a61",
        "a71",
        "a111a",
        "a141g",
        "a144d",
        "a144h",
        "a160k",
        "a162k",
        "a163k",
        "a166f",
        "a166k",
        "a171h",
        "a177d",
        "a211a",
        "a222b",
        "country_iso_cnac",
        "country_iso_nac",
        "weight",
    ],
    "principal_questionnaire": [
        "d1",
        "d2n",
        "d3n",
        "d4n",
        "d5n",
        "d6n",
        "d7n",
        "d8n",
        "d9a1",
        "d9a2",
        "d9b1",
        "d9b2",
        "d9c1",
        "d9c2",
        "d9d1",
        "d9d2",
        "d9e1",
        "d9e2",
        "d9f1",
        "d9f2",
        "d9g1",
        "d9g2",
        "d9h1",
        "d9h2",
        "d10a",
        "d10b",
        "d10c",
        "d11an",
        "d11bn",
        "d12an",
        "d12bn",
        "d13n",
        "d14",
        "d15",
        "d16an",
        "d16bn",
        "d16cn",
        "d16dn",
        "d16en",
        "d16fn",
        "d17a",
        "d17b",
        "d17c",
        "d17d",
        "d17e",
        "d17f",
        "d17g",
        "d17h",
        "d18a",
        "d18b",
        "d18c",
        "d18d",
        "d18e",
        "d18f",
        "d18g",
        "d18h",
        "d18i",
        "d18j",
        "d18k",
        "d18l",
        "d18m",
        "d18n",
        "d19a",
        "d19b",
        "d19c",
        "d19d",
        "d19e",
        "d19f",
        "d19g",
        "d19h",
        "d19i",
        "d19j",
        "d19k",
        "d19l",
        "d19m",
        "d19n",
        "d19o",
        "d19p",
        "d19q",
        "d19r",
        "d20a",
        "d20b",
        "d20c",
        "d20d",
        "d20e",
        "d20f",
        "d20g",
        "d20h",
        "d20i",
        "d20j",
        "d20k",
        "d20l",
        "d21a",
        "d21b",
        "d21c",
        "d21d",
        "d21e",
        "d21f",
        "d22a",
        "d22b",
        "d22c",
        "d22d",
        "d22e",
        "d22f",
        "d30a",
        "d30b",
        "d30c",
        "d30d",
        "d30e",
        "d30f",
        "d31a",
        "d31b",
        "d31c",
        "d32a",
        "d33a",
        "d121a",
        "d121b",
        "d131a",
        "d131b",
        "d301",
        "d302",
        "d303",
        "d304",
        "d305",
        "d306",
        "d307",
        "d308",
        "tasa_nac_eso4",
        "tasa_nac_pri3",
        "tasa_nac_pri6",
        "distnac",
        "distnac_eso4",
        "distnac_pri3",
        "distnac_pri6",
        "groups",
        "island",
        "capital_island",
        "public_private",
    ],
    "family_questionnaire": [
        "f0",
        "f1n",
        "f2an",
        "f2bn",
        "f3a",
        "f3b",
        "mother_education",
        "father_education",
        "f4a",
        "f4b",
        "f5a",
        "f5b",
        "f5n",
        "inmigrant",
        "inmigrant2",
        "inmigrant_second_gen",
        "f6",
        "f7",
        "f8ta",
        "f8tm",
        "start_schooling_age",
        "f9a",
        "f9b",
        "f9c",
        "f9d",
        "f9e",
        "f9f",
        "f9g",
        "f9h",
        "f10n",
        "f11",
        "books",
        "f12a",
        "f12b",
        "f13n",
        "f14a",
        "f14b",
        "f14c",
        "f15a",
        "f15b",
        "f15c",
        "f15d",
        "f15e",
        "f15f",
        "f16a",
        "f16b",
        "f16c",
        "f16d",
        "f16e",
        "f16f",
        "f17a",
        "f17b",
        "f17c",
        "f17d",
        "f18a",
        "f18b",
        "f18c",
        "f18d",
        "f18e",
        "f18f",
        "f18g",
        "f18h",
        "f18i",
        "f19a",
        "f19b",
        "f19c",
        "f19d",
        "f19e",
        "f20",
        "f21n",
        "f22",
        "f23",
        "f24a",
        "f24b",
        "mother_occupation",
        "father_occupation",
        "f30",
        "f31",
        "single_parent_household",
        "f33a",
        "f33b",
        "f33c",
        "f33d",
        "f33e",
        "f33f",
        "f33g",
        "f33h",
        "f34",
        "household_income_q",
        "nhousehold",
        "ESCS",
    ],
    "teacher_questionnaire": [
        "p2",
        "p2n",
        "p3n",
        "p4n",
        "p5",
        "p6n",
        "p7an",
        "p7bn",
        "p7cn",
        "p7dn",
        "p7en",
        "p7fn",
        "p7gn",
        "p8an",
        "p8bn",
        "p9a",
        "p9b",
        "p9c",
        "p9d",
        "p9e",
        "p9f",
        "p10n",
        "p11",
        "p12a",
        "p12b",
        "p12c",
        "p12d",
        "p13",
        "p13b",
        "p13c",
        "p15a",
        "p15b",
        "p15c",
        "p15d",
        "p15e",
        "p15f",
        "p15g",
        "p15h",
        "p15i",
        "p16a",
        "p16b",
        "p16c",
        "p16d",
        "p16e",
        "p16f",
        "p16g",
        "p16h",
        "p18a",
        "p18b",
        "p18c",
        "p18d",
        "p18e",
        "p18f",
        "p18g",
        "p18h",
        "p18i",
        "p19",
        "p20",
        "p21a",
        "p21b",
        "p21c",
        "p21d",
        "p21e",
        "p21f",
        "p22a",
        "p22b",
        "p22c",
        "p22d",
        "p22e",
        "p22f",
        "p22g",
        "p23a",
        "p23b",
        "p23c",
        "p23d",
        "p23e",
        "p23f",
        "p23g",
        "p23h",
        "p23i",
        "p24a",
        "p24b",
        "p24c",
        "p24d",
        "p24e",
        "p24f",
        "p24g",
        "p24h",
        "p24i",
        "p24j",
        "p24k",
        "p25",
        "p26",
        "p26a",
        "p26b",
        "p26c",
        "p26d",
        "p27a",
        "p27b",
        "p27c",
        "p27d",
        "p27e",
        "p27f",
        "p27g",
        "p27h",
        "p28n",
        "p29a",
        "p29b",
        "p29c",
        "p29d",
        "p29e",
        "p30a",
        "p30b",
        "p30c",
        "p31d",
        "p32a",
        "p32b",
        "p32c",
        "p32d",
        "p32e",
        "p34a",
        "p34b",
        "p34c",
        "p34d",
        "p34e",
        "p34f",
        "p34g",
        "p41a",
        "p41b",
        "p41c",
        "p41d",
        "p41e",
        "p41f",
        "p41g",
        "p41h",
        "p41i",
        "p41j",
        "p141",
        "p171n",
        "p172n",
        "p299d",
        "p311a",
        "p311b",
        "p311c",
        "p311e",
        "p311f",
        "p311g",
        "p311h",
        "p331a",
        "p331b",
        "p331c",
        "p331d",
        "p331e",
        "p331f",
        "p331g",
        "p331j",
        "pfc",
        "rep",
    ],
}

agg_mean = {
    "extent_of_evaluation_variety": [
        "p24a",
        "p24b",
        "p24c",
        "p24d",
        "p24e",
        "p24f",
        "p24g",
        "p24h",
        "p24i",
        "p24j",
        "p24k"
    ], 
    "extent_of_pfc_incidence": [
        "p16a",
        "p16b",
        "p16c",
        "p16d",
        "p16e",
        "p16f",
        "p16g",
        "p16h",
    ],
    "extent_of_work_hampered": [
        "p27a",
        "p27b",
        "p27c",
        "p27c",
        "p27d",
        "p27e",
        "p27f",
        "p27g",
        "p27h",
    ],
    "extent_of_family_interest": ["p29a", "p29b", "p29c", "p29d", "p29e", "p299d"],
    "agreement_of_family_support": ["p30a", "p30b", "p30c"],
    "agreement_of_work_facilitated_by_management": ["p34a", "p34b", "p34c", "p34d", "p34e", "p34f", "p34g"],
    "extent_of_positive_relationships": [
        "p31d",
        "p311a",
        "p311b",
        "p311c",
        "p311e",
        "p311f",
        "p311g",
        "p311h",
    ],
    "number_of_special_attention_students": ["p7an", "p7bn", "p7cn", "p7dn", "p7en", "p7gn"],
    "extent_of_student_involvement_during_class": ["p21a", "p21b", "p21c", "p21d", "p21e", "p21f"],
    "extent_of_teaching_methods_variety": [
        "p24a",
        "p24b",
        "p24c",
        "p24d",
        "p24e",
        "p24f",
        "p24g",
        "p24h",
        "p24i",
        "p24j",
        "p24k",
    ],
    "agreement_of_opinion_on_school": ["p32a", "p32b", "p32c", "p32d", "p32e"],
    "agreement_of_class_behaviour": ["p12a", "p12b", "p12c", "p12d"],
    "extent_of_teaching_methods_variety": [
        "p22a",
        "p22b",
        "p22c",
        "p22d",
        "p22e",
        "p22f",
        "p22g",
    ],
    "extent_of_resource_variety": [
        "p23a",
        "p23b",
        "p23c",
        "p23d",
        "p23e",
        "p23f",
        "p23g",
        "p23h",
        "p23i",
    ],
    "extent_of_good_work_by_non_teachers": [
        "p331a",
        "p331b",
        "p331c",
        "p331d",
        "p331e",
        "p331f",
        "p331g",
        "p331j",
    ]
}

agg_sum = {
    "number_of_individual_training_topics": [
        "p18a",
        "p18b",
        "p18c",
        "p18d",
        "p18e",
        "p18f",
        "p18g",
        "p18h",
        "p18i",
    ],
}

agg_custom_binary = {"subjects_taught": ["p9a", "p9b", "p9c", "p9d", "p9e", "p9f"]}

to_rename = {
    "p2": "gender",
    "p2n": "age",
    "p3n": "number_of_years_as_teacher",
    "p4n": "numer_of_years_in_school",
    "p5": "has_taught_same_group_last_two_years",
    "p6n": "number_of_students_in_group",
    "p7fn": "number_of_students_disadvanteged_economic_situation",
    "p8an": "number_of_foreign_students_speaking_spanish",
    "p8bn": "number_of_foreign_students_not_speaking_spanish",
    "p10n": "number_of_teaching_hours_per_week",
    "p11": "average_explanation_time",
    "p19": "agreement_of_training_offer_adequate_to_needs",
    "p20": "extent_of_individual_training_incidence",
    "p25": "seat_configuration",
    "p26": "behaviour_problems_solution_categorical",
    "p28n": "number_of_meetings_with_families",
    "p141": "is_enrolled_in_school_training_plan",
    "p171n": "number_of_training_hours_last_six_years",
    "p172n": "number_of_training_ceu_offer",
    "pfc": "main_topic_of_pfc"
}

agg_mix = {
    "a": {
        "agreement_of_satisfaction_job_and_school": [
            # sensitive feature
            "p41e",
            "p41g",
            "p41i",
            "p41a",
            "p41b",
            "p41h",
            "p41j",
        ],
        "agreement_of_results_satisfaction": ["p13", "p13b"]
    },
    "b": {
        # sensitive feature
        "agreement_of_satisfaction_job_and_school": ["p41c", "p41d", "p41f"],
        "agreement_of_results_satisfaction": ["p13c"]
    },
}
