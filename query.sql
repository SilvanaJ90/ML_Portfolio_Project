SELECT COUNT(d.tipo_contribuyente_id) AS total_donantes_monotributistas
FROM donantes d
INNER JOIN contribuyente c ON d.tipo_contribuyente_id = c.tipo_contribuyente_id
WHERE c.tipo_contribuyente = 'Monotributista';
