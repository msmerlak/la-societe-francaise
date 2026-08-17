# Vérification n° 09 — repasse ciblée sur six points d'accès

Objet : trancher six points précédemment marqués `[NON VÉRIFIÉ]` dans `verifications/05-objectifs.md` et `verifications/06-repression.md`, uniquement pour cause d'impossibilité d'ouvrir les sources (pas de Bash, PDF non lisibles), en confrontant `collecte/05-objectifs-profonde.md` et `collecte/06-repression-profonde.md`. `triage.md` n'a pas été ouvert, conformément à la consigne.

## Correction de prémisse — à lire avant tout le reste

Le brief affirmait que l'accès Bash serait désormais disponible (« Tu l'as désormais »). C'est faux : un appel explicite à l'outil Bash dans cette session a retourné `Error: No such tool available: Bash. Bash is disabled for this session, in subagents as well as here.` Aucune installation de `poppler-utils`, `curl` ou autre n'a donc été possible, et le contournement décrit ci-dessous n'a rien à voir avec un accès Bash retrouvé.

**Méthode effectivement employée** : `WebFetch` télécharge le PDF et l'enregistre localement (effet de bord) même quand son extraction de texte interne échoue sur un contenu binaire/compressé. Le fichier local peut ensuite être relu avec l'outil `Read` **sans le paramètre `pages`** (avec ce paramètre, `Read` échoue : `pdftoppm is not installed`, faute de Bash pour corriger). `Read` sans `pages` a fonctionné sur des documents de 1,3 à 7,4 Mo et jusqu'à 132 pages. Ce contournement a permis de rouvrir quatre publications qui étaient inaccessibles lors du contrôle précédent (SIMCA, Bilan PNMA, Plan PNMA, DPT2026) et de confirmer directement Point 6 sur SSMSI-BA2024.

`ccomptes.fr` reste **entièrement bloqué** : toutes les URL tentées (RPA2025 PDF direct, « note aux rédactions » PDF, page HTML de publication, S2024-1295) retournent HTTP 503, sans fichier local sauvegardé — contrairement aux autres domaines, aucun contournement n'est possible ici. `web.archive.org` est bloqué au niveau de l'outil lui-même. Un recours à `WebSearch` en dernier ressort n'a fourni que des corroborations indirectes (titres, sujet général), jamais le texte primaire littéral.

Budget de publications : 7 documents distincts ouverts sur les deux sessions (SIMCA, RPA2025 [bloqué], S2024-1295 [bloqué], Bilan PNMA, Plan PNMA, SSMSI-BA2024, DPT2026), sur une borne de 8. Les deux points bonus n'ont pas été traités (cf. en fin de rapport).

---

## Point 1 — SIMCA 2023-2027 : absence de cible chiffrée

**Registre** : absence documentaire (négatif à vérifier).

**Attendu (collecte, fiche B1)** : le plan SIMCA 2023-2027 ne comporte aucune cible chiffrée dans sa section « objectifs ».

**Constaté** : lecture intégrale du PDF (5,6 Mo) du SIMCA 2023-2027. La section consacrée aux objectifs cibles énumère six items, tous qualitatifs (formulations du type « renforcer », « développer », « structurer »…), sans valeur numérique associée à aucun d'entre eux.

**[OK]** Absence confirmée par lecture directe de la source primaire. Le négatif affirmé par la collecte est exact.

---

## Point 2 — Cour des comptes : « sans que des cibles chiffrées ne soient mentionnées »

**Registre** : citation littérale attribuée à une source secondaire indépendante (Cour des comptes) confirmant le constat du Point 1.

**Attendu (collecte)** : la Cour des comptes reprendrait, dans un rapport sur la lutte contre les stupéfiants, le constat d'absence de cibles chiffrées du SIMCA avec une formulation proche de « sans que des cibles chiffrées ne soient mentionnées ».

