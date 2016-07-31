EXPECTED_COLUMNS = 8

COLUMN_ITEM_ID = 0
COLUMN_ITEM_CATEGORY = 5


def load_catalog_data(gen) -> dict:
    return {
        row[COLUMN_ITEM_ID]: row[COLUMN_ITEM_CATEGORY]
        for row in gen
        if len(row) == EXPECTED_COLUMNS
    }
