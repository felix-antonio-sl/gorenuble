_manifest:
  urn: "urn:knowledge:gorenuble:gn:manual-activo-fijo:1.0.0"
  title: "Manual 2.3: Gestión del Ciclo de Vida del Activo Fijo"
  federation:
    visibility: internal
  provenance:
    created_by: "GORE Ñuble"
    created_at: "2025-12-14"

ID: MANUAL-ACTIVO-FIJO-01
Status: Draft

# Manual 2.3: Gestión del Ciclo de Vida del Activo Fijo

**Objetivo:** Administrar el patrimonio físico institucional, asegurando el correcto registro, valorización, control y disposición de los bienes conforme a las Normas Internacionales de Contabilidad del Sector Público (NICSP).

## Sección I: Marco Normativo y Clasificación

### 1. Fundamentos Legales

La gestión de activos fijos se rige por:

* **NICSP 17:** Propiedad, Planta y Equipo.
* **NICSP 21:** Deterioro del Valor de Activos No Generadores de Efectivo.
* **NICSP 31:** Activos Intangibles.
* **Resoluciones CGR:** Normativa sobre control patrimonial, bajas y remates.
* **DL 1.263/1975:** Ley de Administración Financiera del Estado.
* **Ley 21.180:** Obligatoriedad del registro electrónico del inventario.

### 2. Clasificación de Bienes

**Por Naturaleza:**

* **Bienes Muebles:** Mobiliario, equipos computacionales, maquinaria, vehículos.
* **Bienes Inmuebles:** Terrenos, edificios, instalaciones, infraestructura.
* **Bienes Intangibles:** Software, licencias, derechos, patentes.

**Por Tratamiento Contable:**

* **Patrimoniales:** Registrados en el balance (valor ≥ umbral de capitalización).
* **Inventario Administrativo:** Bienes menores controlados pero no capitalizados.

**Por Uso:**

* **En Uso:** Asignados a funcionarios o unidades.
* **En Bodega:** Disponibles para asignación.
* **En Comodato:** Cedidos temporalmente a terceros.
* **Dados de Baja:** Fuera de servicio, pendientes de disposición final.

### 3. Umbral de Capitalización

* El GORE define un umbral monetario (típicamente 3 UTM) bajo el cual los bienes se consideran "gasto" y no se capitalizan.
* Bienes bajo el umbral pueden registrarse en inventario administrativo para control físico sin impacto patrimonial.

---

## Sección II: Alta de Bienes

### 4. Recepción y Prealta

**Origen de los Bienes:**

* **Compra Directa (Subtítulo 29):** Adquisición de Activos No Financieros (vehículos, equipos, terrenos) con presupuesto de funcionamiento.
* **Proyectos de Inversión (Subtítulo 31):** Bienes adquiridos en el marco de iniciativas de inversión propia o programas ejecutados directamente (Glosa 06/10).
* **Donaciones recibidas.**
* **Traspasos desde otras instituciones públicas.**
* **Construcción o fabricación propia.**

**Registro Preliminar (Prealta):**

* Verificación física del bien recibido.
* Asignación de tipología y clasificación.
* Registro de datos: fecha de ingreso, documento tributario, valor de adquisición.
* Indicación de ubicación física provisional.
* Asociación de responsable temporal.

### 5. Codificación y Etiquetado

* **Código Único de Bien:** Identificador alfanumérico secuencial generado por el sistema.
* **Etiqueta Física:** Placa metálica o adhesivo con código de barras/QR.
* **Información de Etiqueta:** Código, descripción abreviada, año de alta.
* **Impresión:** El sistema permite imprimir etiquetas individuales o masivas.

### 6. Datos del Alta

* **Datos de Adquisición:**
  * Proveedor.
  * Número de factura u OC.
  * Valor de compra (incluido IVA si no recuperable).
  * Fecha de puesta en marcha (inicio de depreciación).
* **Datos Técnicos:**
  * Marca, modelo, número de serie.
  * Color, dimensiones, características técnicas.
  * Imagen fotográfica.
* **Datos de Gestión:**
  * Ubicación física (edificio, piso, sala).
  * Responsable asignado.
  * Centro de costo asociado.
* **Documentos Adjuntos:**
  * Factura, garantía, manual, póliza de seguro.

### 7. Tipos de Alta

