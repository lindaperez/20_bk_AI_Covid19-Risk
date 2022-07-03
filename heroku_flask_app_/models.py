def create_classes(db):
    class Patient(db.Model):
        __tablename__ = 'sitepatients'

        id = db.Column(db.Integer, primary_key=True)
        first_name = db.Column(db.String(30))
        last_name = db.Column(db.String(30))
        # resp_monitoring = db.Column(db.Integer)
        # type_institution = db.Column(db.Integer)
        # state_medical_unit = db.Column(db.Integer)
        gender = db.Column(db.Integer)
        # state_patient_birth  = db.Column(db.Integer)
        # state_residence  = db.Column(db.Integer)
        # city_patient_birth  = db.Column(db.Integer)
        # type_patient  = db.Column(db.Integer)
        # # date_admitted text COLLATE pg_catalog."default",
        # date_patient_symp  = db.Column(db.DateTime)
        # #date_patient_death = db.Column(db.DateTime)
        newage = db.Column(db.String(60))
        # resident = db.Column(db.Integer)
        pregnant = db.Column(db.Integer)
        # indigenous_lang = db.Column(db.Integer)
        # indigenous = db.Column(db.Integer)
        intubated = db.Column(db.Integer)
        pneumonia = db.Column(db.Integer)
        diabetes = db.Column(db.Integer)
        copd = db.Column(db.Integer)
        asthma = db.Column(db.Integer)
        immunosup = db.Column(db.Integer)
        hypertension = db.Column(db.Integer)
        another_complication = db.Column(db.Integer)
        cardiovascular = db.Column(db.Integer)
        obesity = db.Column(db.Integer)
        renal_chronic = db.Column(db.Integer)
        tobacco = db.Column(db.Integer)
        closed_contanct = db.Column(db.Integer)
        icu = db.Column(db.Integer)
        # lab_sample = db.Column(db.Integer)
        # lab_result = db.Column(db.Integer)
        # antigen_sample = db.Column(db.Integer)
        # antigen_result = db.Column(db.Integer)
        # final_class = db.Column(db.Integer)
        # migrant = db.Column(db.Integer)
        # country_nationality = db.Column(db.Integer)
        # country_patient_birth = db.Column(db.Integer)
    

        def __repr__(self):
            return '<Patient %r>' % (self.name)
    return {'Patient':Patient}


#     -- Table: public.patient

# -- DROP TABLE IF EXISTS public.patient;

