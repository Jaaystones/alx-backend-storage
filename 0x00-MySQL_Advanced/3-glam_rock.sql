-- This SQL script select band_name, and lifespan column which is difference
-- Query the bands with Glam rock as their main style
SELECT band_name, (2022 - SUBSTRING_INDEX(band_formed, '-', 1)) AS lifespan
    FROM metal_bands
    WHERE band_style LIKE '%Glam rock%'
    ORDER BY lifespan DESC;
