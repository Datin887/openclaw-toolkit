---
name: offer_copy_pipeline_premium
description: "Create high-converting offers, headlines, hooks, and sales copy based on audience analysis. Use when you need marketing offers, ad copy, landing page text, email campaigns, or full marketing pipeline. Triggers on: create offer, write sales copy, generate headlines, marketing pipeline, оффер, продающий текст, заголовки, рекламный копирайтинг, ad copy, landing page."
---

# Offer & Copy Pipeline Premium

Elite direct-response offer design and copywriting based on audience psychology.

## When to Use

- Creating marketing offers and positioning
- Writing sales copy, headlines, hooks, CTAs
- Building full marketing pipeline (ads → landing → email)
- Adapting copy for different platforms (Meta, Google, Telegram, Instagram, email)
- Working with audience analysis output

## Input Options

**Option A — Raw product data:**
```
ИНФОРМАЦИЯ О ПРОДУКТЕ:
РЫНОК:
СЕГМЕНТ:
ЦЕЛЬ:
ФОРМАТ:
ПЛОЩАДКА:
CTA:
ТОН:
```

**Option B — Audience analysis output:**
Pass the full output from `deep_audience_analysis_premium` skill — it contains all needed context.

**Option C — Mixed:**
Product info + existing audience analysis + specific goals.

## Workflow

1. **Extract audience essence** — pain, desire, fear, objections, identity
2. **Formulate strategic summary** — who, what, why, how
3. **Generate marketing angles** — 5-10 different approaches
4. **Create offers** — 5-10 offers with mechanics, value, risk reversal
5. **Select top 3** — explain why they're strongest
6. **Big Ideas** — 3-5 memorable marketing concepts
7. **Headlines & subheadlines** — 15 headlines + 10 subheaders
8. **Hooks** — 10-15 opening lines for ads/posts/video
9. **Sales copy** — short, medium, hero block, email, CTAs
10. **Objection handling** — responses to top objections
11. **Platform adaptation** — if multiple channels requested

## Output Format

1. Стратегическая выжимка
2. Ключевые маркетинговые углы (5-10)
3. Офферы (5-10)
4. Топ-3 лучших оффера
5. Big Idea / Основная маркетинговая идея (3-5)
6. Заголовки (15) + подзаголовки (10)
7. Хуки / первые строки (10-15)
8. Продающий текст (набор)
9. Структура среднего продающего текста
10. Работа с возражениями
11. Доказательная логика
12. CTA-пакет (10 вариантов)
13. Адаптация под платформы (если запрошено)

## Master Prompt

For the full system prompt with all algorithms and detailed instructions, see:
`references/system_prompt.md`

## Language

Default: **Russian**. Switch to English only when the source material is English or the user explicitly requests it.

## Rules

- Never invent testimonials, case studies, numbers, or guarantees
- No fake urgency or scarcity unless provided in input
- No misleading claims
- No discriminatory or harmful language
- Write strong but honest
- Match output to requested format (offers only, copy only, or full pipeline)
