_manifest:
  urn: "urn:knowledge:gorenuble:gn:manual-inventarios-bodegas:1.0.0"
  title: "Manual 2.2: Gestión de Inventarios y Bodegas"
  federation:
    visibility: internal
  provenance:
    created_by: "GORE Ñuble"
    created_at: "2025-12-14"

ID: MANUAL-INVENTARIOS-BODEGAS-01
Status: Draft

# Manual 2.2: Gestión de Inventarios y Bodegas

**Objetivo:** Controlar el flujo físico de existencias y materiales, asegurando la disponibilidad oportuna de insumos para la operación institucional y el correcto registro contable de los movimientos.

## Sección I: Marco Normativo y Organización

### 1. Fundamentos Legales

La gestión de inventarios se rige por:

* **NICSP (Normas Internacionales de Contabilidad del Sector Público):** Tratamiento contable de existencias y valorización.
* **Resoluciones CGR:** Normativa sobre control patrimonial y rendición de cuentas.
* **Reglamento Interno de Bodegas:** Documento institucional que define procedimientos operativos y responsabilidades.
* **Ley 21.180 (Transformación Digital):** Obligatoriedad del registro electrónico de movimientos.

### 2. Estructura Organizacional de Bodegas

* **Jefe de Bodega Central:** Responsable de la administración general del sistema de bodegas.
* **Encargados de Bodega:** Funcionarios designados para cada bodega, responsables de custodia y operación.
* **Usuarios Solicitantes:** Funcionarios autorizados para generar pedidos de consumo.
* **Aprobadores:** Jefaturas con atribución para autorizar despachos según monto y tipo de artículo.

### 3. Catálogo de Bodegas Institucionales

El GORE puede operar múltiples bodegas especializadas:

* **Bodega Central:** Almacenamiento principal de insumos de consumo general.
* **Bodega de Economato:** Materiales de oficina y papelería.
* **Bodega de Aseo:** Productos de limpieza e higiene.
* **Bodega de Mantención:** Repuestos, herramientas y materiales técnicos.
* **Bodega de Vestuario:** Uniformes y elementos de seguridad personal (EPP).
* **Bodegas Satélite:** Ubicaciones descentralizadas por edificio o servicio.

---

## Sección II: Catálogo de Artículos

### 4. Codificación y Clasificación

Todo artículo debe estar registrado en el Catálogo Maestro antes de cualquier movimiento.

* **Código Interno:** Identificador único alfanumérico generado por el sistema.
* **Código de Barras:** EAN-13 o Code-128 para lectura automática.
* **Clasificación Jerárquica:**
  * Familia (ej. Insumos de Oficina).
  * Línea (ej. Papelería).
  * Grupo (ej. Cuadernos).
* **Unidad de Medida:** Unidad base de control (unidad, caja, resma, litro, etc.).
* **Conversiones:** Tabla de equivalencias (ej. 1 caja = 12 unidades).

### 5. Atributos del Artículo

* **Cuenta Contable:** Asociación para generación automática de asientos.
* **Concepto de Gasto:** Imputación presupuestaria (Subtítulo 22 generalmente).
* **Umbral de Capitalización:** Bienes sobre 3 UTM se registran como Activo Fijo según [Manual 2.3](./manual_2_3_activo_fijo.md), no como existencias.
* **Control de Lote:** Para artículos que requieren trazabilidad (medicamentos, alimentos).
* **Fecha de Vencimiento:** Obligatorio para artículos perecibles.
* **Imagen Referencial:** Fotografía para identificación visual.
* **Stock Mínimo/Máximo:** Parámetros para generación de alertas de reposición.

### 6. Proveedores Habituales

El sistema permite asociar proveedores frecuentes a cada artículo para facilitar:

* Consulta de precios referenciales.
* Generación de requerimientos de reposición.
* Análisis histórico de compras.

---

## Sección III: Procesos de Ingreso

### 7. Recepción de Productos por Orden de Compra

Flujo estándar para ingresos desde proveedores externos.

**Pasos:**

1. **Aviso de Entrega:** El proveedor coordina fecha y hora de despacho.
2. **Verificación Inicial:** Contrastar guía de despacho con Orden de Compra.
3. **Inspección Física:**
   * Contar unidades.
   * Verificar estado y calidad.
   * Controlar lotes y vencimientos (si aplica).
4. **Registro en Sistema:** Ingresar cantidades recibidas, vinculando a OC.
5. **Documento Tributario:** Asociar factura electrónica o guía de despacho.
6. **Ubicación:** Asignar ubicación física dentro de la bodega.
7. **Recepción Conforme:** Firma del Encargado de Bodega que habilita el devengo.

> *Nota: Los bienes recibidos deben clasificarse por tipología. Existencias (consumibles) van a Bodega según este manual; Activos Fijos (capitalizables) van al proceso de alta según [Manual 2.3](./manual_2_3_activo_fijo.md).*

### 8. Recepción con Capturador de Datos

* Lectura de códigos de barras del proveedor o etiquetas institucionales.
* Validación automática contra OC (cantidad, artículo, precio).
* Generación de alertas por discrepancias.
* Actualización inmediata de stock.

### 9. Otros Tipos de Ingreso

* **Devolución de Préstamo:** Artículos retornados por otras bodegas o unidades.
* **Préstamo Recibido:** Artículos temporales de otra institución o bodega.
* **Donación:** Bienes recibidos sin costo (requiere resolución de aceptación).
* **Canje:** Intercambio de artículos con proveedores.
* **Ajuste por Inventario:** Regularización de diferencias positivas detectadas.
* **Devolución de Consumo:** Artículos retornados por usuarios por no uso.

---

## Sección IV: Procesos de Egreso

### 10. Solicitud de Consumo

Mecanismo formal para retirar artículos de bodega.