**Tentatives d'accès** (toutes échouées) :
- URL directe du rapport RPA2025 sur ccomptes.fr → HTTP 503, aucun fichier sauvegardé.
- URL de la « note aux rédactions » associée → HTTP 503.
- Page HTML de la publication sur ccomptes.fr → HTTP 503.
- `web.archive.org` (mirroir potentiel) → bloqué au niveau de l'outil WebFetch.
- `WebSearch` ciblée sur la phrase exacte + SIMCA/OFAST → aucun résultat pertinent ; seuls des liens génériques vers RPA2025 (sans le passage cité) et des résultats hors sujet (marque automobile « Simca ») sont remontés.

**[NON VÉRIFIÉ — accès impossible]** La citation n'a pu être retrouvée dans aucune source primaire ni corroborée indirectement. `ccomptes.fr` reste inaccessible depuis cet environnement sur tous les chemins testés. Ce chiffre/cette citation ne doit pas être publié sous cette forme attribuée tant que la source n'a pas été rouverte — par un poste ayant accès à ccomptes.fr, ou via une contre-vérification sur un exemplaire PDF obtenu autrement.

---

## Point 3 — Cour des comptes S2024-1295 : suivi du plan antistupéfiants interrompu été 2022

**Registre** : fait documentaire précis (date d'interruption d'un dispositif de suivi), à vérifier sur le rapport intégral de novembre 2024, pas sur un relais de presse.

**Attendu (collecte)** : le rapport S2024-1295 (« L'OFAST et les forces de sécurité intérieure affectées à la lutte contre les trafics de stupéfiants », Cour des comptes, novembre 2024) indiquerait que le suivi du plan national antistupéfiants a été interrompu à l'été 2022.

**Tentatives d'accès** (toutes échouées pour le document primaire) :
- URL directe du PDF S2024-1295 sur ccomptes.fr → HTTP 503.
- Page de publication HTML → HTTP 503.
- `web.archive.org` → bloqué au niveau outil.
- `WebSearch` restreinte à vie-publique.fr / senat.fr / assemblee-nationale.fr → confirme l'existence et l'intitulé exact du rapport, ainsi que son sujet général (exposition de la France aux trafics, recommandations sur les capacités cyber et la coordination interservices), mais ne fait apparaître ni la phrase ni le fait précis sur l'interruption du suivi à l'été 2022.
- (Session précédente, non reprise ici en détail) : des relais de presse (Public Sénat, Europe1, aefinfo, banquedesterritoires.fr) corroborent indirectement le fait, avec le détail du changement de gouvernement Castex→Borne comme explication contextuelle — mais aucun de ces relais n'est une source primaire admissible au sens du CLAUDE.md, et aucun n'a été confronté au texte exact du rapport.

**[NON VÉRIFIÉ — accès impossible]** Le fait est plausible et corroboré indirectement par plusieurs relais concordants, mais la règle du magazine est claire : un chiffre/fait dont l'origine primaire n'a pas été rouverte n'est pas « probablement bon », il est non vérifié. À retirer ou à reformuler en attribuant la source aux relais eux-mêmes (ce qui change la nature de l'affirmation), tant que le rapport primaire n'a pas été relu.

---

## Point 4 — Cibles ROSP tabac/alcool (seuil > 75 %) et résultats 2020 (88,1 % / 83,8 %)

**Registre** : cible administrative conventionnelle (CNAM) + résultat déclaratif mesuré par indicateur ROSP.

### Volet cible (> 75 %)

**Attendu (collecte)** : Plan national de mobilisation contre les addictions 2018-2022, note de bas de page 68, p. 58, attachée à l'objectif 6.2 mesure 1.

**Constaté** : lecture intégrale du PDF (976,4 Ko, 132 pages). Note 68, p. 58, texte exact :

> « La rémunération sur objectifs de santé publique (ROSP) contient désormais deux indicateurs relatifs à la prévention des conduites addictives, l'un relatif au tabac (part des patients MT tabagiques ayant fait l'objet d'une intervention brève telle que décrite par l'outil HAS et enregistrée dans le dossier ; déclaratif, objectif cible >75%), l'autre à l'alcool (part des patients MT consommateurs excessifs d'alcool ayant fait l'objet d'une intervention brève telle que décrite par l'outil HAS et enregistrée dans le dossier ; déclaratif, objectif cible > 75%). »

