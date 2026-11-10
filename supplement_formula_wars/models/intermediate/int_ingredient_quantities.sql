SELECT
 LABEL_ID,
 PRODUCT_NAME,
ingredient.value AS INGREDIENT_JSON,
qty.value:servingSizeOrder::NUMBER AS SERVING_SIZE_ORDER,
qty.value:unit::VARCHAR AS UNIT,
qty.value:quantity::NUMBER AS QUANTITY

FROM {{ ref('stg_supplement_labels') }} AS labels,
LATERAL FLATTEN(
    INPUT => labels.INGREDIENT_ROWS
) AS ingredient,
LATERAL FLATTEN(
    INPUT => ingredient.value:quantity
) AS qty