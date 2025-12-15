_manifest:
  urn: "urn:knowledge:gorenuble:gn:manual-contabilidad-cierre:1.0.0"
  title: "Manual de Contabilidad Gubernamental y Cierre Financiero"
  federation:
    visibility: internal
  provenance:
    created_by: "GORE Ñuble"
    created_at: "2025-12-14"

ID: MANUAL-CONTABILIDAD-CIERRE-01
Status: Draft

# Manual 1.2: Contabilidad Gubernamental y Cierre Financiero

**Objetivo:** Asegurar la integridad contable bajo normativa NICSP y CGR, garantizando un registro fidedigno, oportuno y trazable de los hechos económicos del Gobierno Regional.

## Sección I: Fundamentos y Marco Normativo

### 1. Introducción y Propósito

El presente manual tiene como objetivo estandarizar y normar los procedimientos contables del Gobierno Regional de Ñuble, asegurando que cada transacción financiera sea registrada de acuerdo con los principios de contabilidad del sector público y la normativa legal vigente. Proporciona una guía clara para los analistas contables, tesoreros, jefaturas y la División de Presupuesto e Inversión Regional (DIPIR) sobre la operación diaria y los procesos críticos de cierre financiero.

### 2. Marco Legal Aplicable

La gestión contable del GORE se rige estrictamente por:

* **Decreto Ley N° 1.263 (1975):** Ley Orgánica de Administración Financiera del Estado.
* **Resolución N° 16 (2015) CGR:** Aprueba normativa del Sistema de Contabilidad General de la Nación (NICSP-CGR).
* **Resolución N° 30 (2015) CGR:** Fija normas sobre rendición de cuentas.
* **Oficios Circulares CGR:** Instrucciones anuales sobre cierres contables y apertura de ejercicio.
* **Instrucciones DIPRES:** Clasificador Presupuestario y manuales operativos SIGFE.

### 3. Glosario de Términos Contables Clave

* **Devengo:** Reconocimiento de una obligación de pago o un derecho de cobro, independientemente de la fecha efectiva de pago o recaudación.
* **NICSP:** Normas Internacionales de Contabilidad para el Sector Público, base del estándar contable chileno.
* **SIGFE:** Sistema de Información para la Gestión Financiera del Estado (agregador central).
* **Deuda Flotante:** Obligaciones devengadas y no pagadas al cierre del ejercicio.
* **Interoperabilidad:** Capacidad de intercambiar información financiera automáticamente entre sistemas (ej. SIGFIN <-> Banco).

---

## Sección II: Plan de Cuentas y Estructura Contable

### 4. Plan de Cuentas Patrimonial CGR

El GORE adopta integralmente el Plan de Cuentas definido por la CGR, estructurado en niveles jerárquicos:

* **Título:** (Ej. 1 ACTIVO)
* **Grupo:** (Ej. 11 ACTIVOS CIRCULANTES)
* **Subgrupo:** (Ej. 111 DISPONIBILIDADES)
* **Cuenta Nivel 1:** (Ej. 11101 BANCO ESTADO)
* **Cuenta Nivel 2:** (Ej. 1110101 CUENTA ÚNICA FISCAL)
* **Desagregados Institucionales:** Niveles adicionales para control de gestión (Ej. Auxiliar por Proyecto/IPR).

**Cuentas de Orden:** Se utilizarán para el control de garantías (boletas, pólizas) y responsabilidades eventuales, sin afectar el patrimonio directamente pero sí la responsabilidad administrativa.

### 5. Configuración del Ambiente Contable Institucional

* **Centros de Costo:** Se definirá un catálogo de centros de costo asociado a la estructura organizacional (Divisiones/Departamentos) para imputar gastos operativos.
* **Centros de Gestión (IPR):** Cada Iniciativa de Inversión (IDI) funcionará como un centro de gestión contable, permitiendo balances por proyecto.
* **Asociación Contable-Presupuestaria:** La "Matriz de Devengamiento" debe mantenerse actualizada en el ERP (SIGFIN), asegurando que cada imputación presupuestaria (Subtítulo/Ítem/Asig) genere automáticamente el asiento contable patrimonial correcto (Ej. Gastos en Personal -> Cuenta de Gasto Patrimonial + Pasivo Corriente).

