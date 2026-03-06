# Data

The dataset used in this project was provided as part of the ESILV Information Retrieval & NLP course and is not publicly redistributable.

To reproduce the results, you will need the following files placed in this `data/` directory:

---

## Required Files

### `Tripadvisor.csv`
One row per place. Key columns used:

| Column | Description |
|---|---|
| `id` | Unique place identifier |
| `typeR` | Place type: `H` (Hotel), `R` (Restaurant), `A` (Attraction), `AP` (Attraction Product) |
| `activiteSubCategorie` | List of attraction subcategory IDs |
| `activiteSubType` | List of attraction subtype IDs (more granular) |
| `restaurantType` | Restaurant type IDs |
| `cuisine` | Cuisine type IDs |
| `priceRange` | Hotel price range |

### `reviews83325.csv`
One row per review. Key columns used:

| Column | Description |
|---|---|
| `id` | Review identifier |
| `idplace` | Links to `id` in `Tripadvisor.csv` |
| `review` | Full review text |
| `langue` | Language code (we filter for `en` — English only) |

---

## Reference Tables (also required)

| File | Description |
|---|---|
| `AttractionSubType.csv` | ID → name mapping for attraction subtypes |
| `AttractionSubCategorie.csv` | ID → name mapping for attraction subcategories |
| `restaurantType.csv` | ID → name mapping for restaurant types |
| `cuisine.csv` | ID → name mapping for cuisine types |
| `dietary_restrictions.csv` | ID → name mapping for dietary restrictions |

---

## Notes

- Only English reviews (`langue == "en"`) are used
- Reviews are aggregated per place before indexing
- Metadata columns are used **only for evaluation**, never as model input