# CREATE TABLE IF NOT EXISTS public.patient
# (
#   x  data_file_updated text COLLATE pg_catalog."default",
#     id_patient text COLLATE pg_catalog."default",
#     resp_monitoring smallint,
#     type_institution smallint,
#     state_medical_unit smallint,
#     gender smallint,
#     state_patient_birth smallint,
#     state_residence smallint,
#     city_patient_birth smallint,
#     type_patient smallint,
#     date_admitted text COLLATE pg_catalog."default",
#     date_patient_symp text COLLATE pg_catalog."default",
#     date_patient_death text COLLATE pg_catalog."default",
#     intubated smallint,
#     pneumonia smallint,
#     age smallint,
#     resident smallint,
#     pregnant smallint,
#     indigenous_lang smallint,
#     indigenous smallint,
#     diabetes smallint,
#     copd smallint,
#     asthma smallint,
#     immunosup smallint,
#     hypertension smallint,
#     another_complication smallint,
#     cardiovascular smallint,
#     obesity smallint,
#     renal_chronic smallint,
#     tobacco smallint,
#     closed_contanct smallint,
#     lab_sample smallint,
#     lab_result smallint,
#     antigen_sample smallint,
#     antigen_result smallint,
#     final_class smallint,
#     migrant smallint,
#     country_nationality text COLLATE pg_catalog."default",
#     country_patient_birth text COLLATE pg_catalog."default",
#     icu smallint,
#     index bigint,
#     CONSTRAINT constraint_name FOREIGN KEY (type_patient)
#         REFERENCES public.cat_type_patient (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION,
#     CONSTRAINT pat_another_complication FOREIGN KEY (another_complication)
#         REFERENCES public.cat_yes_no (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION,
#     CONSTRAINT pat_antigen_result FOREIGN KEY (antigen_result)
#         REFERENCES public.cat_antigen_result (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION,
#     CONSTRAINT pat_antigen_sample FOREIGN KEY (antigen_sample)
#         REFERENCES public.cat_yes_no (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION,
#     CONSTRAINT pat_athma FOREIGN KEY (asthma)
#         REFERENCES public.cat_yes_no (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION,
#     CONSTRAINT pat_cardiovascular FOREIGN KEY (cardiovascular)
#         REFERENCES public.cat_yes_no (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION,
#     CONSTRAINT pat_city FOREIGN KEY (city_patient_birth)
#         REFERENCES public.cat_city (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION,
#     CONSTRAINT pat_closed_contanct FOREIGN KEY (closed_contanct)
#         REFERENCES public.cat_yes_no (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION,
#     CONSTRAINT pat_copd FOREIGN KEY (copd)
#         REFERENCES public.cat_yes_no (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION,
#     CONSTRAINT pat_diabetes FOREIGN KEY (diabetes)
#         REFERENCES public.cat_yes_no (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION,
#     CONSTRAINT pat_final_class FOREIGN KEY (final_class)
#         REFERENCES public.cat_final_class (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION,
#     CONSTRAINT pat_gender FOREIGN KEY (gender)
#         REFERENCES public.cat_gender (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION,
#     CONSTRAINT pat_hypertension FOREIGN KEY (hypertension)
#         REFERENCES public.cat_yes_no (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION,
#     CONSTRAINT pat_icu FOREIGN KEY (icu)
#         REFERENCES public.cat_yes_no (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION,
#     CONSTRAINT pat_immunosup FOREIGN KEY (immunosup)
#         REFERENCES public.cat_yes_no (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION,
#     CONSTRAINT pat_indigenous FOREIGN KEY (indigenous)
#         REFERENCES public.cat_yes_no (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION,
#     CONSTRAINT pat_indigenous_lang FOREIGN KEY (indigenous_lang)
#         REFERENCES public.cat_yes_no (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION,
#     CONSTRAINT pat_intubated FOREIGN KEY (intubated)
#         REFERENCES public.cat_yes_no (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION,
#     CONSTRAINT pat_lab_result FOREIGN KEY (lab_result)
#         REFERENCES public.cat_lab_result (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION,
#     CONSTRAINT pat_lab_sample FOREIGN KEY (lab_sample)
#         REFERENCES public.cat_yes_no (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION,
#     CONSTRAINT pat_migrant FOREIGN KEY (migrant)
#         REFERENCES public.cat_yes_no (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION,
#     CONSTRAINT pat_obesity FOREIGN KEY (obesity)
#         REFERENCES public.cat_yes_no (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION,
#     CONSTRAINT pat_pneumonia FOREIGN KEY (pneumonia)
#         REFERENCES public.cat_yes_no (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION,
#     CONSTRAINT pat_pregnant FOREIGN KEY (pregnant)
#         REFERENCES public.cat_yes_no (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION,
#     CONSTRAINT pat_renal_chronic FOREIGN KEY (renal_chronic)
#         REFERENCES public.cat_yes_no (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION,
#     CONSTRAINT pat_resident FOREIGN KEY (resident)
#         REFERENCES public.cat_resident (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION,
#     CONSTRAINT pat_resp_monitoring FOREIGN KEY (resp_monitoring)
#         REFERENCES public.cat_resp_monitoring (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION,
#     CONSTRAINT pat_state FOREIGN KEY (state_patient_birth)
#         REFERENCES public.cat_state (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION,
#     CONSTRAINT pat_state_med_unit FOREIGN KEY (state_medical_unit)
#         REFERENCES public.cat_state (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION,
#     CONSTRAINT pat_state_patient_birth FOREIGN KEY (state_patient_birth)
#         REFERENCES public.cat_state (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION,
#     CONSTRAINT pat_state_residence FOREIGN KEY (state_residence)
#         REFERENCES public.cat_state (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION,
#     CONSTRAINT pat_tobacco FOREIGN KEY (tobacco)
#         REFERENCES public.cat_yes_no (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION,
#     CONSTRAINT pat_type_institution FOREIGN KEY (type_institution)
#         REFERENCES public.cat_type_institution (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION,
#     CONSTRAINT pat_type_patient FOREIGN KEY (type_patient)
#         REFERENCES public.cat_type_patient (id) MATCH SIMPLE
#         ON UPDATE NO ACTION
#         ON DELETE NO ACTION
# )

# TABLESPACE pg_default;

# ALTER TABLE IF EXISTS public.patient
#     OWNER to postgres;

