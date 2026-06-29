-- ============================================================
-- DATOS DE PRUEBA — ejecutar solo una vez
-- ============================================================

INSERT INTO veterinarios (nombre, especialidad) VALUES
    ('Dr. García', 'Clínica General'),
    ('Dra. Martínez', 'Cirugía'),
    ('Dr. López', 'Dermatología');

INSERT INTO servicios (nombre, precio) VALUES
    ('Consulta General', 3500.00),
    ('Vacunación', 2800.00),
    ('Cirugía', 25000.00),
    ('Baño y Peluquería', 4500.00),
    ('Desparasitación', 1800.00);

INSERT INTO turnos (cliente_nombre, mascota_nombre, veterinario_id, servicio_id, fecha, hora) VALUES
    ('Ana Pérez',     'Firulais', 1, 1, '2025-06-01', '09:00'),
    ('Carlos Ruiz',   'Michi',    2, 3, '2025-06-05', '10:30'),
    ('Laura Gómez',   'Rocky',    1, 2, '2025-06-10', '11:00'),
    ('María Díaz',    'Pelusa',   3, 5, '2025-06-12', '15:00'),
    ('Juan Torres',   'Max',      1, 4, '2025-06-15', '09:30'),
    ('Sofia Blanco',  'Luna',     2, 1, '2025-06-18', '14:00'),
    ('Pedro Castro',  'Toby',     1, 2, '2025-06-20', '10:00'),
    ('Elena Vega',    'Nala',     3, 4, '2025-06-22', '16:00');

INSERT INTO pagos (turno_id, monto, metodo_pago, estado, fecha_pago) VALUES
    (1, 3500.00,  'efectivo',      'pagado',   '2025-06-01'),
    (2, 25000.00, 'tarjeta',       'pagado',   '2025-06-05'),
    (3, 2800.00,  'transferencia', 'pagado',   '2025-06-10'),
    (4, 1800.00,  'efectivo',      'pagado',   '2025-06-12'),
    (5, 4500.00,  'tarjeta',       'pendiente', NULL),
    (6, 3500.00,  'transferencia', 'pendiente', NULL),
    (7, 2800.00,  'efectivo',      'pagado',   '2025-06-20'),
    (8, 4500.00,  'tarjeta',       'pendiente', NULL);