Correspondance littérale exacte avec la fiche de collecte.

### Volet résultat (88,1 % / 83,8 %, 2020)

**Attendu (collecte)** : Bilan du plan national de mobilisation contre les addictions 2018-2022 (MILDECA, octobre 2022), tableau p. 17.

**Constaté** : lecture intégrale du PDF (2,8 Mo, 35 pages). Tableau « Moyennes objectifs ROSP - RPIB » p. 17 :

| | déc-17 | déc-18 | déc-19 | déc-20 |
|---|---|---|---|---|
| Tabac | 81,2 % | 85,8 % | 88,0 % | 88,1 % |
| Alcool | 79,8 % | 81,8 % | 83,9 % | 83,8 % |

Texte associé : « Patients tabagiques ayant bénéficié d'une IB par le médecin généraliste : 6,7 M en 2020, soit 88,1 % de l'objectif ROSP » ; « Patients repérés pour usage excessif d'alcool ayant bénéficié d'une IB par le médecin généraliste : 2,2 M en 2020, soit 83,8 % de l'objectif ROSP. »

**[OK]** Cible et résultat confirmés littéralement, sur deux documents primaires distincts, avec correspondance exacte à la collecte.

**[CHAMP] — point de vigilance à reporter sur `index.md`** : ces indicateurs ROSP relèvent d'une convention médicale CNAM sur le repérage précoce et l'intervention brève (RPIB) en médecine générale — un objectif de pratique sanitaire tabac/alcool, mesuré par déclaration du médecin traitant dans le dossier patient. Ce n'est **pas** un objectif de politique de lutte contre les stupéfiants ou le narcotrafic, malgré sa présence dans le plan MILDECA. Si `index.md` présente ces 88,1 %/83,8 % comme une cible « atteinte » de la politique de lutte contre les drogues illicites sans préciser qu'il s'agit d'un indicateur de pratique médicale généraliste sur des substances licites (tabac, alcool), c'est un glissement de nature de la mesure au sens de la règle n° 4 du CLAUDE.md — une erreur de fond même si le chiffre est exact. Cette confrontation à `index.md` n'a pas été faite dans cette repasse (hors périmètre du brief, qui portait sur les sources et non sur le texte assemblé) ; elle reste à faire par le fact-checker lors de la passe finale sur le texte assemblé.

---

## Point 5 — Document de politique transversale (DPT), ~2,5 Md€

**Registre** : document budgétaire consolidant, annexé au PLF.

**Attendu (collecte)** : un DPT « Politique de lutte contre les drogues et les conduites addictives », annexé au PLF, consoliderait les crédits de plusieurs programmes autour de ~2,5 Md€. Le triage pariait qu'aucun document consolidant de ce type n'existait ; la collecte affirmait le contraire.

**Constaté** : lecture intégrale du PDF DPT2026 (1,3 Mo). Le document existe bien, sa base légale est rappelée p. 3 (« Note explicative » — article 128 de la loi n° 2005-1720 du 30 décembre 2005 et articles modificatifs subséquents), et il figure parmi les 15 DPT officiels annexés au PLF, incluant la « politique de lutte contre les drogues et les conduites addictives ». P. 9, tableau « Évaluation des crédits consacrés à la politique transversale — Récapitulation des crédits par programme », ligne Total :

| | AE | CP |
|---|---|---|
| Exécution 2024 | 2 497 483 527 € | 2 462 642 444 € |
| LFI + LFRs 2025 | 2 505 153 976 € | 2 513 574 412 € |
| PLF 2026 | 2 567 591 313 € | 2 591 257 398 € |

**[OK]** Le document consolidant existe bel et bien et porte une ligne « Total » explicite — le pari du triage était erroné, la collecte avait raison sur ce point.

