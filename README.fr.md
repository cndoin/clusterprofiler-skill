# clusterprofiler-skill · Skill pour l’écosystème R de YuLab-SMU

<p align="center"><img src="docs/clusterprofiler-skill.svg" alt="Flux de travail du skill" width="900"></p>

**38 packages · 6 137 clés d’API · outils Python hors ligne · 19/19 vérifications réussies**

Ce skill multi-agent aide à écrire, vérifier, planifier et exécuter des analyses avec l’écosystème bioinformatique R de YuLab-SMU. L’index d’API est généré à partir des `NAMESPACE` et des signatures du code R amont. `cp_lint.py` vérifie les scripts avant leur livraison.

## Fonctionnalités

- `cp_lint.py` vérifie les scripts R hors ligne : fonctions inconnues, arguments invalides lorsque la signature est connue, erreurs fréquentes, syntaxe et ponctuation pleine chasse.
- `cp_api.py` recherche les signatures réelles dans l’index local.
- `cp_plan.py` propose des étapes et fonctions à partir d’une demande en langage naturel.
- Couverture de 38 packages YuLab-SMU et de 6 137 clés ; 3 087 signatures comportent des arguments formels analysés.
- `scripts/run_cp.R` lance les vrais packages R ; Python ne fabrique pas de résultats.

## Démarrage rapide

```bash
python3 install.py --host codex       # aussi : claude, workbuddy, deepseek
python3 tools/selftest.py             # 19 vérifications
python3 tools/cp_lint.py analysis.R --json
```

Sous Windows, utilisez `python` si `python3` est indisponible. Les outils Python utilisent uniquement la bibliothèque standard ; l’exécution d’analyses nécessite R et les packages Bioconductor/CRAN concernés. Consultez le [guide d’installation](INSTALL.md).

L’autotest comprend 9 fixtures R, 44 blocs de code documentaire, des tests rapides des outils et des contrôles d’intégrité de l’index : **19/19 réussis**. R n’était pas installé dans l’environnement de validation ; aucune analyse R réelle n’a donc été exécutée.

## Documentation

[Page en anglais](README.md) · [Guide d’installation](INSTALL.md) · [Instructions du skill](SKILL.md) · [Historique](CHANGELOG.md)

Projet communautaire indépendant, non officiel pour YuLab-SMU et clusterProfiler. Voir [NOTICE](NOTICE) pour les licences et attributions.
