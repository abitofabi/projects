-- Number of menu items
SELECT COUNT(*) AS total_items FROM MENU;

-- Top 10 menu items
SELECT TOP 10 * FROM MENU;

-- Menu items sold by Freezing Point
SELECT menu_item_name
FROM MENU
WHERE truck_brand_name = 'Freezing Point';

-- Profit on Mango Sticky Rice
SELECT menu_item_name,
       sale_price_usd - cost_of_goods_usd AS profit_usd
FROM MENU
WHERE truck_brand_name = 'Freezing Point'
  AND menu_item_name = 'Mango Sticky Rice';