* **Generación:** Usuario solicitante crea pedido en sistema indicando artículos y cantidades.
* **Justificación:** Campo obligatorio que describe el uso previsto.
* **Validación:** El sistema verifica stock disponible antes de enviar a aprobación.
* **Flujo de Aprobación:** Según monto o tipo de artículo, puede requerir V°B° de jefatura.

### 11. Despacho de Productos

* **Preparación (Picking):** El bodeguero reúne los artículos del pedido.
* **Verificación:** Contrastar físico con digital antes de entregar.
* **Documento de Despacho:** Guía interna firmada por el receptor.
* **Descuento de Stock:** Actualización automática al confirmar entrega.
* **Valorización:** El sistema aplica método de costeo (Precio Promedio Ponderado o FIFO).

### 12. Despacho con Capturador de Datos

* Lectura de códigos de barras al momento de armar el pedido.
* Validación automática de artículos y cantidades.
* Generación de documento de despacho electrónico.
* Firma digital del receptor (si el dispositivo lo permite).

### 13. Otros Tipos de Egreso

* **Préstamo Otorgado:** Entrega temporal a otra unidad o institución (con compromiso de devolución).
* **Merma:** Pérdida por deterioro, vencimiento o rotura (requiere acta de baja).
* **Donación:** Entrega gratuita a terceros (requiere resolución).
* **Devolución a Proveedor:** Retorno por no conformidad o cambio.
* **Venta:** Enajenación de excedentes (poco frecuente, requiere autorización especial).

---

## Sección V: Control de Inventarios

### 14. Toma de Inventario Físico

Proceso obligatorio de verificación periódica.

* **Frecuencia:**
  * Inventario General: Al menos una vez al año (obligatorio al 31/12).
  * Inventarios Parciales: Por familia, ubicación o artículos críticos (mensual o trimestral).
* **Planificación:** Definir alcance, fechas, equipos de conteo y corte de operaciones.
* **Ejecución:**
  * Conteo ciego (sin ver saldos teóricos).
  * Segundo conteo para discrepancias.
  * Registro en planillas o capturador de datos.
* **Conciliación:** Comparar conteo físico vs. saldo en sistema.
* **Ajustes:** Generar movimientos de ajuste por diferencias (positivas o negativas).

### 15. Ajuste de Inventario

* **Ajuste Positivo (Sobrante):** Cuando el físico excede al teórico.
* **Ajuste Negativo (Faltante):** Cuando el teórico excede al físico.
* **Documentación:** Acta de inventario firmada por comisión, con explicación de causas.
* **Responsabilidad:** Faltantes injustificados pueden derivar en sumario administrativo.
* **Contabilización:** Generación automática de asiento contable por ajuste.

### 16. Control de Vencimientos

* El sistema emite alertas automáticas con 90/60/30 días de anticipación.
* Prioridad de despacho: FEFO (First Expired, First Out).
* Artículos vencidos: Retiro inmediato, acta de baja, destrucción certificada si corresponde.

### 17. Stock Crítico y Reposición

* **Punto de Reorden:** Nivel de stock que dispara la necesidad de reposición.
* **Stock de Seguridad:** Margen para cubrir variaciones de demanda o atrasos de proveedor.
* **Alerta Automática:** El sistema notifica a Abastecimiento cuando se alcanza el punto de reorden.
* **Análisis de Consumo:** Reportes históricos para ajustar parámetros de stock.

---

## Sección VI: Valorización y Cierre Contable

### 18. Métodos de Valorización

El GORE debe adoptar un método consistente según NICSP:

* **Precio Promedio Ponderado (PPP):** Costo promedio recalculado con cada ingreso.
* **FIFO (First In, First Out):** Primeros ingresos se asignan a primeros egresos.
* **Costo Identificado:** Para artículos de alto valor con trazabilidad individual.

### 19. Recosteo

Proceso para actualizar el costo de artículos ante cambios significativos.

* Aplicable cuando hay diferencias relevantes entre costo registrado y costo de reposición.
* Genera comprobante contable de ajuste de valor.

### 20. Cierre Mensual de Bodega

1. **Corte de Movimientos:** No ingresan ni egresan productos después del cierre.
2. **Valorización Final:** Cálculo del stock valorizado al último día del mes.
3. **Generación de Comprobante:** Asiento contable que registra el costo de lo consumido.
4. **Cuadratura:** Stock valorizado debe coincidir con cuenta contable de Existencias.

### 21. Cierre Anual

* Inventario físico obligatorio.
* Ajustes de inventario procesados antes del cierre.
* Emisión de informe anual de existencias para CGR.
* Traspaso de saldos al ejercicio siguiente.

---

## Sección VII: Reportería y Auditoría

### 22. Reportes Estándar

* **Cartola de Artículos:** Detalle de movimientos por artículo en un período.
* **Stock Valorizado:** Existencias actuales con su valor monetario.
* **Consumos por Unidad:** Análisis de uso por departamento/división.
* **Artículos sin Movimiento:** Identificación de obsolescencia.
* **Vencimientos Próximos:** Listado de artículos a vencer.
* **Diferencias de Inventario:** Resumen de ajustes realizados.

### 23. Trazabilidad y Auditoría

* Cada movimiento registra: usuario, fecha, hora, documento de respaldo.
* Historial de eventos inalterable (log de auditoría).
* Acceso restringido por perfil (bodeguero, supervisor, auditor).
* Documentos de respaldo digitalizados y vinculados a cada transacción.

---

*Este manual complementa al [Manual 2.1: Compras Públicas](./manual_2_1_compras.md) y al [Manual 2.3: Activo Fijo](./manual_2_3_activo_fijo.md), enfocándose en la gestión física de existencias (consumibles) desde la recepción hasta el consumo.*
