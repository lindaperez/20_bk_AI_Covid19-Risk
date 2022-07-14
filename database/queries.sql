SELECT data_file_updated, id_patient, crm.value as resp_monitoring, cti.value as type_institution, csm.federated_state as state_medical_unit, 
gg.value as gender, cspb.federated_state as state_patient_birth, csrr.federated_state as state_residence, cc.value as city_patient_birth,
ctp.value as type_patient, date_admitted, date_patient_symp,
date_patient_death, cyni.value as intubated, cynn.value as pneumonia, age, rr.value as resident, cynp.value as pregnant, 
cynil.value as indigenous_lang, cyii.value as indigenous, cydb.value as diabetes, cynco.value as copd, cynas.value as asthma,
cynii.value as immunosup, cynhh.value as hypertension, 
cynac.value as another_complication, cycc.value as cardiovascular, cynoo.value as obesity, cynrc.value as renal_chronic,
cyntt.value as tobacco, cyncc.value as closed_contanct, lab_sample, clr.value as lab_result, antigen_sample, car.value as antige_result,
cfc.classification as final_class_classification, cfc.description as final_class_description, cynmm.value as migrant, 
country_nationality, country_patient_birth, cynpii.value as icu, index
	FROM public.patient pat LEFT JOIN public.cat_antigen_result car ON car.id = pat.antigen_result
	LEFT JOIN public.cat_city cc ON cc.id = pat.city_patient_birth
	LEFT JOIN public.cat_final_class cfc ON cfc.id = pat.final_class
	LEFT JOIN public.cat_gender gg ON gg.id = pat.gender
	LEFT JOIN public.cat_lab_result clr ON clr.id = pat.lab_result
	LEFT JOIN public.cat_resident rr ON rr.id = pat.resident
	LEFT JOIN public.cat_resp_monitoring crm ON crm.id = pat.resp_monitoring
	LEFT JOIN public.cat_type_institution cti ON cti.id = pat.type_institution
	LEFT JOIN public.cat_type_patient ctp ON ctp.id = pat.type_patient
	LEFT JOIN public.cat_yes_no cyni ON cyni.id = pat.intubated
	LEFT JOIN public.cat_state csm ON csm.id = pat.state_medical_unit
	LEFT JOIN public.cat_state cspb ON cspb.id = pat.state_patient_birth
	LEFT JOIN public.cat_state csrr ON csrr.id = pat.state_residence
	LEFT JOIN public.cat_yes_no cynn ON cynn.id = pat.pneumonia
	LEFT JOIN public.cat_yes_no cynp ON cynp.id = pat.pregnant
	LEFT JOIN public.cat_yes_no cynil ON cynil.id = pat.indigenous_lang
	LEFT JOIN public.cat_yes_no cyii ON cyii.id = pat.indigenous
	LEFT JOIN public.cat_yes_no cydb ON cydb.id = pat.diabetes
	LEFT JOIN public.cat_yes_no cynco ON cynco.id = pat.copd
	LEFT JOIN public.cat_yes_no cynas ON cynas.id = pat.asthma
	LEFT JOIN public.cat_yes_no cynii ON cynii.id = pat.immunosup
	LEFT JOIN public.cat_yes_no cynhh ON cynhh.id = pat.hypertension
	LEFT JOIN public.cat_yes_no cynac ON cynac.id = pat.another_complication
	LEFT JOIN public.cat_yes_no cycc ON cycc.id = pat.cardiovascular
	LEFT JOIN public.cat_yes_no cynoo ON cynoo.id = pat.obesity
	LEFT JOIN public.cat_yes_no cynrc ON cynrc.id = pat.renal_chronic
	LEFT JOIN public.cat_yes_no cyntt ON cyntt.id = pat.tobacco
	LEFT JOIN public.cat_yes_no cyncc ON cyncc.id = pat.closed_contanct
	LEFT JOIN public.cat_yes_no cynmm ON cynmm.id = pat.migrant
	LEFT JOIN public.cat_yes_no cynpii ON cynpii.id = pat.icu
	LIMIT 20;
	
	
SELECT state_medical_unit, date_patient_death, count(id_patient) 
FROM public.patient
WHERE date_patient_death!= '9999-99-99'
GROUP BY state_medical_unit,date_patient_death
ORDER BY state_medical_unit,date_patient_death
LIMIT 5;

SELECT id_patient, age
FROM public.patient
group by age,id_patient
limit 5;
	