* **Alta Normal:** Bien nuevo adquirido por compra.
* **Alta por Donación:** Requiere resolución de aceptación y valorización por perito si no hay documento de respaldo.
* **Alta por Traspaso:** Desde otra entidad pública, con valor libro informado.
* **Alta por Revalorización:** Bienes detectados en inventario sin registro previo (regularización).
* **Alta Postergada:** Permite registrar el bien sin contabilizarlo inmediatamente (útil para proyectos en curso).

---

## Sección III: Valorización y Depreciación

### 8. Valor Inicial

El bien se registra a su **costo de adquisición**, que incluye:

* Precio de compra.
* Impuestos no recuperables.
* Costos de transporte e instalación.
* Costos de desmantelamiento estimados (si aplica provisión).

### 9. Depreciación

Distribución sistemática del valor del bien a lo largo de su vida útil.

* **Método:** Línea recta (más común en sector público).
* **Inicio:** Mes siguiente a la fecha de puesta en marcha.
* **Vida Útil Estimada:** Según tablas NICSP o definición institucional.
  * Edificios: 50-80 años.
  * Vehículos: 7-10 años.
  * Equipos computacionales: 3-5 años.
  * Mobiliario: 10-15 años.
* **Valor Residual:** Valor estimado al final de la vida útil (puede ser cero).
* **Cálculo Mensual:** Depreciación = (Valor Inicial - Valor Residual) / Vida Útil en meses.
* **Contabilización:** Asiento mensual automático (Gasto Depreciación / Depreciación Acumulada).

### 10. Revalorización

Ajuste del valor contable a valor razonable.

* **Periodicidad:** Al menos cada 5 años para bienes significativos.
* **Método:** Tasación por perito o índices oficiales (IPC, UF).
* **Efecto:** Incremento de valor se registra en Patrimonio (Superávit por Revalorización).
* **Aplicación:** Principalmente para bienes inmuebles y terrenos.

### 11. Deterioro (Impairment)

Reconocimiento de pérdida de valor cuando el valor recuperable es inferior al valor libro.

* **Indicadores:** Daño físico, obsolescencia tecnológica, cambio de uso.
* **Evaluación:** Al menos anual para bienes significativos.
* **Registro:** Gasto por deterioro y reducción del valor libro.
* **Reversión:** Posible si las circunstancias cambian (con límite del valor original depreciado).

---

## Sección IV: Movimientos de Bienes

### 12. Traslado

Cambio de ubicación física dentro de la institución.

* **Tipos:**
  * Entre edificios o pisos.
  * Entre centros de costo.
  * Cambio de responsable.
* **Procedimiento:**
  * Solicitud del área origen.
  * Aceptación del área destino.
  * Actualización en sistema con nuevo responsable y ubicación.
  * Respaldar con acta de entrega-recepción.

### 13. Préstamo y Comodato

* **Préstamo Interno:** Cesión temporal a otra unidad del GORE.
* **Comodato Externo:** Cesión gratuita a terceros (municipalidades, organizaciones).
  * Requiere resolución fundada.
  * Contrato de comodato con plazo y obligaciones.
  * Registro del bien como "En Comodato" sin baja patrimonial.
  * Seguimiento de fecha de devolución.

### 14. Mantención Mayor

Erogaciones que extienden la vida útil o mejoran el rendimiento del bien.

* **Capitalizable:** Si cumple criterios NICSP, se suma al valor del activo.
* **Gasto:** Si solo mantiene capacidades actuales, se registra como gasto del período.
* **Ejemplos Capitalizables:** Ampliación de edificio, overhaul de maquinaria.
* **Registro:** Actualización del valor y recálculo de depreciación futura.

### 15. Descomponetización

Separación de un bien en sus componentes significativos para depreciación diferenciada.

* **Aplicación:** Típico en bienes inmuebles (estructura, instalaciones, acabados).
* **Beneficio:** Reflejar con mayor precisión el consumo de valor de cada componente.
* **Registro:** Cada componente con su propia vida útil y valor.

---

## Sección V: Baja de Bienes

### 16. Causales de Baja

* **Obsolescencia:** Tecnológica o funcional.
* **Deterioro Irreparable:** Daño que hace inviable la reparación.
* **Siniestro:** Robo, incendio, catástrofe.
* **Término de Vida Útil:** Bien completamente depreciado y sin utilidad.
* **Venta o Remate:** Enajenación mediante proceso público.
* **Donación:** Cesión gratuita a otra entidad.
* **Canje:** Intercambio con proveedor.

### 17. Procedimiento de Baja

