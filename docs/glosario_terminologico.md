# Glosario Terminológico - Ontologías GORE Ñuble & TDE

> **Generado automáticamente**: 2026-01-27 15:57
> 
> Este glosario contiene las definiciones de clases, propiedades y aspectos
> extraídos de las ontologías GORE Ñuble y TDE del Estado de Chile.

---

## Tabla de Contenidos

- [alignmentGnubTde](#alignmentgnubtde) (1 términos)
- [goreNubleDipirOntology](#gorenubledipirontology) (6 términos)
- [goreNubleOntology](#gorenubleontology) (199 términos)
- [tdeCore](#tdecore) (19 términos)
- [tdeDatos](#tdedatos) (8 términos)
- [tdeLexicon](#tdelexicon) (1 términos)
- [tdePrincipios](#tdeprincipios) (3 términos)
- [tdeProcesos](#tdeprocesos) (7 términos)

---

## alignmentGnubTde

### Alineamiento GNUB-TDE `Ontology`

**URI**: `alignmentGnubTde`

**Definición**: Módulo de alineamiento formal entre las ontologías GNUB (GORE Ñuble) y TDE (Transformación Digital del Estado). Define jerarquías, equivalencias y mappings semánticos. NOTA: Cargar después de goreNubleOntology.ttl.

---

## goreNubleDipirOntology

### aprueba acto `ObjectProperty`

**URI**: `approvesAct`

**Definición**: Vincula un evento de aprobación con el acto administrativo que aprueba.

---

### DIPIR Ontology `Ontology`

**URI**: `goreNubleDipirOntology`

**Definición**: Extensión de la ontología GORE Ñuble para modelar workflows específicos de la División de Inversión y Presupuesto Regional (DIPIR). Reutiliza gnub:IPR, gnub:BudgetaryTransaction y gnub:GOREAgreement.

---

### Evento de Aprobación `Class`

**URI**: `AprobacionEvent`

**Definición**: Evento de aprobación final en el flujo administrativo DIPIR. Representa la firma o autorización definitiva de un acto administrativo.

*Nota*: Típicamente ejecutado por Gobernador Regional (Jefe Superior de Servicio). Marca la transición de un acto de 'En Tramitación' a 'Aprobado'.

---

### Evento de Visación `Class`

**URI**: `VisacionEvent`

**Definición**: Evento de visación en el flujo de aprobación administrativo DIPIR. Representa la acción de un actor que valida un documento antes de la aprobación final.

*Nota*: Usar gist:hasParticipant para el visador (Person/Organization), gist:isCategorizedBy con gnub:ApprovalFlowStage para etapa (V°B° Presupuesto, V°B° Jurídico, etc.).

---

### Evento Toma de Razón `Class`

**URI**: `TomaRazonEvent`

**Definición**: Evento de Toma de Razón por la Contraloría General de la República (CGR). Control externo de legalidad de actos administrativos afectos.

*Nota*: Solo aplica a Resoluciones AFECTAS y Decretos. Marca el hito de validación externa.

---

### visa acto `ObjectProperty`

**URI**: `visatesAct`

**Definición**: Vincula un evento de visación con el acto administrativo que visa.

---

## goreNubleOntology

### Acto Administrativo `Class`

**URI**: `AdministrativeAct`

**Definición**: Acto administrativo formal del GORE que genera obligaciones o derechos (Resolución, Decreto, Convenio).

*Nota*: Patrón Gist v2.2 - Acto como Agreement: Un acto administrativo es un Agreement (no Commitment) porque: 1. Tiene múltiples partes (GORE + Receptor) 2. Contiene Commitments de ambas partes: - GORE: transferir recursos - Receptor: rendir cuentas, ejecutar proyecto El acto se expresa en un documento (FormattedContent): gnubd:_Resolution_001 a gnub:Resolution ; gist:isExpressedIn gnubd:_Doc_001 . gnubd:_Doc_001 a gist:FormattedContent ; gist:isCategorizedBy gnubd:_DocType_Resolution .

---

### Adquisición ANF `Class`

**URI**: `ANFAcquisition`

**Definición**: Adquisición de Activos No Financieros (Vehículos, Equipos) vía Circular 33.

---

### afecta cuenta `ObjectProperty`

**URI**: `affectsAccount`

**Definición**: Transacción que modifica el saldo de una cuenta presupuestaria.

---

### Alerta `Class`

**URI**: `Alert`

**Definición**: Notificación de evento que requiere atención: umbral superado, vencimiento próximo, anomalía detectada o riesgo identificado.

*Nota*: Identificado en 59 menciones en US. Patrón Gist: Event con severidad y destinatarios.

---

### aprueba convenio `ObjectProperty`

**URI**: `approvesAct`

**Definición**: Resolución que aprueba y formaliza un convenio de transferencia.

---

### articulación productiva `ObjectProperty`

**URI**: `coordinatesProductivelyWith`

**Definición**: Relación de articulación productiva (p.ej., DIFOI articula con servicios públicos regionales).

---

### Artículo Legal `Class`

**URI**: `LegalArticle`

**Definición**: Artículo específico dentro de un documento legal que contiene una o más disposiciones normativas.

---

### asigna presupuesto `ObjectProperty`

**URI**: `allocatesBudgetTo`

**Definición**: Relación de asignación de presupuesto (p.ej., DIPRES asigna presupuesto al GORE).

---

### Asignación Presupuestaria `Class`

**URI**: `BudgetAllocation`

**Definición**: Nivel 6: Asignación presupuestaria (ej. 33.03.001 A Otras Entidades Públicas).

---

### Avance Físico `Aspect`

**URI**: `PhysicalProgressAspect`

**Definición**: Aspecto: porcentaje de avance físico de una IPR (0-100%).

*Nota*: Usar con gist:Magnitude y gist:numericValue para representar el % de avance.

---

### Avance Planificado `Aspect`

**URI**: `PlannedProgressAspect`

**Definición**: Aspecto: porcentaje de avance físico planificado según cronograma.

---

### cantidad beneficiarios `DatatypeProperty`

**URI**: `beneficiaryCount`

**Definición**: Cantidad estimada de beneficiarios anuales.

---

### Capítulo Presupuestario `Class`

**URI**: `BudgetChapter`

**Definición**: Nivel 2: Capítulo presupuestario (ej. Capítulo 16 GORE Ñuble).

---

### Categoría CTCI `Class`

**URI**: `CTCIInitiative`

**Definición**: Categorización temática CTCI que aplica a proyectos y programas de Ciencia, Tecnología, Conocimiento e Innovación.

---

### Categoría FRIL `Class`

**URI**: `FRILCategory`

**Definición**: Categoría temática de proyectos FRIL (A, B, C, D).

---

### Clasificador Presupuestario `Class`

**URI**: `BudgetClassifier`

**Definición**: Clasificador presupuestario en cualquier nivel jerárquico. Usa gist:isDirectPartOf para estructura.

*Nota*: Superclase unificadora. Subclases representan niveles específicos por conveniencia.

---

### Componente de Programa `Class`

**URI**: `ProgramComponent`

**Definición**: Bien o servicio directo (producto) entregado a la población objetivo como parte de un Programa Operacional.

---

### Compromiso `Class`

**URI**: `CommitmentEvent`

**Definición**: Compromiso: acto administrativo (OC, Contrato) que reserva recursos definitivamente.

---

### Compromiso Presupuestario `Class`

**URI**: `BudgetaryCommitment`

**Definición**: Compromiso presupuestario sostenido: obligación institucional de transferir recursos, creada por un acto administrativo (CDP, Resolución, Convenio) y extinguida por el pago.

> **Ejemplo**: Un CDP emitido (PreCommitmentEvent) confiere un BudgetaryCommitment con hasGiver=GORE, hasGetter=Municipality, hasMagnitude=500M CLP.

*Nota*: Remediación Gist v2.1: Separa el Evento (gnub:CommitmentEvent) de la Obligación sostenida (gist:Commitment). El evento 'confers' el compromiso. Permite modelar compromisos multi-año y su estado de cumplimiento independiente del evento que lo creó.

---

### Comuna `Class`

**URI**: `Commune`

**Definición**: Unidad territorial básica de administración local en Chile, gobernada por una Municipalidad.

---

### contiene geo-región (DEPRECATED) `ObjectProperty`

**URI**: `containsGeoRegion`

**Definición**: DEPRECATED: Usar gist:isGeoContainedIn (inversa) desde la región contenida.

---

### Convenio de Transferencia `Class`

**URI**: `TransferAgreement`

**Definición**: Convenio de Transferencia: entrega recursos para ejecución directa del beneficiario (subvenciones, fondos concursables). Requiere rendición SISREC.

*Nota*: Modelo pago: transferencia upfront → rendición posterior vía SISREC/CGR.

---

### Convenio GORE `Class`

**URI**: `GOREAgreement`

**Definición**: Convenio formalizado por el GORE con una entidad ejecutora, con fuerza legal y obligaciones mutuas.

*Nota*: Distinción con gnub:AdministrativeAct: - GOREAgreement (Convenio): gist:Contract → gist:Agreement Acuerdo BILATERAL con partes explícitas (GORE + Ejecutor). Ejemplos: Convenio Mandato, Convenio Transferencia. - AdministrativeAct (Resolución/Decreto): gist:Agreement Acto FORMAL que puede generar obligaciones implícitas. Crea Commitments sin necesariamente tener contraparte bilateral. Ambos son gist:Agreement pero con diferente nivel de formalización contractual.

---

### Convenio Mandato `Class`

**URI**: `MandateAgreement`

**Definición**: Convenio Mandato: GORE encarga ejecución a tercero (MOP, SERVIU, Municipalidad); transfiere recursos contra avance (Estados de Pago).

*Nota*: Modelo pago: estados de pago contra avance de obra. Unidades técnicas: MOP, SERVIU, Municipios.

---

### coordina planes `ObjectProperty`

**URI**: `coordinatesPlansWith`

**Definición**: Relación de coordinación de planes (p.ej., DIPLADE coordina planes con SEREMIs).

---

### Cuenta Presupuestaria `Class`

**URI**: `BudgetaryAccount`

**Definición**: Cuenta presupuestaria con saldos para seguimiento de ejecución (vigente, comprometido, devengado, pagado, disponible).

*Nota*: Para clasificadores usar FundingSource. Esta clase modela saldos según gist:Account.

---

### Código BIP `DatatypeProperty`

**URI**: `codigoBIP`

**Alias**: código BIP

**Definición**: Código único de la Iniciativa en el Banco Integrado de Proyectos (BIP) del SNI.

*Nota*: Formato típico: XXXXXXXX-X (ej. 40028237-0). Para FRIL se usa prefijo FRIL-. Patrón Gist: subPropertyOf gist:uniqueText para semántica de identificador único.

---

### Dataset `Class`

**URI**: `Dataset`

**Definición**: Conjunto de datos estructurados para análisis, interoperabilidad o publicación.

*Nota*: Identificado en 14 menciones en US. Alineado con DCAT para interoperabilidad.

---

### Decreto `Class`

**URI**: `Decree`

**Definición**: Norma dictada por autoridad sujeta a control externo de CGR (Toma de Razón), típicamente para modificaciones presupuestarias que afectan Partida 31.

---

### Departamento `Class`

**URI**: `Department`

**Definición**: Unidad organizacional de segundo nivel, subordinada a una División.

---

### deriva de artículo `ObjectProperty`

**URI**: `derivesFromArticle`

**Definición**: Relaciona un mandato legal con el artículo específico de ley del que deriva.

---

### descripción población objetivo `DatatypeProperty`

**URI**: `targetPopulationDescription`

**Definición**: Descripción cualitativa de la población objetivo.

---

### desde fase `ObjectProperty`

**URI**: `fromIPRPhase`

**Definición**: Fase de origen de la transición.

---

### designa `ObjectProperty`

**URI**: `designates`

**Definición**: Relación institucional de designación/nombramiento (p.ej., Presidencia designa Delegado Presidencial Regional).

---

### Devengo `Class`

**URI**: `AccrualEvent`

**Definición**: Devengo: hito de recepción conforme que genera obligación de pago y pasivo contable.

---

### dispara alerta `ObjectProperty`

**URI**: `triggersAlert`

**Definición**: Evento que dispara una alerta en el sistema.

---

### División `Class`

**URI**: `Division`

**Definición**: Unidad organizacional de primer nivel dentro del GORE, con responsabilidad sobre un área funcional específica.

> **Ejemplo**: División de Planificación y Desarrollo (DIPLADE), División de Presupuesto e Inversión Regional (DIPIR).

---

### Documento Legal `Class`

**URI**: `LegalDocument`

**Definición**: Cuerpo normativo formal (ley, decreto, reglamento) que establece obligaciones y derechos.

> **Ejemplo**: DFL 1-19.175 (LOC GORE), Ley 21.033 (Creación Región de Ñuble).

---

### es administrado por `ObjectProperty`

**URI**: `isManagedBy`

**Definición**: Indica la organización que administra operacionalmente una fuente de financiamiento.

---

### es BNUP `DatatypeProperty`

**URI**: `isBNUP`

**Definición**: Indica si el terreno de intervención es Bien Nacional de Uso Público.

---

### es capital de `ObjectProperty`

**URI**: `isCapitalOf`

**Definición**: Indica que una comuna es la capital administrativa de una provincia.

---

### es evaluada por `ObjectProperty`

**URI**: `isEvaluatedBy`

**Definición**: Organización responsable de la evaluación técnica (se puede aplicar tanto a una IPR concreta como a un mecanismo de financiamiento).

*Nota*: Alineado con gist:hasParticipant para participación en rol de evaluador.

---

### es propiedad de `ObjectProperty`

**URI**: `isOwnedBy`

**Definición**: Indica la organización responsable/propietaria (en términos institucionales) de un instrumento de planificación.

---

### es provista por `ObjectProperty`

**URI**: `isProvidedBy`

**Definición**: Indica qué organización provee o ejerce una función institucional.

---

### establece `ObjectProperty`

**URI**: `establishes`

**Definición**: Relaciona un artículo con los mandatos que establece.

*Nota*: Inversa de gnub:derivesFromArticle para navegación bidireccional.

---

### Estado de Admisibilidad `Class`

**URI**: `AdmissibilityState`

**Definición**: Estado de admisibilidad de una IPR en el proceso de gestión.

---

### Estado de Convenio `Class`

**URI**: `AgreementState`

**Definición**: Estado de tramitación del convenio (Borrador, Visado, Firmado, TdR Pendiente, Formalizado).

---

### Estado de Programa `Class`

**URI**: `ProgramIPRState`

**Definición**: Estado operativo válido exclusivamente para Programas Operacionales.

> **Ejemplo**: RF, ITF

---

### Estado de Proyecto `Class`

**URI**: `ProjectIPRState`

**Definición**: Estado operativo válido exclusivamente para Proyectos de Inversión.

> **Ejemplo**: RS, FI, OT, AD, En Licitación, Contrato Firmado

---

### Estado de Rendición `Class`

**URI**: `RenditionState`

**Definición**: Estado del proceso de rendición (Pendiente, En Revisión, Observada, Aprobada, Rechazada).

---

### Estado de Rendición `Class`

**URI**: `AccountabilityState`

**Definición**: Estado de una rendición (Pendiente, En Revisión, Aprobada, Observada, Rechazada).

---

### Estado Operativo IPR `Class`

**URI**: `IPRState`

**Definición**: Estado operativo de una IPR en su ciclo de vida. Granularidad fina para tracking de gestión.

*Nota*: Clase abstracta. Subclases: ProjectIPRState, ProgramIPRState, UniversalIPRState.

---

### Estado Universal IPR `Class`

**URI**: `UniversalIPRState`

**Definición**: Estado operativo válido para cualquier tipo de IPR (Proyecto, Programa, Estudio).

> **Ejemplo**: Admisible, CDP Emitido, Convenio Formalizado, En Obra, IPR Cerrada

---

### Estudio Básico `Class`

**URI**: `BasicStudy`

**Definición**: Iniciativa de inversión (Subt. 31 Item 01) destinada a generar información para decisiones futuras (diagnósticos, planes).

---

### está en etapa de preinversión `ObjectProperty`

**URI**: `currentPreinvestmentStage`

**Definición**: Etapa actual de preinversión en formulación.

---

### está ubicado en `ObjectProperty`

**URI**: `isLocatedIn`

**Definición**: Ubicación geográfica de una entidad.

*Nota*: Reemplazo local para gist:isLocatedIn (no existe en Gist Core).

---

### Etapa de Aprobación `Class`

**URI**: `ApprovalFlowStage`

**Definición**: Etapa del flujo de aprobación de un acto administrativo (Elaboración, V°B° Jurídico, V°B° Control, V°B° Jefatura, Firma Gobernador, TdR CGR).

---

### Etapa de Preinversión `Class`

**URI**: `PreinvestmentStage`

**Definición**: Etapa de madurez del estudio preinversional según normas SNI (Perfil, Factibilidad).

---

### Evento Documental `Class`

**URI**: `DocumentEvent`

**Definición**: Evento documental asociado a IPR (resolución, decreto, certificado, acta).

*Nota*: Modela fact_evento_documental.csv. Extiende gist:Event para trazabilidad de hitos.

---

### Fase de IPR `Class`

**URI**: `IPRPhase`

**Definición**: Fase del ciclo de vida de una IPR según proceso estándar GORE (F0-Postulación, F1-Admisibilidad, F2-Evaluación, F3-Priorización, F4-Formalización, F5-Cierre).

*Nota*: Las transiciones entre fases están modeladas por gnub:IPRStateTransition.

---

### Fase del Ciclo Presupuestario `Class`

**URI**: `BudgetCyclePhase`

**Definición**: Fase del ciclo presupuestario anual (Formulación, Aprobación, Ejecución, etc.).

---

### financia `ObjectProperty`

**URI**: `funds`

**Definición**: Relación de financiamiento institucional (p.ej., SUBDERE financia al GORE).

---

### fiscaliza `ObjectProperty`

**URI**: `audits`

**Definición**: Relación de fiscalización/auditoría (p.ej., CGR fiscaliza al GORE; CORE fiscaliza a la administración regional).

---

### fomento productivo `ObjectProperty`

**URI**: `promotesProductiveDevelopmentIn`

**Definición**: Relación del diagrama: DIFOI ejecuta/coordina fomento productivo en el territorio.

---

### Fondo Temático `Class`

**URI**: `ThematicFund`

**Definición**: Fondo temático específico dentro de la Subvención 8%.

---

### Fuente de Financiamiento `Class`

**URI**: `FundingSource`

**Definición**: Clasificador de origen de recursos presupuestarios regionales (FNDR, FRPD, FATC, FIC, etc.).

*Nota*: Clasificador puro (Category). FRIL/8% son Mecanismos, no Fondos. Para saldos usar BudgetaryAccount.

---

### Función de Desarrollo Social `Class`

**URI**: `DesarrolloSocialFunction`

**Definición**: Funciones relacionadas con el desarrollo social y cultural (Art. 19 LOC).

---

### Función de Fomento Productivo `Class`

**URI**: `FomentoProductivoFunction`

**Definición**: Funciones relacionadas con el fomento productivo y la innovación (Art. 18 LOC).

---

### Función de Gestión Interna `Class`

**URI**: `GestionInternaFunction`

**Definición**: Atribuciones de gestión administrativa y financiera interna (Art. 20 LOC).

---

### Función de Ordenamiento Territorial `Class`

**URI**: `OrdenamientoTerritorialFunction`

**Definición**: Funciones relacionadas con la organización del territorio (Art. 17 LOC).

---

### Función del GORE `Class`

**URI**: `GOREFunction`

**Definición**: Función del Gobierno Regional según LOC GORE: planificar, financiar, ejecutar, coordinar, normar.

---

### gatilla pago `ObjectProperty`

**URI**: `triggersPayment`

**Definición**: Hito cumplido que gatilla un pago (cuota de convenio).

---

### gatillada por `ObjectProperty`

**URI**: `triggeredBy`

**Definición**: Acto administrativo que gatilla la transición (ej. Resolución de aprobación, Certificado CORE).

---

### gestiona financiamiento para `ObjectProperty`

**URI**: `managesFundingFor`

**Definición**: Relación de gestión de financiamiento para proyectos (p.ej., DIPIR gestiona financiamiento para servicios públicos regionales).

---

### gobierna `ObjectProperty`

**URI**: `governs`

**Definición**: Superpropiedad que agrupa todas las formas de ejercicio de autoridad, control, financiamiento o regulación.

---

### gobierno interior `ObjectProperty`

**URI**: `exercisesInteriorGovernmentOver`

**Definición**: Relación del diagrama: Delegación Presidencial ejerce gobierno interior sobre un territorio (provincia/región).

---

### hacia fase `ObjectProperty`

**URI**: `toIPRPhase`

**Definición**: Fase de destino de la transición.

---

### Hito de Proyecto `Class`

**URI**: `ProjectMilestone`

**Definición**: Hito clave de ejecución de IPR (Inicio Obras, Recepción Provisoria, Término). Tiene objetivo y fecha planificada.

*Nota*: Usa gist:plannedStartDateTime y gist:actualStartDateTime para fechas planificadas vs. reales. Subclase de ScheduledTask porque tiene Goal.

---

### Indicador `Class`

**URI**: `Indicator`

**Definición**: Métrica o indicador de gestión para medición de desempeño, avance o cumplimiento.

*Nota*: Usar con gist:Magnitude para valores y gist:Aspect para dimensión medida.

---

### Indicador Territorial `Class`

**URI**: `TerritorialIndicator`

**Definición**: Indicador con dimensión territorial: asociado a comuna, provincia o región.

---

### Informe de Ejecución `Class`

**URI**: `ExecutionReport`

**Definición**: Reporte mensual de ejecución física y financiera de una IPR.

*Nota*: Modela fact_ejecucion_mensual.csv. Extiende gist:Event como ocurrencia periódica.

---

### Institución Postulante `Class`

**URI**: `ApplicantInstitution`

**Definición**: Tipo de entidad habilitada para postular a fondos (ej. Municipalidad, ONG, Univ).

---

### Instrumento de Planificación `Class`

**URI**: `PlanningInstrument`

**Definición**: Instrumento de planificación regional vinculante (ERD, PROT, ARI, etc.).

*Nota*: Modela documentos normativos/especificaciones que guían la planificación territorial.

---

### Instrumento Financiero `Class`

**URI**: `FinancialInstrument`

**Definición**: Instrumento financiero o presupuestario (ej. Línea Presupuestaria).

*Nota*: Creada localmente para reemplazar gist:FinancialInstrument que no existe en Gist 14 Core.

---

### Intervención Pública Regional `Class`

**URI**: `IPR`

**Alias**: IPR

**Definición**: Intervención Pública Regional: término paraguas para cualquier acción (proyecto, programa, estudio) financiada por el GORE para objetivos de desarrollo.

---

### Log de Auditoría `Class`

**URI**: `AuditLog`

**Definición**: Registro de auditoría con trazabilidad completa de acciones de usuarios y cambios en el sistema.

*Nota*: Cumple con requisitos CGR de trazabilidad.

---

### Log de Errores `Class`

**URI**: `ErrorLog`

**Definición**: Registro de errores y excepciones del sistema para debugging y monitoreo.

---

### Log de Sistema `Class`

**URI**: `SystemLog`

**Definición**: Registro de actividad del sistema para trazabilidad y auditoría. Captura eventos, acciones de usuarios y cambios de estado.

*Nota*: Identificado en 72 menciones en US. Patrón Gist: Content con timestamp.

---

### Log de Transacciones `Class`

**URI**: `TransactionLog`

**Definición**: Registro de transacciones del sistema, especialmente operaciones financieras y presupuestarias.

---

### Línea Presupuestaria `Class`

**URI**: `BudgetLine`

**Definición**: Línea presupuestaria asignada a una IPR, vinculando clasificadores, montos y años.

*Nota*: Modela fact_linea_presupuestaria.csv. Extiende gist:FinancialInstrument para alineación con finanzas.

---

### Mandato Legal `Class`

**URI**: `LegalMandate`

**Definición**: Obligación, atribución o deber impuesto por una ley o norma jurídica a un órgano o autoridad.

> **Ejemplo**: La obligación del Gobernador de someter al CORE el presupuesto regional.

---

### Mecanismo de Financiamiento `Class`

**URI**: `FinancingMechanism`

**Definición**: Especificación de la vía de aplicación y evaluación de una IPR. Define proceso, criterios y responsables de evaluación técnica.

*Nota*: Alineado con gist:CatalogItem ya que los mecanismos son 'plantillas' que definen cómo se materializan IPRs concretas.

---

### Meses Máximos Ejecución `DatatypeProperty`

**URI**: `maxExecutionMonths`

**Definición**: Plazo máximo de ejecución en meses permitido por la normativa del mecanismo.

*Nota*: Excepción pragmática: valor simple sin reificar como gist:Magnitude dado que no hay razonamiento dimensional requerido.

---

### Modalidad de Implementación `Class`

**URI**: `ImplementationMode`

**Definición**: Modalidad de ejecución administrativa de una iniciativa (Directa GORE, Transferencia).

---

### Modificación Presupuestaria `Class`

**URI**: `BudgetModificationEvent`

**Definición**: Modificación presupuestaria: reasignación, suplemento o transferencia de recursos.

---

### Modificación Presupuestaria `Class`

**URI**: `BudgetModification`

**Definición**: Modificación presupuestaria que afecta recursos asignados a IPR.

*Nota*: Modela fact_modificacion.csv. Extiende gist:Event como cambio en el tiempo.

---

### Monto Comprometido `Aspect`

**URI**: `CommittedAmountAspect`

**Definición**: Aspecto: monto comprometido cierto (OC, Contratos formalizados).

---

### Monto Devengado `Aspect`

**URI**: `AccruedAmountAspect`

**Definición**: Aspecto: monto devengado (obligación exigible tras recepción conforme).

---

### Monto Ejecutado (DEPRECATED) `Aspect`

**URI**: `ExecutedAmountAspect`

**Definición**: DEPRECATED: Usar gnub:AccruedAmountAspect para nuevas implementaciones.

---

### Monto Pagado `Aspect`

**URI**: `PaidAmountAspect`

**Definición**: Aspecto: monto pagado (egreso efectivo que extinguió obligación).

---

### Monto Pre-Comprometido `Aspect`

**URI**: `PreCommittedAmountAspect`

**Definición**: Aspecto: monto pre-afectado (CDPs emitidos).

---

### Monto Presupuestado `Aspect`

**URI**: `BudgetedAmountAspect`

**Definición**: Aspecto: monto presupuestado inicial (Ley de Presupuestos).

---

### máximo gasto administrativo `ObjectProperty`

**URI**: `hasMaxAdminCost`

**Definición**: Porcentaje máximo del presupuesto total permitido para gastos administrativos.

---

### Nivel de Evaluación `Class`

**URI**: `EvaluationTier`

**Definición**: Nivel de proporcionalidad de la evaluación SNI (Nivel 0 a 3).

---

### nomina terna para `ObjectProperty`

**URI**: `nominatesCandidatesFor`

**Definición**: Relación de nominación de terna del diagrama: el Gobernador nomina candidatos para cargos SEREMI.

---

### norma `ObjectProperty`

**URI**: `regulates`

**Definición**: Relación de regulación normativa (p.ej., SUBDERE norma al GORE).

---

### Notificación `Class`

**URI**: `Notification`

**Definición**: Mensaje informativo enviado a un usuario del sistema. Menos urgente que una Alerta.

---

### número de artículo `DatatypeProperty`

**URI**: `articleNumber`

**Definición**: Número del artículo dentro del documento legal (ej. '16', '21 bis').

---

### obliga a `ObjectProperty`

**URI**: `binds`

**Definición**: Indica a qué organización obliga o aplica un mandato legal.

---

### obras públicas `ObjectProperty`

**URI**: `deliversPublicWorksIn`

**Definición**: Relación del diagrama: DIINF ejecuta/coordina obras públicas en el territorio.

---

### Ontología GORE Ñuble (Core) `Ontology`

**URI**: `goreNubleOntology`

**Definición**: Esquema conceptual unificado (TBox) del Gobierno Regional de Ñuble. Consolida modelos organizacionales, legales y de gestión de inversiones, extendiendo gist 14.0.

---

### Pago `Class`

**URI**: `PaymentEvent`

**Definición**: Pago: egreso efectivo de fondos (TEF/Cheque) que extingue la obligación.

---

### Partida Presupuestaria `Class`

**URI**: `BudgetPartida`

**Definición**: Nivel 1: Partida presupuestaria (ej. Partida 31 GORES).

---

### Permite Gastos Personal `DatatypeProperty`

**URI**: `allowsPersonnelExpenses`

**Definición**: Indica si la regla permite imputar gastos en personal.

---

### pertenece a disciplina `ObjectProperty`

**URI**: `belongsToDiscipline`

**Definición**: Disciplina de conocimiento a la que pertenece una entidad o proceso.

*Nota*: Usado para clasificar entidades en las 12 disciplinas identificadas: FIN, IPR, ORG, GOV, NORM, LOC, PLAN, SEG, SOC, SYS, TDE, GEST.

---

### pertenece a documento `ObjectProperty`

**URI**: `belongsToLegalDocument`

**Definición**: Relaciona un artículo con el documento legal al que pertenece.

*Nota*: Alineado con gist:isPartOf: un artículo es parte de un documento legal.

---

### pertenece a fase `ObjectProperty`

**URI**: `belongsToPhase`

**Definición**: Vincula un estado operativo con su fase de alto nivel.

---

### pertenece a track `ObjectProperty`

**URI**: `hasEvaluationTrack`

**Definición**: Track de evaluación al que pertenece este resultado.

---

### Playbook `Class`

**URI**: `Playbook`

**Definición**: Procedimiento operativo estándar para respuesta a incidentes o situaciones predefinidas.

*Nota*: Usado en CIES para gestión de emergencias.

---

### plazo máximo ejecución `ObjectProperty`

**URI**: `hasMaxExecTime`

**Definición**: Plazo máximo de ejecución.

---

### Pre-Compromiso (CDP) `Class`

**URI**: `PreCommitmentEvent`

**Definición**: Pre-afectación: emisión de CDP que reserva saldo presupuestario.

---

### preside `ObjectProperty`

**URI**: `chairs`

**Definición**: Relación de presidencia de órgano colegiado (p.ej., Gobernador preside el CORE).

---

### Presupuesto Vigente `Aspect`

**URI**: `CurrentBudgetAspect`

**Definición**: Aspecto: presupuesto vigente (post-modificaciones).

---

### Proceso de Rendición `Class`

**URI**: `AccountabilityProcess`

**Definición**: Proceso de rendición de cuentas de transferencias GORE, ejecutado vía SISREC.

*Nota*: Gobernado por GOREAgreement. Participantes: RTF y UCR.

---

### produce resultado `ObjectProperty`

**URI**: `producesResult`

**Definición**: Tipo de resultado/dictamen que produce este track de evaluación.

---

### Programa de Inversión (SNI) `Class`

**URI**: `InvestmentProgram`

**Alias**: ProgInv

**Definición**: Conjunto de proyectos de inversión (Subt. 31 Item 03) articulados bajo un propósito común y duración finita.

---

### Programa Operacional `Class`

**URI**: `OperationalProgram`

**Alias**: PPR

**Definición**: IPR de gasto corriente (Subtítulo 24) orientada a entregar servicios o prestaciones continuas a una población objetivo (PPR).

---

### Programa Presupuestario `Class`

**URI**: `BudgetProgram`

**Definición**: Nivel 3: Programa presupuestario (ej. Programa 01 Funcionamiento, 02 Inversión).

---

### programas sociales `ObjectProperty`

**URI**: `deliversSocialProgramsIn`

**Definición**: Relación del diagrama: DIDESO ejecuta/coordina programas sociales en el territorio.

---

### Provincia `Class`

**URI**: `Province`

**Definición**: División político-administrativa intermedia entre región y comuna en Chile, gobernada por un Delegado Presidencial Provincial.

*Nota*: Extendida de gist:GovernedGeoRegion (no GeoRegion) ya que es una entidad con gobierno propio.

---

### Proyecto de Inversión `Class`

**URI**: `IPRProject`

**Alias**: IDI

**Definición**: IPR de gasto de capital (Subtítulo 31 o 33) orientada a crear, ampliar, reponer o mejorar activos físicos o intangibles de larga duración.

---

### recibe rendición (otorgante) `ObjectProperty`

**URI**: `receivesRendition`

**Definición**: Entidad otorgante que recibe la rendición (GORE como participante en rol de otorgante).

---

### Regla Presupuestaria `Class`

**URI**: `BudgetaryRule`

**Definición**: Regla operativa definida en la Ley de Presupuestos o normativa financiera que restringe el uso de recursos.

---

### Rendición de Cuentas `Class`

**URI**: `Rendition`

**Definición**: Procedimiento administrativo mediante el cual una entidad ejecutora demuestra y justifica la correcta utilización de fondos públicos recibidos del GORE.

*Nota*: Modela el evento de rendición como gist:Event con participantes (entidad ejecutora, GORE) y fases.

---

### Requiere Cofinanciamiento `DatatypeProperty`

**URI**: `requiresCoFinancing`

**Definición**: Indica si la regla exige cofinanciamiento por parte de la entidad postulante.

---

### requiere evaluación `ObjectProperty`

**URI**: `requiresEvaluation`

**Definición**: Track de evaluación técnica requerido por el mecanismo.

---

### requiere rendición `ObjectProperty`

**URI**: `requiresAccountability`

**Definición**: Convenio que requiere proceso de rendición de cuentas.

---

### Resolución `Class`

**URI**: `Resolution`

**Definición**: Decisión formal del GORE que puede ser exenta o afecta a Toma de Razón de CGR. Según Ley 19.880, es el medio principal de formalización de actos administrativos.

*Nota*: Dualidad Gist: Es un gnub:AdministrativeAct (Agreement/Commitment) expresado en un gist:FormattedContent categorizado como gnub:AdministrativeDocumentType.

---

### Resultado de Evaluación `Class`

**URI**: `EvaluationResult`

**Definición**: Resultado de la evaluación técnico-económica de una IPR.

---

### Riesgo `Class`

**URI**: `Risk`

**Definición**: Categoría de riesgo identificado en gestión institucional: operacional, financiero, reputacional, legal o de seguridad.

*Nota*: Identificado en 16 menciones en US. Base para sistema CIES.

---

### rinde cuentas (ejecutor) `ObjectProperty`

**URI**: `rendersAccount`

**Definición**: Entidad ejecutora que rinde cuentas (participante en rol de ejecutor).

---

### rinde por convenio `ObjectProperty`

**URI**: `rendersFor`

**Definición**: Convenio de transferencia al que corresponde esta rendición.

---

### Rol en Rendición `Class`

**URI**: `RenditionRole`

**Definición**: Rol de un actor en el proceso de rendición SISREC (Analista Ejecutor, Ministro de Fe, Encargado Ejecutor, Analista Otorgante, Encargado Otorgante).

---

### Saldo Disponible `Aspect`

**URI**: `AvailableBalanceAspect`

**Definición**: Aspecto: saldo disponible (Vigente - Comprometido).

---

### se ejecuta mediante `ObjectProperty`

**URI**: `isExecutedVia`

**Definición**: Convenio a través del cual se ejecuta la IPR.

---

### Subtítulo Presupuestario `Class`

**URI**: `BudgetSubtitle`

**Definición**: Nivel 4: Subtítulo del gasto (ej. 21 Personal, 24 Transferencias Corrientes, 33 Transferencias Capital).

---

### supervisa `ObjectProperty`

**URI**: `supervises`

**Definición**: Relación de supervisión jerárquica entre Asignaciones (ej. Jefatura de División supervisa a Jefatura de Departamento).

---

### tiene avance físico `ObjectProperty`

**URI**: `hasPhysicalProgress`

**Definición**: Avance físico actual de la IPR (Magnitude con PhysicalProgressAspect).

---

### tiene avance planificado `ObjectProperty`

**URI**: `hasPlannedProgress`

**Definición**: Avance físico planificado según cronograma (Magnitude con PlannedProgressAspect).

---

### tiene componente `ObjectProperty`

**URI**: `hasProgramComponent`

**Definición**: Relaciona un programa con sus componentes (bienes/servicios).

---

### tiene cuenta presupuestaria `ObjectProperty`

**URI**: `hasBudgetaryAccount`

**Definición**: Cuenta presupuestaria asociada a la IPR para seguimiento de ejecución.

---

### tiene ejecutor `ObjectProperty`

**URI**: `hasExecutor`

**Definición**: Organización responsable de ejecutar técnica y financieramente la IPR (puede ser distinta del postulante).

*Nota*: Para FRIL: municipio. Para SNI directa: GORE. Para transferencias: ONG/Universidad/Servicio.

---

### tiene estado de admisibilidad `ObjectProperty`

**URI**: `hasAdmissibilityState`

**Definición**: Estado de admisibilidad actual de la IPR.

---

### tiene estado de convenio `ObjectProperty`

**URI**: `hasAgreementState`

**Definición**: Estado actual de tramitación del convenio.

---

### tiene estado de rendición `ObjectProperty`

**URI**: `hasRenditionState`

**Definición**: Estado actual del proceso de rendición.

---

### tiene estado de rendición `ObjectProperty`

**URI**: `hasAccountabilityState`

**Definición**: Estado actual del proceso de rendición.

---

### tiene estado operativo `ObjectProperty`

**URI**: `hasIPRState`

**Definición**: Estado operativo actual de la IPR (granularidad fina).

---

### tiene etapa de aprobación `ObjectProperty`

**URI**: `hasApprovalStage`

**Definición**: Etapa actual en el flujo de aprobación del acto administrativo.

---

### tiene evento documental `ObjectProperty`

**URI**: `hasDocumentEvent`

**Definición**: Evento documental asociado a esta IPR.

---

### tiene expediente `ObjectProperty`

**URI**: `hasExpedient`

**Definición**: Relaciona una rendición con su expediente electrónico (tde:ExpedienteElectronico).

---

### tiene fase actual `ObjectProperty`

**URI**: `hasCurrentPhase`

**Definición**: Fase actual del ciclo de vida de la IPR.

---

### tiene fuente de financiamiento `ObjectProperty`

**URI**: `hasFundingSource`

**Definición**: Clasificador de fuente de recursos para la IPR (FNDR, FRPD, etc.).

*Nota*: Apunta a FundingSource (Category). Para saldos usar hasBudgetaryAccount.

---

### tiene hito `ObjectProperty`

**URI**: `hasProjectMilestone`

**Definición**: Conecta una IPR con sus hitos de ejecución.

---

### tiene informe de ejecución `ObjectProperty`

**URI**: `hasExecutionReport`

**Definición**: Informe de ejecución asociado a esta IPR.

---

### tiene línea presupuestaria `ObjectProperty`

**URI**: `hasBudgetLine`

**Definición**: Línea presupuestaria asignada a esta IPR.

---

### tiene mandato legal `Class`

**URI**: `hasLegalMandate`

**Definición**: Relaciona un órgano o autoridad con un mandato legal específico.

*Nota*: Alineado con gist:isGovernedBy: los mandatos legales gobiernan el comportamiento de las organizaciones.

---

### tiene modalidad de implementación `ObjectProperty`

**URI**: `hasImplementationMode`

**Definición**: Modalidad de ejecución del IPR (Directa o Transferencia).

---

### tiene modificación presupuestaria `ObjectProperty`

**URI**: `hasBudgetModification`

**Definición**: Modificación presupuestaria que afecta a esta IPR.

---

### tiene nivel de evaluación `ObjectProperty`

**URI**: `hasEvaluationTier`

**Definición**: Nivel de proporcionalidad asignado para evaluación (0, 1, 2, 3).

---

### tiene postulante `ObjectProperty`

**URI**: `hasApplicant`

**Definición**: Organización que postula la iniciativa (distinto del ejecutor financiero).

*Nota*: Alineado con gist:hasParty para participación en el contexto de la IPR.

---

### tiene riesgo `ObjectProperty`

**URI**: `hasRisk`

**Definición**: Riesgo asociado a una entidad, proceso o proyecto.

---

### tiene severidad `ObjectProperty`

**URI**: `hasSeverity`

**Definición**: Nivel de severidad de la alerta (Crítica, Alta, Media, Baja, Informativa).

---

### tiene tag `ObjectProperty`

**URI**: `hasTag`

**Definición**: Tag o etiqueta de folksonomy asociada a una entidad para clasificación flexible.

*Nota*: 2,002 tags identificados en análisis de US. Instancias en goreNubleReferenceData.ttl.

---

### tiene tipo de alerta `ObjectProperty`

**URI**: `hasAlertType`

**Definición**: Tipo de alerta según clasificación institucional.

---

### tiene tipología de inversión `ObjectProperty`

**URI**: `hasInvestmentTypology`

**Definición**: Clasificación sectorial (RIS) requerida para iniciativas evaluadas bajo el Sistema Nacional de Inversiones (SNI) (ej. Edificación, Patrimonio).

---

### tiene umbral máximo `ObjectProperty`

**URI**: `hasThreshold`

**Definición**: Umbral o monto máximo aplicable (requiere magnitud con unidad: UTM, CLP, etc).

---

### tiene URI `DatatypeProperty`

**URI**: `hasURI`

**Definición**: Enlace a recurso web externo (URL).

*Nota*: Reemplazo local para gist:hasURI.

---

### Tipo de Alerta `Class`

**URI**: `AlertType`

**Definición**: Categoría de alerta según su naturaleza: seguridad, cumplimiento, operacional, vencimiento, umbral o reputacional.

---

### Tipo de Cargo `Class`

**URI**: `PositionType`

**Definición**: Tipo de cargo o posición dentro de la estructura organizacional.

---

### Tipo de Competencia `Class`

**URI**: `CompetencyType`

**Definición**: Tipo de competencia administrativa transferible (temporal o definitiva).

---

### Tipo de Convenio `Class`

**URI**: `AgreementType`

**Definición**: Tipo de convenio según su naturaleza (Mandato, Transferencia, Colaboración, etc.).

*Nota*: Para clasificación adicional más allá de las subclases.

---

### Tipo de Documento `Class`

**URI**: `DocumentType`

**Definición**: Categoría que clasifica tipos de documentos administrativos del GORE.

*Nota*: DEPRECADO: Usar gnub:AdministrativeDocumentType preferentemente. Mantenido por compatibilidad.

---

### Tipo de Documento Administrativo `Class`

**URI**: `AdministrativeDocumentType`

**Definición**: Categoría que clasifica documentos administrativos por su tipo jurídico (Resolución, Decreto, Oficio, etc.).

*Nota*: Usar con gist:FormattedContent + gist:isCategorizedBy. Las instancias son Reference Data en goreNubleApprovalData.ttl.

---

### Tipo de Glosa `Class`

**URI**: `GlossType`

**Definición**: Tipo de glosa presupuestaria según su naturaleza y estructura.

---

### Tipo de Población `Class`

**URI**: `PopulationType`

**Definición**: Tipo de población según Marco Lógico (Potencial, Objetivo, Beneficiaria).

---

### Tipo de Unidad Organizacional `Class`

**URI**: `OrganizationalUnitType`

**Definición**: Tipo de unidad organizacional (ej. División, Departamento, Unidad).

---

### Tipología de Inversión `Class`

**URI**: `InvestmentTypology`

**Definición**: Tipología de inversión que determina los Requisitos de Información Sectorial (RIS) aplicables.

---

### Track de Evaluación `Class`

**URI**: `EvaluationTrack`

**Definición**: Vía o sistema de evaluación técnico-económica de IPR (RATE, Glosa06, Local, CTCI).

---

### Transacción Presupuestaria `Class`

**URI**: `BudgetaryTransaction`

**Definición**: Operación que modifica saldo de cuenta presupuestaria.

---

### transición de `ObjectProperty`

**URI**: `transitionOf`

**Definición**: IPR sujeta a la transición de estado.

---

### Transición de Estado IPR `Class`

**URI**: `IPRStateTransition`

**Definición**: Transición entre dos fases/estados en el ciclo de vida de una IPR (ej. F1→F2, PRE-ADMISIBLE→ADMISIBLE).

*Nota*: Modela el MCD (Modelo Canónico de Estados) del modelo Omega como eventos de transición.

---

### tutela `ObjectProperty`

**URI**: `hasTutelaOver`

**Definición**: Relación de tutela administrativa (p.ej., Ministerio del Interior tutela al Gobierno Interior regional).

---

### Unidad `Class`

**URI**: `Unit`

**Definición**: Unidad organizacional de tercer nivel, subordinada a un Departamento o División.

---

### Unidad de Staff `Class`

**URI**: `StaffUnit`

**Definición**: Unidad de apoyo o staff, con funciones transversales (ej. Gabinete, Jurídica, Auditoría).

---

### usa mecanismo de financiamiento `ObjectProperty`

**URI**: `usesFinancingMechanism`

**Definición**: Mecanismo/track de postulación y evaluación utilizado por la IPR.

---

### Usuario de Sistema `Class`

**URI**: `SystemUser`

**Alias**: Usuario

**Definición**: Usuario autenticado del sistema con credenciales y permisos asignados.

*Nota*: Identificado en 28 menciones en US. Normalizado de USER y USUARIO.

---

### vigencia (años) `DatatypeProperty`

**URI**: `hasValidityPeriod`

**Definición**: Vigencia del resultado de evaluación en años.

---

### Ítem Presupuestario `Class`

**URI**: `BudgetItem`

**Definición**: Nivel 5: Ítem presupuestario (ej. 01 Al Sector Privado, 03 A Otras Entidades).

---

### Órgano Asesor `Class`

**URI**: `AdvisoryBody`

**Definición**: Órgano asesor o consultivo sin jerarquía lineal (ej. COSOC, Comité CTCI).

---

## tdeCore

### Cargo `Class`

**URI**: `Cargo`

**Definición**: Posición o puesto de trabajo formal dentro de la estructura de un OAE.

*Nota*: Reemplaza a gist:Position (no presente en Gist 14). Usar con gist:Assignment.

---

### Disponibilidad `Aspect`

**URI**: `AspectDisponibilidad`

**Definición**: Aspecto medible que representa el porcentaje de disponibilidad (SLA) de una plataforma.

---

### Estado de Trámite `Class`

**URI**: `EstadoTramite`

**Definición**: Categoría que representa el estado del ciclo de vida de un trámite.

---

### Estado de Vigencia `Class`

**URI**: `EstadoVigencia`

**Definición**: Categoría que representa el estado de vigencia de una norma o especificación.

---

### Expediente Electrónico `Class`

**URI**: `ExpedienteElectronico`

**Definición**: Conjunto ordenado de documentos y actuaciones electrónicas que sirven de antecedente y fundamento a la resolución administrativa, conforme DS N°10.

*Nota*: Los documentos se relacionan mediante gist:isMemberOf. Debe tener gist:uniqueText con el IUIe (Identificador Único).

---

### Fase de Iniciativa de Inversión `Class`

**URI**: `FaseIniciativaInversion`

**Definición**: Categoría que representa las fases del ciclo de vida de una iniciativa de inversión (Formulación, Evaluación, Ejecución, Cierre).

*Nota*: Alternativa Gist-pura a gnub:IPRPhase. Usar con gist:Project + gist:isCategorizedBy.

---

### Nivel de Gobierno `Class`

**URI**: `NivelGobierno`

**Definición**: Categoría que clasifica organizaciones gubernamentales por su nivel (central, regional, municipal).

---

### Nivel de Madurez `Aspect`

**URI**: `AspectNivelMadurez`

**Definición**: Aspecto medible que representa el nivel de madurez en gestión de datos (MGDE).

---

### Nivel de Madurez MGDE `Class`

**URI**: `NivelMadurezMGDE`

**Definición**: Categoría que representa los niveles de madurez del Marco de Gestión de Datos del Estado.

---

### Plataforma Digital `Class`

**URI**: `PlataformaDigital`

**Definición**: Sistema tecnológico del Estado que habilita la provisión de servicios digitales o funciones transversales de soporte.

> **Ejemplo**: ClaveÚnica, SIMPLE, DocDigital, PISEE, Datos.gob.cl

*Nota*: Usa gist:isGovernedBy para OAE responsable (mínimo 1). Usa gist:conformsTo para norma técnica aplicable. Usa gist:isCategorizedBy con tde:TipoPlataforma.

---

### Rol TDE `Class`

**URI**: `RolTDE`

**Definición**: Categoría que representa roles funcionales en la Transformación Digital.

---

### TDE Core Ontology `Ontology`

**URI**: `tde`

**Definición**: Ontología Core para la Transformación Digital del Estado de Chile (TDE). Extensión de Gist 14.0 con máximo alineamiento.

---

### Tiempo de Respuesta `Aspect`

**URI**: `AspectTiempoRespuesta`

**Definición**: Aspecto medible que representa el tiempo normado para respuesta administrativa.

---

### Tipo de Iniciativa de Inversión `Class`

**URI**: `TipoIniciativaInversion`

**Definición**: Categoría que clasifica iniciativas de inversión pública por su fuente de financiamiento o mecanismo.

*Nota*: Usar con gist:Project + gist:isCategorizedBy. NO crear subclases de Project.

---

### Tipo de Norma `Class`

**URI**: `TipoNorma`

**Definición**: Categoría que clasifica instrumentos normativos del marco legal TDE.

---

### Tipo de Plataforma `Class`

**URI**: `TipoPlataforma`

**Definición**: Categoría que clasifica plataformas digitales por su función principal.

---

### Tipo de Servicio Digital `Class`

**URI**: `TipoServicioDigital`

**Definición**: Categoría que clasifica la naturaleza de un servicio digital.

---

### Trámite `Class`

**URI**: `Tramite`

**Definición**: Secuencia de actuaciones administrativas iniciada por un interesado ante un OAE para obtener un derecho, beneficio o cumplir una obligación.

> **Ejemplo**: Solicitud de certificado de nacimiento, postulación a subsidio habitacional.

*Nota*: Usa gist:actualStartDateTime/actualEndDateTime para temporalidad. Usa gist:isCategorizedBy con tde:EstadoTramite para estado.

---

### Órgano de la Administración del Estado `Class`

**URI**: `OrganoAdministracionEstado`

**Alias**: OAE

**Definición**: Entidad administrativa del Estado de Chile según Ley Orgánica Constitucional 18.575.

> **Ejemplo**: Ministerio de Hacienda, Servicio de Registro Civil, Municipalidad de Santiago.

*Nota*: Incluye ministerios, servicios públicos, gobiernos regionales y municipalidades.

---

## tdeDatos

### Calidad de Datos `Aspect`

**URI**: `AspectCalidadDatos`

**Definición**: Aspecto medible que representa el porcentaje de calidad de un conjunto de datos.

---

### Dimensión de Calidad de Datos `Class`

**URI**: `DimensionCalidadDatos`

**Definición**: Categoría que representa las dimensiones de calidad de datos (exactitud, completitud, etc.).

---

### Dimensión MGDE `Class`

**URI**: `DimensionMGDE`

**Definición**: Categoría que representa las 12 dimensiones del Marco de Gestión de Datos del Estado.

---

### Etapa del Ciclo de Vida de Datos `Class`

**URI**: `EtapaCicloVidaDatos`

**Definición**: Categoría que representa las 8 etapas del ciclo de vida de los datos según MGDE.

---

### Madurez MGDE `Aspect`

**URI**: `AspectMadurezMGDE`

**Definición**: Aspecto medible que representa el porcentaje de madurez en una dimensión MGDE (0-100%).

---

### Rol de Gobernanza de Datos `Class`

**URI**: `RolGobernanzaDatos`

**Definición**: Categoría que representa roles en la gobernanza de datos según MGDE.

*Nota*: Usar con gist:Position + gist:isCategorizedBy, o gist:Assignment para asignaciones temporales.

---

### TDE Datos `Ontology`

**URI**: `tdeDatos`

**Definición**: Extensión de la ontología TDE para modelar gestión de datos según el Marco MGDE (adaptación de DAMA al Estado chileno).

---

### Tipo de Activo de Datos `Class`

**URI**: `TipoActivoDatos`

**Definición**: Categoría que clasifica activos de datos por su naturaleza.

*Nota*: Usar con gist:Content + gist:isCategorizedBy.

---

## tdeLexicon

### TDE Lexicon `Ontology`

**URI**: `tdeLexicon`

**Definición**: Lexicon terminológico de la Transformación Digital del Estado de Chile, estructurado como SKOS ConceptScheme.

---

## tdePrincipios

### Objetivo Estratégico TDE `Class`

**URI**: `ObjetivoEstrategicoTDE`

**Definición**: Categoría que representa los objetivos estratégicos de alto nivel que orientan las políticas, lineamientos y proyectos de Transformación Digital.

*Nota*: Usar con gist:Specification (estrategias, planes), gist:Task (proyectos), gist:Organization (OAEs) mediante gist:isCategorizedBy para trazar alineamiento estratégico.

---

### Principio TDE `Class`

**URI**: `PrincipioTDE`

**Definición**: Categoría que representa los principios rectores transversales de la Transformación Digital del Estado.

*Nota*: Usar con gist:Specification (normativas, políticas), gist:System (plataformas), gist:Event (proyectos) mediante gist:isCategorizedBy para indicar alineamiento con principios.

---

### TDE Principios `Ontology`

**URI**: `tdePrincipios`

**Definición**: Extensión de la ontología TDE para modelar principios rectores y objetivos estratégicos de la Transformación Digital del Estado de Chile.

---

## tdeProcesos

### Cantidad de Documentos `Aspect`

**URI**: `AspectCantidadDocumentos`

**Definición**: Aspecto medible que representa el número de documentos en un expediente.

---

### Duración del Trámite `Aspect`

**URI**: `AspectDuracionTramite`

**Definición**: Aspecto medible que representa la duración en días hábiles de un trámite.

---

### Estado de Expediente `Class`

**URI**: `EstadoExpediente`

**Definición**: Categoría que representa el estado del ciclo de vida de un expediente electrónico según NT DS N°10.

---

### Rol en Procedimiento `Class`

**URI**: `RolProcedimiento`

**Definición**: Categoría que representa los roles de participantes en un procedimiento administrativo.

---

### TDE Procesos `Ontology`

**URI**: `tdeProcesos`

**Definición**: Extensión de la ontología TDE para modelar el ciclo de vida de trámites y expedientes electrónicos según NT DS N°10.

---

### Tipo de Acción de Trazabilidad `Class`

**URI**: `TipoAccionTrazabilidad`

**Definición**: Categoría que clasifica las acciones registradas en la trazabilidad del expediente según Art. 11 DS N°10.

---

### Tipo de Documento Electrónico `Class`

**URI**: `TipoDocumentoElectronico`

**Definición**: Categoría que clasifica documentos electrónicos por su naturaleza jurídico-administrativa.

*Nota*: Usar con gist:FormattedContent + gist:isCategorizedBy.

---

## Estadísticas

- **Total de términos**: 244
- **alignmentGnubTde**: 1 términos
- **goreNubleDipirOntology**: 6 términos
- **goreNubleOntology**: 199 términos
- **tdeCore**: 19 términos
- **tdeDatos**: 8 términos
- **tdeLexicon**: 1 términos
- **tdePrincipios**: 3 términos
- **tdeProcesos**: 7 términos
