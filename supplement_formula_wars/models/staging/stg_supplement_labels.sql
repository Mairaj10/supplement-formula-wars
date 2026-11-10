SELECT
    RAW_RECORD:id::STRING AS LABEL_ID,
    RAW_RECORD:fullName::STRING AS PRODUCT_NAME,
    RAW_RECORD:ingredientRows AS INGREDIENT_ROWS

FROM {{ source('raw', 'supplement_labels') }} AS labels