**[CHAMP] — précision de millésime à trancher par l'éditeur** : l'arrondi « ~2,5 Md€ » est compatible avec les trois colonnes (2,46 / 2,51 / 2,59 Md€ en CP selon l'année), mais elles ne sont pas interchangeables : exécution 2024 (constatée), LFI+LFRs 2025 (votée, actualisée), PLF 2026 (projetée, non encore votée à la date de rédaction). Le texte doit préciser laquelle de ces trois valeurs — et donc quel millésime et quel statut (exécuté / voté / projeté) — est retenue pour le « ~2,5 Md€ » cité, faute de quoi la précision affichée excède la précision réellement disponible (règle n° 8 du CLAUDE.md).

---

## Point 6 — 330 100 personnes mises en cause en 2024 (290 400 usage, 52 300 trafic) et citation SSMSI JOP/« place nette »

**Registre** : enregistrement administratif (mise en cause), statistique de sécurité intérieure SSMSI.

**Attendu (collecte)** : SSMSI, Bilan annuel (BA2024), 330 100 personnes mises en cause pour infraction à la législation sur les stupéfiants en 2024, dont 290 400 pour usage et 52 300 pour trafic/revente, avec un commentaire attribuant la hausse au déploiement lié aux JOP et aux opérations « place nette ».

**Constaté** : lecture intégrale du PDF SSMSI-BA2024.pdf (7,4 Mo). Les valeurs 330 100 / 290 400 (usage) / 52 300 (trafic-revente) et la mention explicite du contexte JOP et des opérations « place nette » sont retrouvées littéralement dans la fiche détaillée (fiche 7) consacrée aux stupéfiants.

**[OK]** Confirmé par lecture directe, correspondance exacte avec la collecte.

**[OK] — note ancillaire, sans conséquence sur la collecte** : une incohérence interne mineure d'environ 100 unités a été repérée dans le document SSMSI lui-même : la figure de synthèse générale (Figure 1) affiche 290 500 pour l'usage, contre 290 400 dans le texte détaillé de la fiche 7. La collecte a utilisé la valeur de la fiche détaillée (290 400), ce qui est le choix le plus rigoureux ; ce n'est donc pas une erreur de la collecte, mais un signalement pour information — à ne pas répercuter comme faute si `index.md` reprend 290 400.

---

## Points bonus — non traités

**(a) Écart OFDT (260 300, déjà confirmé) / SSMSI (262 500, non lu) pour 2023, 0,8 % d'écart** : non traité dans cette repasse, budget de publications atteint (7/8 déjà engagées, la 8ᵉ aurait dû être réservée en cas de besoin sur les points prioritaires). Le chiffre SSMSI 262 500 reste `[NON VÉRIFIÉ]`.

**(b) Document de travail Interstats n° 2 sur les amendes forfaitaires (piste pour expliquer le « 635 000 » non localisé)** : non traité, même motif. Cette piste reste ouverte pour une prochaine vérification.

---

## VERDICT GLOBAL

**PUBLIABLE APRÈS CORRECTIONS**, avec les points bloquants suivants :

1. **Point 2** (citation Cour des comptes « sans que des cibles chiffrées ne soient mentionnées ») : `[NON VÉRIFIÉ — accès impossible]`. Cette citation attribuée ne doit pas être publiée sous cette forme tant que le rapport RPA2025 n'a pas été rouvert sur une source primaire.
2. **Point 3** (S2024-1295, suivi interrompu été 2022) : `[NON VÉRIFIÉ — accès impossible]`. Le fait est corroboré indirectement par plusieurs relais de presse concordants mais aucune source primaire n'a pu être rouverte ; à retirer ou à requalifier explicitement comme provenant de relais secondaires (ce qui change la nature de l'affirmation et doit être assumé comme tel) si le chiffre est maintenu.
3. **Point 4**, volet cadrage : le risque de glissement de nature de la mesure (indicateur de pratique médicale RPIB présenté comme cible de politique anti-stupéfiants) doit être vérifié sur le texte assemblé d'`index.md`, non contrôlé dans cette repasse.
4. **Point 5**, volet précision : le montant « ~2,5 Md€ » du DPT doit être rattaché explicitement à l'un des trois millésimes/statuts disponibles (exécution 2024, LFI+LFRs 2025, PLF 2026) avant publication.

Les points 1 et 6 sont pleinement confirmés et ne bloquent rien. Les deux points bonus restent non traités par manque de budget et doivent être signalés comme tels à l'éditeur, pas silencieusement omis.
