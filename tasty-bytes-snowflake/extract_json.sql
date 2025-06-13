-- Extract ingredients from semi-structured JSON column
SELECT
    m.menu_item_name,
    obj.value:"ingredients"::ARRAY AS ingredients
FROM MENU m,
     LATERAL FLATTEN(input => m.menu_item_health_metrics_obj:menu_item_health_metrics) obj
WHERE truck_brand_name = 'Freezing Point'
  AND menu_item_name IN ('Mango Sticky Rice', 'Lemonade');