1. **Informe Técnico:** El área usuaria o mantención certifica el estado del bien.
2. **Resolución de Baja:** Acto administrativo firmado por autoridad competente.
3. **Registro en Sistema:** Cambio de estado a "Dado de Baja", fecha y causal.
4. **Contabilización:** Reverso del valor libro (Activo y Depreciación Acumulada) y reconocimiento de pérdida/utilidad si aplica.
5. **Disposición Final:**
   * Destrucción certificada.
   * Entrega a beneficiario (donación).
   * Venta/remate.

### 18. Remate de Bienes

* **Normativa:** Según instrucciones CGR y reglamento interno.
* **Publicidad:** Aviso público con descripción, valor base y fecha de remate.
* **Modalidad:** Presencial o electrónica.
* **Adjudicación:** Al mejor postor sobre valor base.
* **Registro:** Baja del bien e ingreso contable por venta.

### 19. Donación de Bienes

* Requiere resolución fundada del Gobernador Regional.
* Beneficiarios típicos: Municipalidades, organizaciones sin fines de lucro, otras entidades públicas.
* El bien se da de baja sin generar ingreso.

---

## Sección VI: Control e Inventario

### 20. Toma de Inventario Físico

Verificación periódica obligatoria.

* **Frecuencia:** Al menos anual (obligatorio al 31/12).
* **Alcance:** Totalidad de bienes o por ubicación/responsable.
* **Método:**
  * Lectura de códigos de barras/QR con capturador.
  * Verificación visual del estado.
  * Registro de ubicación real.
  * Actualización de fotografía (opcional).
* **Conciliación:** Comparar inventario físico vs. registro en sistema.

### 21. Tratamiento de Diferencias

* **Sobrante:** Bien físico sin registro. Investigar origen y regularizar con alta por revalorización.
* **Faltante:** Registro sin respaldo físico.
  * Investigación administrativa.
  * Si hay responsabilidad: sumario y reintegro.
  * Si no hay responsabilidad demostrable: baja por pérdida.

### 22. Asignación de Responsables

* Cada bien debe tener un funcionario responsable de su custodia.
* El cambio de responsable se formaliza con acta de entrega-recepción.
* El responsable tiene obligación de informar daños, pérdidas o traslados.
* La desvinculación de un funcionario obliga a reasignar sus bienes.

---

## Sección VII: Cierre y Reportería

### 23. Cierre Mensual

* Ejecución de depreciación del período.
* Generación de comprobante contable (Depreciación/Deterioro).
* Cuadratura entre módulo de Activo Fijo y Contabilidad Patrimonial.

### 24. Cierre Anual

* Inventario físico obligatorio.
* Ajustes de deterioro si corresponde.
* Informe de Activos Fijos para CGR y memorias institucionales.
* Traspaso de saldos al ejercicio siguiente.

### 25. Reportes Estándar

* **Inventario Valorizado:** Listado de bienes con valor libro actual.
* **Bienes por Responsable:** Asignación por funcionario.
* **Bienes por Ubicación:** Distribución geográfica/física.
* **Cuadro de Depreciación:** Valores iniciales, depreciación acumulada, valor libro.
* **Bienes Totalmente Depreciados:** Para evaluación de baja o continuidad de uso.
* **Movimientos del Período:** Altas, bajas, traslados, revalorizaciones.

---

## Sección VIII: Casos Especiales

### 26. Bienes Inmuebles

* Registro detallado: Rol de avalúo, superficie, inscripción CBR.
* Avalúo fiscal actualizado anualmente.
* Seguros y pólizas asociadas.
* Control de concesiones o arriendos si aplica.

### 27. Vehículos

* Datos específicos: Patente, año, kilometraje, revisión técnica.
* Integración con módulo de Flota (ver Manual 2.4).
* Seguros obligatorios (SOAP) y voluntarios.
* Control de mantenciones y combustible.

### 28. Equipamiento TIC

* Registro de licencias asociadas.
* Control de garantías y soporte técnico.
* Vida útil acelerada (3-5 años).
* Procedimiento de sanitización de datos antes de baja.

### 29. Concesiones

Bienes recibidos o entregados en concesión con tratamiento NICSP específico.

* **Fases:** Construcción, explotación, devolución.
* **Registro:** Según modelo NICSP 32 (Acuerdos de Concesión de Servicios).
* **Control:** Seguimiento de obligaciones del concesionario.

---

*Este manual establece el marco integral para la gestión patrimonial del GORE, desde la adquisición hasta la disposición final de los bienes.*
