# clusterprofiler-skill · Skill del ecosistema R de YuLab-SMU

<p align="center"><img src="docs/clusterprofiler-skill.svg" alt="Flujo de trabajo del skill" width="900"></p>

**38 paquetes · 6.137 claves de API · herramientas Python sin conexión · 19/19 comprobaciones superadas**

Skill multiplataforma para agentes de IA que ayuda a escribir, revisar, planificar y ejecutar análisis con el ecosistema bioinformático de YuLab-SMU. El índice de API se genera a partir de los `NAMESPACE` y las firmas del código R original. `cp_lint.py` revisa los scripts antes de entregarlos.

## Funciones

- `cp_lint.py` valida scripts R sin conexión y detecta funciones desconocidas, argumentos inválidos cuando hay firmas disponibles, errores frecuentes, problemas de sintaxis y puntuación de ancho completo.
- `cp_api.py` consulta las firmas reales del índice local.
- `cp_plan.py` propone pasos y funciones a partir de una solicitud en lenguaje natural.
- Incluye 38 paquetes del ecosistema YuLab-SMU y 6.137 claves; 3.087 tienen argumentos formales analizados.
- `scripts/run_cp.R` ejecuta los paquetes R reales. Python no inventa resultados.

## Inicio rápido

```bash
python3 install.py --host codex       # también: claude, workbuddy, deepseek
python3 tools/selftest.py             # 19 comprobaciones
python3 tools/cp_lint.py analysis.R --json
```

En Windows, usa `python` si no existe `python3`. Las herramientas Python solo usan la biblioteca estándar; para ejecutar análisis se necesita R y los paquetes Bioconductor/CRAN correspondientes. Consulta la [guía de instalación](INSTALL.md).

La autocomprobación incluye 9 fixtures R, 44 bloques de código de documentación, pruebas rápidas de herramientas e integridad del índice: **19/19 superadas**. R no estaba instalado en el entorno de validación, así que no se ejecutaron análisis R reales.

## Documentación

[Página en inglés](README.md) · [Guía de instalación](INSTALL.md) · [Instrucciones del skill](SKILL.md) · [Cambios](CHANGELOG.md)

Proyecto comunitario independiente; no es un producto oficial de YuLab-SMU ni de clusterProfiler. Consulta [NOTICE](NOTICE) para la licencia y atribución.
