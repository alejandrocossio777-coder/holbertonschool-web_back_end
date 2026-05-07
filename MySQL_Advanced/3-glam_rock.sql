-- List Glam rock bands ranked by longevity
-- Lifespan is computed using formed year and split year or 2024 if still active
SELECT band_name,
       (IFNULL(split, 2024) - formed) AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;