### 6. Biblioteca de Asientos Contables (Memoria Contable)

El sistema ERP debe operar con "Asientos Tipo" pre-parametrizados para evitar errores manuales en operaciones recurrentes:

* **Devengo de Remuneraciones:** Automático desde módulo SIGPER.
* **Devengo de Bienes y Servicios:** Automático desde módulo Adquisiciones/Activo Fijo.
* **Ingresos por Transferencia:** Asiento tipo de recepción de aporte fiscal.
* **Rendiciones de Cuentas:** Asiento tipo para regularizar anticipos.
* **Creación de Nuevos Asientos:** Solo el Jefe de Finanzas tiene atribución para crear nuevos modelos de asientos.

---

## Sección III: Registro y Operación Contable

### 7. Comprobantes Contables

El "Comprobante Contable" es el documento fuente único de registro (en papel o digital firmado).

* **Comprobantes Automáticos (Interfaz):** Se generan sin intervención humana directa al aprobarse hitos en módulos auxiliares (Ej. "Recepción Conforme" en Bodega genera el devengo).
* **Comprobantes Manuales:** Se restringen a ajustes, regularizaciones, depreciaciones manuales y correcciones de errores. Deben contar con V°B° de jefatura y adjuntar la "minuta explicativa".
* **Validaciones:** El sistema bloqueará comprobantes descuadrados o aquellos que rompan la lógica "Financiero-Económico" (ej. gasto presupuestario sin contrapartida patrimonial de gasto o activo).

### 8. Centralización Contable

Proceso crítico de integración de sistemas satélites al ERP Financiero:

* **Remuneraciones (SIGPER):** Se centraliza mensualmente tras el cierre de sueldos. Debe validar integridad total (Monto Bruto = Líquido + Leyes Sociales + Retenciones).
* **Activo Fijo y Existencias (SIGAS):** La entrada de bodega genera el alta del activo/existencia y el pasivo con el proveedor (Facturas por Recibir). El consumo de bodega genera el gasto patrimonial.
* **Interoperabilidad Externa:** Recepción automática de decretos de modificación presupuestaria desde DIPRES (si la tecnología lo permite) y cartolas bancarias.

### 9. Gestión de Honorarios

Registro de prestaciones de servicios personales boletas de honorarios:

* Importación de Boletas Electrónicas desde SII.
* Cálculo automático de Retención (tasa vigente).
* Generación de obligación de pago (Devengo) y cuentas por pagar.
* Emisión mensual del **Libro de Honorarios Auxiliar** y certificados de retención anuales (DJ 1879).

### 10. Gestión de Deuda Institucional

Control de la posición financiera:

* **Cuentas por Pagar:** Monitoreo de antigüedad de deuda (Aging). Alerta obligatoria sobre facturas devengadas con más de 30 días de antigüedad (cumplimiento Ley Pago a 30 Días).
* **Deuda Flotante:** Al cierre de año, segregación clara de compromisos devengados no pagados para imputación a caja del año siguiente.
* **Anticipos:** Control estricto de "Fondos por Rendir" y viáticos. Bloqueo de nuevos anticipos a funcionarios/proveedores con rendiciones pendientes.
* **Rendiciones Externas (SISREC):** Las transferencias a terceros (Subtítulos 24 y 33) deben rendirse obligatoriamente a través del Sistema de Rendición Electrónica de Cuentas (SISREC) de la CGR, según Res. Ex. N° 1.858/2023.

---

## Sección IV: Integración Bancaria y Conciliación Contable

> *Nota: Para los procedimientos operativos de Tesorería (pagos, ingresos, garantías), consulte el [Manual 1.3: Tesorería y Gestión de Ingresos](./manual_1_3_tesoreria.md).*

