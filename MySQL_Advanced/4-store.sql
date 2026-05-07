-- Trigger that decreases item quantity after a new order is added
-- Activity 4
CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.quantity
WHERE id = NEW.item_id;

