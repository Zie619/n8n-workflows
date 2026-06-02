-- ============================================================================
-- MEDCARDS.AI - Seed Data: Clinical Cases Examples
-- Sample cases for initial testing and development
-- ============================================================================

-- Cardiologia Cases
INSERT INTO clinical_cases (
    case_code,
    title,
    clinical_presentation,
    patient_data,
    question,
    options,
    correct_answer_id,
    explanation,
    clinical_reasoning,
    key_concepts,
    differential_diagnosis,
    specialty,
    subspecialty,
    difficulty_level,
    clinical_algorithm,
    source,
    tags
) VALUES
(
    'CARDIO-001',
    'IAM com Supradesnivelamento de ST - Conduta Imediata',
    'Paciente masculino, 58 anos, tabagista, com dor precordial em aperto há 2 horas, irradiando para membro superior esquerdo e mandíbula. Nega náuseas ou vômitos. Ao exame: PA 140/90 mmHg, FC 98 bpm, sudorese fria. ECG mostra supradesnivelamento de ST > 2mm em V1-V4.',
    '{
        "age": 58,
        "sex": "masculino",
        "vitals": {
            "blood_pressure": "140/90",
            "heart_rate": 98,
            "respiratory_rate": 18,
            "temperature": 36.8,
            "spo2": 96
        },
        "labs": {
            "troponin": "elevada",
            "ck_mb": "elevada"
        },
        "ecg": "Supradesnivelamento de ST > 2mm em V1-V4 (parede anterior)",
        "time_from_symptom_onset": "2 horas",
        "hospital_resources": "Hospital com hemodinâmica disponível 24h"
    }'::jsonb,
    'Qual a conduta imediata mais adequada?',
    '[
        {
            "id": "A",
            "text": "Angioplastia primária",
            "is_correct": true
        },
        {
            "id": "B",
            "text": "Trombolítico (Tenecteplase)",
            "is_correct": false
        },
        {
            "id": "C",
            "text": "Observação clínica com AAS e anticoagulação",
            "is_correct": false
        },
        {
            "id": "D",
            "text": "Teste ergométrico para estratificação",
            "is_correct": false
        }
    ]'::jsonb,
    'A',
    'STEMI de parede anterior com indicação de reperfusão imediata. Angioplastia primária é superior ao trombolítico quando disponível em tempo adequado (tempo porta-balão < 90 minutos). O hospital possui hemodinâmica, tornando a angioplastia a primeira escolha conforme diretrizes brasileiras da SBC.',
    'Raciocínio clínico correto:
    1. IDENTIFICAR: Dor precordial típica (aperto, irradiação para MSE e mandíbula) + supra ST no ECG = STEMI
    2. CONFIRMAR INDICAÇÃO: Tempo < 12h do início dos sintomas → indicação de reperfusão
    3. AVALIAR RECURSOS: Hospital possui hemodinâmica disponível
    4. ESCOLHER MÉTODO: Angioplastia primária > Trombolítico (quando disponível e tempo porta-balão < 90-120min)
    5. CONTRAINDICAÇÕES: Verificar se não há contraindicações absolutas (não há neste caso)

    Pegadinha comum: Pensar em trombolítico simplesmente porque o paciente está dentro da janela de 12h, sem considerar a disponibilidade de hemodinâmica.',
    ARRAY['Síndrome coronariana aguda', 'STEMI', 'Reperfusão miocárdica', 'Angioplastia primária', 'Janela terapêutica'],
    ARRAY['STEMI', 'Angina instável', 'Pericardite', 'Dissecção de aorta', 'Embolia pulmonar'],
    'cardiologia',
    'síndrome coronariana aguda',
    3, -- Difficulty: medium (requires guideline knowledge)
    'Manejo de STEMI - Escolha do método de reperfusão',
    'Caso elaborado baseado em diretrizes SBC 2021',
    ARRAY['REVALIDA', 'SBC Guidelines', 'Emergência cardiológica']
),
(
    'CARDIO-002',
    'Fibrilação Atrial - Anticoagulação',
    'Mulher, 72 anos, hipertensa e diabética, procura ambulatório por palpitações intermitentes há 3 meses. ECG mostra fibrilação atrial com resposta ventricular de 110 bpm. Nega sintomas de ICC. Ecocardiograma: função sistólica preservada (FE 60%), sem trombos visíveis. Score CHA₂DS₂-VASc = 5 pontos.',
    '{
        "age": 72,
        "sex": "feminino",
        "comorbidities": ["hipertensão arterial", "diabetes mellitus tipo 2"],
        "cha2ds2_vasc_score": 5,
        "has_bleed_score": 2,
        "echocardiogram": {
            "ejection_fraction": 60,
            "left_atrium": "discretamente aumentado",
            "thrombus": "ausente",
            "valves": "sem alterações significativas"
        },
        "symptoms": "Palpitações intermitentes, sem dispneia ou dor torácica"
    }'::jsonb,
    'Qual a melhor conduta terapêutica para prevenção de eventos embólicos?',
    '[
        {
            "id": "A",
            "text": "AAS 100mg/dia",
            "is_correct": false
        },
        {
            "id": "B",
            "text": "Anticoagulação oral com warfarina (INR alvo 2-3)",
            "is_correct": true
        },
        {
            "id": "C",
            "text": "Clopidogrel 75mg/dia",
            "is_correct": false
        },
        {
            "id": "D",
            "text": "Apenas controle de frequência cardíaca, sem anticoagulação",
            "is_correct": false
        }
    ]'::jsonb,
    'B',
    'Paciente com FA e CHA₂DS₂-VASc ≥ 2 tem indicação formal de anticoagulação oral para prevenção de AVC. Score de 5 indica alto risco embólico (~6-7% ao ano sem anticoagulação). Warfarina ou DOACs são opções válidas (DOACs preferíveis quando disponíveis). AAS é insuficiente para FA com alto risco.',
    'Raciocínio clínico:
    1. CONFIRMAR DIAGNÓSTICO: FA no ECG (confirmado)
    2. CALCULAR RISCO EMBÓLICO: CHA₂DS₂-VASc
       - C (CHF): 0
       - H (Hipertensão): 1
       - A₂ (Idade ≥75): 0 (72 anos = 0)
       - D (Diabetes): 1
       - S₂ (AVC prévio): 0
       - V (Doença vascular): 0
       - A (Idade 65-74): 1
       - Sc (Sexo feminino): 1
       Total = 5 pontos → ALTO RISCO
    3. INDICAÇÃO: CHA₂DS₂-VASc ≥ 2 = anticoagulação obrigatória
    4. ESCOLHER ANTICOAGULANTE: Warfarina OU DOACs (rivaroxabana, apixabana, dabigatrana)
    5. VERIFICAR CONTRAINDICAÇÕES: Avaliar HAS-BLED para risco de sangramento (score 2 = risco moderado, não contraindica)

    Erro comum: Usar AAS em FA de alto risco (AAS só reduz 20% risco vs 60-70% com anticoagulação).',
    ARRAY['Fibrilação atrial', 'Anticoagulação', 'CHA₂DS₂-VASc', 'Prevenção de AVC', 'Warfarina'],
    ARRAY['Fibrilação atrial', 'Flutter atrial', 'Taquicardia supraventricular'],
    'cardiologia',
    'arritmias',
    2,
    'Estratificação de risco e anticoagulação em FA',
    'Baseado em diretrizes ESC/SBC',
    ARRAY['Ambulatório', 'Anticoagulação', 'FA']
),
(
    'NEURO-001',
    'Cefaleia em Trovoada - Hemorragia Subaracnóidea',
    'Mulher, 35 anos, previamente hígida, dá entrada no PS com cefaleia súbita de forte intensidade iniciada há 1 hora durante atividade sexual. Descreve como "a pior dor de cabeça da vida". Ao exame: consciente, orientada, rigidez de nuca discreta, sem déficits focais. PA 160/100 mmHg. Nega febre. Nega história de enxaqueca.',
    '{
        "age": 35,
        "sex": "feminino",
        "vitals": {
            "blood_pressure": "160/100",
            "heart_rate": 95,
            "glasgow": 15
        },
        "onset": "súbito durante coito",
        "pain_characteristics": "pior cefaleia da vida, intensidade 10/10",
        "exam": {
            "neck_stiffness": "presente (discreta)",
            "focal_deficits": "ausentes",
            "fever": "ausente"
        },
        "time_since_onset": "1 hora"
    }'::jsonb,
    'Qual a principal hipótese diagnóstica e conduta inicial?',
    '[
        {
            "id": "A",
            "text": "Enxaqueca - Analgesia e alta com seguimento ambulatorial",
            "is_correct": false
        },
        {
            "id": "B",
            "text": "Hemorragia subaracnóidea - TC de crânio sem contraste imediata",
            "is_correct": true
        },
        {
            "id": "C",
            "text": "Meningite viral - Análise do LCR",
            "is_correct": false
        },
        {
            "id": "D",
            "text": "Crise hipertensiva - Anti-hipertensivo e reavaliação",
            "is_correct": false
        }
    ]'::jsonb,
    'B',
    'Cefaleia súbita de forte intensidade ("trovoada"), descrita como a pior da vida, especialmente durante esforço físico/Valsalva, é altamente sugestiva de hemorragia subaracnóidea (HSA). Rigidez de nuca reforça o diagnóstico. TC de crânio sem contraste é o exame inicial de escolha (sensibilidade >95% nas primeiras 6h). Se TC negativa e suspeita alta, fazer punção lombar.',
    'Raciocínio diagnóstico de cefaleia em trovoada:
    1. CARACTERÍSTICAS ALARMANTES (red flags):
       ✓ Início súbito ("thunderclap headache")
       ✓ "Pior cefaleia da vida"
       ✓ Início durante esforço/Valsalva
       ✓ Rigidez de nuca
       ✓ Idade jovem sem história de enxaqueca

    2. PRINCIPAL HIPÓTESE: Hemorragia subaracnóidea
       - Causa mais comum: ruptura de aneurisma sacular
       - Mortalidade alta (40-50%)
       - Diagnóstico e tratamento são urgências

    3. CONDUTA DIAGNÓSTICA:
       - TC crânio sem contraste IMEDIATA (sensibilidade 98% em 6h, 93% em 24h)
       - Se TC negativa + alta suspeita: punção lombar (xantocromia após 12h)
       - Se confirmado: angio-TC ou angiografia para identificar aneurisma

    4. POR QUE NÃO É ENXAQUECA:
       - Enxaqueca tem início gradual (não súbito)
       - Geralmente história prévia
       - Rigidez de nuca não é típica

    Regra de ouro: TODA cefaleia em trovoada = HSA até prova em contrário.',
    ARRAY['Hemorragia subaracnóidea', 'Cefaleia em trovoada', 'Red flags cefaleia', 'Aneurisma cerebral'],
    ARRAY['Hemorragia subaracnóidea', 'Enxaqueca', 'Meningite', 'Dissecção de artéria vertebral', 'Trombose venosa cerebral'],
    'neurologia',
    'cefaleia',
    3,
    'Investigação de cefaleia aguda grave',
    'Caso clássico de HSA',
    ARRAY['Emergência', 'Red flags', 'Neurologia']
);

-- Insert more cases as needed...
-- TODO: Add cases for all major specialties:
-- - Pneumologia (pneumonia, DPOC, asma, TEP)
-- - Gastroenterologia (hemorragia digestiva, abdome agudo, hepatopatias)
-- - Nefrologia (IRA, síndrome nefrótica, distúrbios eletrolíticos)
-- - Endocrinologia (diabetes, tireoide, insuficiência adrenal)
-- - Infectologia (sepse, meningite, tuberculose, HIV)
-- - Pediatria (bronquiolite, desidratação, vacinação)
-- - Gineco-Obstetrícia (pré-eclâmpsia, hemorragia, trabalho de parto)

-- ============================================================================
-- Quick stats after seeding
-- ============================================================================

-- Verify inserted cases
SELECT
    specialty,
    COUNT(*) as total_cases,
    AVG(difficulty_level) as avg_difficulty
FROM clinical_cases
WHERE is_active = true
GROUP BY specialty
ORDER BY specialty;