### 11. Administración de Cuentas Corrientes

* Registro único de todas las Cuentas Corrientes Institucionales (FNDR, Operacionales, Fondos de Terceros).
* **Libro Banco:** Registro cronológico de todo movimiento. Debe cuadrar diariamente con el saldo contable de la cuenta "Banco".

### 12. Conciliación Bancaria

Proceso de control interno fundamental para validar la disponibilidad real de recursos.

* **Frecuencia:** Diaria para gestión de caja, Mensual para cierre contable.
* **Método:** Carga electrónica de cartola bancaria (archivo del banco) y cruce automático ("matcheo") por monto y número de documento.
* **Partidas Conciliatorias:** Deben analizarse y depurarse mensualmente.
  * *Cheques girados y no cobrados* (validar caducidad).
  * *Depósitos no reconocidos* (investigar origen inmediato).
  * *Cargos bancarios no contabilizados.*
* **Informe:** Generación del Anexo CGR de Conciliación Bancaria firmado por Tesorero y Jefe de Finanzas.

---

## Sección V: Procesos de Cierre

### 13. Cierre Mensual

Cronograma estricto para asegurar reportes oportunos (ej. día 10 del mes siguiente).

1. **Cierre de Módulos Auxiliares:** Bodega, Activo Fijo, Remuneraciones, Tesorería (no más cheques con fecha del mes).
2. **Centralización:** Ejecución de interfaces pendientes.
3. **Análisis de Cuentas:** Revisión de saldos anómalos (cuentas de activo con saldo acreedor, etc.).
4. **Cuadratura Inter-sistémica:** Saldo Presupuestario vs. Contabilidad Patrimonial.
5. **Generación de Reportes:** Balance de Comprobación y de Saldos, Informe de Ejecución Presupuestaria.
6. **Envío SIGFE:** Generación y transmisión de XML/API a la Contraloría/DIPRES.

### 14. Cierre Anual y Apertura

Proceso solemne de fin de ejercicio.

* **Periodo 13/14:** Uso de períodos de ajuste y cierre según instrucciones CGR.
* **Devengo Total:** Asegurar que todos los bienes y servicios recibidos al 31/12 queden devengados, aunque la factura llegue después.
* **Ajustes:** Depreciación anual, corrección monetaria (si aplica), provisiones de vacaciones, castigos de deuda incobrable.
* **Asiento de Apertura:** El sistema debe generar automáticamente el asiento de apertura del año siguiente (Saldos 31/12 Año X -> Saldos 01/01 Año X+1), garantizando la continuidad de saldos patrimoniales. Las cuentas de resultado se refunden en "Resultados Acumulados".

### 15. Reportería Legal

El sistema debe emitir nativamente los formatos exigidos:

* Balance de 8 Columnas.
* Estado de Situación Financiera (Balance General Clasificado).
* Estado de Resultados.
* Estado de Flujo de Efectivo (Método Directo).
* Estado de Cambios en el Patrimonio Neto.
* Informe de Pasivos Contingentes.

---

## Sección VI: Auditoría y Control

### 16. Auditoría 360° (Pista de Auditoría)

Principio de "Quién, Qué, Cuándo":

* Cada comprobante debe registrar usuario creador, usuario aprobador, fecha y hora exacta.
* **Inmutabilidad:** Un comprobante "Aprobado/Mayorizado" NO se edita. Se reversa con otro comprobante contrario.
* Log de cambios para datos maestros (ej. cambio de cuenta bancaria de proveedor).

### 17. Seguridad

* Segregación de funciones: Quien solicita el gasto no debe ser quien lo aprueba; quien gira el pago no debe ser quien concilia el banco.
* Claves únicas e intransferibles.

---
*Este manual es un documento vivo y debe ser actualizado ante cambios en la normativa NICSP-CGR o en los sistemas de información del GORE.*
