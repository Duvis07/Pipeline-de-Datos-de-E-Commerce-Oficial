-- TODO: Esta consulta devolverá una tabla con dos columnas; customer_state y Revenue.
-- La primera contendrá las abreviaturas que identifican a los 10 estados con mayores ingresos,
-- y la segunda mostrará el ingreso total de cada uno.
-- PISTA: Todos los pedidos deben tener un estado "delivered" y la fecha real de entrega no debe ser nula.

SELECT
    oc.customer_state AS customer_state,
    SUM(oop.payment_value) AS Revenue
FROM
    olist_orders oo
JOIN
    olist_customers oc ON oo.customer_id = oc.customer_id
JOIN
    olist_order_payments oop ON oo.order_id = oop.order_id
WHERE
    oo.order_status = 'delivered'
    AND oo.order_delivered_customer_date IS NOT NULL
GROUP BY
    oc.customer_state
ORDER BY
    Revenue DESC
LIMIT 10;